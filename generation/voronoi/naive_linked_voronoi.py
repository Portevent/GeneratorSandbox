from abc import ABC
from typing import List, Tuple

from canvas import Point2D, LinkedCanvas2D, LinkedPixel
from generation.voronoi.voronoi import Voronoi


class NaiveLinkedVoronoi[T: LinkedCanvas2D, U: Point2D, V: LinkedPixel](Voronoi, ABC):
    """
    Abstract Voronoi implementation that solves it naively using Linked Canvas.
    """
    germsPixels: List[List[V]] # Set of point for each germ

    # Borders each germ can expand from
    germsExpansion: List[List[V]]

    def generateGerms(self, germsCount: int) -> Tuple[List[List[V]], int]:
        """
        Divide the canvas into area (*germs_count* rows and *germs_count* columns)
        Generates one germs in each cell, randomly placed inside the cell
        :type germsCount: object
        """
        germs = []

        hStep: int = int(self.canvas.width / germsCount)
        vStep: int = int(self.canvas.height / germsCount)
        for x in range(int(hStep / 2), self.canvas.width, hStep):
            for y in range(int(vStep / 2), self.canvas.height, vStep):
                germs.append([self.canvas.get(self.canvas.getRandomPointAround((x, y), hStep, vStep))])

        return germs, germsCount**2

    def initialize(self):
        germsPixels, self.germsCount = self.generateGerms(germsCount=self.germsCount)
        self.germsPixel = self.generateGermsPixels()

        self.germsPoints = [[] for _ in range(self.germsCount)]
        self.germsExpansion = [[] for _ in range(self.germsCount)]
        for germ, pixels in enumerate(germsPixels):
            for pixel in pixels:
                self.setGermAtPixel(germ, pixel)
                self.germsExpansion[germ].append(pixel)

    def step(self) -> bool:
        """
        Naive solution that expand germs to their empty neighbors until the canvas is filled
        """
        newGerm = False

        newExpansion = [[] for _ in range(self.germsCount)]

        for germId, borders in enumerate(self.germsExpansion):
            for border in borders:
                for pixel in border.getNeighbors():
                    if not pixel or pixel.get() != 0:
                        continue

                    self.setGermAtPixel(germId, pixel)
                    newExpansion[germId].append(pixel)
                    newGerm = True

        self.germsExpansion = newExpansion

        return newGerm

    def setGermAtPixel(self, germId: int, pixel: V):
        """
        Set germ inside pixel
        :param germId:
        :param pixel:
        :return:
        """
        pixel.update(self.getGermPixel(germId))
        self.germsPoints[germId].append(pixel)

