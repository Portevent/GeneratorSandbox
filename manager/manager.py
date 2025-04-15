from canvas.board.board import BaseBoard
from generation import Generator
from painter import BoardPainter
from .profiling import Profiler


class Manager:

    board: BaseBoard
    painter: BoardPainter
    generator: Generator

    running: bool
    currentStep : int

    def __init__(self, board: BaseBoard, painter: BoardPainter, generator: Generator, profiler: Profiler):
        self.board = board
        self.painter = painter
        self.generator = generator
        self.profiler = profiler

        self.painter.setBoard(self.board)
        self.generator.setBoard(self.board)
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

