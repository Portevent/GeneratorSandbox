from canvas import VisualBoard, PixelData, Coordinate, BaseCell
from color import Color
from generation import Filler
from manager import Manager
from painter import ImageBoardPainter
from profiling import SimpleTimeProfiler

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

# Colors
board = VisualBoard.EMPTY(WIDTH, HEIGHT, PixelData)

# Generator
generator = Filler(start=Coordinate(2, 2), end=Coordinate(8,8), fillWith=Color.RED())

# Painter
painter = ImageBoardPainter(board, "out/test_simple.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()