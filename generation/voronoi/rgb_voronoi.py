from abc import ABC
from typing import List

from canvas import Point2D, PaletteCanvas, IntPixel, Color, Palette, PaletteHelper

from generation.voronoi.voronoi import Voronoi

BLACK = Color(0, 0, 0)

class RgbVoronoi[T: RgbCanvas, U: Point2D, V: RgbPixel] (Voronoi, ABC):
    """
    Abstract Voronoi specification that works with Palette Canvas
    """

    def generateGermsPixels(self, **kwargs) -> List[V]:
        """
        Generate a Pixel for each germ
        """
        return [(i*20, 0, 0) for i in range(self.germsCount)]

    def getGermId(self, pixel: V) -> int:
        """
        Get the id of the germ for a given pixel (-1 if pixel is empty)
        :param pixel: Pixel
        :return: Germ ID
        """
        return pixel.get() - 1