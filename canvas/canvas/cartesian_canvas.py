from __future__ import annotations

import random
from abc import ABC
from typing import List, Tuple, Callable, Iterator, Set

from canvas.canvas import Canvas
from canvas.pixel import Pixel


class CartesianCanvas[T: Pixel, Point: Tuple](Canvas, ABC):
    """
    Canvas2D is a finite two-dimensional canvas that can be drawn onto.
    It has a width and a height
    Point must be pairs of integers.
    """

    # How many dimensions this Cartesian Canvas has
    dimensions: int

    dimensionsMax: Tuple # Maximum value for coordinates along dimensions
    dimensionsMin: Tuple # Minimum value for coordinates along dimensions

    def __init__(self, dimensions: int, dimensionsMin: Tuple | None = None, dimensionsMax: Tuple | None = None, pixelClass: Type[CartesianPixel], emptyPixelConstructor: Callable[[], CartesianPixel] | None = None){
        if pixelClass.dimensions != dimensions:
            raise Exception("Trying to create Cartesian Canvas with different dimensions count than its pixels")

        self.dimensions = dimensions
        self.dimensionsMin = dimensionsMin or tuple([0 for _ in range(self.dimensions)])
        self.dimensionsMax = dimensionsMax or tuple([0 for _ in range(self.dimensions)])
        self.pixels = pixelClass.generate(self.dimensionsMin, self.dimensionsMax, emptyPixelConstructor)
    }

    def _validPoint(self, point: Point) -> bool:
        for i in range(dimensions):
            if not dimensionsMin[i] <= point[i] < dimensionsMax[i]: 
                return False

        return True

    def _constrainPoint(self, point: Point) -> Point:
        """
        Constrain a point within the bounds of the canvas
        :param point: Point to be constrained
        :return: Original point, or closest point inside canvas
        """
        return tuple([max(self.dimensionsMin[i], min(self.dimensionsMax[i], point[i])) for i in range(self.dimensions)])

    def getRandomPoint(self) -> Point:
        return tuple([self.dimensionsMin[i] + random.random() * (self.dimensionsMax[i] - self.dimensionsMin[i]) for i in range(self.dimensions)])

    def getRandomPointAround(self, point: Point, maxOffset: int) -> Point:
        return self._constrainPoint(tuple(
            [
                point[i] + int(((random.random() -0.5) * maxOffset))) for i in range(self.dimensions)
            ]
        ));
