from __future__ import annotations

from canvas.pixel import Pixel


class IntPixel(Pixel):
    """
    IntPixel are pixel that hold integer data. Mainly useful for palette generation
    """
    color: int

    def __init__(self, color):
        self.color = color

    def set(self, element: int) -> None:
        self.color = element

    def get(self) -> int:
        return self.color

    @staticmethod
    def empty() -> IntPixel:
        return IntPixel(0)

    def __repr__(self) -> str:
        return f"<{self.color}>"

    def update(self, other: IntPixel):
        self.color = other.get()
