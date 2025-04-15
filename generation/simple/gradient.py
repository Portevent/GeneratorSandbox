from typing import Iterator

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell
from canvas.coordinates.coordinate import Coordinate
from canvas.data import PixelData
from color import Color
from generation.generator import Generator


class Gradient[T: BaseBoard[BaseCell[PixelData]]](Generator):
    """
    Fill a 2D Board area with a certain Pixel
    """

    iterator: Iterator[BaseCell]
    start: Coordinate
    end: Coordinate
    colorA: Color
    colorB: Color

    def __init__(self, start: Coordinate, end: Coordinate, colorA: Color, colorB: Color, **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.colorA = colorA
        self.colorB = colorB
        self.distance = Coordinate.Distance(start, end)

    def initialize(self, **kwargs):
        self.iterator = self.board.getCoordinatesAndCellsInBox(self.start, self.end)

    def step(self) -> bool:
        coordinate: Coordinate
        cell: BaseCell[PixelData]
        coordinate, cell = next(self.iterator, (None, None))

        if cell is None:
            return False

        cell.cell_data.setColor(Color.mix(self.colorA, self.colorB, Coordinate.Distance(coordinate, self.start) / self.distance))
        return True
