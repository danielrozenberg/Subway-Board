"""Sorts the lines by user-chosen order."""

import itertools
from typing import Generator, Sequence

import constants
from entities import Direction, LineStop, LineStopEtaMapping


class Sorter:
  """Helper for sorting the lines."""

  def __init__(self, stop_ids: Sequence[str]):
    self._stop_ids = stop_ids

  @property
  def initial_line_stop(self) -> LineStop:
    return next(self._all_possible_line_stops())

  def next_in_after(self, etas: LineStopEtaMapping,
                    current_line_stop: LineStop) -> LineStop:
    """Returns the next LineStop available in etas after current_line_stop."""
    all_possible_line_stops = self._all_possible_line_stops()
    # Iterate the generator until we find the current LineStop in it.
    while next(all_possible_line_stops) != current_line_stop:
      pass

    # Now continue to iterate it until we find a LineStop that exists in etas.
    return next(
        (line_stop for line_stop in all_possible_line_stops
         if line_stop in etas),
        current_line_stop,
    )

  def _all_possible_line_stops(self) -> Generator[LineStop, None, None]:
    # Repeat twice in case the next available line is before the current one in
    # the producer.
    for _ in range(2):
      for route_id, direction, stop_id in itertools.product(
          constants.ROUTE_IDS, Direction, self._stop_ids):
        yield LineStop(stop_id=stop_id, route_id=route_id, direction=direction)
