import sys

from PySide6 import QtCore, QtWidgets, QtGui


from ui.main_window import Ui_MainWindow
import constants
import db_work
import ui.dialogs

class Form_backend(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_work.Garage_DB()

        self.initUi()
        # self.initThread


    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.createBD_action.triggered.connect(self.db.create_db)   # создание новой бд
        self.ui.chooseBD_action.triggered.connect(self.openDB)                    # выбор существующей бд

    def openDB(self):
        new_name = ui.dialogs.open_file_dialog()
        if new_name:
            if self.db:
                self.db = None
            self.db = db_work.Garage_DB()
            self.ui.statusbar.showMessage("БД открыта")
# Press the green button in the gutter to run the script.


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = Form_backend()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec())  # Если exit, то код дальше не исполняется