class FlowSheet:
    def __init__(self, flowsheet_id, patient, time_line, vital):
        self.flowsheet_id = flowsheet_id
        self.patient = patient
        self.time_line = time_line
        self.vital = vital

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if self.flowsheet_id == other.flowsheet_id:
            return True
        else:
            return False
