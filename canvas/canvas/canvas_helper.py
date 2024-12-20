import struct
from pathlib import Path
from typing import Type, Dict, Iterable, List

import png

from canvas import Canvas, Color
from canvas.pixel.linked_ortho_2d_pixel import LinkedOrtho2DPixel
from canvas.pixel.linked_surrond_2d_pixel import LinkedSurround2DPixel
from canvas.pixel.pixel import Point

def ColorUnpacker(row: List[int]) -> Iterable[Color]:
    elements = iter(row)

    for _ in range(len(row) // 3):
        r, g, b = next(elements), next(elements), next(elements)
        yield Color(r, g, b)


class CanvasHelper:

    @staticmethod
    def loadFromFile(pixelsType: Type[LinkedSurround2DPixel | LinkedOrtho2DPixel], canvasType: Type[Canvas], path: Path):

        colors: Dict[Point, Color] = {}

        with open(path, 'rb') as file:
            WIDTH, HEIGHT, rows, bitdepth = png.Reader(file=file).asDirect()
            for y, row in enumerate(rows):
                for x, color in enumerate(ColorUnpacker(row)):
                    colors[(x, y)] = color

        def EMPTY(point: Point) -> pixelsType:
            return pixelsType(element=colors[point], point=point)

        PIXELS = pixelsType.generate(WIDTH, HEIGHT, empty=EMPTY)
        return canvasType(width=WIDTH, height=HEIGHT, pixels=PIXELS)