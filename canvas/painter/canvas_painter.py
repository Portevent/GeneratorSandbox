from abc import ABC, abstractmethod
from typing import List

from canvas.canvas import Canvas


class CanvasPainter[T: Canvas, Frame](ABC):
    canvas: T
    frames: List[Frame]
    animation = False

    def __init__(self, canvas: T | None = None, **kwargs):
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
        self.frames.append(self.paint())

    @abstractmethod
    def paint(self, **kwargs) -> Frame:
        """
        Generate a new frame of current canvas situation
        """
        raise NotImplementedError()

    def animate(self, **kwargs):
        """
        Return data that represents the whole animation
        """
        raise NotImplementedError()

    def export(self, **kwargs):
        """
        Return data that represent the last frame or the whole animation
        """
        if self.animation:
            return self.animate(**kwargs)
        else:
            return self.frames[-1]

    @abstractmethod
    def save(self, **kwargs):
        """
        Save export
        """
        raise NotImplementedError()
