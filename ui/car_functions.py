from dataclasses import dataclass

from PySide6 import QtCore, QtWidgets, QtGui


import db_work
import sqlite_qwer
from ui.new_car import Ui_Form
import ui.cart_functions
import ui.member_functions
from ui.tableView_Models import *


class Car_frontend(QtWidgets.QWidget):
    TB_NAME = 'automobile'

    def __init__(self, db: db_work.Garage_DB, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.db = db
        self.ui.setupUi(self)

        self.mainForm = None
        self.carInfo = CarInfo()
        self.initUi()

    def initUi(self):

        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.add_pushButton.clicked.connect(self.add_car)

        # модель для changeOwner_tableView
        self.carInDbModel = CarTableViewModel()
        self.ui.carInDb_tableView.setModel(self.carInDbModel)

        # Автоматичкская подгонка столбцов по ширине
        self.ui.carInDb_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.getCarsFromDB()

    def getCarsFromDB(self):
        """Заполнение таблицы существующих пользователей из БД"""
        if self.db:
            self.db.execute(sqlite_qwer.sql_get_all_active(self.TB_NAME))
            if self.db.cursor:

                cars = self.db.cursor.fetchall()
                # self.userListModel.resetData()
                for car in cars:
                    cars_info = CarInfo(car[0], car[1], car[2])
                    self.carInDbModel.setItems(cars_info)

    def add_car(self):
        if not self.ui.carMark_lineEdit.text():
            return
        if not self.ui.gosNum_lineEdit.text():
            return
        self.carInfo.mark = self.ui.carMark_lineEdit.text()
        self.carInfo.gos_num = self.ui.gosNum_lineEdit.text()
        self.carInfo.id = ''        #ToDo здесь добавить запрос на id в БД и запрос собственника
        self.carInfo.own_id = ''
        self.mainForm.carInDbModel.setItems(self.carInfo)
        self.close()


@dataclass
class CarInfo:
    """Класс с инфорамцией об авто"""
    id: str = ''
    own_id: str = ''
    mark: str = ''
    gos_num: str = ''

