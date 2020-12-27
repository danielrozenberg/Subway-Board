"""Subway Board display code for the Raspberry Pi."""

import itertools
import logging
import socket
import time

from PIL import Image
import rgbmatrix

_SOCKET_SERVER_ADDRESS = '192.168.1.12', 7829
_ERROR_COLOR = 255, 0, 0

_MATRIX_OPTIONS = rgbmatrix.RGBMatrixOptions()
_MATRIX_OPTIONS.rows = 32
_MATRIX_OPTIONS.cols = 64
_MATRIX_OPTIONS.chain_length = 2
_MATRIX_OPTIONS.brightness = 25
_MATRIX_OPTIONS.gpio_slowdown = 0

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger('subway_board.rpi')

  width = _MATRIX_OPTIONS.cols * _MATRIX_OPTIONS.chain_length
  height = _MATRIX_OPTIONS.rows
  image_bytes = len('RGB') * width * height

  logger.info('Connecting to LED matrix')
  matrix = rgbmatrix.RGBMatrix(options=_MATRIX_OPTIONS)
  canvas = matrix.CreateFrameCanvas()

  logger.info('You should see a single white pixel on the top-left corner')
  matrix.SetPixel(0, 0, 255, 255, 255)

  while True:
    try:
      logger.info('Connecting to server %r...', _SOCKET_SERVER_ADDRESS)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect(_SOCKET_SERVER_ADDRESS)

      logger.info('... connected!')
      while True:
        # Tell the server that we are ready.
        s.send(b'\x00')

        # Read the next image as an uncompressed stream of RGB pixels.
        data = s.recv(image_bytes)
        while len(data) < image_bytes:
          missing_data = s.recv(image_bytes - len(data))
          if not missing_data:
            raise EOFError('Image data is incomplete')
          data += missing_data

        # Parse the image, draw it to the off-screen canvas, and swap the
        # canvas onto the LED matrix.
        image = Image.frombytes('RGB', (width, height), data)
        canvas.SetImage(image)
        canvas = matrix.SwapOnVSync(canvas)
    except (ConnectionError, EOFError) as e:
      logger.error('Disconnected: %s', e)
      for x, y in itertools.product(range(matrix.width - 4, matrix.width),
                                    range(matrix.height - 4, matrix.height)):
        matrix.SetPixel(x, y, *_ERROR_COLOR)
      time.sleep(1)
