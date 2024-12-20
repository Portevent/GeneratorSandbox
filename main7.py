from canvas import GifFileCanvasPainter, Color, Canvas, Pixel, LinkedPixel, PngFileCanvasPainter
from canvas.pixel.linked_ortho_2d_pixel import LinkedOrtho2DPixel
from canvas.pixel.pixel import Point
from canvas.pixel.simple_pixel import SimplePixel
from generation import Filler, NaiveVoronoi
from manager import AnimationManager, AnimationConfig, AnimationPainting
from profiling import SimpleTimeProfiler

### Base variable
# Canvas
WIDTH = 100
HEIGHT = 100

def EMPTY(point: Point) -> Pixel:
    return LinkedOrtho2DPixel(element=None, point=point)

PIXELS = LinkedOrtho2DPixel.generate(WIDTH, HEIGHT, empty=EMPTY)
canvas = Canvas(width=WIDTH, height=HEIGHT, pixels=PIXELS)

painter = PngFileCanvasPainter(file="out/new_simple.gif", canvas=canvas)

# Animation
ANIMATION_CONFIG = AnimationConfig(max_frame=100, duration=20, mode=AnimationPainting.ON_THE_FLY)

# Generator
generator = NaiveVoronoi(germsCount=3)
# generator = Filler(start=(0, 0), end=(9,9), pixel=SimplePixel(RED))

# Running the generator
with AnimationManager(animationConfig=ANIMATION_CONFIG, canvas=canvas, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()