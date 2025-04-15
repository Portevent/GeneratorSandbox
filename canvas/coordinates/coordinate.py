from typing import Iterator


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    @staticmethod
    def getCoordinatesInBox(coordinateA: "Coordinate", coordinateB: "Coordinate") -> Iterator["Coordinate"]:
        for x in range(coordinateA.x, coordinateB.x + 1):
            for y in range(coordinateA.y, coordinateB.y + 1):
                yield Coordinate(x, y)

    @staticmethod
    def getCoordinatesBox(width: int, height: int) -> Iterator["Coordinate"]:
        for x in range(0, width):
            for y in range(0, height):
                yield Coordinate(x, y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def Distance(start, end):
        """
        Returns the distance between two coordinates.
        """
        return abs(start.x - end.x) + abs(start.y - end.y)

