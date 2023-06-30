import datetime


class TimeLine:
    def __init__(self, time_line_id, time_line_information):
        self.time_line_id = time_line_id
        self.time_line_information = datetime.datetime.strptime(time_line_information, '%Y-%m-%d %H:%M')

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if self.time_line_id == other.time_line_id and self.time_line_information == other.time_line_information:
            return True
        else:
            return False
