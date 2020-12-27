"""Socket server."""

import socket
import tempfile
import threading

import animation

_PORT = 7829


class Server:
  """Socket server that sends current frame from ETA image on every connection."""

  def __init__(self, port: int, animator: animation.Animator):
    self._port = port
    self._animator = animator

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind(('0.0.0.0', self._port))

  def start(self) -> None:
    """Starts the socket server in a background thread."""
    threading.Thread(target=self._start, daemon=True).start()

  def _start(self) -> None:
    """Serves the current frame on any socket connection."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind(('0.0.0.0', self._port))
      s.listen()
      self._animator.event_ready.wait()
      while True:
        conn, _ = s.accept()
        with conn:
          with tempfile.SpooledTemporaryFile(mode='w+b') as stf:
            self._animator.frame.save(stf, 'PNG')
            conn.sendfile(stf)
          conn.close()
