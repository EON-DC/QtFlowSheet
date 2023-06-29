import datetime
import random
import sqlite3
import numpy as np

from faker import Faker

from class_employee import Employee
from class_patient import Patient


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

    def get_patient_by_register_id(self, register_id):
        c = self.start_conn()
        patient_data = c.execute("select * from patients where register_id = (?)", (register_id,)).fetchone()
        patient_obj = Patient(*patient_data)
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

    ## Flowsheet ======================================================================= ##
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
                timeline_id += i
                offset += 1
                c.execute("insert into flowsheet(patient_id, timeline_id, vital_id) values (?, ?, ?)",
                          (patient_id, timeline_id, vital_id,))
                # print((patient_id, timeline_id, vital_id,))

        self.commit_db()
        self.end_conn()

    ## TimeLine ======================================================================= ##

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
    # employees = connector.findAll_employees()
    # for e in employees:
    #     print(e)
    # connector.insert_dummy_time_test()
    # connector.clear_time_line_table()
    # connector.insert_dummy_vital_data()
    # connector.clear_vital_table()

    # connector.insert_dummy_flowsheet()

    # obj = connector.get_patient_by_register_id("048813")
    # connector.insert_dummy_employees()
    # connector.clear_patients_table()
    # connector.insert_dummy_patient()
