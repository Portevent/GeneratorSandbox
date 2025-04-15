from canvas import VisualBoard, Coordinate, BigPixelData
from color import Color
from generation import Gradient
from manager import Manager
from manager.profiling import SimpleTimeProfiler
from painter import ImageBoardPainter

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

# Colors
board = VisualBoard.EMPTY(WIDTH, HEIGHT, BigPixelData)

# Generator
generator = Gradient(start=Coordinate(2, 2), end=Coordinate(7,7), colorA=Color.RED(), colorB=Color.GREEN())

# Painter
painter = ImageBoardPainter(board, "out/gradient.big.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()