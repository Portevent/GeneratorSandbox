from abc import ABC
from typing import List

from canvas import Point2D, PaletteCanvas, IntPixel, Color, Palette, PaletteHelper

from generation.voronoi.voronoi import Voronoi

BLACK = Color(0, 0, 0)

class PaletteVoronoi[T: PaletteCanvas, U: Point2D, V: IntPixel] (Voronoi, ABC):
    """
    Abstract Voronoi specification that works with Palette Canvas
    """

    def generateGermsPixels(self, **kwargs) -> List[V]:
        """
        Generate a Pixel for each germ
        """
        palette = Palette()
        palette.save(BLACK)
        PaletteHelper.distinctHue(self.germsCount, palette=palette)
        self.canvas.setPalette(palette)
        return [IntPixel(i) for i in range(1, self.germsCount+1)]

    def getGermId(self, pixel: V) -> int:
        """
        Get the id of the germ for a given pixel (-1 if pixel is empty)
        :param pixel: Pixel
        :return: Germ ID
        """
        return pixel.get() - 1