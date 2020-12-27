"""Subway Board display code for the Raspberry Pi."""

import itertools
import socket
import tempfile
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
  matrix = rgbmatrix.RGBMatrix(options=_MATRIX_OPTIONS)
  matrix.SetPixel(0, 0, 255, 255, 255)

  image = Image.new('RGB', (1, 1))
  canvas = matrix.CreateFrameCanvas()
  while True:
    with tempfile.SpooledTemporaryFile() as stf:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        s.connect(_SOCKET_SERVER_ADDRESS)
        while True:
          data = s.recv(2**12)
          if not data:
            break
          stf.write(data)
        s.close()

        if not stf.tell():
          time.sleep(0.01)
          continue

        stf.seek(0)
        image = Image.open(stf)
        canvas.SetImage(image)
        canvas = matrix.SwapOnVSync(canvas)
      except (ConnectionRefusedError, OSError):
        for x, y in itertools.product(range(matrix.width - 4, matrix.width),
                                      range(matrix.height - 4, matrix.height)):
          matrix.SetPixel(x, y, *_ERROR_COLOR)
        time.sleep(1)
