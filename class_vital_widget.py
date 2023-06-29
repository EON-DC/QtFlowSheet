from PyQt5 import QtCore, QtGui, QtWidgets

from class_vital_controller import VitalController
from ui_vital_widget import Ui_UIVitalWidget

class VitalWidget(QtWidgets.QWidget, Ui_UIVitalWidget):
    def __init__(self, vital_controller):
        assert isinstance(vital_controller, VitalController)
        self.controller = vital_controller
        super().__init__()
        self.setupUi(self)
