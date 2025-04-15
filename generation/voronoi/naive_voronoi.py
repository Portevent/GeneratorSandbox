from copy import copy
from typing import List

from board import Board, LinkedPixel
from board.pixel.pixel import Point, Pixel
from generation.voronoi.voronoi import Voronoi


class NaiveVoronoi[T: Board[LinkedPixel]](Voronoi):
    """
    Abstract Voronoi implementation that solves it naively
    """

    # Borders germs can expand from
    germsExpansion: List[LinkedPixel]

    def generateInitialGerms(self) -> List[Point]:
        """
        Divide the board into area (*germs_count* rows and *germs_count* columns)
        Generates one germs in each cell, randomly placed inside the cell
        """
        return [self.board.getRandomPoint() for _ in range(self.germsCount)]

    def initialize(self):
        super().initialize()
        self.germsExpansion = [self.board.get(point) for point in self.initialGerms]

    def step(self) -> bool:
        """
        Naive solution that expand germs to their empty neighbors until the board is filled
        """
        try:
            nextGerm = self.germsExpansion.pop(0)
            nextGerm.element.add(-2)
            for neighbor in nextGerm.getNeighbors():
                if neighbor is None:
                    continue

                if neighbor.element is None:
                    neighbor.element = copy(nextGerm.element)
                    self.germsExpansion.append(neighbor)

            return True

        except IndexError:
            return False