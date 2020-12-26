"""Generate images from ETAs."""

import os
from typing import Dict, Iterable, Mapping

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import networking
from networking import LineStopEtaMapping
import sorter


class Imager:
  """Generate images from ETAs."""

  def __init__(self, width: int, stop_names: Mapping[str, str]):
    """Constructor.

    Args:
      width: in pixels.
      stop_names: mapping from stop ID to the display name, based on csv file
        https://atisdata.s3.amazonaws.com/Station/Stations.csv.
    """
    self._width = width
    self._stop_names = stop_names
    self._image_assets: Dict[str, Image.Image] = {}

    directory = os.path.dirname(__file__)
    self._stop_name_font = ImageFont.truetype(os.path.join(
        directory, 'third_party/canonical/Ubuntu-M.ttf'),
                                              size=11)
    self._eta_font = ImageFont.truetype(os.path.join(
        directory, 'third_party/canonical/Ubuntu-B.ttf'),
                                        size=11)

  def draw(self, etas: LineStopEtaMapping) -> Image.Image:
    """Draws the full (uncropped) ETAs image."""
    self._load_assets(line_stop.route_id for line_stop in etas)

    image = Image.new('RGB', (self._width, len(etas) * 16))
    draw = ImageDraw.Draw(image)

    row_y_start = 0
    for named_line_stop, minutes in sorter.by_order(etas, self._stop_names):
      image.paste(self._image_assets[named_line_stop.route_id],
                  (0, row_y_start))
      if named_line_stop.direction == networking.Direction.NORTHBOUND:
        image.paste(self._image_assets['up'], (18, row_y_start + 4))
      else:
        image.paste(self._image_assets['down'], (18, row_y_start + 4))
      minutes_text = ', '.join(str(m) for m in sorted(minutes)[:3])

      draw.text((32, row_y_start + 1),
                named_line_stop.stop_name,
                fill=0xbbbbbb,
                font=self._stop_name_font)
      draw.text((self._width - 2, row_y_start + 1),
                minutes_text,
                fill=0xffffff,
                font=self._eta_font,
                anchor='ra')
      row_y_start += 16

    return image

  def _load_assets(self, route_ids: Iterable[str]) -> None:
    """Loads line bullet images."""
    directory = os.path.dirname(__file__)
    for arrow in ('up', 'down'):
      if arrow not in self._image_assets:
        filepath = os.path.join(directory, 'images', f'{arrow}.png')
        self._image_assets[arrow] = Image.open(filepath)

    for route_id in set(route_ids) - set(self._image_assets):
      filepath = os.path.join(directory, 'third_party/louh/mta-subway-bullets',
                              f'{route_id}.png')
      self._image_assets[route_id] = Image.open(filepath)
