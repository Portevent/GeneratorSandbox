from itertools import chain
from typing import Iterable, Tuple, List, Type, Self, Callable

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell
from canvas.coordinates.coordinate import Coordinate
from canvas.data.VisualData import VisualData


class VisualBoard[T: BaseCell, U: VisualData](BaseBoard):
    """
    VisualBoard are specific BaseBoard than contains VisualData.
    They can be exported by painter.
    They require to specify cell visual dimension (1x1 for pixels for instance)
    """
    cell_visual_dimension: Tuple[int, int]  # Width & Height of visual representation of cell

    def setCellVisualDimension(self, width: int, height: int) -> Self:
        """
        Set cell visual dimension.
        :param width: width of cell visual dimension
        :param height: height of cell visual dimension
        """
        self.cell_visual_dimension = width, height
        return self

    def getRgbRows(self) -> Iterable[List[Tuple[int, int, int]]]:
        """
        Return each row has a list of pixel tuples. Each pixel is a tuple of r, g & b
        :return: iterator over lists of tuples
        """
        cell: BaseCell[VisualData]

        for row in self.getRows():
            for y in range(self.cell_visual_dimension[1]):
                yield list(chain(*[cell.cell_data.getRowRGB(y) for cell in row]))

    def getRawRgbRows(self) -> List[List[int]]:
        """
        Return each row as a flat list of each pixel r, g and b
        :return: iterator over lists of integers
        """
        return [[component for cell in row for component in cell] for row in self.getRgbRows()]

    @property
    def visual_width(self) -> int:
        """
        Return visual width of board (number of cell * width of a cell visual representation)
        :return: visual width of board
        """
        return self._width * self.cell_visual_dimension[0]

    @property
    def visual_height(self) -> int:
        """
        Return visual height of board (number of cell * height of a cell visual representation)
        :return: visual height of board
        """
        return self._height * self.cell_visual_dimension[1]

    @property
    def visual_size(self) -> (int, int):
        """
        Return visual width and visual height of board.
        :return: int, int
        """
        return self.visual_width, self.visual_height

    @classmethod
    def EMPTY(cls, width: int, height: int, cell_type: Type[VisualData]) -> "VisualBoard":
        """
        Create empty visual board from a cell_type
        Note : will infer visual width & height of cell base on cell_type width and height.
        So a size consistent type must be given (i.e. : Pixel).
        :return: VisualBoard
        """

        def getNew(_: Coordinate):
            return BaseCell(cell_type.EMPTY())

        return cls.FROM(width, height, getNew, (cell_type.width, cell_type.height))

    @classmethod
    def FROM(cls, width: int, height: int,
             constructor: Callable[[Coordinate], BaseCell[VisualData]],
             cell_dimension: Tuple[int, int]) -> "VisualBoard":
        """
        Create visual board from width, height, cell's factory callback and cell visual dimension.
        :return: VisualBoard
        """
        return (cls(width, height, {coordinate: constructor(coordinate)
                                    for coordinate in Coordinate.getCoordinatesBox(width, height)})
                .setCellVisualDimension(*cell_dimension))
