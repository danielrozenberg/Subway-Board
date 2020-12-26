"""Options for Subway Board."""

import dataclasses
import datetime
from typing import Union


@dataclasses.dataclass
class PositionalPreference:
  prefer_stop_id: str
  over_stop_id: str


@dataclasses.dataclass
class DirectionalPreference:
  northbound_stop_id: str
  southbound_stop_id: str


Preference = Union[PositionalPreference, DirectionalPreference]

MTA_API_ACCESS_KEY = 'Get your own from the MTA'
STOP_IDS_TO_NAMES = {
    'A25': '50 St',
    '126': '50 St',
    'A24': '59 St',
}
ETA_RANGE = range(5, 45)
DEDUPING_PREFERENCES = (
    PositionalPreference(prefer_stop_id='A25', over_stop_id='A24'),
    DirectionalPreference(northbound_stop_id='A24', southbound_stop_id='126'),
)
WIDTH = 128
HEIGHT = 32
ROW_INTERVAL = datetime.timedelta(seconds=6)
SCROLL_INTERVAL = datetime.timedelta(milliseconds=62.5)
PORT = 7829
