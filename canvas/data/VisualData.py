from abc import ABC, abstractclassmethod, abstractmethod
from typing import Tuple, List


class VisualData(ABC):
    """
    Visual Data are CellData that can be visuallized by a image (1x1 image for simple pixel data)
    """

    def getRGB(self, x: int, y: int) -> Tuple[int, int, int]:
        """
        Returns the RGB value of a pixel at (x, y).
        :param x:
        :param y:
        :return:
        """
        raise NotImplementedError

    def getRowRGB(self, y: int) -> List[Tuple[int, int, int]]:
        return [self.getRGB(x, y) for x in range(0, self.width)]

    @abstractmethod
    def width(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def height(self) -> int:
        raise NotImplementedError
