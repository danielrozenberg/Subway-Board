"""Subway Board display code for the Raspberry Pi."""

import datetime
import logging
import os
import socket
import threading
import time
from typing import Callable

from PIL import Image
import rgbmatrix

import options
import suntime_extra

SunEventTimeFunction = Callable[[], datetime.datetime]

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger('subway_board.rpi')

  initial = suntime_extra.get_initial_values()

  width = options.MATRIX_OPTIONS.cols * options.MATRIX_OPTIONS.chain_length
  height = options.MATRIX_OPTIONS.rows
  options.MATRIX_OPTIONS.brightness = initial.brightness

  offline_icon = Image.open(
      os.path.join(os.path.dirname(__file__), 'offline.png')).convert('RGB')

  logger.info('Connecting to LED matrix')
  matrix = rgbmatrix.RGBMatrix(options=options.MATRIX_OPTIONS)
  canvas = matrix.CreateFrameCanvas()

  logger.info('You should see a single white pixel on the top-left corner')
  matrix.SetPixel(0, 0, 255, 255, 255)

  def handle_sun_event(new_brightness: int,
                       next_sun_event_function: SunEventTimeFunction):
    """Changes the matrix brightness and schedules the same event in a day."""
    logging.info('Changing brightness to %d', new_brightness)
    matrix.brightness = new_brightness
    schedule_at = next_sun_event_function()
    schedule_next_sun_event(schedule_at, next_sun_event_function,
                            new_brightness)

  def schedule_next_sun_event(scheduled_at: datetime.datetime,
                              next_sun_event_function: SunEventTimeFunction,
                              brightness: int) -> None:
    """Schedules a brightness-change event based on sunrise/sunset."""
    scheduled_at_timedelta = scheduled_at - datetime.datetime.now(
        datetime.timezone.utc)
    logging.info('Scheduling next brightness change (%d) event for %r (in %r)',
                 brightness, scheduled_at, scheduled_at_timedelta)
    scheduled_timer = threading.Timer(scheduled_at_timedelta.total_seconds(),
                                      handle_sun_event,
                                      (brightness, next_sun_event_function))
    scheduled_timer.daemon = True
    scheduled_timer.start()

  schedule_next_sun_event(initial.sunrise, suntime_extra.get_sunrise_tomorrow,
                          options.DAYTIME_BRIGHTNESS)
  schedule_next_sun_event(initial.sunset, suntime_extra.get_sunset_tomorrow,
                          options.NIGHTTIME_BRIGHTNESS)

  logger.info('Connecting to server %r...', options.SERVER_ADDRESS)
  while True:
    try:
      with socket.create_connection(
          options.SERVER_ADDRESS, options.TIMEOUT) as s, s.makefile('rb') as fp:
        # Parse the image, draw it to the off-screen canvas, and swap the
        # canvas onto the LED matrix.
        image = Image.open(fp)
        canvas.SetImage(image)
        canvas = matrix.SwapOnVSync(canvas)
    except (EOFError, OSError) as e:
      logger.exception('Disconnected: %s', e)
      matrix.SetImage(offline_icon, matrix.width - offline_icon.width,
                      matrix.height - offline_icon.height)
      time.sleep(1)
