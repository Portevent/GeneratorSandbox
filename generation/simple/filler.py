from typing import Iterator

from canvas import Canvas2D, Point2D, Pixel
from generation.generator import Generator


class Filler[T: Canvas2D](Generator):
    """
    Fill a 2D Canvas area with a certain Pixel
    """

    iterator: Iterator[Point2D]
    start: Point2D
    end: Point2D
    pixel: Pixel

    def __init__(self, start: Point2D, end: Point2D, pixel: Pixel, **kwargs):
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.pixel = pixel

    def initialize(self, **kwargs):
        self.iterator = self.canvas.getPointsIn(self.start, self.end)

    def step(self) -> bool:
        point: Point2D= next(self.iterator, None)

        if point is None:
            return False

        self.canvas.get(point).update(self.pixel)
        return True
