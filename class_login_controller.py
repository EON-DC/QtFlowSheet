from db_connector import DBConnector


class LoginController:
    def __init__(self, conn):
        assert isinstance(conn, DBConnector)
        self.conn = conn

    def get_connect(self):
        return self.conn

    def login_access(self, login_id, login_pw):
        employee = self.conn.find_employee_by_login_id(login_id)

        if employee is not None and employee.login_password == login_pw:
            return True
        else:
            return False
