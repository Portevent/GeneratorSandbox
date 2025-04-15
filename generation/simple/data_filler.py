from typing import Self, Callable

from canvas.board.board import BaseBoard
from canvas.cell.base_cell import BaseCell, CellData
from canvas.coordinates.coordinate import Coordinate
from generation.simple.filler import Filler


class DataFiller[T: BaseBoard[BaseCell]](Filler):
    """
    Filler for cell_data
    """

    data: CellData

    def fillWith(self, data: CellData) -> Self:
        def setData(_: Coordinate, cell: BaseCell, _ad):
            cell.cell_data = data

        self.do(setData)
        return self

    def fillWithCallback(self, data: Callable[[Coordinate, BaseCell], CellData]) -> Self:
        def setData(coordinate: Coordinate, cell: BaseCell, advancement: float):
            cell.cell_data = data(coordinate, cell, advancement)

        self.do(setData)
        return self