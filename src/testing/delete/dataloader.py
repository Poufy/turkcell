from abc import ABC, abstractmethod
class dataloader(ABC):

    @abstractmethod
    def getCapacity(self):
        pass

    @abstractmethod
    def getIops(self):
        pass

    @abstractmethod
    def getThroughput(self):
        pass
