from io import BytesIO

from PIL import Image

from canvas.painter.file_stream_canvas_painter import FileStreamCanvasPainter
from canvas.painter.png_stream_canvas_painter import PngStreamCanvasPainter
from canvas.painter.stream_canvas_painter import Stream


class GifFileCanvasPainter(PngStreamCanvasPainter, FileStreamCanvasPainter):
    """
    Export Canvas to GIF files
    """

    def saveStream(self, duration: int, **kwargs) -> Stream:
        out = BytesIO()
        Image.open(self.frames[0]).save(out, format="GIF", save_all=True, append_images=[Image.open(frame) for frame in self.frames[1:]], loop=0, duration=duration)
        return out
