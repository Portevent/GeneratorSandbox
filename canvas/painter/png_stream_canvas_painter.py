from abc import ABC
from typing import Tuple, List

import png

from canvas.canvas import PaletteCanvas
from canvas.pixel import IntPixel,  Color
from canvas.painter.stream_canvas_painter import StreamCanvasPainter, Stream


class PngStreamCanvasPainter[T: PaletteCanvas, Frame: Stream](StreamCanvasPainter, ABC):
    """
    PngStreamCanvasPainter is a specification of StreamCanvasPainter that works with PNG format.
    It requires PaletteCanvas or RGBCanvas (last one not yet Implemented)
    """

    def __init__(self, canvas: T, **kwargs):
        super().__init__(canvas=canvas, **kwargs)
        self.writer = None

    def _createWriter(self):
        """
        This method create a writer. Once called, width, height and palette cannot be changed
        """
        if self.writer is None:
            colors: List[Tuple[int, int, int]] = list(map(Color.to_rgb, self.canvas.palette.list()))
            self.writer = png.Writer(size=(self.canvas.width, self.canvas.height), palette=colors, bitdepth=self.canvas.palette.bitDepth)

    def _paint(self, stream: Stream):
        self._createWriter()
        self.writer.write(stream, [map(IntPixel.get, row) for row in self.canvas.get_rows()])
