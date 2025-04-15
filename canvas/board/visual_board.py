from itertools import chain
from typing import Iterable, Tuple, List, Dict, Type, Self, Callable

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell
from canvas.coordinates.coordinate import Coordinate
from canvas.data.VisualData import VisualData


class VisualBoard[T: BaseCell, U: VisualData](BaseBoard):

    cell_visual_dimension: Tuple[int, int] # Width & Height of visual representation of cell

    def __init__(self, width: int, height: int, cells: Dict[Coordinate, T]) -> None:
        super().__init__(width, height, cells)

    def setCellVisualDimension(self, width: int, height: int) -> Self:
        self.cell_visual_dimension = width, height
        return self

    def getRgbRows(self) -> Iterable[List[Tuple[int, int, int]]]:
        cell: BaseCell[VisualData]

        for row in self.getRows():
            for y in range(self.cell_visual_dimension[1]):
                yield list(chain(*[cell.cell_data.getRowRGB(y) for cell in row]))

    def getRawRgbRows(self) -> List[List[int]]:
        return [[component for cell in row for component in cell] for row in self.getRgbRows()]

    @property
    def visual_width(self) -> int:
        return self._width * self.cell_visual_dimension[0]

    @property
    def visual_height(self) -> int:
        return self._height * self.cell_visual_dimension[1]

    @property
    def visual_size(self) -> (int, int):
        return self.visual_width, self.visual_height

    @classmethod
    def EMPTY(cls, width: int, height: int, cell_type: Type[VisualData]) -> "VisualBoard":
        def getNew(_: Coordinate):
            return BaseCell(cell_type.EMPTY())

        return cls.FROM(width, height, getNew, (cell_type.width, cell_type.height))

    @classmethod
    def FROM(cls, width: int, height: int, constructor: Callable[[Coordinate], BaseCell[VisualData]], cell_dimension: Tuple[int, int]) -> "VisualBoard":
        return cls(width, height, {coordinate: constructor(coordinate) for coordinate in Coordinate.getCoordinatesBox(width, height)}).setCellVisualDimension(*cell_dimension)