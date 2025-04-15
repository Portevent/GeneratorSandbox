from typing import Tuple, Self, List, Callable

from canvas import Coordinate, BaseCell
from canvas.data.VisualData import VisualData
from color import Color


class ImageData(VisualData):
    """
    Image data that has a specific size and a list of pixels
    """

    width = 1
    height = 1

    image: List[List[Color]] = []

    def __init__(self, width, height, image: List[List[Color]]):
        self.width = width
        self.height = height
        self.image = image

    def getRGB(self, x: int, y: int) -> Tuple[int, int, int]:
        """
        Returns the RGB value of a pixel at (x, y).
        :param x:
        :param y:
        :return:
        """
        return self.image[x][y].to_rgb()

    def setImage(self, image: List[List[Color]]) -> Self:
        self.image = image
        return self

    def fillColor(self, color: Color) -> Self:
        self.image = [[color for x in range(self.width)] for y in range(self.height)]
        return self

    @classmethod
    def EMPTY(cls, width: int = 1, height: int = 1) -> "ImageData":
        return cls(width, height, image=[]).fillColor(Color.BLACK())

    @classmethod
    def CreateEmpty(cls, width: int = 1, height: int = 1) -> Callable[[Coordinate], BaseCell["ImageData"]]:
        def creator(_: Coordinate) -> BaseCell[ImageData]:
            return BaseCell(cls.EMPTY(width, height))

        return creator
