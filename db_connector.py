import datetime
import random
import sqlite3
import numpy as np

from faker import Faker

from class_employee import Employee
from class_flowsheet import FlowSheet
from class_patient import Patient
from class_time_line import TimeLine
from class_vital import Vital


class DBConnector:
    _instance = None

    def __new__(cls, test_option=None):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=None):
        self.conn = None
        self.test_option = test_option
        self.faker = Faker("ko-KR")

    def start_conn(self):
        if self.test_option is True:
            self.conn = sqlite3.connect('db_test.db')
        else:
            self.conn = sqlite3.connect('db_flow.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        if self.conn is not None:
            self.conn.commit()
        else:
            raise f"cannot commit database! {self.__name__}"

    ## Patients ======================================================================= ##

    def findAll_patients(self):
        c = self.start_conn()

        patients_list = list()
        fetched_data = c.execute("select * from patients").fetchall()
        for row in fetched_data:
            patients_list.append(Patient(*row))

        self.end_conn()
        return patients_list

    def insert_dummy_patient(self):
        c = self.start_conn()

        random_register_id_list = DBConnector.get_random_register_num_list(100)
        random_back_ssn_list = DBConnector.get_random_back_ssn_num_list(100)
        for i in range(100):
            name = self.faker.name()
            birth_date = self.faker.date()
            date_obj = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            front_ssn = f'{str(date_obj.year)[2:]}{date_obj.month:02d}{date_obj.day:02d}'
            ssn = f"{front_ssn}-{random_back_ssn_list[i]}"
            register_id = random_register_id_list[i]
            c.execute("insert into patients(name, birth_date, ssn, register_id) values (?, ?, ?, ?)",
                      (name, birth_date, ssn, register_id,))

        self.commit_db()

        self.end_conn()

    def clear_patients_table(self):
        c = self.start_conn()
        c.execute("delete from patients")
        self.commit_db()
        self.end_conn()

    def find_patient_by_id(self, p_id):
        c = self.start_conn()
        patient_data = c.execute("select * from patients where id = (?)", (p_id,)).fetchone()
        patient_obj = Patient(*patient_data)
        return patient_obj

    def find_patient_by_register_id(self, register_id):
        c = self.start_conn()
        patient_data = c.execute("select * from patients where register_id = (?)", (register_id,)).fetchone()
        if patient_data is None:
            return None
        patient_obj = Patient(*patient_data)
        flowsheet_list = list()
        fetched_timeline_vital_id = c.execute("""
        select t.id, t.time_line_information, f.vital_id, bt, hr, rr, sbp, dbp, mbp,f.id from flowsheet f inner join timeline t, vital v
            on f.timeline_id = t.id and f.vital_id == v.id  where f.patient_id=(?)""",
                                              (patient_obj.patient_id,)).fetchall()
        for element in fetched_timeline_vital_id:
            timeline_id = element[0]
            time_line_information = element[1]
            vital_id = element[2]
            bt = element[3]
            hr = element[4]
            rr = element[5]
            sbp = element[6]
            dbp = element[7]
            mbp = element[8]
            flowsheet_id = element[9]
            timeline_obj = TimeLine(timeline_id, time_line_information)
            vital_obj = Vital(vital_id, bt, hr, rr, sbp, dbp, mbp)
            flowsheet_obj = FlowSheet(flowsheet_id, patient_obj, timeline_obj, vital_obj)
            flowsheet_list.append(flowsheet_obj)

        # vital_list = list()

        # for row in fetched_timeline_vital_id:
        #     vital_list.append(
        #         c.execute("""select bt, hr, rr, sbp, dbp, mbp from vital where id = (?)""", (row[1],)).fetchone())
        #
        # for i in range(len(fetched_timeline_vital_id)):
        #     timeline_info = fetched_timeline_vital_id[i][0]
        #     date_time = datetime.datetime.strptime(timeline_info, '%Y-%m-%d %H:%M')
        #     bt, hr, rr, sbp, dbp, mbp = vital_list[i]
        #     flowsheet_list.append((date_time, bt, hr, rr, sbp, dbp, mbp))

        patient_obj.set_flowsheet_list(flowsheet_list)
        self.end_conn()
        return patient_obj

    ## Employees ======================================================================= ##
    def insert_dummy_employees(self):
        c = self.start_conn()

        patient_list = c.execute('select id, name from patients').fetchall()
        random.shuffle(patient_list)
        for i in range(49):
            name = self.faker.name()
            cell_num = self.faker.phone_number()
            simple_profile = self.faker.simple_profile()
            username = simple_profile['username']
            pw = "12345678"
            if random.random() > 0.7:
                patient_id, name = patient_list.pop()
                print(name, patient_id, cell_num, username, pw)
                c.execute(
                    "insert into employees(name, patient_id, cell_phone_num, login_id, login_password) values(?, ?, ?, ?, ?)",
                    (name, patient_id, cell_num, username, pw,))
            else:
                print(name, cell_num, username, pw)
                c.execute("insert into employees(name, cell_phone_num, login_id, login_password) values (?,?,?,?)",
                          (name, cell_num, username, pw,))

        c.execute("insert into employees(name, cell_phone_num, login_id, login_password) values (?,?,?,?)",
                  ('광현', self.faker.phone_number(), 'park', '1234',))
        self.commit_db()

        self.end_conn()

    def findAll_employees(self):
        result_list = list()
        c = self.start_conn()
        fetched_data = c.execute("""
            select * from employees
        """).fetchall()
        for row in fetched_data:
            if row[2] is not None:
                fetched_patient_data = c.execute("""select * from patients where id = (?)""", (row[2],)).fetchone()
                patient = Patient(*fetched_patient_data)
                temp_list = list(row)
                temp_list.pop(2)
                temp_list.insert(2, patient)
                result_list.append(Employee(*temp_list))
            else:
                result_list.append(Employee(*row))

        self.end_conn()
        return result_list

    def find_employee_by_login_id(self, login_id):
        c = self.start_conn()
        fetched_employee_info = c.execute("""select * from employees where login_id = (?)""", (login_id,)).fetchone()
        if fetched_employee_info is None:
            return None
        employee = Employee(*fetched_employee_info)
        self.end_conn()
        return employee

    ## Flowsheet ======================================================================= ##

    def add_flowsheet(self, patient_id, time_line_id, vital_id):
        c = self.start_conn()
        c.execute("insert into flowsheet(patient_id, timeline_id, vital_id) values (?, ?, ?)",
                  (patient_id, time_line_id, vital_id,))
        self.commit_db()
        f_id = c.execute("select id from flowsheet order by id desc limit 1").fetchone()[0]
        self.end_conn()
        return self.find_flowsheet(f_id)

    def find_flowsheet(self, f_id):
        c = self.start_conn()
        flowsheet_info = c.execute("select * from flowsheet order by id=(?)", (f_id,)).fetchone()
        f_id = flowsheet_info[0]
        patient_id = flowsheet_info[1]
        time_line_id = flowsheet_info[2]
        v_id = flowsheet_info[3]

        patient_obj = self.find_patient_by_id(patient_id)
        time_line_obj = self.find_time_line_by_id(time_line_id)
        vital_obj = self.find_vital_by_id(v_id)
        flowsheet = FlowSheet(f_id, patient_obj, time_line_obj, vital_obj)
        self.end_conn()
        return flowsheet

    def clear_flowsheet_table(self):
        c = self.start_conn()
        c.execute("delete from flowsheet")
        self.commit_db()
        self.end_conn()

    def insert_dummy_flowsheet(self):
        c = self.start_conn()

        fetched_patient_id_list = [x[0] for x in c.execute("select id from patients").fetchall()]
        fetched_timeline_list = [x[0] for x in c.execute("select id from timeline").fetchall()]
        fetched_vital_list = [x[0] for x in c.execute("select id from vital").fetchall()]
        offset = 0
        for idx, patient_id in enumerate(fetched_patient_id_list):
            while True:
                timeline_id = random.choice(fetched_timeline_list)
                hospital_hours = random.randrange(40, 100)
                if timeline_id + hospital_hours < 55845:
                    break

            for i in range(hospital_hours):
                vital_id = fetched_vital_list[offset]
                offset += 1
                c.execute("insert into flowsheet(patient_id, timeline_id, vital_id) values (?, ?, ?)",
                          (patient_id, timeline_id + i, vital_id,))
                # print((patient_id, timeline_id, vital_id,))

        self.commit_db()
        self.end_conn()

    ## TimeLine ======================================================================= ##

    def find_date_obj_as_strf(self, strf_date_time):
        c = self.start_conn()
        result = c.execute("""select * from timeline where time_line_information = (?)""", (strf_date_time,)).fetchone()
        timeline_obj = TimeLine(*result)
        self.end_conn()
        return timeline_obj

    def find_time_line_by_id(self, t_id):
        c = self.start_conn()
        result = c.execute("""select * from timeline where id = (?)""", (t_id,)).fetchone()
        timeline_obj = TimeLine(*result)
        self.end_conn()
        return timeline_obj

    def clear_time_line_table(self):
        c = self.start_conn()
        c.execute("""delete from timeline""")
        self.commit_db()
        self.end_conn()

    def insert_dummy_timeline(self):
        c = self.start_conn()
        offset = 0
        date = datetime.datetime.strptime("2022-01-01 00:00", "%Y-%m-%d %H:%M")
        for i in range(365 * 3 * 24):
            temp_date = date + datetime.timedelta(hours=offset)
            offset += 1
            c.execute('insert into timeline(time_line_information) values (?)', (temp_date.strftime('%Y-%m-%d %H:%M'),))

        self.commit_db()
        self.end_conn()

    ## Vital ======================================================================= ##

    def find_vital_by_id(self, v_id):
        c = self.start_conn()
        result = c.execute("""select * from vital where id = (?)""", (v_id,)).fetchone()
        vital_obj = Vital(*result)
        self.end_conn()
        return vital_obj

    def clear_vital_table(self):
        c = self.start_conn()
        c.execute("""delete from vital""")
        self.commit_db()
        self.end_conn()

    def insert_dummy_vital_data(self):
        c = self.start_conn()

        for i in range(10000):
            bt = int(np.random.normal(scale=4) + 370)
            hr = int(np.random.normal(scale=10) + 80)
            rr = int(np.random.normal(scale=4) + 16)
            while True:
                sbp = int(np.random.normal(scale=30) + 140)
                dbp = int(np.random.normal(scale=20) + 100)
                mbp = (dbp * 2 + sbp) // 3
                if 60 > sbp - dbp > 25 and (dbp < 105):
                    break
            c.execute("""
                insert into vital(bt, hr, rr, sbp, dbp, mbp) values (?, ?, ?, ?, ?, ?)
            """, (bt, hr, rr, sbp, dbp, mbp,))

        self.commit_db()
        self.end_conn()

    @staticmethod
    def get_random_register_num_list(size):
        result_list = list()
        while len(result_list) < size:
            rand_num = f"{int(random.random() * (10 ** 6)):06d}"
            if rand_num not in result_list:
                result_list.append(rand_num)
        return result_list

    @staticmethod
    def get_random_back_ssn_num_list(size):
        result_list = list()
        while len(result_list) < size:
            gender = random.randint(1, 5)
            back_num = f'{int(random.random() * (10 ** 6)):06d}'
            sample_ssn = f'{gender}{back_num}'
            if sample_ssn not in result_list:
                result_list.append(sample_ssn)
        return result_list


if __name__ == '__main__':
    connector = DBConnector(test_option=True)
    connector.findAll_patients()
    # employees = connector.findAll_employees()
    # for e in employees:
    #     print(e)
    # connector.insert_dummy_time_test()
    # connector.clear_time_line_table()
    # connector.insert_dummy_vital_data()
    # connector.clear_vital_table()

    # connector.insert_dummy_flowsheet()
    # connector.clear_flowsheet_table()
    # obj = connector.find_patient_by_register_id("250496")
    # print(obj)
    # connector.insert_dummy_employees()
    # connector.clear_patients_table()
    # connector.insert_dummy_patient()
