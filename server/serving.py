"""Socket server."""

import logging
import socketserver
import threading

import animation

_PORT = 7829

_logger = logging.getLogger('subway_board.serving')


class _TCPServer(socketserver.TCPServer):

  allow_reuse_address = True


class Server:
  """Socket server that sends current frame from ETA image on every connection."""

  def __init__(self, port: int, animator: animation.Animator):
    self._port = port
    self._animator = animator

    class Handler(socketserver.StreamRequestHandler):
      """Handle TCP requests."""

      def setup(self) -> None:
        super().setup()
        _logger.info('Client %s connected', self.client_address)
        self._animator = animator

      def handle(self) -> None:
        try:
          while True:
            # Wait for the client to send a newline, indicating it's ready for
            # the next frame.
            self.rfile.readline()

            # Now wait for the next frame before sending data. This could be a
            # few seconds or immediate, depending on whether the animation is
            # currently static or in scroll.
            frame = self._animator.wait_for_new_frame()
            self.wfile.write(frame.tobytes())
        except ConnectionError as e:
          _logger.error('Connection error: %s', e)

    self._handler_class = Handler

  def start(self) -> None:
    """Starts the socket server in a background thread."""
    threading.Thread(target=self._start, daemon=True).start()

  def _start(self) -> None:
    """Serves the current frame on any socket connection."""
    _logger.info('Waiting for the animator to be ready to produce frames...')
    self._animator.event_ready.wait()
    _logger.info('... ready!')

    with _TCPServer(('0.0.0.0', self._port), self._handler_class) as server:
      _logger.info('Listening on port %d', self._port)
      server.serve_forever()
