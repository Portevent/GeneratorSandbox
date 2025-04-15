from canvas import VisualBoard, Coordinate
from canvas.data.ImageData import ImageData
from color import Color
from generation import DataFiller
from manager import Manager
from manager.profiling import SimpleTimeProfiler
from painter import ImageBoardPainter

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

VISUAL_WIDTH = 16
VISUAL_HEIGHT = 16

image = Color.GRADIENT2D(Color.RED(), Color.BLUE(), VISUAL_WIDTH, VISUAL_HEIGHT)

# Colors
board = VisualBoard.FROM(WIDTH, HEIGHT, ImageData.CreateEmpty(16,16), (16,16))

# Generator
generator = DataFiller(start=Coordinate(2, 2), end=Coordinate(7,7)).fillWith(ImageData(16, 16, image))

# Painter
painter = ImageBoardPainter(board, "out/image_gradient.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()