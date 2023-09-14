import sys

from PySide6 import QtCore, QtWidgets, QtGui


from ui.main_window import Ui_MainWindow
import constants
import db_work
import ui.dialogs
import ui.cart_functions

class Form_frontend(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_work.Garage_DB()
        self.cartObj = None                 # для отображения формы с карточкой объекта

        self.initUi()

        self.showStatusBarMessage(self.db.autoConnectBD()[1])  # пробуем подключиться к БД по умолчанию


        # self.initThread


    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.createBD_action.triggered.connect(self.db.create_db)   # создание новой бд
        self.ui.chooseBD_action.triggered.connect(self.openDB)         # выбор существующей бд
        self.ui.search_action.triggered.connect(self.showCartObject)

    def openDB(self):
        new_name = ui.dialogs.open_file_dialog()[0]
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
        self.cartObj = ui.cart_functions.Cart_frontend()
        self.cartObj.show()
# Press the green button in the gutter to run the script.


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = Form_frontend()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec())  # Если exit, то код дальше не исполняется