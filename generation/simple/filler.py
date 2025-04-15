from typing import Iterator

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell
from canvas.coordinates.coordinate import Coordinate
from canvas.data import PixelData
from color import Color
from generation.generator import Generator


class Filler[T: BaseBoard[BaseCell[PixelData]]](Generator):
    """
    Fill a 2D Board area with a certain Pixel
    """

    iterator: Iterator[BaseCell]
    start: Coordinate
    end: Coordinate
    fillWith: Color

    def __init__(self, start: Coordinate, end: Coordinate, fillWith: Color, **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.fillWith = fillWith

    def initialize(self, **kwargs):
        self.iterator = self.board.getCellsInBox(self.start, self.end)

    def step(self) -> bool:
        cell: BaseCell[PixelData] = next(self.iterator, None)

        if cell is None:
            return False

        cell.cell_data.setColor(self.fillWith)
        return True
