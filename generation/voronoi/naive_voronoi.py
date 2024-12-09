from abc import ABC
from typing import Set, List, Tuple

from canvas import Canvas2D, Point2D, Pixel
from generation.voronoi.voronoi import Voronoi


class NaiveVoronoi[T: Canvas2D, U: Point2D, V: Pixel](Voronoi, ABC):
    """
    Abstract Voronoi implementation that solves it naively
    """

    # Borders each germ can expand from
    germsExpansion: List[Set[U]]

    # Previous expansion to avoid traceback
    previousExpansion: Set[U]

    def generateGerms(self, germsCount: int) -> Tuple[List[Set[U]], int]:
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
                germs.append({point})

        return germs, germsCount**2

    def initialize(self):
        super().initialize()
        self.germsExpansion = self.germsPoints
        self.previousExpansion = set()

    def step(self) -> bool:
        """
        Naive solution that expand germs to their empty neighbors until the canvas is filled
        """
        newGerm = False

        currentExpansion = set().union(*self.germsExpansion)
        newExpansion = [set() for _ in range(self.germsCount)]


        avoid = self.previousExpansion.union(currentExpansion)

        for germId, border in enumerate(self.germsExpansion):
            for point in self.canvas.getNeighbors(border, avoid):
                if self.getGermAt(point) != -1:
                    continue

                self.setGermAt(germId, point)
                newExpansion[germId].add(point)
                newGerm = True

        self.previousExpansion = currentExpansion
        self.germsExpansion = newExpansion

        return newGerm

