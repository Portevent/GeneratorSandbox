from abc import ABC, abstractmethod
from io import BytesIO
from pathlib import Path

from canvas.canvas import Canvas
from canvas.painter.stream_canvas_painter import Stream, StreamCanvasPainter


class FileCanvasPainter[T: Canvas, Frame](StreamCanvasPainter, ABC):
    """
    FileCanvasPainter is a specification of StreamCanvasPainter that save generated Frames into files.
    It requires a file during initialization in which the final stream will be written.
    To get this final stream, it introduces saveStream abstract method
    """

    file: Path

    def __init__(self, file: str | Path, canvas: T, **kwargs):
        super().__init__(canvas, **kwargs)
        self.file = file if isinstance(file, Path) else Path(file)

    @abstractmethod
    def saveStream(self, **kwargs) -> Stream:
        """
        Get the final stream to save
        """
        raise NotImplementedError()

    def save(self, **kwargs):
        """
        Save the stream to a binary file
        """
        with self.file.open(mode="bw") as f:
            out = self.saveStream(**kwargs)
            f.write(out.getbuffer() if isinstance(out, BytesIO) else out)
