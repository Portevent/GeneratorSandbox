from typing import Tuple

from canvas.data.VisualData import VisualData
from color import Image


class BaseImageData(VisualData):
    """
    Image data that has a specific size and a list of pixels
    """

    def getRGB(self, x: int, y: int) -> Tuple[int, int, int]:
        """
        Returns the RGB value of a pixel at (x, y).
        :param x:
        :param y:
        :return:
        """
        _x, _y = x, y
        return self.image[_y][_x].to_rgb()

    @property
    def image(self) -> Image:
        raise NotImplementedError
