from db_connector import DBConnector


class LoginController:
    def __init__(self, conn):
        assert isinstance(conn, DBConnector)
        self.conn = conn