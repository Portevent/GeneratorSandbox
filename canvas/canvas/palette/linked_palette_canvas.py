from typing import List, Callable

from canvas import PaletteCanvas, LinkedCanvas2D
from canvas.canvas import Canvas2D
from canvas.canvas.cartesian_canvas import Point2D
from canvas.canvas.palette.palette import Palette
from canvas.pixel.int_pixel import IntPixel


class LinkedPaletteCanvas[T: IntPixel, Point: Point2D](LinkedCanvas2D, PaletteCanvas):
    pass
