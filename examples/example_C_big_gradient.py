from canvas import VisualBoard, Coordinate, BaseCell, BigPixelData
from color import Color
from generation import Filler
from manager import Manager
from manager.profiling import SimpleTimeProfiler
from painter import ImageBoardPainter

### Base variable
# Board
WIDTH = 16
HEIGHT = 16

# Colors
board = VisualBoard.EMPTY(WIDTH, HEIGHT, BigPixelData)


def setGradient(_: Coordinate, cell: BaseCell, advancement: float) -> None:
    """
    Set cell_data's color to a gradient based on advancement
    """
    cell.cell_data.setColor(Color.mix(Color.BLUE(), Color.GREEN(), advancement))


# Generator
generator = Filler(start=Coordinate(2, 2), end=Coordinate(13, 13)).do(setGradient)

# Painter
painter = ImageBoardPainter(board, "out/gradient.big.gif").setGif().setDuration(100)

# Running the generator
with Manager(board=board,
             painter=painter,
             generator=generator,
             profiler=SimpleTimeProfiler()) as manager:
    manager.run()
