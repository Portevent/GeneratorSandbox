from __future__ import annotations

from typing import Callable, Tuple, Dict

from canvas.pixel.linked_pixel import LinkedPixel


class LinkedSurround2DPixel(LinkedPixel):
    """
    LinkedSurround2DPixel is a LinkedPixel with surrounding (8) neighbors (2D)

    If not specified otherwise, expected direction are
    0 topLeft
    1 topMiddle
    2 topRight
    3 middleRigth
    4 bottomRight
    5 bottomMiddle
    6 bottomLeft
    7 middleLeft
    """

    dimensions = 2

    def getOppositePosition(self, position: int) -> int:
        return (position + 4) % 8

    neighborsSize: int = 8

    @staticmethod
    def generate(width: int, height: int, empty: Callable[[Tuple], LinkedPixel] | None = None) -> Dict[Tuple, LinkedPixel]:
        pixels: Dict[Tuple, LinkedPixel] = {}
        for x in range(0, width):
            for y in range(0, height):
                pixels[(x, y)] = empty((x, y))

        for x in range(0, width-1):
            for y in range(0, height-1):
                pixels[(x, y)].linkTo(pixels[(x+1, y)], 3)    # Link to right
                pixels[(x, y)].linkTo(pixels[(x+1, y+1)], 4)  # Link to diagonal
                pixels[(x, y)].linkTo(pixels[(x, y+1)], 5)    # Link to bottom
                pixels[(x+1, y)].linkTo(pixels[(x, y+1)], 6)  # Link to other diagonal

        for x in range(0, width - 1):
            pixels[(x, height-1)].linkTo(pixels[(x+1, height-1)], 3)
        for y in range(0, height-1):
            pixels[(width - 1, y)].linkTo(pixels[(width - 1, y+1)], 5)

        return pixels