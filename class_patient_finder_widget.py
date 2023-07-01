from PyQt5 import QtCore, QtGui, QtWidgets

from class_vital_controller import VitalController
from ui_patient_finder import Ui_PatientFinder


class PatientFinder(QtWidgets.QWidget, Ui_PatientFinder):
    def __init__(self, login_window, controller):
        assert isinstance(controller, VitalController)
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.login_window = login_window
        self.set_trigger()

    def set_trigger(self):
        self.table_widget_patient_list.cellDoubleClicked.connect(
            lambda row, col: self.send_register_id_to_vital_window(row))
        self.btn_cancel.clicked.connect(lambda state: self.hide())
        self.btn_confirm.clicked.connect(lambda state: self.btn_confirm_clicked())
        self.btn_search.clicked.connect(lambda state: self.btn_search_clicked())
        self.le_search.returnPressed.connect(lambda: self.btn_search_clicked())

    def btn_confirm_clicked(self):
        current_row = self.table_widget_patient_list.currentRow()
        if current_row == -1:
            return
        current_row: QtWidgets.QTableWidgetItem
        self.send_register_id_to_vital_window(current_row)

    def btn_search_clicked(self):
        self.table_widget_patient_list.clear()
        self.table_widget_patient_list.setColumnCount(3)
        self.table_widget_patient_list.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("이름"))
        self.table_widget_patient_list.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("생년월일"))
        self.table_widget_patient_list.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("등록번호"))
        self.table_widget_patient_list.setColumnWidth(0, 100)
        self.table_widget_patient_list.setColumnWidth(1, 120)
        self.table_widget_patient_list.setColumnWidth(2, 100)

        all_patient_list = self.controller.fine_all_patients()
        patient_list = list()

        search_text = self.le_search.text()
        for p in all_patient_list:
            if search_text in p.name:
                patient_list.append(p)

        self.table_widget_patient_list.setRowCount(len(patient_list))
        for idx, p in enumerate(patient_list):
            self.table_widget_patient_list.setVerticalHeaderItem(idx, PatientTableWidgetItem(f"{idx + 1}", p))
            self.table_widget_patient_list.setItem(idx, 0, QtWidgets.QTableWidgetItem(p.name))
            birth_day_str = p.birth_date.strftime('%Y년 %m월 %d일')  # 생년월일
            self.table_widget_patient_list.setItem(idx, 1, QtWidgets.QTableWidgetItem(birth_day_str))
            self.table_widget_patient_list.setItem(idx, 2, QtWidgets.QTableWidgetItem(p.register_id))

        row_count = self.table_widget_patient_list.rowCount()
        col_count = self.table_widget_patient_list.columnCount()

        for row in range(row_count):
            for col in range(col_count):
                self.table_widget_patient_list.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)

    def show(self):
        self.refresh_table_widget()
        super().show()

    def send_register_id_to_vital_window(self, row_index):
        r_id = self.table_widget_patient_list.verticalHeaderItem(row_index).patients_obj.register_id
        if r_id is None:
            return
        self.hide()
        self.login_window.le_register_id.setText(f"{r_id}")
        self.login_window.btn_fetch.click()

    def refresh_table_widget(self):
        self.table_widget_patient_list.clear()
        self.table_widget_patient_list.setColumnCount(3)
        self.table_widget_patient_list.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("이름"))
        self.table_widget_patient_list.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("생년월일"))
        self.table_widget_patient_list.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("등록번호"))
        self.table_widget_patient_list.setColumnWidth(0, 100)
        self.table_widget_patient_list.setColumnWidth(1, 120)
        self.table_widget_patient_list.setColumnWidth(2, 100)

        patient_list = self.controller.fine_all_patients()
        self.table_widget_patient_list.setRowCount(len(patient_list))
        for idx, p in enumerate(patient_list):
            self.table_widget_patient_list.setVerticalHeaderItem(idx, PatientTableWidgetItem(f"{idx + 1}", p))
            self.table_widget_patient_list.setItem(idx, 0, QtWidgets.QTableWidgetItem(p.name))
            birth_day_str = p.birth_date.strftime('%Y년 %m월 %d일')  # 생년월일
            self.table_widget_patient_list.setItem(idx, 1, QtWidgets.QTableWidgetItem(birth_day_str))
            self.table_widget_patient_list.setItem(idx, 2, QtWidgets.QTableWidgetItem(p.register_id))

        row_count = self.table_widget_patient_list.rowCount()
        col_count = self.table_widget_patient_list.columnCount()

        for row in range(row_count):
            for col in range(col_count):
                self.table_widget_patient_list.item(row, col).setTextAlignment(QtCore.Qt.AlignCenter)


class PatientTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, text, patient):
        super().__init__(text)
        self.patients_obj = patient
