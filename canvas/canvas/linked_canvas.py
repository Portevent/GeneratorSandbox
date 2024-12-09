from __future__ import annotations

from abc import ABC
from typing import List, Callable, Set

from canvas import Point2D, Canvas2D
from canvas.pixel.linked_pixel import LinkedPixel


class LinkedCanvas2D[T: LinkedPixel, Point: Point2D](Canvas2D, ABC):
    """
    LinkedCanvas2D is a Canvas2D where pixels are linked together
    """

    pixels: List[T]

    width: int
    height: int

    # Screw base __init__
    # noinspection PyMissingConstructor
    def __init__(self, width: int, height: int, constructor: Callable[[int, int], List[T]]):
        """
        Pixels are saved on a List
        """
        self.width = width
        self.height = height

        self.pixels = constructor(width, height)