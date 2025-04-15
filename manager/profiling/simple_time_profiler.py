import time

from manager.profiling.profiler import Profiler


class SimpleTimeProfiler(Profiler):

    startTime: float | None
    endTime: float | None

    def __init__(self):
        self.startTime = None
        self.endTime = None

    def startProfiling(self):
        self.startTime = time.time()

    def stopProfiling(self):
        self.endTime = time.time()

    def getProfilingResult(self) -> str:
        if self.startTime is None:
            return f"Not started profiling"
        if self.endTime is None:
            return f"[Currently profiling] {time.time() - self.startTime} seconds"

        return f"Execution time : {self.endTime - self.startTime} seconds"
