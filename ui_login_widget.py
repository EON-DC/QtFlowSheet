# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_login_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UILoginWidget(object):
    def setupUi(self, UILoginWidget):
        UILoginWidget.setObjectName("UILoginWidget")
        UILoginWidget.resize(1300, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UILoginWidget.sizePolicy().hasHeightForWidth())
        UILoginWidget.setSizePolicy(sizePolicy)
        UILoginWidget.setStyleSheet("#whole_widget {\n"
"    background-image: url(src/login_background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#frame_login{\n"
"    background-color: white;\n"
"}\n"
"\n"
"* {\n"
"    \n"
"    font: 12pt \"나눔고딕OTF\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(UILoginWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.whole_widget = QtWidgets.QWidget(UILoginWidget)
        self.whole_widget.setObjectName("whole_widget")
        self.frame_login = QtWidgets.QFrame(self.whole_widget)
        self.frame_login.setGeometry(QtCore.QRect(860, 240, 351, 141))
        self.frame_login.setObjectName("frame_login")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_login)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.frame_login)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.le_login = QtWidgets.QLineEdit(self.widget)
        self.le_login.setObjectName("le_login")
        self.verticalLayout_2.addWidget(self.le_login)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.le_pw = QtWidgets.QLineEdit(self.widget)
        self.le_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pw.setObjectName("le_pw")
        self.verticalLayout_2.addWidget(self.le_pw)
        self.horizontalLayout.addWidget(self.widget)
        self.btn_login = QtWidgets.QPushButton(self.frame_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.verticalLayout.addWidget(self.whole_widget)

        self.retranslateUi(UILoginWidget)
        QtCore.QMetaObject.connectSlotsByName(UILoginWidget)

    def retranslateUi(self, UILoginWidget):
        _translate = QtCore.QCoreApplication.translate
        UILoginWidget.setWindowTitle(_translate("UILoginWidget", "Form"))
        self.label.setText(_translate("UILoginWidget", "ID"))
        self.label_2.setText(_translate("UILoginWidget", "Password"))
        self.btn_login.setText(_translate("UILoginWidget", "로그인"))
