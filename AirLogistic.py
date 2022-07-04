from LogisticInterface import LogisticInterface

class AirLogistic(LogisticInterface):

    def __init__(self):
        self.possible_status = {0: 'pendente de envio', 1: 'em rota', 2: 'entregue'}

    def new_logistic(self) -> dict:
        self.dest_name = str(input('Nome Destinatário: '))
        self.dest_estate = str(input('Estado Destinatário: '))
        self.dest_city = str(input('Cidade Destinatário: '))
        self.cep_number = int(input('CEP Destinatário (sem traços): '))
        self.id_number = int(LogisticInterface.LAST_DELIVER_ID_NUMBER + 1)
        LogisticInterface.LAST_DELIVER_ID_NUMBER = self.id_number
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
        self.logistic_data['status'] = self.possible_status[status]

        return self.logistic_data

    def logistic_status(self):
        return self.logistic_data

a = AirLogistic()
a.new_logistic()