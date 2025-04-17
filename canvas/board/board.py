from random import random
from typing import Dict, Iterator, List, Callable

from canvas.board.exceptions import BoardException
from canvas.cell.base_cell import BaseCell
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
            raise BoardException(f"{coordinate} is not a valid coordinate")

        return self._cells[coordinate]

    def set(self, cell: T, coordinate: Coordinate):
        """
        Set the cell at the given coordinate.
        :param cell: Cell
        :param coordinate: Coordinate
        """
        if not self._validCoordinate(coordinate):
            raise BoardException(f"{coordinate} is not a valid coordinate")

        self._cells[coordinate] = cell

    def getCellsInBox(self, start: Coordinate, end: Coordinate) -> Iterator[T]:
        """
        Iterate over cells within a rectangle.
        :param start: Coordinate of the top left corner of the box
        :param end: Coordinate of the bottom right corner of the box
        :return: cells
        """
        for coordinate in Coordinate.getCoordinatesInBox(start, end):
            yield self.get(coordinate)

    def getCoordinatesAndCellsInBox(self, start: Coordinate, end: Coordinate) -> Iterator[T]:
        """
        Iterate over cells within a rectangle.
        :param start: Coordinate of the top left corner of the box
        :param end: Coordinate of the bottom right corner of the box
        :return: coordinate and their corresponding cell.
        """
        for coordinate in Coordinate.getCoordinatesInBox(start, end):
            yield coordinate, self.get(coordinate)

    def getRows(self) -> Iterator[List[T]]:
        """
        Iterate over rows of the board.
        :return: Rows
        """
        for row in range(self._height):
            yield [self.get(Coordinate(x, row)) for x in range(self._width)]

    def getCells(self) -> Iterator[T]:
        """
        Iterate over all cells of the board.
        :return: Cells
        """
        yield from self._cells.values()

    def _constrainCoordinate(self, coordinate: Coordinate) -> Coordinate:
        """
        Constrain a coordinate within the bounds of the board
        :param coordinate: coordinate to be constrained
        :return: Original coordinate, or closest coordinate inside board
        """
        return Coordinate(max(0, min(self.width, coordinate.x)),
                          max(0, min(self.height, coordinate.y)))

    def getRandomCoordinate(self) -> Coordinate:
        """
        Get a random coordinate within the bounds of the board
        :return: Coordinate
        """
        return Coordinate(int(random() * self.width), int(random() * self.height))

    def getRandomCoordinateAround(self, coordinate: Coordinate, maxOffset: int) -> Coordinate:
        """
        Get a random coordinate within the bounds of the board, around the given coordinate.
        :param coordinate: Coordinate
        :param maxOffset: Maximum offset to add or remove
        :return: Coordinate
        """
        return self._constrainCoordinate(
            Coordinate(int(coordinate.x + (random() - 0.5) * 2 * maxOffset),
                       int(coordinate.y + (random() - 0.5) * 2 * maxOffset)))

    @property
    def width(self) -> int:
        """
        Get width of the board
        :return: int
        """
        return self._width

    @property
    def height(self) -> int:
        """
        Get height of the board
        :return: int
        """
        return self._height

    @classmethod
    def EMPTY(cls, width: int, height: int) -> "BaseBoard":
        """
        Create a BaseBoard with empty cells.
        :param width: Width of the board
        :param height: Height of the board
        :return: BaseBoard
        """
        return cls(width, height,
                   {coordinate: BaseCell(None)
                    for coordinate in Coordinate.getCoordinatesBox(width, height)}
                   )

    @classmethod
    def FROM(cls, width: int, height: int,
             constructor: Callable[[Coordinate], BaseCell]) -> "BaseBoard":
        """
        Create a BaseBoard of given width and height.
        Take a callback to assign each cell a value.
        :param width: Width of the board
        :param height: Height of the board
        :param constructor: Constructor function for each cell
        :return: BaseBoard
        """
        return cls(width, height,
                   {coordinate: constructor(coordinate)
                    for coordinate in Coordinate.getCoordinatesBox(width, height)})
