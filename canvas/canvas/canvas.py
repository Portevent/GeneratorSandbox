from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator

from canvas.pixel import Pixel


class Canvas[T: Pixel, Point](ABC):
    """
    Canvas represent set of Point each having a Pixel
    """

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

    @abstractmethod
    def _getPixel(self, point: Point) -> T:
        """
        Get the pixel at the given point
        """
        raise NotImplementedError()

    @abstractmethod
    def _setPixel(self, point: Point, pixel: T):
        """
        Set the pixel at the given point
        """
        raise NotImplementedError()

    def get(self, point: Point) -> T:
        """
        Get the value at the given point.
        :return: Element
        """
        if not self._validPoint(point):
            raise Exception(f"{point} is not a valid coordinate")

        return self._getPixel(point)

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

        return self._setPixel(point, pixel)

    @abstractmethod
    def get_points_in(self, pointA: Point, pointB: Point) -> Iterator[Point]:
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
        if not self._validPoint(pointA):
            raise Exception(f"{pointA} is not a valid coordinate")
        if not self._validPoint(pointB):
            raise Exception(f"{pointB} is not a valid coordinate")
        for point in self.get_points_in(pointA, pointB):
            self._getPixel(point).update(pixel)
