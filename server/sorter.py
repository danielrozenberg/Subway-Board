"""Sorts the lines by user-chosen order."""

import dataclasses
import itertools
from typing import Generator, Mapping, Sequence, Tuple

import networking
from networking import LineStopEtaMapping


@dataclasses.dataclass(frozen=True, order=True)
class NamedLineStop(networking.LineStop):
  stop_name: str

  @classmethod
  def from_line_stop(cls, line_stop: networking.LineStop,
                     stop_names: Mapping[str, str]) -> 'NamedLineStop':
    return cls(stop_id=line_stop.stop_id,
               route_id=line_stop.route_id,
               direction=line_stop.direction,
               stop_name=stop_names[line_stop.stop_id])


def by_order(
    etas: LineStopEtaMapping, stop_names: Mapping[str, str]
) -> Generator[Tuple[NamedLineStop, Sequence[int]], None, None]:
  """Yields the resulting lines by preference."""

  for route_id, direction, stop_id in itertools.product(
      '123456ACEGBDFMJZNQRWLS', networking.Direction, stop_names):
    line_stop = networking.LineStop(stop_id=stop_id,
                                    route_id=route_id,
                                    direction=direction)
    if line_stop in etas:
      named_line_stop = NamedLineStop.from_line_stop(line_stop, stop_names)
      yield named_line_stop, etas[line_stop]
