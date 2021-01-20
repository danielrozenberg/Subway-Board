"""Updater for MTA real-time data."""

import collections
import collections.abc
from concurrent import futures
import datetime
import logging
import time
from typing import Callable

from google.protobuf import message
import gtfs_realtime_pb2
import nyct_subway_pb2
import requests

from entities import Direction, Eta, LineStop, LineStopEtaMapping

_FETCH_TIMEOUT_SECS = 30

_REAL_TIME_FEED_BASE_URL = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
_REAL_TIME_FEED_URLS = (
    _REAL_TIME_FEED_BASE_URL,  # 123456
    f'{_REAL_TIME_FEED_BASE_URL}-7',
    f'{_REAL_TIME_FEED_BASE_URL}-ace',
    f'{_REAL_TIME_FEED_BASE_URL}-bdfm',
    f'{_REAL_TIME_FEED_BASE_URL}-g',
    f'{_REAL_TIME_FEED_BASE_URL}-jz',
    f'{_REAL_TIME_FEED_BASE_URL}-l',
    f'{_REAL_TIME_FEED_BASE_URL}-nqrw',
)

_logger = logging.getLogger('subway_board.updater')


class Updater:
  """Real-time MTA subway info."""

  def __init__(
      self,
      api_key: str,
      stop_ids: collections.abc.Set[str],
      eta_range: range,
      refresh_interval: datetime.timedelta = datetime.timedelta(seconds=30)):
    """Updater constructor.

    Args:
      api_key: MTA real-time API access key, obtained from
        https://api.mta.info/.
      eta_range: [min, max) minutes for ETAs.
      refresh_interval: how often to refresh the feed.
    """
    self._api_key = api_key
    self._stop_ids = stop_ids
    self._eta_range = eta_range
    self._refresh_interval_secs = refresh_interval.total_seconds()

  def run(self, on_update: Callable[[LineStopEtaMapping], None],
          on_error: Callable[[Exception], None]) -> None:
    """Runs the updater; blocking call."""
    _logger.info('Starting Updater for stops %r', self._stop_ids)
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
      while True:
        future = executor.submit(self._fetch)
        try:
          etas = future.result(timeout=_FETCH_TIMEOUT_SECS)
          on_update(etas)
        except (
            futures.TimeoutError,
            message.DecodeError,
            requests.exceptions.RequestException,
        ) as e:
          _logger.exception('Failed to fetch updates')
          on_error(e)

        time.sleep(self._refresh_interval_secs)

  def _fetch(self) -> LineStopEtaMapping:
    """Fetches real-time data for all stops."""
    etas: LineStopEtaMapping = collections.defaultdict(list)
    for feed_url in _REAL_TIME_FEED_URLS:
      response = requests.get(feed_url, headers={'x-api-key': self._api_key})
      feed = gtfs_realtime_pb2.FeedMessage.FromString(response.content)  # pylint: disable=no-member
      for entity in feed.entity:
        self._process(entity, etas)

    return etas

  def _process(self, entity: gtfs_realtime_pb2.FeedEntity,
               etas: LineStopEtaMapping) -> None:
    """Processes a single FeedEntity and adds it to the ETAs results."""
    now = datetime.datetime.now()

    for stop_time_update in entity.trip_update.stop_time_update:
      if stop_time_update.stop_id[-1] not in 'NS':
        continue

      stop_id = stop_time_update.stop_id[:-1]
      direction = Direction(stop_time_update.stop_id[-1])
      if stop_id not in self._stop_ids:
        continue

      if not stop_time_update.departure.time:
        continue

      minutes = int(
          (datetime.datetime.fromtimestamp(stop_time_update.departure.time) -
           now).total_seconds()) // 60
      if minutes not in self._eta_range:
        continue

      route_id: str = entity.trip_update.trip.route_id
      line_stop = LineStop(stop_id=stop_id,
                           route_id=route_id,
                           direction=direction)

      is_assigned = entity.trip_update.trip.Extensions[
          nyct_subway_pb2.nyct_trip_descriptor].is_assigned
      etas[line_stop].append(Eta(minutes=minutes, is_assigned=is_assigned))
