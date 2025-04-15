from canvas import VisualBoard, PixelData, Coordinate, BaseCell
from color import Color
from generation import Filler
from manager import Manager
from manager.profiling import SimpleTimeProfiler
from painter import ImageBoardPainter

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

# Colors
board = VisualBoard.EMPTY(WIDTH, HEIGHT, PixelData)

def setGradient(_: Coordinate, cell: BaseCell, advancement: float) -> None:
    cell.cell_data.setColor(Color.mix(Color.BLUE(), Color.GREEN(), advancement))

# Generator
generator = Filler(start=Coordinate(2, 2), end=Coordinate(7,7)).do(setGradient)

# Painter
painter = ImageBoardPainter(board, "out/gradient.gif").setGif().setDuration(20)

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()