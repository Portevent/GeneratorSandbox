import random

from canvas import VisualBoard, Coordinate, BaseCell
from canvas.data.ImagePaletteData import ImagePaletteData
from color.image_palette_helper import ImagePaletteHelper
from generation import Filler
from manager import SimpleTimeProfiler, Manager
from painter import ImageBoardPainter

palette = ImagePaletteHelper.FromDir("in/flowers")

### Base variable
# Board
WIDTH = 10
HEIGHT = 10

VISUAL_WIDTH = palette.width
VISUAL_HEIGHT = palette.height

def createBaseCell(_: Coordinate) -> BaseCell[ImagePaletteData]:
    return BaseCell(ImagePaletteData(palette))

def setIndex(_: Coordinate, cell: BaseCell[ImagePaletteData], __: float):
    return cell.cell_data.setIndex(random.randint(0, palette.size - 1))

# Colors
board = VisualBoard.FROM(WIDTH, HEIGHT, createBaseCell, (16,16))



# Generator
generator = Filler(start=Coordinate(0, 0), end=Coordinate(9, 9)).do(setIndex)

# Painter
painter = ImageBoardPainter(board, "out/images_from_dir.gif").setGif()

# Running the generator
with Manager(board=board, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()