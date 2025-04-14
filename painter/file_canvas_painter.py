from abc import ABC, abstractmethod
from io import BytesIO
from pathlib import Path

from canvas.canvas import Canvas
from painter.canvas_painter import CanvasPainter

Stream = BytesIO | BinaryIO

class FileCanvasPainter[T: Canvas, Frame](CanvasPainter, ABC):
    """
    FileCanvasPainter is a specification of CanvasPainter that save generated Frames into files.
    It requires a file during initialization in which the final stream will be written.
    To get this final stream, it introduces getFileStream abstract method
    """

    file: Path

    def __init__(self, canvas: T, file: str | Path | None = None):
        super().__init__(canvas)
        if file is not None:
            self.setFile(file)

    def setFile(self, file: str | Path) -> Self:
        """
        Set the default file to save to
        """
        self.file = file if isinstance(file, Path) else Path(file)
        return self

    @abstractmethod
    def getFileStream(self) -> Stream:
        """
        Get the final stream to save
        """
        raise NotImplementedError()

    def save(self):
        """
        Save the stream to a binary file
        """
        if self.file is None:
            raise Exception("Trying to save export but no file given")

        self.saveAs(self.file, self.getFinalStream())

    def saveAs(self, file: str | Path, stream: Stream):
        """
        Save a stream to a binary file
        """
        with file.open(mode="bw") as f:
            f.write(stream.getbuffer() if isinstance(stream, BytesIO) else stream)
            print(f"Saved into {file}")
