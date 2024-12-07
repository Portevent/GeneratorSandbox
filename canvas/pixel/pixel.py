from __future__ import annotations

from abc import ABC, abstractmethod

class Element(ABC):
    pass

class Pixel[T: Element](ABC):
    """
    Pixel is an interface that represent the content of a Point on a canvas.

    It must :
    1 --- Be able to be converted to a single Data (Gray tone, RGB, Palette) for painters
    2 --- Have a static method to create an empty Pixel
    3 - implements update() and set() to edit its content. But complex Pixels can have their own way of editing themselves

    """

    @abstractmethod
    def set(self, element: T) -> None:
        """
        Set the element.
        """
        raise NotImplementedError()

    @abstractmethod
    def get(self) -> T:
        """
        Get the element.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def empty() -> Pixel:
        """
        Create an empty pixel.
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self, other: Pixel):
        """
        Update the element with the other pixel.
        """
        raise NotImplementedError()