from typing import List, Tuple

from color import Color


class Palette:

    colors: List[Color]
    size: int
    bitDepth: int
    _maxColors: int

    def __init__(self):
        self.colors = []
        self.size = 0
        self.bitDepth = 1
        self._maxColors = 2

    def save(self, color: Color) -> int:
        if color in self.colors:
            return self.colors.index(color)
        else:
            self.colors.append(color)
            self.size += 1
            if self.size >= self._maxColors:
                self.bitDepth *= 2
                self._maxColors = 2**self.bitDepth

            return self.size - 1

    def list(self) -> List[Color]:
        return self.colors

    def as_rgbs(self) -> List[Tuple[int, int, int]]:
        return [color.to_rgb() for color in self.colors]

    def get(self, color: Color) -> int:
        return self.colors.index(color)