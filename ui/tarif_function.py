from PySide6 import QtCore, QtWidgets, QtGui


# from ui.tarif import Ui_Form

class Tarif_frontend(QtWidgets.QWidget):
    def __init__(self, db, main_form: QtWidgets.QWidget, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector
        self.main_form = main_form
        self.initUi()

    def initUi(self):
        self.ui.meterType_comboBox.addItem('220')
        self.ui.meterType_comboBox.addItem('380')

    def close(self) -> bool:
        self.main_form = None
        super().close()
