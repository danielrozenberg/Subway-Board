"""Dedupes lines that stop in multiple stations."""

from typing import Sequence

import frozendict

import options
from options import Preference
import networking
from networking import LineStopEtaMapping

_OTHER_DIRECTION = frozendict.frozendict({
    networking.Direction.NORTHBOUND: networking.Direction.SOUTHBOUND,
    networking.Direction.SOUTHBOUND: networking.Direction.NORTHBOUND,
})


def dedup(etas: LineStopEtaMapping, preferences: Sequence[Preference]) -> None:
  """Dedupes lines that stop in multiple stations."""

  for preference in preferences:
    if isinstance(preference, options.PositionalPreference):
      _dedup_by_position(etas, preference.prefer_stop_id,
                         preference.over_stop_id)
    elif isinstance(preference, options.DirectionalPreference):
      _dedup_by_direction(etas, preference.northbound_stop_id,
                          networking.Direction.NORTHBOUND,
                          preference.southbound_stop_id)
      _dedup_by_direction(etas, preference.southbound_stop_id,
                          networking.Direction.SOUTHBOUND,
                          preference.northbound_stop_id)
    else:
      raise NotImplementedError(
          f'Unimplemented Preference type {type(preference)}')


def _dedup_by_position(etas: LineStopEtaMapping, prefer_stop_id: str,
                       over_stop_id: str) -> None:
  """Dedups the same line if the same direction appears in two stations."""
  preferred = set(
      line_stop for line_stop in etas if line_stop.stop_id == prefer_stop_id)

  for preferred_line_stop in preferred:
    duplicate_line_stop = networking.LineStop(
        stop_id=over_stop_id,
        route_id=preferred_line_stop.route_id,
        direction=preferred_line_stop.direction)
    if duplicate_line_stop in etas:
      del etas[duplicate_line_stop]


def _dedup_by_direction(etas: LineStopEtaMapping, prefer_stop_id: str,
                        direction: networking.Direction,
                        over_stop_id: str) -> None:
  """Dedups the same line if the opposite directions appears in two stations."""
  preferred = set(line_stop for line_stop in etas
                  if line_stop.stop_id == prefer_stop_id and
                  line_stop.direction == direction)

  for preferred_line_stop in preferred:
    duplicate_line_stop = networking.LineStop(
        stop_id=over_stop_id,
        route_id=preferred_line_stop.route_id,
        direction=direction)
    if duplicate_line_stop in etas:
      del etas[duplicate_line_stop]
