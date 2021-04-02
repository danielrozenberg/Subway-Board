"""Options for LED Matrix Controller."""

import rgbmatrix

# Server address as a tuple of domain/ip and port.
SERVER_ADDRESS = '127.0.0.1', 7829

# Seconds to wait until displaying the offline icon.
TIMEOUT = 5

MATRIX_OPTIONS = rgbmatrix.RGBMatrixOptions()
MATRIX_OPTIONS.rows = 32
MATRIX_OPTIONS.cols = 64
MATRIX_OPTIONS.chain_length = 2
MATRIX_OPTIONS.brightness = 25

# Tested values for...
# RPi 2 B+ --- 0
# RPi 4 B+ --- 3
MATRIX_OPTIONS.gpio_slowdown = 3

# 'adafruit-hat-pwm' if you chose the "Quality" setting when running
# rgb-matrix.sh, 'adafruit-hat' otherwise.
MATRIX_OPTIONS.hardware_mapping = 'adafruit-hat-pwm'
