from datetime import datetime

from db_connector import DBConnector


class VitalController:
    def __init__(self, conn):
        assert isinstance(conn, DBConnector)
        self.conn = conn

    def get_connect(self):
        return self.conn

    def fine_all_patients(self):
        return self.conn.findAll_patients()

    def find_patient(self, register_id):
        register_id: str
        return self.conn.find_patient_by_register_id(register_id)

    def find_date(self, datetime_obj):
        assert isinstance(datetime_obj, datetime)
        strf_date_time = datetime_obj.strftime("%Y-%m-%d %H:%M")
        time_line_obj = self.conn.find_date_obj_as_strf(strf_date_time)
        return time_line_obj

    def create_flowsheet(self, patient_obj, vital_category, value, time_line_id):
        pstmt = f"insert into vital({vital_category}) values ({value})"
        c = self.conn.start_conn()
        c.execute(pstmt)
        self.conn.commit_db()
        find_pstmt = f"select id from vital order by id desc limit 1"
        v_id = c.execute(find_pstmt).fetchone()[0]
        flowsheet = self.conn.add_flowsheet(patient_obj.patient_id, time_line_id, v_id)
        return flowsheet
    def execute_query_list(self, queries):
        c = self.conn.start_conn()
        try:
            for query in queries:
                c.execute(query)
            self.conn.commit_db()
        except Exception:
            print("commit 실패")
        finally:
            self.conn.end_conn()
