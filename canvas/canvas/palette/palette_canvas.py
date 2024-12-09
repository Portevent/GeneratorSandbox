from typing import List, Callable

from canvas.canvas import Canvas2D
from canvas.canvas.canvas_2d import Point2D
from canvas.canvas.palette.palette import Palette
from canvas.pixel.int_pixel import IntPixel


class PaletteCanvas[T: IntPixel, Point: Point2D](Canvas2D):
    palette: Palette

    def __init__(self, width: int, height: int, palette: Palette, constructor: Callable[[], T],
                 pixels: List[T] | None = None):
        self.palette = palette
        super().__init__(width, height, constructor, pixels)

    def setPalette(self, palette: Palette):
        """
        Sets the palette
        :param palette: Palette
        """
        self.palette = palette

    def shift_pixel(self, value: int, point: Point):
        self.set(self.get(point) + value, point)

    def _validPixel(self, element: IntPixel) -> bool:
        return self.palette.size > element.get() >= 0
