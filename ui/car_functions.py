from PySide6 import QtCore, QtWidgets, QtGui

import db_work
from ui.new_car import Ui_Form
import ui.cart_functions




class Car_frontend(QtWidgets.QWidget):

    def __init__(self, db: db_work.Garage_DB, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db

        self.mainForm = None
        self.carInfo = CarInfo()
        self.initUi()

    def initUi(self):

        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.add_pushButton.clicked.connect(self.add_car)


    def add_car(self):
        if not self.ui.carMark_lineEdit.text():
            return
        if not self.ui.gosNum_lineEdit.text():
            return
        self.carInfo.mark = self.ui.carMark_lineEdit.text()
        self.carInfo.gos_num = self.ui.gosNum_lineEdit.text()
        self.carInfo.id = ''        #ToDo здесь добавить запрос на id в БД и запрос собственника
        self.carInfo.own_id = ''
        self.mainForm.carModel.setItems(self.carInfo)
        self.close()




class CarInfo():
    """Класс с инфорамцией об авто"""
    def __init__(self):
        self.id = ''
        self.own_id = ''
        self.mark = ''
        self.gos_num = ''

