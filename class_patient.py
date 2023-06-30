import datetime

from class_flowsheet import FlowSheet


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
        return f"{self.__dict__}"

    def set_flowsheet_list(self, list_):
        for i in list_:
            assert isinstance(i, FlowSheet)
        self.flowSheet_list = list_

    def find_flowsheet_by_strf_date(self, strf_date):
        same_index = -1
        for idx, f in enumerate(self.flowSheet_list):
            if f.time_line.strftime('%m-%d %H:%M') == strf_date:
                same_index = idx
                break

        if same_index == -1:
            return None
        else:
            return self.flowSheet_list[same_index]
    def update_flowsheet(self, flowsheet):
        has_same_flowsheet = False
        same_flowsheet_index = -1
        for idx, f in enumerate(self.flowSheet_list):
            if f == flowsheet:
                has_same_flowsheet = True
                same_flowsheet_index = idx
                break
        if has_same_flowsheet is True:
            self.flowSheet_list.pop(same_flowsheet_index)
            self.flowSheet_list.insert(same_flowsheet_index, flowsheet)
        else:
            self.flowSheet_list.append(flowsheet)
    def find_flowsheet_by_datetime(self, datetime_str):
        flowsheet_idx = -1
        for idx, flowsheet in enumerate(self.flowSheet_list):
            if flowsheet.time_line.time_line_information.strftime('%m-%d %H:%M') == datetime_str:
                flowsheet_idx = idx
                break
        if flowsheet_idx < 0:
            return None
        else:
            return self.flowSheet_list[flowsheet_idx]


    @staticmethod
    def set_date_time(birth_date_str):
        return datetime.datetime.strptime(birth_date_str, '%Y-%m-%d')

