"""Helper methods on top of suntime."""

import dataclasses
import datetime
from typing import Tuple

import suntime

import options

SUN = suntime.Sun(options.LATITUDE, options.LONGITUDE)


@dataclasses.dataclass(frozen=True)
class Initial:
  sunrise: datetime.datetime
  sunset: datetime.datetime
  brightness: int


def get_sunrise_tomorrow() -> datetime.datetime:
  return SUN.get_sunrise_time(datetime.date.today() +
                              datetime.timedelta(days=1))


def get_sunset_tomorrow() -> datetime.datetime:
  return SUN.get_sunset_time(datetime.date.today() + datetime.timedelta(days=1))


def get_initial_values() -> Initial:
  sunrise = _get_initial_sunrise()
  sunset = _get_initial_sunset()
  brightness = (options.NIGHTTIME_BRIGHTNESS
                if sunrise < sunset else options.DAYTIME_BRIGHTNESS)
  return Initial(sunrise, sunrise, brightness)


def _get_initial_sunrise() -> datetime.datetime:
  sunrise_today = SUN.get_sunrise_time()
  sunrise_tomorrow = get_sunrise_tomorrow()
  if sunrise_today < datetime.datetime.utcnow():
    return sunrise_today
  return sunrise_tomorrow


def _get_initial_sunset() -> datetime.datetime:
  sunset_today = SUN.get_sunset_time()
  sunset_tomorrow = get_sunset_tomorrow()
  if sunset_today < datetime.datetime.utcnow():
    return sunset_today
  return sunset_tomorrow
