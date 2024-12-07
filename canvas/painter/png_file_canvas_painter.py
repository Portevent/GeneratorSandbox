from canvas.canvas import PaletteCanvas
from canvas.painter.file_canvas_painter import FileCanvasPainter
from canvas.painter.png_stream_canvas_painter import PngStreamCanvasPainter
from canvas.painter.stream_canvas_painter import Stream


class PngFileCanvasPainter[T: PaletteCanvas, Frame: Stream](PngStreamCanvasPainter, FileCanvasPainter):
    """
    Export Canvas to PNG files
    """

    def saveStream(self, **kwargs) -> Stream:
        if len(self.frames) == 0:
            self.createFrame()

        return self.frames[-1]