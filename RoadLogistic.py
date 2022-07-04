from LogisticInterface import LogisticInterface
from Truck import Truck

class RoadLogistic(LogisticInterface):

    def __init__(self):
        self.possible_status = {0: 'pendente de envio', 1: 'em rota', 2: 'entregue'}
        self.new_logistic()

    def new_logistic(self) -> dict:
        self.dest_name = str(input('Nome Destinatário: '))
        self.dest_estate = str(input('Estado Destinatário: '))
        self.dest_city = str(input('Cidade Destinatário: '))
        self.cep_number = int(input('CEP Destinatário (sem traços): '))
        self.id_number = int(LogisticInterface.LAST_LOGISTIC_ID_NUMBER + 1)
        LogisticInterface.LAST_LOGISTIC_ID_NUMBER = self.id_number
        self.status = str(self.possible_status[0])
        self.transport_id = None

        self.logistic_data = {
        'logistic_id': self.id_number,
        'status': self.status,
        'transport_id': self.transport_id,
        'dest_name': self.dest_name,
        'dest_estate': self.dest_estate,
        'dest_city': self.dest_city,
        'cep_number': self.cep_number
        }

        return self.logistic_data

    def update_logistic(self, status):
        if status in self.possible_status:
            self.logistic_data['status'] = self.possible_status[status]
            if self.logistic_data['status'] == self.possible_status[1]:
                self.transport_id = int(input('Insert existing transport_id: '))
                print(Truck.ALL_TRANSPORTS)
                
                if self.transport_id not in Truck.ALL_TRANSPORTS:
                    self.truck = Truck()
                    self.transport_status = self.truck.transport_status()
                    self.logistic_data['transport_id'] = self.transport_status['transport_id']
                    print(self.truck.update_transport(self.logistic_data['logistic_id']))
                    return self.logistic_data
                else:
                    Truck.update_transport(self.logistic_data['logistic_id'])
                    print(Truck.ALL_TRANSPORTS)






        else:
            print('Invalid Status!')

    def logistic_status(self):
        return self.logistic_data

a = RoadLogistic()
print(a.update_logistic(1))
b = RoadLogistic()
print(b.update_logistic(1))
