from abc import ABC, abstractmethod


class Profiler(ABC):

    @abstractmethod
    def startProfiling(self):
        """
        Start profiling.
        """
        raise NotImplementedError()

    @abstractmethod
    def stopProfiling(self):
        """
        Stop profiling.
        """
        raise NotImplementedError()

    @abstractmethod
    def getProfilingResult(self) -> str:
        """
        Get profiling result.
        """
        raise NotImplementedError()
