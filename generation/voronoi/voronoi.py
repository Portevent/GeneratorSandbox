from abc import ABC, abstractmethod
from typing import List, Set, Tuple

from canvas import Point2D, Canvas2D, Pixel
from generation.generator import Generator

class Voronoi[T: Canvas2D, U: Point2D, V: Pixel] (Generator, ABC):
    """
    Abstract Voronoi class that defines the basis of a Voronoi Diagram
    """

    germsCount: int # Number of germs

    germsPixel: List[V] # Pixel representing each germ
    germsPoints: List[List[U]] # Set of point for each germ

    def __init__ (self, germsCount: int | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.germsCount = germsCount

    def getGermPixel(self, germ: int, variant: int = 0) -> V:
        """
        Get the Pixel for a given germ and its variant
        :param germ: Germ number
        :param variant: Variant
        :return: Pixel
        """
        return self.germsPixel[germ]

    def getGermId(self, pixel: V) -> int:
        """
        Get the id of the germ for a given pixel (-1 if pixel is empty)
        :param pixel: Pixel
        :return: Germ ID
        """
        try:
            return self.germsPixel.index(pixel)
        except ValueError:
            return -1

    def setGermAt(self, germ: int, point: Point2D) -> None:
        """
        Set a point to a specific germ on the canvas
        :param germ: Germ ID
        :param point: Point
        """
        self.germsPoints[germ].append(point)
        self.canvas.set(point, self.getGermPixel(germ))

    def setGermsAt(self, germ: int, points: List[Point2D] | Set[Point2D]) -> None:
        """
        Set germ on points
        :param germ: Germ ID
        :param points: Points
        """
        for point in points:
            self.setGermAt(germ, point)

    def getGermAt(self, point: Point2D) -> int:
        """
        Get the germ at specific point on the canvas
        :param point: Point
        :return: Germ ID
        """
        return self.getGermId(self.canvas.get(point))

    def initialize(self):
        germsPoints, self.germsCount = self.generateGerms(germsCount=self.germsCount)
        self.germsPixel = self.generateGermsPixels()

        self.germsPoints = [[] for _ in range(self.germsCount)]

        for germ, points in enumerate(germsPoints):
            self.setGermsAt(germ, points)

    @abstractmethod
    def generateGermsPixels(self) -> List[V]:
        """
        Generate a Pixel for each germ
        """
        raise NotImplementedError

    @abstractmethod
    def generateGerms(self, germsCount: int) -> Tuple[List[Set[U]], int]:
        """
        Generate initial germs
        """
        raise NotImplementedError