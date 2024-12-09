from __future__ import annotations

from abc import abstractmethod
from typing import Tuple, Callable, List

from canvas.pixel.pixel import Pixel


class LinkedPixel(Pixel):
    """
    LinkedPixel is an interface that represent linked pixel
    """

    neighbors: List[LinkedPixel | None]
    neighborsSize: int

    def __init__(self):
        self.neighbors = [None] * self.neighborsSize

    def getNeighbors(self) -> Tuple[LinkedPixel | None]:
        """
        Return neighbors
        :return: List of neighbors
        """
        return *self.neighbors,

    @abstractmethod
    def getOppositePosition(self, position: int) -> int:
        """
        Get the opposition position (as South for North, UpperLeft for BottomRight, etc)
        :param position: integer
        :return: Other way
        """
        raise NotImplementedError()

    def linkTo(self, other: LinkedPixel, position: int):
        """
        Link one pixel to another
        :param other: Pixel to link to
        :param position: Position of the other relative to self
        """
        self.neighbors[position] = other
        other.neighbors[self.getOppositePosition(position)] = self

    @staticmethod
    @abstractmethod
    def generate(constructor: Callable[[], LinkedPixel], **kwargs) -> Tuple[LinkedPixel]:
        """
        Generate linked pixels
        :param constructor:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()