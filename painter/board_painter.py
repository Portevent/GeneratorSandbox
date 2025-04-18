from abc import ABC, abstractmethod
from typing import List, Self

from canvas.board.board import BaseBoard


class BoardPainter[T: BaseBoard, Frame](ABC):
    """
    BoardPainter is an abstract class that export Board to Frames, and then save them somewhere
    BoardPainters must implement :

    - paint : To export current Board to a Frame
    - save : To save current Frames to something
    """
    board: T
    frames: List[Frame]
    animation = False
    maxFrame: int | None = None
    frameRate: int = 1
    frameLoop: int = 0

    def __init__(self, board: T | None = None):
        self.board = board
        self.frames = []

    def setBoard(self, board: T):
        """
        Set Board to paint to
        :param board: Board to paint
        """
        self.board = board

    def createFrame(self):
        """
        Create a new frame and save it within frames
        """
        self.frameLoop += 1

        if self.frameLoop == self.frameRate:
            self.frameLoop = 0
        else:
            return

        if self.animation:

            if self.maxFrame is not None and len(self.frames) >= self.maxFrame:
                self.frames = self.frames[::2]
                self.frameRate *= 2

            self.frames.append(self.paint())
        else:
            self.frames = [self.paint()]

        if self.frameLoop == self.frameRate:
            self.frameLoop = 0

    def setMaxFrame(self, maxFrame: int) -> Self:
        """
        Define the max number of frames to store
        """
        self.maxFrame = maxFrame
        return self

    @abstractmethod
    def paint(self) -> Frame:
        """
        Generate a new frame of current board situation
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self):
        """
        Save export
        """
        raise NotImplementedError()
