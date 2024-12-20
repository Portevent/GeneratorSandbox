from __future__ import annotations

from abc import abstractmethod
from typing import Tuple, List, Self

from canvas.pixel.pixel import Point
from canvas.pixel.simple_pixel import SimplePixel


class LinkedPixel[T](SimplePixel):
    """
    LinkedPixel is an interface that represent linked pixel
    """

    neighbors: List[Self | None]
    neighborsSize: int

    def __init__(self, element: T | None = None, point: Point | None = None) -> None:
        super().__init__(element, point)
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