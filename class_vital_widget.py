import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from class_patient import Patient
from class_vital import Vital
from class_vital_controller import VitalController
from ui_vital_widget import Ui_UIVitalWidget


class VitalWidget(QtWidgets.QWidget, Ui_UIVitalWidget):
    def __init__(self, vital_controller):
        assert isinstance(vital_controller, VitalController)
        self.controller = vital_controller
        super().__init__()
        self.setupUi(self)
        self.initialize_label()
        self.initialize_trigger()
        self.patient_obj = None
        self.query_list = list()

    def initialize_label(self):
        self.label_name.setText('')
        self.label_birth_date.setText('')
        self.label_admission_date.setText('')
        now_date = datetime.datetime.now()
        two_day_before = datetime.datetime.now()
        two_day_before = two_day_before - datetime.timedelta(days=2)
        q_start_date = QtCore.QDate()
        q_start_date.setDate(two_day_before.year, two_day_before.month, two_day_before.day)
        q_end_date = QtCore.QDate()
        q_end_date.setDate(now_date.year, now_date.month, now_date.day)
        self.date_start.setDate(q_start_date)
        self.date_end.setDate(q_end_date)
        self.resize_column_width_and_auto_scroll_move()

    def resize_column_width_and_auto_scroll_move(self):
        for i in range(self.vital_table.columnCount()):
            self.vital_table.setColumnWidth(i, self.width() // 10)
        self.vital_table.verticalHeader().setFixedWidth(130)
        end_index = 0
        first_cell = self.vital_table.item(0, 0)
        if first_cell is None:
            return

        for i in range(self.vital_table.columnCount() - 1, 0, -1):
            if self.vital_table.item(0, i).text() != '':
                if i + 3 < self.vital_table.columnCount():
                    end_index = i + 3
                else:
                    end_index = i
                break
        if end_index != 0:
            self.vital_table.scrollTo(self.vital_table.model().index(0, end_index))

    def restore_btn_clicked(self):
        self.table_refresh_as_date()
        self.query_list.clear()

    def add_change_query(self, row, col):
        if self.vital_table.item(row, col).text().isdigit() is False:
            self.vital_table.cellChanged.disconnect()
            self.vital_table.item(row, col).setText('')
            self.vital_table.cellChanged.connect(lambda row, col: self.add_change_query(row, col))
            QtWidgets.QMessageBox.about(self, "알림", "숫자로 입력해주세요.")
            return

        has_same_item = False
        same_item_index = -1
        for idx, element in enumerate(self.query_list):
            if element[0] == row and element[1] == col:
                has_same_item = True
                same_item_index = idx
                break
        if has_same_item is True:
            self.query_list.pop(same_item_index)
            self.query_list.insert(same_item_index, (row, col, int(self.vital_table.item(row, col).text())))
        else:
            self.query_list.append((row, col, int(self.vital_table.item(row, col).text())))

    def convert_query_list(self):
        result_list = list()
        for element in self.query_list:
            row = element[0]
            col = element[1]
            changed_value = element[2]
            col_head_text = self.vital_table.horizontalHeaderItem(col).text()
            find_flowsheet = self.patient_obj.find_flowsheet_by_datetime(col_head_text)
            row_name = Vital.vital_column_name_list[row]
            if find_flowsheet is not None:
                print('found!')
                v_id = find_flowsheet.vital.vital_id
            else:
                print("cannot found")
                print(type(self.vital_table.item(row, col)))
                t_id = self.vital_table.item(row, col).time_line.time_line_id
                flowsheet = self.controller.create_flowsheet(self.patient_obj, row_name, changed_value, t_id)
                v_id = flowsheet.vital.vital_id
                self.patient_obj.update_flowsheet(flowsheet)
            pstmt = f"update vital set {row_name} = {changed_value} where id = {v_id}"
            result_list.append(pstmt)
        return result_list

    def btn_save_clicked(self):
        converted_query_list = self.convert_query_list()
        for i in converted_query_list:
            print(i)
        self.controller.execute_query_list(converted_query_list)
        self.btn_fetch.click()

    def btn_restore_clicked(self):
        self.btn_fetch.click()

    def close(self):
        if len(self.query_list) != 0:
            question_dialog = QtWidgets.QMessageBox.question(self, '확인', "변경 후 저장되지 않은 정보가 있습니다. 그래도 변경하시겠습니까?")
            if question_dialog == QtWidgets.QMessageBox.Yes:
                super().close()

    def initialize_trigger(self):
        self.btn_fetch.clicked.connect(lambda state: self.search_patient(self.le_register_id.text()))
        self.le_register_id.returnPressed.connect(lambda: self.btn_fetch.click())
        self.btn_select_date.clicked.connect(lambda state: self.table_refresh_as_date())
        self.btn_select_optimal_date.clicked.connect(lambda state: self.btn_fetch.click())
        self.vital_table.cellChanged.connect(lambda row, col: self.add_change_query(row, col))
        self.btn_save.clicked.connect(lambda state: self.btn_save_clicked())
        self.btn_restore.clicked.connect(lambda state: self.btn_restore_clicked())

    def search_patient(self, register_id):
        register_id: str
        patient = self.controller.find_patient(register_id)
        if patient is None:
            return
        else:
            self.patient_obj = patient
            self.refresh_patient_information()

    def refresh_patient_information(self):
        patient = self.patient_obj
        self.label_name.setText(patient.name)
        patient.birth_date: datetime.datetime
        self.label_birth_date.setText(patient.birth_date.strftime('%Y-%m-%d'))
        self.label_admission_date.setText(
            patient.flowSheet_list[0].time_line.time_line_information.strftime('%Y-%m-%d'))
        start_date = patient.flowSheet_list[0].time_line.time_line_information
        end_date = patient.flowSheet_list[len(patient.flowSheet_list) - 1].time_line.time_line_information
        q_start_date = QtCore.QDate()
        q_start_date.setDate(start_date.year, start_date.month, start_date.day)
        q_end_date = QtCore.QDate()
        q_end_date.setDate(end_date.year, end_date.month, end_date.day)
        self.date_start.setDate(q_start_date)
        self.date_end.setDate(q_end_date)
        self.btn_select_date.click()

    def table_refresh_as_date(self):
        start_date = datetime.datetime.strptime(self.date_start.text(), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(self.date_end.text(), '%Y-%m-%d')

        if (end_date - start_date).days >= 60:
            QtWidgets.QMessageBox.warning(self, "오류", "60일 이상 한번에 조회하실 수 없습니다.")
            return

        patient = self.patient_obj

        self.clear_table(start_date, end_date)

        # start_index = 0
        # for col_idx in range(self.vital_table.columnCount()):
        #     col_header_text = self.vital_table.horizontalHeaderItem(col_idx).text()
        #     start_datetime_text = patient.flowSheet_list[0].time_line.time_line_information.strftime('%m-%d %H:%M')
        #     if col_header_text == start_datetime_text:
        #         start_index = col_idx
        #         break
        self.vital_table.cellChanged.disconnect()
        patient: Patient

        selected_strf_date = list()

        for col_idx in range(self.vital_table.columnCount()):
            strf_date = self.vital_table.horizontalHeaderItem(col_idx).text()
            selected_strf_date.append((col_idx, strf_date))

        for col_idx, strf_date in selected_strf_date:
            flowsheet = self.patient_obj.find_flowsheet_by_datetime(strf_date)
            if flowsheet is not None:
                bt_str = str(flowsheet.vital.body_temperature)
                bt = f"{bt_str[:2]}.{bt_str[2:]}"
                hr = str(flowsheet.vital.heart_rate)
                rr = str(flowsheet.vital.respiration_rate)
                sbp = str(flowsheet.vital.systolic_blood_pressure)
                dbp = str(flowsheet.vital.diastolic_blood_pressure)
                mbp = str(flowsheet.vital.mean_blood_pressure)
                time_line_obj = flowsheet.time_line
                self.set_table_cell_info(bt, 0, col_idx, time_line_obj, Vital.vital_column_name_list[0])
                self.set_table_cell_info(hr, 1, col_idx, time_line_obj, Vital.vital_column_name_list[1])
                self.set_table_cell_info(rr, 2, col_idx, time_line_obj, Vital.vital_column_name_list[2])
                self.set_table_cell_info(sbp, 3, col_idx, time_line_obj, Vital.vital_column_name_list[3])
                self.set_table_cell_info(dbp, 4, col_idx, time_line_obj, Vital.vital_column_name_list[4])
                self.set_table_cell_info(mbp, 5, col_idx, time_line_obj, Vital.vital_column_name_list[5])

        # for idx, flowsheet in enumerate(patient.flowSheet_list):
        #     col_idx = idx + start_index
        #     bt_str = str(flowsheet.vital.body_temperature)
        #     bt = f"{bt_str[:2]}.{bt_str[2:]}"
        #     hr = str(flowsheet.vital.heart_rate)
        #     rr = str(flowsheet.vital.respiration_rate)
        #     sbp = str(flowsheet.vital.systolic_blood_pressure)
        #     dbp = str(flowsheet.vital.diastolic_blood_pressure)
        #     mbp = str(flowsheet.vital.mean_blood_pressure)
        #     time_line_obj = flowsheet.time_line
        #
        #     self.set_table_cell_info(bt, 0, col_idx, time_line_obj)
        #     self.set_table_cell_info(hr, 1, col_idx,time_line_obj)
        #     self.set_table_cell_info(rr, 2, col_idx,time_line_obj)
        #     self.set_table_cell_info(sbp, 3, col_idx,time_line_obj)
        #     self.set_table_cell_info(dbp, 4, col_idx,time_line_obj)
        #     self.set_table_cell_info(mbp, 5, col_idx,time_line_obj)

        for row_index in range(self.vital_table.rowCount()):
            for col_index in range(self.vital_table.columnCount()):
                if self.vital_table.item(row_index, col_index) is None:
                    col_time_line_obj = self.vital_table.horizontalHeaderItem(col_idx).time_line
                    category = Vital.vital_column_name_list[row_index]
                    self.vital_table.setItem(row_index, col_index,
                                             CustomQTableWidgetItem('', col_time_line_obj, category))

        self.resize_column_width_and_auto_scroll_move()
        self.vital_table.cellChanged.connect(lambda row, col: self.add_change_query(row, col))

        self.query_list.clear()

    def set_table_cell_info(self, text, row, col, time_line_obj, category):
        cell = CustomQTableWidgetItem(text, time_line_obj, category)
        self.vital_table.setItem(row, col, cell)

    def clear_table(self, start_date, end_date):
        row = self.vital_table.rowCount()
        col = self.vital_table.columnCount()
        for col_idx in range(col):
            self.vital_table.takeHorizontalHeaderItem(col_idx)

        for row_idx in range(row):
            for col_idx in range(col):
                if self.vital_table.cellWidget(row_idx, col_idx) is not None:
                    self.vital_table.cellWidget(row_idx, col_idx).deleteLater()

        delta = end_date - start_date
        col_count = (delta.days + 1) * 24
        self.vital_table.setColumnCount(col_count)
        for col_idx in range(col_count):
            start_date: datetime.datetime
            header = start_date + datetime.timedelta(hours=col_idx)
            time_line_obj = self.controller.find_date(header)
            header_str = header.strftime('%m-%d %H:%M')
            self.vital_table.setHorizontalHeaderItem(col_idx,
                                                     CustomQTableWidgetItem(header_str, time_line_obj, 'header'))


class CustomQTableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, text, time_line_obj, category):
        self.value = text
        self.time_line = time_line_obj
        self.category = category
        super().__init__(text)
        self.setTextAlignment(QtCore.Qt.AlignCenter)
