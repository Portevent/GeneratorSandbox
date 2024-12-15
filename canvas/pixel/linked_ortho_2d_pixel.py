from __future__ import annotations

from typing import Callable, Tuple, Dict

from canvas.pixel.linked_pixel import LinkedPixel


class LinkedOrtho2DPixel(LinkedPixel):
    """
    LinkedOrtho2DPixel is a LinkedPixel with orthogonal (4) neighbors (2D)

    If not specified otherwise, expected direction are
    0 top
    1 right
    2 bottom
    3 left
    """

    dimensions = 2

    neighborsSize: int = 4

    def getOppositePosition(self, position: int) -> int:
        return (position + 2) % 4

    @staticmethod
    def generate(width: int, height: int, empty: Callable[[Tuple], LinkedPixel] | None = None) -> Dict[Tuple, LinkedPixel]:
        pixels: Dict[Tuple, LinkedPixel] = {}
        for x in range(0, width):
            for y in range(0, height):
                pixels[(x, y)] = empty((x, y))

        for x in range(0, width-1):
            for y in range(0, height-1):
                pixels[(x, y)].linkTo(pixels[(x+1, y)], 1)    # Link to right
                pixels[(x, y)].linkTo(pixels[(x, y+1)], 2)    # Link to bottom

        for x in range(0, width - 1):
            pixels[(x, height-1)].linkTo(pixels[(x+1, height-1)], 1)
        for y in range(0, height-1):
            pixels[(width - 1, y)].linkTo(pixels[(width - 1, y+1)], 2)

        return pixels
