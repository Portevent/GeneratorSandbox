from __future__ import annotations

from abc import ABC
from itertools import chain
from typing import Callable, List

from canvas.pixel.linked_pixel import LinkedPixel


class LinkedSurround2DPixel(LinkedPixel, ABC):
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

    def getOppositePosition(self, position: int) -> int:
        return (position + 4) % 8

    neighborsSize: int = 8

    @staticmethod
    def generate(constructor: Callable[[], LinkedSurround2DPixel], width: int, height: int, **kwargs) -> List[LinkedSurround2DPixel]:
        pixels: List[List[LinkedSurround2DPixel]] = [
            [constructor() for _ in range(width)]
            for _ in range(height)
        ]

        for x in range(width-1):
            for y in range(height-1):
                pixels[y][x].linkTo(pixels[y][x+1], 3)    # Link to right
                pixels[y][x].linkTo(pixels[y+1][x+1], 4)  # Link to diagonal
                pixels[y][x].linkTo(pixels[y+1][x], 5)    # Link to bottom
                pixels[y][x+1].linkTo(pixels[y+1][x], 6)  # Link to other diagonal

        for x in range(width - 1):  # Link bottom line
            pixels[height-1][x].linkTo(pixels[height-1][x+1], 3)
        for y in range(height-1):  # Link far right line
            pixels[y][width - 1].linkTo(pixels[y+1][width - 1], 5)

        return list(chain(*pixels))