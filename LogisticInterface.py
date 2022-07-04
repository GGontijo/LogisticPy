from abc import ABC, abstractmethod

class LogisticInterface(ABC):
    LAST_LOGISTIC_ID_NUMBER = 0
    ALL_LOGISTICS = []
    
    @abstractmethod
    def new_logistic(self):
        pass

    @abstractmethod
    def update_logistic(self):
        pass

    @abstractmethod
    def logistic_status(self):
        pass