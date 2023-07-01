from PyQt5 import QtCore, QtGui, QtWidgets

from class_login_controller import LoginController
from class_vital_controller import VitalController
from class_vital_widget import VitalWidget
from ui_login_widget import Ui_UILoginWidget


class LoginWidget(QtWidgets.QWidget, Ui_UILoginWidget):
    def __init__(self, login_controller):
        assert isinstance(login_controller, LoginController)
        self.controller = login_controller
        super().__init__()
        self.setupUi(self)
        self.setFixedWidth(1300)
        self.setFixedHeight(500)
        self.main_window = None

        # 버튼 기능
        self.btn_login.clicked.connect(lambda state: self.login_button_clicked())
        # 엔터 칠시
        self.le_pw.returnPressed.connect(lambda: self.login_button_clicked())

    def login_button_clicked(self):
        login_id = self.le_login.text()
        login_pw = self.le_pw.text()
        if self.controller.login_access(login_id, login_pw):
            vital_controller = VitalController(self.controller.get_connect())
            self.main_window = VitalWidget(vital_controller)
            self.main_window.show()
            self.hide()
        else:
            QtWidgets.QMessageBox.warning(self, "인증 실패", "로그인 정보가 잘못 되었습니다.")




