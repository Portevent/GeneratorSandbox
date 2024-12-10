from abc import ABC
from typing import List, Tuple

from canvas import Canvas2D, Point2D, Pixel
from generation.voronoi.voronoi import Voronoi


class NaiveListVoronoi[T: Canvas2D, U: Point2D, V: Pixel](Voronoi, ABC):
    """
    Abstract Voronoi implementation that solves it naively using List
    """
    germsPoints: List[List[U]] # Set of point for each germ

    # Borders each germ can expand from
    germsExpansion: List[List[U]]

    def generateGerms(self, germsCount: int) -> Tuple[List[List[U]], int]:
        """
        Divide the canvas into area (*germs_count* rows and *germs_count* columns)
        Generates one germs in each cell, randomly placed inside the cell
        """
        germs = []

        hStep: int = int(self.canvas.width / germsCount)
        vStep: int = int(self.canvas.height / germsCount)
        for x in range(int(hStep / 2), self.canvas.width, hStep):
            for y in range(int(vStep / 2), self.canvas.height, vStep):
                point = self.canvas.getRandomPointAround((x, y), hStep, vStep)
                germs.append([point])

        return germs, germsCount**2

    def initialize(self):
        super().initialize()
        self.germsExpansion = [germ.copy() for germ in self.germsPoints]

    def step(self) -> bool:
        """
        Naive solution that expand germs to their empty neighbors until the canvas is filled
        """
        newGerm = False

        newExpansion = [[] for _ in range(self.germsCount)]

        for germId, borders in enumerate(self.germsExpansion):
            for border in borders:
                for point in self.canvas.getNeighbor(border):
                    if self.getGermAt(point) != -1:
                        continue

                    self.setGermAt(germId, point)
                    newExpansion[germId].append(point)
                    newGerm = True

        self.germsExpansion = newExpansion

        return newGerm

