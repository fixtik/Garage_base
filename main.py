import sys
import os

from PySide6 import QtCore, QtWidgets, QtGui

import sqlite_qwer
from ui.main_window import Ui_MainWindow
import constants
import db_work
import ui.dialogs
import ui.cart_functions
import ui.contribute_functions
import ui.member_functions
import ui.electric_meter_func
import ui.new_garage_size_func
import ui.tableView_Models


class Form_frontend(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_work.Garage_DB()
        self.cartObj = None                 # для отображения формы с карточкой объекта
        self.typePay = None                 # для отображения формы редактирования видов платежей
        self.newMember = None               # для отображения формы добавления нового члена
        self.elMeter = None                 # для отображения формы с счетчиком
        self.garageSize = None             # для отображения формы размера гаража
        self.obj_model = ui.tableView_Models.ObjectTableViewModel()


        self.initUi()

        res, msg = self.db.autoConnectBD() # пробуем подключиться к БД по умолчанию
        self.showStatusBarMessage(msg)
        self.hideObjectUI(res)
        self.fill_main_tableview()



        # self.initThread

    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.createBD_action.triggered.connect(self.db.create_db)   # создание новой бд
        self.ui.chooseBD_action.triggered.connect(self.openDB)         # выбор существующей бд
        self.ui.openBase_pushButton.clicked.connect(self.openDB)
        self.ui.search_action.triggered.connect(self.showCartObject)   # отображение главной карточки объекта
        self.ui.kindPay_action.triggered.connect(self.showKindPayWindow) #отображение окна редактирования типов платежей
        self.ui.member_action.triggered.connect(self.showAddMemberWindow) # окно добавления нового члена
        self.ui.electric_action.triggered.connect(self.showElMeterWindow)
        self.ui.garage_action.triggered.connect(self.showGarageSizeWindow) # окно добавления размеров гаража
        self.ui.add_action.triggered.connect(self.showFullAddCart)  #окно добавления всех данных
        # таблица для отображения полей
        self.ui.tableView.setModel(self.obj_model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                           ResizeToContents)

        if os.path.isfile(constants.DEFAULT_VOA_IMG):
            pix = QtGui.QPixmap(constants.DEFAULT_VOA_IMG)
            pix = pix.scaled(constants.IMG_W, constants.IMG_W, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.voa_label.setPixmap(pix)

    def hideObjectUI(self, flag):
        """скрывает или показывает объекты интерфейса"""
        self.ui.voa_label.setVisible(not flag)
        self.ui.openBase_pushButton.setVisible(not flag)

        self.ui.tableView.setVisible(flag)
        if flag:
            self.ui.tableView.setFixedHeight(self.height())
        else:
            self.ui.tableView.setFixedHeight(self.height() // 2)

    def openDB(self):
        new_name = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_BD, constants.FILTER_BD)[0]
        if new_name:
            if self.db.choose_db(new_name):
                if not self.db:
                    self.db = db_work.Garage_DB(new_name)
                else:
                    self.db.choose_db(new_name)
                self.showStatusBarMessage(f"Файл БД {new_name} открыт")


    def showStatusBarMessage(self, msg: str):
        """вывод сообщения в статус бар"""
        self.ui.statusbar.showMessage(msg)

    def showCartObject(self):
        """Отображение окна карточки объекта"""
        self.cartObj = ui.cart_functions.Cart_frontend(db=self.db)
        self.cartObj.show()


    def showKindPayWindow(self):
        """Отображение окна редактирования вида платежа"""
        self.typePay = ui.contribute_functions.AddContrib_front(db=self.db)
        self.typePay.updateDataFromDB()
        self.typePay.hideDateField(False)
        self.typePay.show()

    def showGarageSizeWindow(self):
        """Отображение окна добавления размеров гаража"""
        self.garageSize = ui.new_garage_size_func.AddGarageSize_front(db=self.db)
        self.garageSize.updateDataFromDB()
        self.garageSize.show()

    def showAddMemberWindow(self):
        """Отображение окна добавления нового члена"""
        self.newMember = ui.member_functions.Member_front(db=self.db)
        self.newMember.show()

    def showElMeterWindow(self):
        """Отображение окна работы с эл. счетчкиами"""
        self.elMeter = ui.electric_meter_func.Electric_front(db=self.db)
        self.elMeter.show()

    def showFullAddCart(self):
        """Отображение окна для добавления всех данных одновременно (на основе карточки объекта)"""
        self.cartObj = ui.cart_functions.Cart_frontend(db=self.db)
        self.cartObj.ui.change_pushButton.setText(constants.BTN_TEXT_ADD)
        self.cartObj.show()

    def fill_main_tableview(self):
        """заполнение данных tableview"""
        if self.db:
            if self.db.execute(sqlite_qwer.sql_get_all_objects_for_list()):
                for obj in self.db.cursor.fetchall():
                    item = ui.cart_functions.ObjectInfo(obj[0], obj[1], obj[2], f'{obj[3]} {obj[4]} {obj[5]}', obj[6],
                                                        obj[7])
                    self.obj_model.setItems(item)





if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = Form_frontend()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec())  # Если exit, то код дальше не исполняется