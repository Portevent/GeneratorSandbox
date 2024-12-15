from __future__ import annotations

from typing import Callable, Tuple, Dict

from canvas.pixel.pixel import Pixel, Color


class SimplePixel[T: Color](Pixel):

    @staticmethod
    def generate(width: int, height: int, empty: Callable[[Tuple], Pixel] | None = None) -> Dict[Tuple, Pixel]:
        pixels: Dict[Tuple, Pixel] = {}

        for x in range(width):
            for y in range(height):
                pixels[x, y] = empty((x, y))

        return pixels

    def getColor(self) -> Tuple[int, int, int]:
        return self.element.to_rgb() if self.element is not None else [0, 0, 0]