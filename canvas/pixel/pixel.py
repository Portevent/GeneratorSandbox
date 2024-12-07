from __future__ import annotations

from abc import ABC, abstractmethod

class Element(ABC):
    pass

class Pixel(ABC):

    @abstractmethod
    def set(self, element: Element) -> None:
        """
        Set the element.
        """
        raise NotImplementedError()

    @abstractmethod
    def get(self) -> Element:
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