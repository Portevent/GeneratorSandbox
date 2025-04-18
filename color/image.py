from _ast import Tuple
from pathlib import Path
from typing import List, Tuple

import png

from color import Color

type Image = List[List[Color]]


def rowToColors(row: List[int], width: int):
    return [Color(row[i*3], row[i*3+1], row[i*3+2]) for i in range(width)]

class ImageLoader:

    @staticmethod
    def from_file(filename: str | Path) -> tuple[Image, int, int]:
        width: int
        height: int

        with open(filename, "rb") as file:
            # Create reader from file
            reader = png.Reader(file=file)

            # Read image data
            width, height, pixels, _ = reader.asRGB8()

            return [
                rowToColors(row, width) for row in pixels
            ], width, height

