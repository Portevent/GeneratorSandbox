from canvas.canvas import PaletteCanvas
from canvas.painter.file_stream_canvas_painter import FileStreamCanvasPainter
from canvas.painter.png_stream_canvas_painter import PngStreamCanvasPainter
from canvas.painter.stream_canvas_painter import Stream


class PngFileCanvasPainter[T: PaletteCanvas, Frame: Stream](PngStreamCanvasPainter, FileStreamCanvasPainter):
    """
    Export Canvas to PNG files
    """

    def saveStream(self) -> Stream:
        if len(self.frames) == 0:
            self.createFrame()

        return self.frames[-1]