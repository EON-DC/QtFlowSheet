class TimeLine:
    def __init__(self, time_line_id, time_line_information):
        self.time_line_id = time_line_id
        self.time_line_information = time_line_information

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return self.__dict__