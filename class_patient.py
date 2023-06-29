import datetime


class Patient:
    def __init__(self, patient_id, name, birth_date, ssn, register_id):
        self.patient_id = patient_id
        self.name = name
        self.birth_date = Patient.set_date_time(birth_date)
        self.ssn = ssn
        self.register_id = register_id
        self.flowSheet_list = None

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return self.__dict__

    def set_flowsheet_list(self, list_):
        assert isinstance(list_, list)
        self.flowSheet_list = list_

    @staticmethod
    def set_date_time(birth_date_str):
        return datetime.datetime.strptime(birth_date_str, '%Y-%m-%d')
