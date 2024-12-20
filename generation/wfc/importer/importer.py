from typing import Dict, List

from canvas import Canvas, Color, LinkedPixel
from generation.wfc.module import Module


class WfModulesImporter:
    colors: List[Color] = []
    def __init__(self):
        self.colors = []

    def getColorId(self, pixel: LinkedPixel[Color]):
        if pixel is None:
            return -1
        try:
            return self.colors.index(pixel.element)
        except ValueError:
            self.colors.append(pixel.element)
            return len(self.colors) - 1

    def fromCanvas(self, canvas: Canvas[LinkedPixel[Color]]):
        modules: Dict[int, Module] = {}

        pixel: LinkedPixel[Color]
        for index, pixel in enumerate(canvas.getPixels()):

            colorId: int = self.getColorId(pixel)

            modules[index] = Module(index, colorId, list(map(self.getColorId, pixel.getNeighbors())))

        return modules, self.colors

