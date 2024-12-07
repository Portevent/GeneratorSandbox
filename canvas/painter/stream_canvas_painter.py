from abc import ABC, abstractmethod
from io import BytesIO
from typing import BinaryIO

from canvas.canvas import Canvas
from canvas.painter import CanvasPainter

Stream = BytesIO | BinaryIO


class StreamCanvasPainter[T: Canvas, Frame: Stream](CanvasPainter, ABC):

    @abstractmethod
    def _paint(self, stream: Stream):
        """
        Paint the canvas on the given stream.
        :param stream: Stream to paint to
        """
        raise NotImplementedError()

    def paint(self, stream: Frame | None = None) -> Stream:
        """
        Paint the canvas on a BytesIO
        :param stream: Stream to paint to (or a new one)
        :return: Stream painted
        """
        if stream is None:
            stream = BytesIO()

        self._paint(stream)

        return stream