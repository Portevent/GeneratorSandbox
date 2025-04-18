from pathlib import Path

from canvas import VisualBoard, Coordinate
from canvas.data.ImageData import ImageData
from generation import DataFiller
from manager import SimpleTimeProfiler, Manager
from painter import ImageBoardPainter

imageData: ImageData = ImageData.FromFile(Path("in/flower.png"))

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

VISUAL_WIDTH = 16
VISUAL_HEIGHT = 16

# Colors
board = VisualBoard.FROM(WIDTH, HEIGHT, ImageData.CreateEmpty(16,16), (16,16))

# Generator
generator = DataFiller(start=Coordinate(2, 2), end=Coordinate(7,7)).fillWith(imageData)

# Painter
painter = ImageBoardPainter(board, "out/image_from_file.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()