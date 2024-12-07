from io import BytesIO

from PIL import Image

from canvas import PngFileCanvasPainter
from canvas.painter.stream_canvas_painter import Stream


class GifFileCanvasPainter(PngFileCanvasPainter):
    """
    Export Canvas to GIF files
    Override PngFileCanvasPainter to add support for GIF files.
    """

    def saveStream(self, duration: int, **kwargs) -> Stream:
        out = BytesIO()
        Image.open(self.frames[0]).save(out, format="GIF", save_all=True, append_images=[Image.open(frame) for frame in self.frames[1:]], loop=0, duration=duration)
        return out
