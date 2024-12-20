from typing import List


class Module[T]:

    _id: int
    value: T

    neighbors: List[T]

    def __init__(self, id: int, value: T, neighbors: List[T]):
        self._id = id
        self.value = value
        self.neighbors = neighbors

    def __str__(self):
        return f"[{self._id}] {self.value}"