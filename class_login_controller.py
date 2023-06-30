from db_connector import DBConnector


class LoginController:
    def __init__(self, conn):
        assert isinstance(conn, DBConnector)
        self.conn = conn

    def get_connect(self):
        return self.conn

    def login_access(self, login_id, login_pw):
        # if login_id == 'qwer' and login_pw == '1234':
        #     return True
        # else:
        #     return False
        return True