import sys

from PySide6 import QtCore, QtWidgets, QtGui


from ui.main_window import Ui_MainWindow
import constants
import db_work
import ui.dialogs
import ui.cart_functions
import ui.contribute_functions
import ui.member_functions
import ui.electric_meter_func
import ui.new_garage_size_func


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

        self.initUi()

        self.showStatusBarMessage(self.db.autoConnectBD()[1])  # пробуем подключиться к БД по умолчанию


        # self.initThread

    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.createBD_action.triggered.connect(self.db.create_db)   # создание новой бд
        self.ui.chooseBD_action.triggered.connect(self.openDB)         # выбор существующей бд
        self.ui.search_action.triggered.connect(self.showCartObject)   # отображение главной карточки объекта
        self.ui.kindPay_action.triggered.connect(self.showKindPayWindow) #отображение окна редактирования типов платежей
        self.ui.member_action.triggered.connect(self.showAddMemberWindow) # окно добавления нового члена
        self.ui.electric_action.triggered.connect(self.showElMeterWindow)
        self.ui.garage_action.triggered.connect(self.showGarageSizeWindow) # окно добавления размеров гаража

    def openDB(self):
        new_name = ui.dialogs.open_file_dialog("Выберите файл БД", '*.db')[0]
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
        self.cartObj = ui.cart_functions.Cart_frontend()
        self.cartObj.db = self.db
        self.cartObj.updateDataFromDB()
        self.cartObj.show()


    def showKindPayWindow(self):
        """Отображение окна редактирования вида платежа"""
        self.typePay = ui.contribute_functions.AddContrib_front()
        self.typePay.db = self.db
        self.typePay.updateDataFromDB()
        self.typePay.hideDateField(False)
        self.typePay.show()

    def showGarageSizeWindow(self):
        """Отображение окна добавления размеров гаража"""
        self.garageSize = ui.new_garage_size_func.AddGarageSize_front()
        self.garageSize.db = self.db
        self.garageSize.updateDataFromDB()
        self.garageSize.show()

    def showAddMemberWindow(self):
        """Отображение окна добавления нового члена"""
        self.newMember = ui.member_functions.Member_front()
        self.newMember.db = self.db
        self.newMember.show()

    def showElMeterWindow(self):
        """Отображение окна работы с эл. счетчкиами"""
        self.elMeter = ui.electric_meter_func.Electric_front()
        self.elMeter.db = self.db
        self.elMeter.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = Form_frontend()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec())  # Если exit, то код дальше не исполняется