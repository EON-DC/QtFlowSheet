from class_patient import Patient


class FlowSheet:
    def __init__(self, flowsheet_id, patient, time_line_vital):
        self.flowsheet_id = flowsheet_id
        self.patient = patient
        self.time_line_vital = time_line_vital

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return self.__dict__
