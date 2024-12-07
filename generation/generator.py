from abc import ABC, abstractmethod
import random

from canvas import Canvas


class Generator[T: Canvas](ABC):
    canvas: T
    seed: float

    def __init__(self, seed: float | None = None,
                 canvas: T | None = None, **kwargs):
        """
        Create a Generator
        Randomness can be seed
        """
        random.seed(seed)
        self.setCanvas(canvas)

    @abstractmethod
    def initialize(self, **kwargs):
        """
        Initialize the generator
        """
        raise NotImplementedError()

    @abstractmethod
    def step(self) -> bool:
        """
        Process a step of the generator
        :return: True if the generation is finished
        """
        raise NotImplementedError()

    def setCanvas(self, canvas: T):
        """
        Set the canvas
        :param canvas: New canvas
        """
        self.canvas = canvas