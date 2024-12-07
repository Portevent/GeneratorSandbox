from copy import deepcopy
from enum import Enum, auto
from typing import List, Generator

from canvas import Canvas, CanvasPainter
from manager.manager import Manager
from profiling import Profiler


class AnimationPainting(Enum):
    ON_THE_FLY = auto() # Generate frame as steps advance
    AT_THE_END = auto() # Generate Canvas as steps advance and paint them at the end

class AnimationConfig:
    max_frame: int
    duration: int
    mode: AnimationPainting

    def __init__(self, max_frame: int, duration: int, mode: AnimationPainting):
        self.max_frame = max_frame
        self.duration = duration
        self.mode = mode

class AnimationManager(Manager):

    config: AnimationConfig
    currentInterval: int
    frameCount: int
    canvasCache: List[Canvas]

    def __init__(self, canvas: Canvas, painter: CanvasPainter, generator: Generator, profiler: Profiler, animationConfig: AnimationConfig):
        super().__init__(canvas, painter, generator, profiler)
        self.config = animationConfig
        self.currentInterval = 1
        self.frameCount = 0
        self.canvasCache = []

    def _start(self, **kwargs):
        self.currentInterval = 1
        self.frameCount = 0

        super()._start(**kwargs)

    def _stop(self, **kwargs):
        super()._stop(duration=self.config.duration, **kwargs)

    def step(self) -> bool:
        res: bool = self.generator.step()

        if self.currentStep % self.currentInterval == 0:
            self.frameCount += 1

            if self.config.mode == AnimationPainting.ON_THE_FLY:
                self.painter.createFrame()
            if self.config.mode == AnimationPainting.AT_THE_END:
                self.canvasCache.append(deepcopy(self.canvas))

            if self.frameCount > self.config.max_frame:
                self.currentInterval *= 2
                self.frameCount /= 2

                if self.config.mode == AnimationPainting.ON_THE_FLY:
                    self.painter.frames = self.painter.frames[::2]
                if self.config.mode == AnimationPainting.AT_THE_END:
                    self.canvasCache = self.canvasCache[::2]

        return res

    def end(self):
        if self.config.mode == AnimationPainting.AT_THE_END:
            for canvas in self.canvasCache:
                self.painter.setCanvas(canvas)
                self.painter.createFrame()

        super().end()