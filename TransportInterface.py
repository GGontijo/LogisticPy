from abc import ABC, abstractmethod

class TransportInterface(ABC):
    LAST_TRANSPORT_ID_NUMBER = 0
    ALL_TRANSPORTS = []

    @abstractmethod
    def new_transport(self):
        pass

    @abstractmethod
    def update_transport(self):
        pass

    @abstractmethod
    def transport_status(self):
        pass