from io import BytesIO

from PIL import Image

from painter.file_canvas_painter import FileCanvasPainter
from painter.stream_canvas_painter import Stream


class ImageCanvasPainter[T: Canvas, Frame: Stream](FileCanvasPainter):
    """
    Export Canvas to PNG or GIF files
    """
    gif: bool = False
    duration: int = 20
    loop: bool = True

    def setGif(self) -> Self:
        """
        Flag this painter as gif output
        """
        self.gif = True
        self.animation = True
        return self

    def setDuration(self, duration: int) -> Self:
        """
        Set the duration in seconds (GIF Only)
        """
        self.duration = duration
        return self

    def setLoop(self, loop: bool) -> Self:
        """
        Activate or desactivate looping (GIF Only)
        """
        self.loop = loop
        return self

    def setPalette(self, palette: Palette | None = None) -> Self:
        """
        Set the Palette to use
        """
        self.palette = palette
        return self

    def _createWriter(self):
        """
        This method create a writer. Once called, width, height and palette cannot be changed
        """
        if self.writer is None:
            if palette:
                colors: List[Tuple[int, int, int]] = list(map(Color.to_rgb, palette.list()))
                self.writer = png.Writer(size=(self.canvas.width, self.canvas.height), palette=colors, bitdepth=palette.bitDepth)
            else:
                self.writer = png.Writer(size=(self.canvas.width, self.canvas.height), greyscale=False, alpha=False, bitdepth=8)

    def paint(self):
        self._createWriter()
        stream = BytesIO()

        self.writer.write(stream, [list(chain(*[pixel.getColor() for pixel in row])) for row in self.canvas.getRows()])

        return stream

    def getFinalStream(self, duration: int | None = None, loop: bool | None = None) -> Stream:

        if len(self.frames) == 0:
            self.createFrame()

        if self.gif:
            out = BytesIO()
            Image.open(self.frames[-1]).save(out, format="GIF", save_all=True, append_images=[Image.open(frame) for frame in self.frames], loop=0 if (loop or self.loop) else None, duration=duration or self.duration)
            return out
        else:
            return self.frames[-1]
