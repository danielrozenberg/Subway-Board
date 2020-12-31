"""Continously generate an ETA image for display on LED matrix."""

import logging

import animation
import deduper
import options
import serving
import networking
from networking import LineStopEtaMapping

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)

  updater = networking.Updater(options.MTA_API_ACCESS_KEY,
                               set(options.STOP_IDS_TO_NAMES),
                               options.ETA_RANGE)
  animator = animation.Animator(options.WIDTH, options.HEIGHT,
                                options.ROW_INTERVAL, options.SCROLL_INTERVAL,
                                options.STOP_IDS_TO_NAMES)
  server = serving.Server(options.PORT, animator)

  def on_update(etas: LineStopEtaMapping) -> None:
    deduper.dedup(etas, options.DEDUPING_PREFERENCES)
    animator.update_etas(etas)

  def on_error(_: Exception) -> None:
    animator.mark_offline()

  animator.start()
  server.start()

  updater.run(on_update, on_error)
