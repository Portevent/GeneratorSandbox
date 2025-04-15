from io import BytesIO
from itertools import chain
from typing import Self, List, Tuple

import png
from PIL import Image

from canvas.board.visual_board import VisualBoard
from painter.file_board_painter import FileBoardPainter, Stream
from painter.palette import Palette


class ImageBoardPainter[T: VisualBoard, Frame: Stream](FileBoardPainter):
    """
    Export Board to PNG or GIF files
    """
    gif: bool = False
    duration: int = 20
    loop: bool = True
    palette: Palette = None

    writer = None

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
            if self.palette:
                colors: List[Tuple[int, int, int]] = list([color.to_rgb() for color in self.palette.list()])
                self.writer = png.Writer(size=(self.board.visual_width, self.board.visual_height), palette=colors, bitdepth=self.palette.bitDepth)
            else:
                self.writer = png.Writer(size=(self.board.visual_width, self.board.visual_height), greyscale=False, alpha=False, bitdepth=8)

    def paint(self):
        self._createWriter()
        stream = BytesIO()

        self.writer.write(stream, self.board.getRawRgbRows())

        return stream

    def getFileStream(self, duration: int | None = None, loop: bool | None = None) -> Stream:

        if len(self.frames) == 0:
            self.createFrame()

        if self.gif:
            out = BytesIO()
            Image.open(self.frames[-1]).save(out, format="GIF", save_all=True, append_images=[Image.open(frame) for frame in self.frames], loop=0 if (loop or self.loop) else None, duration=duration or self.duration)
            return out
        else:
            return self.frames[-1]
