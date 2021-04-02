"""Subway Board display code for the Raspberry Pi."""

import logging
import os
import socket
import time

from PIL import Image
import rgbmatrix

import options

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger('subway_board.rpi')

  width = options.MATRIX_OPTIONS.cols * options.MATRIX_OPTIONS.chain_length
  height = options.MATRIX_OPTIONS.rows

  offline_icon = Image.open(
      os.path.join(os.path.dirname(__file__), 'offline.png')).convert('RGB')

  logger.info('Connecting to LED matrix')
  matrix = rgbmatrix.RGBMatrix(options=options.MATRIX_OPTIONS)
  canvas = matrix.CreateFrameCanvas()

  logger.info('You should see a single white pixel on the top-left corner')
  matrix.SetPixel(0, 0, 255, 255, 255)

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
