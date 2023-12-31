# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_vital_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UIVitalWidget(object):
    def setupUi(self, UIVitalWidget):
        UIVitalWidget.setObjectName("UIVitalWidget")
        UIVitalWidget.resize(1300, 770)
        UIVitalWidget.setStyleSheet("* {\n"
"    font: 12pt \"나눔고딕OTF\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color : white;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(UIVitalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(UIVitalWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.le_register_id = QtWidgets.QLineEdit(self.widget_2)
        self.le_register_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_register_id.setObjectName("le_register_id")
        self.horizontalLayout_2.addWidget(self.le_register_id)
        self.btn_fetch = QtWidgets.QPushButton(self.widget_2)
        self.btn_fetch.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_fetch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../src/lense_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fetch.setIcon(icon)
        self.btn_fetch.setObjectName("btn_fetch")
        self.horizontalLayout_2.addWidget(self.btn_fetch)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_name = QtWidgets.QLabel(self.widget_2)
        self.label_name.setMinimumSize(QtCore.QSize(60, 0))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_2.addWidget(self.label_name)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_birth_date = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_birth_date.sizePolicy().hasHeightForWidth())
        self.label_birth_date.setSizePolicy(sizePolicy)
        self.label_birth_date.setMinimumSize(QtCore.QSize(100, 0))
        self.label_birth_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birth_date.setObjectName("label_birth_date")
        self.horizontalLayout_2.addWidget(self.label_birth_date)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_admission_date = QtWidgets.QLabel(self.widget_2)
        self.label_admission_date.setMinimumSize(QtCore.QSize(100, 0))
        self.label_admission_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_admission_date.setObjectName("label_admission_date")
        self.horizontalLayout_2.addWidget(self.label_admission_date)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.date_start = QtWidgets.QDateEdit(self.widget_3)
        self.date_start.setObjectName("date_start")
        self.horizontalLayout.addWidget(self.date_start)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.date_end = QtWidgets.QDateEdit(self.widget_3)
        self.date_end.setObjectName("date_end")
        self.horizontalLayout.addWidget(self.date_end)
        self.btn_select_date = QtWidgets.QPushButton(self.widget_3)
        self.btn_select_date.setText("")
        self.btn_select_date.setIcon(icon)
        self.btn_select_date.setObjectName("btn_select_date")
        self.horizontalLayout.addWidget(self.btn_select_date)
        self.btn_select_optimal_date = QtWidgets.QPushButton(self.widget_3)
        self.btn_select_optimal_date.setObjectName("btn_select_optimal_date")
        self.horizontalLayout.addWidget(self.btn_select_optimal_date)
        spacerItem1 = QtWidgets.QSpacerItem(752, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.vital_table = QtWidgets.QTableWidget(self.widget)
        self.vital_table.setObjectName("vital_table")
        self.vital_table.setColumnCount(12)
        self.vital_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.vital_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.vital_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.vital_table.setItem(0, 0, item)
        self.verticalLayout_2.addWidget(self.vital_table)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(1015, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_restore = QtWidgets.QPushButton(self.widget_4)
        self.btn_restore.setObjectName("btn_restore")
        self.horizontalLayout_3.addWidget(self.btn_restore)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_save = QtWidgets.QPushButton(self.widget_4)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(UIVitalWidget)
        QtCore.QMetaObject.connectSlotsByName(UIVitalWidget)

    def retranslateUi(self, UIVitalWidget):
        _translate = QtCore.QCoreApplication.translate
        UIVitalWidget.setWindowTitle(_translate("UIVitalWidget", "Form"))
        self.label.setText(_translate("UIVitalWidget", "등록번호"))
        self.label_2.setText(_translate("UIVitalWidget", "이름"))
        self.label_name.setText(_translate("UIVitalWidget", "OOO"))
        self.label_4.setText(_translate("UIVitalWidget", "생년월일"))
        self.label_birth_date.setText(_translate("UIVitalWidget", "1900-01-01"))
        self.label_6.setText(_translate("UIVitalWidget", "입원일자"))
        self.label_admission_date.setText(_translate("UIVitalWidget", "1900-01-01"))
        self.label_8.setText(_translate("UIVitalWidget", "조회시작"))
        self.label_9.setText(_translate("UIVitalWidget", "조회종료"))
        self.btn_select_optimal_date.setToolTip(_translate("UIVitalWidget", "최근3일 데이터를 조회합니다."))
        self.btn_select_optimal_date.setText(_translate("UIVitalWidget", "최적조회"))
        item = self.vital_table.verticalHeaderItem(0)
        item.setText(_translate("UIVitalWidget", "BT(℃)"))
        item = self.vital_table.verticalHeaderItem(1)
        item.setText(_translate("UIVitalWidget", "HR(bpm)"))
        item = self.vital_table.verticalHeaderItem(2)
        item.setText(_translate("UIVitalWidget", "RR(/min)"))
        item = self.vital_table.verticalHeaderItem(3)
        item.setText(_translate("UIVitalWidget", "SBP(mmHg)"))
        item = self.vital_table.verticalHeaderItem(4)
        item.setText(_translate("UIVitalWidget", "DBP(mmHg)"))
        item = self.vital_table.verticalHeaderItem(5)
        item.setText(_translate("UIVitalWidget", "mBP(mmHg)"))
        item = self.vital_table.horizontalHeaderItem(0)
        item.setText(_translate("UIVitalWidget", "01-01 00:00"))
        item = self.vital_table.horizontalHeaderItem(1)
        item.setText(_translate("UIVitalWidget", "01-01 01:00"))
        item = self.vital_table.horizontalHeaderItem(2)
        item.setText(_translate("UIVitalWidget", "01-01 02:00"))
        item = self.vital_table.horizontalHeaderItem(3)
        item.setText(_translate("UIVitalWidget", "01-01 03:00"))
        item = self.vital_table.horizontalHeaderItem(4)
        item.setText(_translate("UIVitalWidget", "01-01 04:00"))
        item = self.vital_table.horizontalHeaderItem(5)
        item.setText(_translate("UIVitalWidget", "01-01 05:00"))
        item = self.vital_table.horizontalHeaderItem(6)
        item.setText(_translate("UIVitalWidget", "01-01 06:00"))
        item = self.vital_table.horizontalHeaderItem(7)
        item.setText(_translate("UIVitalWidget", "01-01 07:00"))
        item = self.vital_table.horizontalHeaderItem(8)
        item.setText(_translate("UIVitalWidget", "01-01 08:00"))
        item = self.vital_table.horizontalHeaderItem(9)
        item.setText(_translate("UIVitalWidget", "01-01 09:00"))
        item = self.vital_table.horizontalHeaderItem(10)
        item.setText(_translate("UIVitalWidget", "01-01 10:00"))
        item = self.vital_table.horizontalHeaderItem(11)
        item.setText(_translate("UIVitalWidget", "01-01 11:00"))
        __sortingEnabled = self.vital_table.isSortingEnabled()
        self.vital_table.setSortingEnabled(False)
        self.vital_table.setSortingEnabled(__sortingEnabled)
        self.btn_restore.setText(_translate("UIVitalWidget", "되돌리기"))
        self.btn_save.setText(_translate("UIVitalWidget", "저장"))
