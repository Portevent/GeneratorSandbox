from abc import ABC, abstractmethod
from typing import List

from canvas.canvas import Canvas


class CanvasPainter[T: Canvas, Frame](ABC):
    """
    CanvasPainter is an abstract class that export Canvas to Frames, and then save them somewhere
    CanvasPainters must implement :

    - paint : To export current Canvas to a Frame
    - save : To save current Frames to something
    """
    canvas: T
    frames: List[Frame]
    animation = False
    maxFrame: int | None = None

    def __init__(self, canvas: T | None = None):
        self.canvas = canvas
        self.frames = []

    def setCanvas(self, canvas: T):
        """
        Set Canvas to paint to
        :param canvas: Canvas to paint
        """
        self.canvas = canvas

    def createFrame(self):
        """
        Create a new frame and save it within frames
        """
        if self.animation:

            if self.maxFrame is not None and len(self.frames) >= self.maxFrame:
                self.frames = self.frames[::2]

            self.frames.append(self.paint())
        else:
            self.frames = [self.paint()]

    def setMaxFrame(self, maxFrame: int) -> Self:
        """
        Define the max number of frames to store
        """
        self.maxFrame = maxFrame
        return self

    @abstractmethod
    def paint(self) -> Frame:
        """
        Generate a new frame of current canvas situation
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self):
        """
        Save export
        """
        raise NotImplementedError()
