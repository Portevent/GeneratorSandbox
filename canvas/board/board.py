from random import random
from typing import Dict, Iterator, List, Callable

from ..cell.base_cell import BaseCell
from canvas.coordinates import Coordinate


class BaseBoard[T: BaseCell]:
    """
    BaseBoard represent set of BaseCell each having a Coordinate
    """

    _width: int
    _height: int
    _cells: Dict[Coordinate, T]

    def __init__(self, width: int, height: int, cells: Dict[Coordinate, T]) -> None:
        self._width = width
        self._height = height
        self._cells = cells

    def _validCoordinate(self, coordinate: Coordinate) -> bool:
        """
        Assert a cell is valid
        """
        return 0 <= coordinate.x < self._width and 0 <= coordinate.y < self._height

    def get(self, coordinate: Coordinate) -> T:
        """
        Get the cell at the given coordinate.
        :return: Cell
        """
        if not self._validCoordinate(coordinate):
            raise Exception(f"{coordinate} is not a valid coordinate")

        return self._cells[coordinate]

    def set(self, cell: T, coordinate: Coordinate):
        """
        Set the cell at the given coordinate.
        :param cell: Cell
        :param coordinate: Coordinate
        """
        if not self._validCoordinate(coordinate):
            raise Exception(f"{coordinate} is not a valid coordinate")

        self._cells.update(coordinate, cell)

    def getCellsInBox(self, coordinateA: Coordinate, coordinateB: Coordinate) -> Iterator[T]:
        for coordinate in Coordinate.getCoordinatesInBox(coordinateA, coordinateB):
            yield self.get(coordinate)

    def getRows(self) -> Iterator[List[T]]:
        for row in range(self._height):
            yield [self.get(Coordinate(x, row)) for x in range(self._width)]

    def getCells(self) -> Iterator[T]:
        for cell in self._cells.values():
            yield cell

    def _constrainCoordinate(self, coordinate: Coordinate) -> Coordinate:
        """
        Constrain a coordinate within the bounds of the board
        :param coordinate: coordinate to be constrained
        :return: Original coordinate, or closest coordinate inside board
        """
        return Coordinate(max(0, min(self.width, coordinate.x)), max(0, min(self.height, coordinate.y)))

    def getRandomCoordinate(self) -> Coordinate:
        return Coordinate(int(random() * self.width), int(random() * self.height))

    def getRandomCoordinateAround(self, coordinate: Coordinate, maxOffset: int) -> Coordinate:
        return self._constrainCoordinate(Coordinate(int(coordinate.x + (random()-0.5) * maxOffset), int(coordinate.y + (random()-0.5) * maxOffset)))

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @classmethod
    def EMPTY(cls, width: int, height: int) -> "BaseBoard":
        return cls(width, height, {coordinate: BaseCell(None) for coordinate in Coordinate.getCoordinatesBox(width, height)})

    @classmethod
    def FROM(cls, width: int, height: int, constructor: Callable[[Coordinate], BaseCell]) -> "BaseBoard":
        return cls(width, height, {coordinate: constructor(coordinate) for coordinate in Coordinate.getCoordinatesBox(width, height)})