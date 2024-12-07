from abc import ABC, abstractmethod
import random

from canvas import Canvas


class Generator[T: Canvas](ABC):
    """
    Generator is an abstract class that represents algorithms working on canvas.
    Each implementation of Generator can require more that any Canvas (for instance, only work on Canvas2D)
    Generator must implement the following methods:
    - initialize : Set up the initial state of the algorithm
    - step : Process an iteration and return False if the algorithm reached the end
    (Implementations of Generator can refuse to divided themselves to step, and just process everything on one step() call
    It will just look bad on animations)
    """
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

    def setCanvas(self, canvas: T):
        """
        Set the canvas
        :param canvas: New canvas
        """
        self.canvas = canvas

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