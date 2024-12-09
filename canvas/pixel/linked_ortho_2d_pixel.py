from __future__ import annotations

from abc import ABC
from itertools import chain
from typing import Callable, List

from canvas.pixel.linked_pixel import LinkedPixel


class LinkedOrtho2DPixel(LinkedPixel, ABC):
    """
    LinkedOrtho2DPixel is a LinkedPixel with orthogonal (4) neighbors (2D)

    If not specified otherwise, expected direction are
    0 top
    1 right
    2 bottom
    3 left
    """

    neighborsSize: int = 4

    def getOppositePosition(self, position: int) -> int:
        return (position + 2) % 4

    @staticmethod
    def generate(constructor: Callable[[], LinkedOrtho2DPixel], width: int, height: int, **kwargs) -> List[
        LinkedOrtho2DPixel]:
        pixels: List[List[LinkedOrtho2DPixel]] = [
            [constructor() for _ in range(width)]
            for _ in range(height)
        ]

        for x in range(width - 1):
            for y in range(height - 1):
                pixels[y][x].linkTo(pixels[y][x + 1], 1)  # Link to right
                pixels[y][x].linkTo(pixels[y + 1][x], 2)  # Link to bottom

        for x in range(width - 1):  # Link bottom line
            pixels[height - 1][x].linkTo(pixels[height - 1][x + 1], 1)
        for y in range(height - 1):  # Link far right line
            pixels[y][width - 1].linkTo(pixels[y + 1][width - 1], 2)

        return list(chain(*pixels))
