from typing import Iterator

from canvas import Canvas, Pixel
from canvas.canvas.canvas import Point
from generation.generator import Generator


class Filler[T: Canvas](Generator):
    """
    Fill a 2D Canvas area with a certain Pixel
    """

    iterator: Iterator[Point]
    start: Point
    end: Point
    pixel: Pixel

    def __init__(self, start: Point, end: Point, pixel: Pixel, **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.pixel = pixel

    def initialize(self, **kwargs):
        self.iterator = self.canvas.getPixelsIn(self.start, self.end)

    def step(self) -> bool:
        pixel: Pixel = next(self.iterator, None)

        if pixel is None:
            return False

        pixel.update(self.pixel)
        return True
