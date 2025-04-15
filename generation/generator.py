from abc import ABC, abstractmethod
import random

from canvas.board.board import BaseBoard


class Generator[T: BaseBoard](ABC):
    """
    Generator is an abstract class that represents algorithms working on board.
    Each implementation of Generator can require more that any Board (for instance, only work on Board2D)
    Generator must implement the following methods:
    - initialize : Set up the initial state of the algorithm
    - step : Process an iteration and return False if the algorithm reached the end
    (Implementations of Generator can refuse to divided themselves to step, and just process everything on one step() call
    It will just look bad on animations)
    """
    board: T
    seed: float

    def __init__(self, seed: float | None = None,
                 board: T | None = None, **kwargs):
        """
        Create a Generator
        Randomness can be seed
        """
        random.seed(seed)
        self.setBoard(board)

    def setBoard(self, board: T):
        """
        Set the board
        :param board: New board
        """
        self.board = board

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