from abc import ABC, abstractmethod
from typing import List

from color import Color
from generation.generator import Generator



class Voronoi[T: Board] (Generator, ABC):
    """
    Abstract Voronoi class that defines the basis of a Voronoi Diagram
    """

    germsCount: int # Number of germs

    germsColor: List[Color] # Pixel representing each germ
    initialGerms: List[Point] # Initial germs

    def __init__ (self, germsCount: int | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.germsCount = germsCount

    def getGermColor(self, germ: int) -> Color:
        """
        Get the Color for a given germ and its variant
        :param germ: Germ number
        :return: Pixel
        """
        return self.germsColor[germ]

    def setGermAt(self, germ: int, point: Point) -> None:
        """
        Set a point to a specific germ on the board
        :param germ: Germ ID
        :param point: Point
        """
        self.board.get(point).element = self.getGermColor(germ)

    def initialize(self):
        self.initialGerms = self.generateInitialGerms()
        self.germsColor = self.generateGermsColors()

        for germ, point in enumerate(self.initialGerms):
            self.setGermAt(germ, point)

    def generateGermsColors(self) -> List[Color]:
        """
        Generate a Color for each germ
        """
        return PaletteHelper.distinctHue(self.germsCount).list()

    @abstractmethod
    def generateInitialGerms(self) -> List[Point]:
        """
        Generate initial germs
        """
        raise NotImplementedError