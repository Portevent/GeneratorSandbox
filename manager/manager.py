from abc import ABC, abstractmethod

from canvas import Canvas, CanvasPainter
from generation import Generator
from profiling import Profiler


class Manager:

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

    def _stop(self, error: Exception = None):
        self.running = False
        self.profiler.stopProfiling()
        self.painter.createFrame()
        self.painter.save()

        print(self.profiler.getProfilingResult())

        if error:
            print(f"Process stopped at step {self.currentStep} because of {error}")
        else:
            print(f"Process successfully ended at step {self.currentStep}")

    def _start(self):
        self.running = True
        self.currentStep = 0
        self.generator.initialize()
        self.painter.createFrame()
        self.profiler.startProfiling()


    def run(self, maxSteps: int = -1):
        """
        Run the algorithm
        :param maxSteps: maximum number of steps to run
        """

        self._start()

        while self.generator.step() and self.currentStep != maxSteps:
            self.currentStep += 1
            self.painter.createFrame()

        self._stop()

