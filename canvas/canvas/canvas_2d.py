from __future__ import annotations

import random
from abc import ABC
from typing import List, Tuple, Callable, Iterator, Set

from canvas.canvas import Canvas
from canvas.pixel import Pixel

Point2D = Tuple[int, int]


class Canvas2D[T: Pixel, Point: Point2D](Canvas, ABC):
    """
    Canvas2D is a finite two-dimensional canvas that can be drawn onto.
    It has a width and a height
    Point must be pairs of integers.
    """

    pixels: List[T]

    width: int
    height: int

    def __init__(self, width: int, height: int, constructor: Callable[[], T], pixels: List[T] | None = None):
        """
        Pixels are saved on a List
        """
        self.width = width
        self.height = height

        self.pixels = pixels or [constructor() for _ in range(width * height)]

    def _validPoint(self, point: Point) -> bool:
        if point[0] < 0:
            return False
        if point[0] >= self.width:
            return False
        if point[1] < 0:
            return False
        if point[1] >= self.height:
            return False

        return True

    def _getPixel(self, point: Point) -> T:
        return self.pixels[point[0] + (point[1] * self.width)]

    def _setPixel(self, point: Point, pixel: T):
        self.pixels[point[0] + (point[1] * self.width)] = pixel

    def _constrainPoint(self, point: Point) -> Point:
        """
        Constrain a point within the bounds of the canvas
        :param point: Point to be constrained
        :return: Original point, or closest point inside canvas
        """
        return max(0, min(self.width-1, point[0])), max(0, min(self.height-1, point[1]))

    def getRows(self) -> Iterator[List[T]]:
        for i in range(0, self.width * self.height, self.width):
            yield self.pixels[i: i + self.width]

    def getPointsIn(self, pointA: Point, pointB: Point) -> Iterator[Point]:
        for x in range(pointA[0], pointB[0]):
            for y in range(pointA[1], pointB[1]):
                yield x, y

    def getNeighborPoints(self, point: Point, orthogonal: bool = False) -> Set[Point]:
        """
        Get Set of Neighbor points (direct or orthogonal)
        :param point: Point
        :param orthogonal: Orthogonal (true = takes account touching corners)
        """
        return set(filter(self._validPoint,
                          [
                              (point[0] - 1, point[1] - 1),
                              (point[0] - 1, point[1]),
                              (point[0] - 1, point[1] + 1),
                              (point[0], point[1] - 1),
                              (point[0], point[1] + 1),
                              (point[0] + 1, point[1] - 1),
                              (point[0] + 1, point[1]),
                              (point[0] + 1, point[1] + 1),
                          ] if orthogonal else [
                              (point[0] - 1, point[1]),
                              (point[0] + 1, point[1]),
                              (point[0], point[1] - 1),
                              (point[0], point[1] + 1)
                          ]))

    def getNeighborsPoints(self, points: Set[Point], avoid: Set[Point] | None = None) -> Set[Point]:
        """
        Return all the neighbors points from Set (contain only new point)
        :param points: Set of points
        :param avoid: Point to exclude (useful to avoid traceback)
        :return: Neighbors
        """
        if avoid is None:
            avoid = set()

        neighbors = set()
        for point in points:
            neighbors = neighbors.union(self.getNeighborPoints(point))
        return neighbors.difference(points).difference(avoid)

    def getRandomPoint(self) -> Point:
        return int(random.random() * self.width), int(random.random() * self.height)

    def getRandomPointAround(self, point: Point, vRange: int, hRange: int) -> Point:
        return self._constrainPoint((int(point[0] + ((random.random() -0.5) * vRange)), int(point[1] + ((random.random() - 0.5) * hRange))))

