from typing import List

from canvas.pixel.color import Color


class Palette:

    colors: List[Color]
    size: int
    bitdepth: int
    max_colors: int

    def __init__(self):
        self.colors = []
        self.size = 0
        self.bitdepth = 1
        self.max_colors = 2

    def save(self, color: Color) -> int:
        if color in self.colors:
            return self.colors.index(color)
        else:
            self.colors.append(color)
            self.size += 1
            if self.size >= self.max_colors:
                self.bitdepth *= 2
                self.max_colors = 2**self.bitdepth

            return self.size - 1

    def list(self) -> List[Color]:
        return self.colors

    def get(self, color: Color) -> int:
        return self.colors.index(color)