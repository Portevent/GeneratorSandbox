from canvas import VisualBoard, Coordinate, BaseCell
from canvas.data.ImageData import ImageData
from color import Color
from generation import DataFiller
from manager import Manager
from manager.profiling import SimpleTimeProfiler
from painter import ImageBoardPainter

### Base variable
# Board
WIDTH = 5
HEIGHT = 5

VISUAL_WIDTH = 16
VISUAL_HEIGHT = 16

colorA = Color(240,110,60)
colorB = Color(70, 255, 100)

gradient = Color.SUPER_GRADIENT2D(colorA, colorB, WIDTH, HEIGHT, VISUAL_WIDTH, VISUAL_HEIGHT, inverted=True)

def getImageData(coordinate: Coordinate, _: BaseCell, __: float) -> ImageData:
    return ImageData(16, 16, gradient[coordinate.x][coordinate.y])

# Colors
board = VisualBoard.FROM(WIDTH, HEIGHT, ImageData.CreateEmpty(16,16), (16,16))

# Generator
generator = DataFiller(start=Coordinate(0, 0), end=Coordinate(WIDTH-1,HEIGHT-1)) \
                                        .fillWithCallback(getImageData)

# Painter
painter = ImageBoardPainter(board, "out/image_super_gradient.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()