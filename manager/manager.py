from abc import ABC, abstractmethod

from canvas import Canvas, CanvasPainter
from generation import Generator
from profiling import Profiler


class Manager(ABC):

    canvas: Canvas
    painter: CanvasPainter
    generator: Generator

    running: bool
    currentStep : int

    def __init__(self, canvas: Canvas, painter: CanvasPainter, generator: Generator, profiler: Profiler):
        self.canvas = canvas
        self.painter = painter
        self.generator = generator
        self.profiler = profiler

        self.painter.setCanvas(self.canvas)
        self.generator.setCanvas(self.canvas)
        self.running = False
        self.currentStep = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self._stop(error=exc_type)

    def _stop(self, error: Exception = None, **kwargs):
        self.running = False
        self.profiler.stopProfiling()
        self.painter.createFrame()
        self.painter.save(**kwargs)

        print(self.profiler.getProfilingResult())

        if error:
            print(f"Process stopped at step {self.currentStep} because of {error}")
        else:
            print(f"Process successfully ended at step {self.currentStep}")

    def _start(self, **kwargs):
        self.running = True
        self.currentStep = 0
        self.generator.initialize(**kwargs)
        self.painter.createFrame()
        self.profiler.startProfiling()


    def run(self, maxSteps: int = -1, **kwargs):
        """
        Run the algorithm
        :param maxSteps: maximum number of steps to run
        """

        self._start(**kwargs)

        while self.step() and self.currentStep != maxSteps:
            self.currentStep += 1

        self._stop(**kwargs)

    @abstractmethod
    def step(self) -> bool:
        """
        Run a step in the generator
        Occasionally save the resulting frame
        :param step: Current step
        """
        raise NotImplementedError()
