from pathlib import Path
from typing import Tuple, Self, Callable

from canvas import Coordinate, BaseCell
from canvas.data.ImageData import ImageData
from color import Color, Image, ImageLoader


class ImagePaletteData(ImageData):
    """
    Image data that has a specific size and a list of pixels
    """

    width = 1
    height = 1

    image: Image = []

    def __init__(self, width, height, image: Image):
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
        return self.image[y][x].to_rgb()

    def setImage(self, image: Image) -> Self:
        self.image = image
        return self

    def fillColor(self, color: Color) -> Self:
        self.image = [[color for x in range(self.width)] for y in range(self.height)]
        return self

    @classmethod
    def EMPTY(cls, width: int = 1, height: int = 1) -> "ImageData":
        return cls(width, height, image=[]).fillColor(Color.BLACK())

    @classmethod
    def CreateEmpty(cls, width: int = 1, height: int = 1) \
            -> Callable[[Coordinate], BaseCell["ImageData"]]:
        def creator(_: Coordinate) -> BaseCell[ImageData]:
            return BaseCell(cls.EMPTY(width, height))

        return creator

    @classmethod
    def FromFile(cls, filename: str | Path) -> "ImageData":
        image, width, height = ImageLoader.from_file(filename)
        return cls(width, height, image)