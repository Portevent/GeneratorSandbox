from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator, Dict, Tuple

from canvas.pixel import Pixel


class Canvas[T: Pixel, Point: Tuple](ABC):
    """
    Canvas represent set of Point each having a Pixel
    """

    pixels: Dict[Point, T]

    def __init__(self, pixels: Dict[Point, T] | None = None):
        self.pixels = pixels or {}

    @abstractmethod
    def _validPoint(self, point: Point) -> bool:
        """
        Assert a point is valid
        """
        raise NotImplementedError()

    @abstractmethod
    def _validPixel(self, pixel: T) -> bool:
        """
        Assert a pixel is valid
        """
        raise NotImplementedError()

    def get(self, point: Point) -> T:
        """
        Get the value at the given point.
        :return: Element
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")

        return self.pixels[point]

    def set(self, point: Point, pixel: T):
        """
        Set the pixel at the given point.
        :param point: Point
        :param pixel: Pixel
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")
        if not self._validPixel(pixel):
            raise Exception(f"{pixel} is not a valid pixel")

        return self.pixels[point] = pixel

    def update(self, point: Point, pixel: T):
        """
        Update the pixel at the given point.
        :param point: Point
        :param pixel: Pixel
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")
        if not self._validPixel(pixel):
            raise Exception(f"{pixel} is not a valid pixel")

        return self.pixels[point].update(pixel)

    @abstractmethod
    def getPointsIn(self, pointA: Point, pointB: Point) -> Iterator[Point]:
        """
        Get the sequence of points inside a rectangle.
        """
        raise NotImplementedError()

    def fill(self, pointA: Point, pointB: Point, pixel: Pixel):
        """
        Fill the area with the given element.
        :param pointA: From
        :param pointB: To
        :param pixel: Pixel (will be copied())
        """
        for point in self.getPointsIn(pointA, pointB):
            self.update(point, pixel)
