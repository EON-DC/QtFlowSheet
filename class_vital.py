class Vital:
    def __init__(self, vital_id, bt, hr, rr, sbp, dbp, mbp):
        self.vital_id = vital_id
        self.body_temperature = bt
        self.heart_rate = hr
        self.respiration_rate = rr
        self.systolic_blood_pressure = sbp
        self.diastolic_blood_pressure = dbp
        self.mean_blood_pressure = mbp

    def __str__(self):
        return f"{self.__repr__()}"

    def __repr__(self):
        return self.__dict__

