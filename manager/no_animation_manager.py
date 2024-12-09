from copy import deepcopy
from enum import Enum, auto
from typing import List, Generator

from canvas import Canvas, CanvasPainter
from manager.manager import Manager
from profiling import Profiler


class NoAnimationManager(Manager):

    def __init__(self, canvas: Canvas, painter: CanvasPainter, generator: Generator, profiler: Profiler):
        super().__init__(canvas, painter, generator, profiler)

    def step(self) -> bool:
        return self.generator.step()
