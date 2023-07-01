# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_patient_finder.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PatientFinder(object):
    def setupUi(self, PatientFinder):
        PatientFinder.setObjectName("PatientFinder")
        PatientFinder.resize(635, 562)
        self.verticalLayout = QtWidgets.QVBoxLayout(PatientFinder)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(PatientFinder)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.le_search = QtWidgets.QLineEdit(self.widget_2)
        self.le_search.setObjectName("le_search")
        self.horizontalLayout_2.addWidget(self.le_search)
        self.btn_search = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        spacerItem = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.table_widget_patient_list = QtWidgets.QTableWidget(self.widget)
        self.table_widget_patient_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget_patient_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_widget_patient_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_widget_patient_list.setObjectName("table_widget_patient_list")
        self.table_widget_patient_list.setColumnCount(3)
        self.table_widget_patient_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_patient_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_patient_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_patient_list.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.table_widget_patient_list)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(316, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.btn_cancel = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_confirm = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_confirm.sizePolicy().hasHeightForWidth())
        self.btn_confirm.setSizePolicy(sizePolicy)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(PatientFinder)
        QtCore.QMetaObject.connectSlotsByName(PatientFinder)

    def retranslateUi(self, PatientFinder):
        _translate = QtCore.QCoreApplication.translate
        PatientFinder.setWindowTitle(_translate("PatientFinder", "Form"))
        self.label.setText(_translate("PatientFinder", "이름 검색"))
        self.btn_search.setText(_translate("PatientFinder", "찾기"))
        item = self.table_widget_patient_list.horizontalHeaderItem(0)
        item.setText(_translate("PatientFinder", "이름"))
        item = self.table_widget_patient_list.horizontalHeaderItem(1)
        item.setText(_translate("PatientFinder", "생년월일"))
        item = self.table_widget_patient_list.horizontalHeaderItem(2)
        item.setText(_translate("PatientFinder", "등록번호"))
        self.label_2.setText(_translate("PatientFinder", "더블클릭도 선택가능"))
        self.btn_cancel.setText(_translate("PatientFinder", "취소"))
        self.btn_confirm.setText(_translate("PatientFinder", "선택하기"))
