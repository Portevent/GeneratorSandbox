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

def setRed(_: Coordinate, cell: BaseCell, __: float) -> None:
    cell.cell_data.setColor(Color.RED())

# Generator
generator = Filler(start=Coordinate(2, 2), end=Coordinate(7,7)).do(setRed)

# Painter
painter = ImageBoardPainter(board, "out/filler.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()