from __future__ import annotations

from abc import ABC
from random import random
from typing import Iterator, Dict, List

from canvas.pixel import Pixel
from canvas.pixel.pixel import Point


class Canvas[T: Pixel](ABC):
    """
    Canvas represent set of Point each having a Pixel
    """
    _width: int
    _height: int
    _pixels: Dict[Point, T]

    def __init__(self, width: int, height: int, pixels: Dict[Point, T]) -> None:
        self._width = width
        self._height = height
        self._pixels = pixels

    def _validPoint(self, point: Point) -> bool:
        """
        Assert a point is valid
        """
        return 0 <= point[0] < self._width and 0 <= point[1] < self._height

    def get(self, point: Point) -> T:
        """
        Get the pixel at the given point.
        :return: Element
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")

        return self._pixels[point]

    def set(self, point: Point, pixel: T):
        """
        Set the pixel at the given point.
        :param point: Point
        :param pixel: Pixel
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")

        self._pixels[point] = pixel

    def update(self, point: Point, pixel: T):
        """
        Update the pixel at the given point.
        :param point: Point
        :param pixel: Pixel
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")

        return self._pixels[point].update(pixel)

    def getPixelsIn(self, pointA: Point, pointB: Point) -> Iterator[T]:
        for x in range(pointA[0], pointB[0] + 1):
            for y in range(pointA[1], pointB[1] + 1):
                yield self.get((x, y))

    def getRows(self) -> Iterator[List[Pixel]]:
        for row in range(self._height):
            yield [self.get((x, row)) for x in range(self._width)]

    def _constrainPoint(self, point: Point) -> Point:
        """
        Constrain a point within the bounds of the canvas
        :param point: Point to be constrained
        :return: Original point, or closest point inside canvas
        """
        return max(0, min(self.width, point[0])), max(0, min(self.height, point[1]))

    def getRandomPoint(self) -> Point:
        return int(random() * self.width), int(random() * self.height)

    def getRandomPointAround(self, point: Point, maxOffset: int) -> Point:
        return self._constrainPoint((int(point[0] + (random()-0.5) * maxOffset), int(point[1] + (random()-0.5) * maxOffset)))

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height