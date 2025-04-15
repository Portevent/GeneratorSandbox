from canvas.board.board import BaseBoard
from canvas.coordinates import Coordinate
from canvas.cell.base_cell import BaseCell

CellData = any

class SentientCell[T: CellData](BaseCell):
    """
    Sentient Cells are aware of their board and coordinates.
    They can ask their neighbors
    """

    coordinate: Coordinate
    board: BaseBoard

    def __init__(self, cell_data: T, coordinate: Coordinate, board: BaseBoard):
        super().__init__(cell_data)
        self.coordinate = coordinate
        self.board = board
