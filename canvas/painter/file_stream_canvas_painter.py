from abc import ABC, abstractmethod
from io import BytesIO

from canvas.canvas import Canvas
from canvas.painter.file_canvas_painter import FileCanvasPainter
from canvas.painter.stream_canvas_painter import Stream


class FileStreamCanvasPainter[T: Canvas, Frame](FileCanvasPainter, ABC):

    @abstractmethod
    def saveStream(self, **kwargs) -> Stream:
        """
        Get the stream to save
        """
        raise NotImplementedError()

    def save(self, **kwargs):
        """
        Save the stream to a binary file
        """
        with self.file.open(mode="bw") as f:
            out = self.saveStream(**kwargs)
            f.write(out.getbuffer() if isinstance(out, BytesIO) else out)
