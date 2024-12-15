from abc import ABC
from itertools import chain
from typing import Tuple, List

import png

from canvas import Canvas, Palette
from canvas.pixel import Color
from canvas.painter.stream_canvas_painter import StreamCanvasPainter, Stream


class PngStreamCanvasPainter[T: Canvas, Frame: Stream](StreamCanvasPainter, ABC):
    """
    PngStreamCanvasPainter is a specification of StreamCanvasPainter that works with PNG format.
    It requires PaletteCanvas or RGBCanvas (last one not yet Implemented)
    """

    def __init__(self, canvas: T, **kwargs):
        super().__init__(canvas=canvas, **kwargs)
        self.writer = None

    def _createWriter(self, palette: Palette | None = None):
        """
        This method create a writer. Once called, width, height and palette cannot be changed
        """
        if self.writer is None:
            if palette:
                colors: List[Tuple[int, int, int]] = list(map(Color.to_rgb, palette.list()))
                self.writer = png.Writer(size=(self.canvas._width, self.canvas._height), palette=colors, bitdepth=palette.bitDepth)
            else:
                self.writer = png.Writer(size=(self.canvas._width, self.canvas._height), greyscale=False, alpha=False, bitdepth=8)

    def _paint(self, stream: Stream, palette: Palette | None = None, **kwargs):
        self._createWriter(palette)
        self.writer.write(stream, [list(chain(*[pixel.getColor() for pixel in row])) for row in self.canvas.getRows()])
