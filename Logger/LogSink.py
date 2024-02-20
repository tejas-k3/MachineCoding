from abc import ABC, abstractmethod

class LogSink(ABC):
    @abstractmethod
    def log(self, message):
        pass
