from canvas import VisualBoard, PixelData, Coordinate
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

# Generator
generator = Filler(start=Coordinate(2, 2), end=Coordinate(7,7), fillWith=Color.RED())

# Painter
painter = ImageBoardPainter(board, "out/filler.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()