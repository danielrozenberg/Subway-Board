"""Perform animations on ETA image."""

import collections
import datetime
import logging
import os
import threading
import time
from typing import Mapping

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import constants
import networking
from networking import LineStop, LineStopEtaMapping
import sorter

_LINE_HEIGHT = 16
_FONT_SIZE = 11

_logger = logging.getLogger('subway_board.animator')


class Animator:
  """Crops and scrolls the ETAs image."""

  def __init__(
      self,
      width: int,
      height: int,
      row_interval: datetime.timedelta,
      scroll_interval: datetime.timedelta,
      stop_names: Mapping[str, str],
  ):
    """Constructor.

    Args:
      width: in pixels.
      height: in pixels.
      row_interval: how long to wait between moving rows.
      scroll_interval: how long to wait between scrolling.
      stop_names: mapping from stop ID to the display name, based on csv file
        https://atisdata.s3.amazonaws.com/Station/Stations.csv.
    """
    self._sorter = sorter.Sorter(list(stop_names))

    self._width = width
    self._height = height
    self._row_interval_seconds = row_interval.total_seconds()
    self._scroll_interval_seconds = scroll_interval.total_seconds()
    self._stop_names = stop_names

    self._etas: LineStopEtaMapping = collections.defaultdict()
    self._vertical_scroll = 0
    self._top_line = self._sorter.initial_line_stop
    self._offline = False
    self._frame = Image.new('RGB', (width, height))

    self._event_ready = threading.Event()
    self._event_new_frame = threading.Event()

    self._load_assets()

  def _load_assets(self) -> None:
    """Loads image and font assets."""
    directory = os.path.dirname(__file__)

    self._offline_icon = Image.open(
        os.path.join(directory, 'images/offline.png'))

    self._arrow_icons = {}
    for direction in networking.Direction:
      filepath = os.path.join(directory, 'images',
                              f'arrow_{direction.value}.png')
      self._arrow_icons[direction] = Image.open(filepath)

    self._route_icons = {}
    for route_id in constants.ROUTE_IDS:
      filepath = os.path.join(
          directory, f'third_party/louh/mta-subway-bullets/{route_id}.png')
      self._route_icons[route_id] = Image.open(filepath)

    self._stop_name_font = ImageFont.truetype(os.path.join(
        directory, 'third_party/canonical/Ubuntu-M.ttf'),
                                              size=_FONT_SIZE)
    self._eta_font = ImageFont.truetype(os.path.join(
        directory, 'third_party/canonical/Ubuntu-B.ttf'),
                                        size=_FONT_SIZE)

  @property
  def event_ready(self) -> threading.Event:
    return self._event_ready

  def wait_for_new_frame(self) -> Image.Image:
    self._event_new_frame.wait()
    return self._draw()

  def mark_offline(self) -> None:
    self._offline = True
    self._event_new_frame.set()

  def update_etas(self, etas: LineStopEtaMapping) -> None:
    """Updates the ETAs."""
    self._etas = etas
    self._offline = False

    if self._top_line not in etas:
      self._advance_top_line()

    self._event_ready.set()
    self._event_new_frame.set()

  def start(self) -> None:
    _logger.info('Starting scrolling animation')
    threading.Thread(target=self._start, daemon=True).start()

  def _start(self) -> None:
    while True:
      time.sleep(self._row_interval_seconds)

      self._scroll()
      while self._vertical_scroll < 0:
        time.sleep(self._scroll_interval_seconds)
        self._scroll()

  def _scroll(self) -> None:
    self._vertical_scroll -= 1

    if self._vertical_scroll == -_LINE_HEIGHT:
      self._vertical_scroll = 0
      self._advance_top_line()

    self._event_new_frame.set()

  def _advance_top_line(self) -> None:
    self._top_line = self._sorter.next_in_after(self._etas, self._top_line)

  def _draw(self) -> Image.Image:
    """Crops the current frame and returns the resulting image."""
    line_stop = self._top_line
    for upper in range(self._vertical_scroll, self._height, _LINE_HEIGHT):
      self._frame.paste(self._draw_line(line_stop), (0, upper))
      line_stop = self._sorter.next_in_after(self._etas, line_stop)

    if self._offline:
      self._frame.paste(self._offline_icon,
                        (self._frame.width - self._offline_icon.width,
                         self._frame.height - self._offline_icon.height),
                        self._offline_icon)

    self._event_new_frame.clear()
    return self._frame

  def _draw_line(self, line_stop: LineStop) -> Image.Image:
    """Draws a single line."""
    image = Image.new('RGB', (self._width, _LINE_HEIGHT))
    if line_stop not in self._etas:
      return image

    minutes = self._etas[line_stop]
    draw = ImageDraw.Draw(image)

    route_icon = self._route_icons[line_stop.route_id]
    arrow_icon = self._arrow_icons[line_stop.direction]

    image.paste(route_icon, (0, 0), route_icon)
    image.paste(arrow_icon, (18, 4), arrow_icon)

    minutes_text = ' • '.join(str(m) for m in sorted(minutes)[:3])
    draw.text((32, 1),
              self._stop_names[line_stop.stop_id],
              fill=0xbbbbbb,
              font=self._stop_name_font)
    draw.text((self._width - 2, 1),
              minutes_text,
              fill=0xffffff,
              font=self._eta_font,
              anchor='ra')

    return image
