from pathlib import Path
from typing import Tuple, Self, Callable

from canvas import Coordinate, BaseCell
from canvas.data.BaseImageData import BaseImageData
from color import Color, Image, ImageLoader


class ImagePaletteData(BaseImageData):
    """
    Image data that has a specific size and a list of pixels
    """

    palette : ImagePalette
    index : int = 0

    def __init__(self, palette: ImagePalette, index: int = 0):
        self.palette = palette
        self.index = index

    def setIndex(self, new_index: int) -> Self:
        self.index = new_index
        return self

    @property
    def width(self):
        return self.palette.width

    @property
    def height(self):
        return self.palette.height

    @property
    def image(self):
        return self.palette.get(self.index)
