from TransportInterface import TransportInterface

class Truck(TransportInterface):

    def __init__(self):
        self.possible_status = {0: 'waiting', 1: 'enroute'}
        self.new_transport()

    def new_transport(self) -> dict:
        self.driver = str(input("Driver's Name: "))
        self.plate = str(input("Truck's Plate: "))
        self.logistics = []
        self.id_number = int(TransportInterface.LAST_TRANSPORT_ID_NUMBER + 1)
        TransportInterface.LAST_TRANSPORT_ID_NUMBER = self.id_number
        self.status = str(self.possible_status[0])

        self.transport_data = {
            'transport_id': self.id_number,
            'driver': self.driver,
            'plate': self.plate,
            'logistics': self.logistics,
            'status': self.status
        }

        TransportInterface.ALL_TRANSPORTS.append(self.transport_data)
        return self.transport_data

    def update_transport(self, logistic_id) -> dict:
        if isinstance(logistic_id, int):
            self.logistics.append(logistic_id)
            self.transport_data['status'] = self.possible_status[1]
            id_aux = self.id_number - 1
            TransportInterface.ALL_TRANSPORTS[id_aux] = self.transport_data
        return self.transport_data


    def transport_status(self) -> dict:
        return self.transport_data
