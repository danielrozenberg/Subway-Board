"""Perform animations on ETA image."""

import datetime
import logging
import os
import threading
import time

from PIL import Image

_logger = logging.getLogger('subway_board.animator')


class Animator:
  """Crops and scrolls the ETAs image."""

  def __init__(self, width: int, height: int, row_interval: datetime.timedelta,
               scroll_interval: datetime.timedelta):
    self._width = width
    self._height = height
    self._row_interval_seconds = row_interval.total_seconds()
    self._scroll_interval_seconds = scroll_interval.total_seconds()

    self._vertical_scroll = 0
    self._offline = False
    self._image = Image.new('RGB', (width, height))
    self._frame = Image.new('RGB', (width, height))

    self._offline_icon = Image.open(
        os.path.join(os.path.dirname(__file__), 'images/offline.png'))

    self._event_ready = threading.Event()
    self._event_new_frame = threading.Event()

  @property
  def event_ready(self) -> threading.Event:
    return self._event_ready

  def wait_for_new_frame(self) -> Image.Image:
    self._event_new_frame.wait()
    return self._draw()

  def mark_offline(self) -> None:
    self._event_new_frame.set()
    self._offline = True

  def replace_image(self, image: Image.Image) -> None:
    """Replaces the full (uncropped) image."""
    self._event_new_frame.set()
    self._image = image
    self._offline = False
    self._vertical_scroll %= self._image.height
    self._event_ready.set()

  def start(self) -> None:
    _logger.info('Starting scrolling animation')
    threading.Thread(target=self._start, daemon=True).start()

  def _start(self) -> None:
    while True:
      time.sleep(self._row_interval_seconds)

      self._scroll()
      while self._vertical_scroll % 16 != 0:
        time.sleep(self._scroll_interval_seconds)
        self._scroll()

  def _scroll(self) -> None:
    self._event_new_frame.set()
    self._vertical_scroll = (self._vertical_scroll + 1) % self._image.height

  def _draw(self) -> Image.Image:
    """Crops the current frame and returns the resulting image."""
    upper = self._vertical_scroll
    lower = min(upper + self._height, self._image.height)
    self._frame.paste(self._image.crop((0, upper, self._width - 1, lower)),
                      (0, 0))

    if lower - upper < self._height:
      self._frame.paste(self._image, (0, lower - upper))

    if self._offline:
      self._frame.paste(self._offline_icon,
                        (self._frame.width - self._offline_icon.width,
                         self._frame.height - self._offline_icon.height))

    self._event_new_frame.clear()
    return self._frame
