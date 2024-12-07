from abc import ABC, abstractmethod
from pathlib import Path

from canvas.canvas import Canvas
from canvas.painter.stream_canvas_painter import StreamCanvasPainter


class FileCanvasPainter[T: Canvas, Frame](StreamCanvasPainter, ABC):

    file: Path

    def __init__(self, file: str | Path, canvas: T, **kwargs):
        super().__init__(canvas, **kwargs)
        self.file = file if isinstance(file, Path) else Path(file)

    @abstractmethod
    def save(self, **kwargs):
        raise NotImplementedError()
