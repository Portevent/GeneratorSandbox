from abc import ABC
from typing import Iterator, Self, Callable

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell
from canvas.coordinates.coordinate import Coordinate
from canvas.data import PixelData
from generation.generator import Generator


class Filler[T: BaseBoard](Generator, ABC):
    """
    Fill a 2D Board area with a certain Pixel
    """

    iterator: Iterator[Coordinate]
    start: Coordinate
    end: Coordinate

    callback: Callable[[Coordinate, BaseCell, float], None | bool] = None
    distance: int | None = None

    def __init__(self, start: Coordinate | None = None, end: Coordinate | None = None,
                 seed: float | None = None,
                 board: T | None = None):
        super().__init__(seed, board)
        self.start = start
        self.end = end

    def startAt(self, start: Coordinate | None = None) -> Self:
        self.start = start
        return self

    def endAt(self, end: Coordinate | None = None) -> Self:
        self.end = end
        return self

    def do(self, callback: Callable[[Coordinate, BaseCell, float], None | bool]) -> Self:
        self.callback = callback
        return self

    def initialize(self, **kwargs):
        self.iterator = self.board.getCoordinatesAndCellsInBox(self.start, self.end)
        self.distance = Coordinate.Distance(self.start, self.end)

    def step(self) -> bool:
        coordinate: Coordinate
        cell: BaseCell[PixelData]
        coordinate, cell = next(self.iterator, (None, None))

        if cell is None:
            return False

        if self.callback is not None:
            return self.callback(coordinate, cell, self._get_advancement(coordinate)) or True

        return True

    def _get_advancement(self, coordinate) -> float:
        return Coordinate.Distance(coordinate, self.start) / self.distance
