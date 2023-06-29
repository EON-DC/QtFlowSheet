from PyQt5 import QtCore, QtGui, QtWidgets

from class_login_controller import LoginController
from ui_login_widget import Ui_UILoginWidget


class LoginWidget(QtWidgets.QWidget, Ui_UILoginWidget):
    def __init__(self, login_controller):
        assert isinstance(login_controller, LoginController)
        self.controller = login_controller
        super().__init__()
        self.setupUi(self)
