from PySide6 import QtCore, QtWidgets, QtGui


import db_work
import sqlite_qwer
from ui.new_car import Ui_Form
import ui.cart_functions
import ui.member_functions
from ui.tableView_Models import *


class Car_frontend(QtWidgets.QWidget):
    TB_NAME = 'garage_member'

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
        self.changeOwnerModel = UsersTableViewModelLite()
        self.ui.changeOwner_tableView.setModel(self.changeOwnerModel)

        # Автоматичкская подгонка столбцов по ширине
        self.ui.changeOwner_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.getUsersListFromDB()

    def getUsersListFromDB(self):
        """Заполнение таблицы существующих пользователей из БД"""
        if self.db:
            self.db.execute(sqlite_qwer.sql_get_all_active(self.TB_NAME))
            if self.db.cursor:

                users = self.db.cursor.fetchall()
                # self.userListModel.resetData()
                for user in users:
                    us_info = ui.member_functions.User_Info(user[0], f'{user[1]} {user[2]} {user[3]}', user[4], user[6],
                                                            user[7])
                    self.changeOwnerModel.setItems(us_info)

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

