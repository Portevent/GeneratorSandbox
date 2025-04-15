from typing import Tuple, Self

from canvas.data.VisualData import VisualData
from color import Color


class PixelData(VisualData):
    """
    Simple color Pixel
    """

    width = 1
    height = 1

    color: Color = Color.BLACK()

    def getRGB(self, x: int, y: int) -> Tuple[int, int, int]:
        """
        Returns the RGB value of a pixel at (x, y).
        :param x:
        :param y:
        :return:
        """
        return self.color.to_rgb()

    def setColor(self, color: Color) -> Self:
        self.color = color
        return self



    @classmethod
    def EMPTY(cls) -> "PixelData":
        return cls().setColor(Color.BLACK())
