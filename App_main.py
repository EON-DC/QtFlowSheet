import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from class_login_controller import LoginController
from class_login_widget import LoginWidget
from class_vital_controller import VitalController
from db_connector import DBConnector


def main():
    connector = DBConnector(test_option=True)
    login_controller = LoginController(connector)

    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWidget(login_controller)
    login_window.show()

    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)

    app.exec_()


def show_error_message(message, traceback):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()
    traceback.print_exc()


if __name__ == '__main__':
    main()
