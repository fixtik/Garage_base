
from PySide6 import QtCore, QtWidgets, QtGui


from ui.cart_ import Ui_Form

import constants
import db_work
import ui.dialogs

class Cart_frontend(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()



    def initUi(self):
        self.setMinimumWidth(1000)