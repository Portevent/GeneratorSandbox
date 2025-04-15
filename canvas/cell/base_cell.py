
CellData = any

class BaseCell[T: CellData]:
    """
    Base Cell that contains data
    """

    _data: T

    def __init__(self, cell_data: T):
        self._data = cell_data

    @property
    def cell_data(self) -> T:
        return self._data

    @cell_data.setter
    def cell_data(self, cell_data: T):
        self._data = cell_data

