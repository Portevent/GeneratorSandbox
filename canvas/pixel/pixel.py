from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, Tuple, Dict

from canvas.pixel.color import Color

Point = Tuple[int, int]

class Pixel[T](ABC):
    """
    Pixel is an interface that represent the content of a Point on a canvas.

    It must :
    1 --- Be able to be converted to a single Data (Gray tone, RGB, Palette) for painters
    2 --- Have a static method to create an empty Pixel
    3 - implements update() and set() to edit its content. But complex Pixels can have their own way of editing themselves

    """

    _element: T | None
    _point: Point | None

    def __init__(self, element: T | None = None, point: Point | None = None) -> None:
        self._element = element
        self._point = point

    def __str__(self):
        return f"[{self._point} : {self._element}]"

    @property
    def element(self) -> T:
        return self._element

    @property
    def point(self) -> Point:
        return self._point

    @element.setter
    def element(self, element: T):
        self._element = element

    @point.setter
    def point(self, point: Point):
        self._point = point

    def update(self, other: Pixel):
        """
        Update the element with the other pixel.
        """
        self._element = other._element

    @staticmethod
    @abstractmethod
    def generate(width: int, height: int, empty: Callable[[Tuple], Pixel] | None = None) -> Dict[Tuple, Pixel]:
        """
        Generate a dictionary of pixels
        """
        raise NotImplementedError()

    @abstractmethod
    def getColor(self) -> Tuple[int, int, int]:
        raise NotImplementedError()