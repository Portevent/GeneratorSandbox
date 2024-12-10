from __future__ import annotations

from canvas import LinkedPixel, IntPixel
from canvas.pixel.linked_ortho_2d_pixel import LinkedOrtho2DPixel


class IntLinkedPixel(LinkedOrtho2DPixel, IntPixel):

    def __init__(self, color: int):
        LinkedOrtho2DPixel.__init__(self)
        IntPixel.__init__(self, color=color)

    @staticmethod
    def empty() -> IntLinkedPixel:
        return IntLinkedPixel(color=0)