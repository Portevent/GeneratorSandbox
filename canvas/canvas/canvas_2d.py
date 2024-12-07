from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Callable, Iterator

from canvas.canvas import Canvas
from canvas.pixel import Pixel


Point2D = Tuple[int, int]

class Canvas2D[T: Pixel, Point: Point2D](Canvas, ABC):
    """
    Canvas2D is a finite two-dimensional canvas that can be drawn onto.
    It has a width and a height
    Point must be pairs of integers.
    """

    pixels: List[T]

    width: int
    height: int

    def __init__(self, width: int, height: int, constructor: Callable[[], T], pixels: List[T] | None = None):
        """
        Pixels are saved on a List
        """
        self.width = width
        self.height = height

        self.pixels = pixels or [constructor() for _ in range(width * height)]

    def _validPoint(self, point: Point) -> bool:
        if point[0] < 0:
            raise Exception(f"X ({point[0]}) too small")
        if point[0] >= self.width:
            raise Exception(f"X ({point[0]}) too big")
        if point[1] < 0:
            raise Exception(f"Y ({point[1]}) too small")
        if point[1] > self.height:
            raise Exception(f"Y ({point[1]}) too big")

        return True

    def _getPixel(self, point: Point) -> T:
        return self.pixels[point[0] + (point[1] * self.width)]

    def _setPixel(self, point: Point, pixel: T):
        self.pixels[point[0] + (point[1] * self.width)] = pixel

    def get_rows(self) -> Iterator[List[T]]:
        for i in range(0, self.width * self.height, self.width):
            yield self.pixels[i: i + self.width]

    def get_points_in(self, pointA: Point, pointB: Point) -> Iterator[Point]:
        for x in range(pointA[0], pointB[0]):
            for y in range(pointA[1], pointB[1]):
                yield x, y