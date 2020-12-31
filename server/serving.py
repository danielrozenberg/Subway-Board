"""Socket server."""

import logging
import socket
import threading

import animation

_PORT = 7829

_logger = logging.getLogger('subway_board.serving')


class Server:
  """Socket server that sends current frame from ETA image on every connection."""

  def __init__(self, port: int, animator: animation.Animator):
    self._port = port
    self._animator = animator

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      _logger.info('Verifying that the socket can be bound to port %d...',
                   self._port)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s.bind(('0.0.0.0', self._port))
      _logger.info('... verified!')

  def start(self) -> None:
    """Starts the socket server in a background thread."""
    threading.Thread(target=self._start, daemon=True).start()

  def _start(self) -> None:
    """Serves the current frame on any socket connection."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      _logger.info('Listening on port %d', self._port)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      s.bind(('0.0.0.0', self._port))
      s.listen()

      _logger.info('Waiting for the animator to be ready to produce frames...')
      self._animator.event_ready.wait()
      _logger.info('... ready!')

      while True:
        self._connect_and_produce(s)

  def _connect_and_produce(self, s: socket.socket) -> None:
    """Connects with the client and produces image bytes for it."""
    _logger.info('Waiting for a client to connect...')
    try:
      conn, _ = s.accept()
      with conn:
        while True:
          # Wait for a signal from the client.
          conn.recv(1)

          # Now wait for the next frame. This could be a few seconds or
          # immediate, depending on whether the animation is currently static
          # or in scroll.
          frame = self._animator.wait_for_new_frame()
          conn.send(frame.tobytes())
    except ConnectionError as e:
      _logger.info('Client disconnected: %s', e)
