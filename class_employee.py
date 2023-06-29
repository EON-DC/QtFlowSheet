from class_patient import Patient


class Employee:
    def __init__(self, employee_id, name, patient, cell_phone_num, login_id, login_password):
        self.employee_id = employee_id
        self.name = name
        self.patient = patient
        self.cell_phone_num = cell_phone_num
        self.login_id = login_id
        self.login_password = login_password

    def __str__(self):
        result_dict = self.__dict__
        if self.patient is not None:
            patient_obj = result_dict.pop('patient')
            assert isinstance(patient_obj, Patient)
            patient_obj: Patient
            result_dict.update({'patient': patient_obj.__str__()})

        return f'{result_dict}'

    def __repr__(self):
        return self.__dict__
