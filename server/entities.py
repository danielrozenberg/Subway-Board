"""Data classes."""

import enum
import dataclasses
import functools
from typing import DefaultDict, List


@functools.total_ordering
class Direction(enum.Enum):
  NORTHBOUND = 'N'
  SOUTHBOUND = 'S'

  def __lt__(self, other: 'Direction') -> bool:
    if isinstance(other, Direction):
      return str(self.value) < str(other.value)
    return NotImplemented


@dataclasses.dataclass(frozen=True)
class LineStop:
  stop_id: str
  route_id: str
  direction: Direction


@functools.total_ordering
@dataclasses.dataclass(frozen=True)
class Eta:
  minutes: int
  is_assigned: bool

  def __lt__(self, other: 'Eta') -> bool:
    if isinstance(other, Eta):
      return self.minutes < other.minutes
    return NotImplemented


LineStopEtaMapping = DefaultDict[LineStop, List[Eta]]
