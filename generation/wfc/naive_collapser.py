from typing import List, Set

from canvas import Color
from canvas.pixel.wave_pixel import WavePixel
from generation import Generator

def notCollapsed(pixel: WavePixel):
    return not pixel.collapsed

class NaiveCollapser(Generator):

    pixelsToCollapse: Set[WavePixel]

    def initialize(self, **kwargs):
        self.pixelsToCollapse = {self.canvas.get(self.canvas.getRandomPoint())}

    def step(self) -> bool:
        self.pixelsToCollapse = set(filter(notCollapsed, self.pixelsToCollapse))

        minPixel = None
        for pixel in iter(self.pixelsToCollapse):
            if minPixel is None or pixel.entropy < minPixel.entropy:
                minPixel = pixel
            if minPixel.entropy <= 1:
                break

        if minPixel is None:
            return False

        minPixel.collapse()
        self.pixelsToCollapse.remove(minPixel)
        for neighbor in minPixel.getNeighbors():
            if neighbor is None or neighbor.collapsed:
                continue
            self.pixelsToCollapse.add(neighbor)

        if minPixel.entropy == 0: # Stop on first impossible
            print(minPixel)
            minPixel.color = Color(255, 0, 0)

        return True

