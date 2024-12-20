from pathlib import Path

from canvas import Canvas, PngFileCanvasPainter, GifFileCanvasPainter
from canvas.canvas.canvas_helper import CanvasHelper
from canvas.pixel.linked_ortho_2d_pixel import LinkedOrtho2DPixel
from canvas.pixel.linked_surrond_2d_pixel import LinkedSurround2DPixel
from canvas.pixel.pixel import Point
from canvas.pixel.wave_pixel import WavePixel
from generation.wfc.importer.importer import WfModulesImporter
from generation.wfc.naive_collapser import NaiveCollapser
from generation.wfc.wave_function import WaveFunction
from manager import AnimationConfig, AnimationPainting, AnimationManager
from profiling import SimpleTimeProfiler

model_canvas = CanvasHelper.loadFromFile(pixelsType=LinkedSurround2DPixel, canvasType=Canvas, path=Path("in/aaa.png"))

modules, colors = WfModulesImporter().fromCanvas(model_canvas)

waveFunction = WaveFunction(modules, colors)

WIDTH = 100
HEIGHT = 100

def EMPTY(point: Point) -> WavePixel:
    return WavePixel(element=None, point=point, waveFunction=waveFunction)

PIXELS = WavePixel.generate(WIDTH, HEIGHT, empty=EMPTY)
result_canvas = Canvas[WavePixel](width=WIDTH, height=HEIGHT, pixels=PIXELS)

ANIMATION_CONFIG = AnimationConfig(max_frame=100, duration=20, mode=AnimationPainting.ON_THE_FLY)
painter = GifFileCanvasPainter(file="out/oskourAAA.gif", canvas=result_canvas)

# Generator
generator = NaiveCollapser(seed=1)

# Running the generator
with AnimationManager(animationConfig=ANIMATION_CONFIG, canvas=result_canvas, painter=painter, generator=generator, profiler=SimpleTimeProfiler()) as manager:
    manager.run()