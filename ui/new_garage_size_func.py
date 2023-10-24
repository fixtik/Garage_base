import dataclasses

from PySide6 import QtCore, QtWidgets, QtGui

import constants
import ui.new_garage_size as addWid
import ui.new_garage_size_addSize as addK
import ui.dialogs
import ui.cart_functions
import ui.cart_functions
import sqlite_qwer
import ui.validators


class AddGarageSize_front(QtWidgets.QWidget):
    TB_NAME = 'type_size'

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = addWid.Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # БД
        self.mainForm = None  # Родительская форма
        self.garageSize_form = None # Форма добавления нового вида платежа
        self.garage = None       # объект для передачи данных в другую форму
        self.garage_ids = []   # список с id-платежа из БД, индекс соответствует индексу в combobox
        self.cur_indx = None   # текущий выбранный индекс в combobox

        self.initUi()

    def initUi(self):
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.ok_pushButton.clicked.connect(self.okPushBtnClk)
        # self.ui.addSize_pushButton.clicked.connect(self.addGarageSize)
        self.ui.delSize_pushButton.clicked.connect(self. delGarageSize)
        self.ui.size_comboBox.currentIndexChanged.connect(self.itemChanged)
        # валидаторы
        self.ui.width_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.length_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.height_lineEdit.setValidator(ui.validators.floatValidator())
        # заголовки
        self.setWindowTitle(constants.WINDOW_TITLE_ADD_SIZE)



    def addGarageSize(self):
        """вызов окна для добавления размеров гаража"""
        self.garageSize_form = AddSizeGarage_front(self.db)
        self.garageSize_form.mainForm = self
        self.garageSize_form.show()

    def fillGarageSizeFromBase(self):
        if self.db:
            self.db.execute(sqlite_qwer.sql_select_all_from_table(self.TB_NAME))
            size = self.db.cursor.fetchall()
            self.garage_ids.clear()
            self.ui.size_comboBox.clear()
            for item in size:
                cont = GarageSizeStructure()
                cont.id = item[0]
                self.garage_ids.append(cont.id)
                cont.width = format(item[1]).rstrip('0').rstrip('.')
                cont.len = format(item[2]).rstrip('0').rstrip('.')
                cont.height = format(item[3]).rstrip('0').rstrip('.')
                cont.comment = item[4]
                self.ui.size_comboBox.addItem(str(cont.width) + ' x ' + str(cont.len) + ' x ' + str(cont.height))

            self.itemChanged()

    def itemChanged(self):
        """изменение данных в полях при изменении выбранной позиции"""
        if self.ui.size_comboBox.currentIndex() == -1:
            return
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(self.TB_NAME,
                                                             self.garage_ids[self.ui.size_comboBox.currentIndex()]))
        contrib = self.db.cursor.fetchall()

        self.ui.width_lineEdit.setText(str(contrib[0][1]))
        self.ui.length_lineEdit.setText(str(contrib[0][2]))
        self.ui.height_lineEdit.setText(str(contrib[0][3]))
        self.ui.comment_lineEdit.setText(contrib[0][4])

    def updateDataFromDB(self):
        """Обновление данных из БД для отображения в полях"""
        self.fillGarageSizeFromBase()

    def delGarageSize(self):
        """удаление размеров гаража из базы"""
        if not self.ui.size_comboBox.itemText(self.ui.size_comboBox.currentIndex()):
            return
        q = ui.dialogs.onShowСonfirmation(self, "Подтверждение действия", "Вы уверены, что хотите удалить выбранные размеры гаража?")
        if q:
            self.db.execute(sqlite_qwer.sql_delete_rec_by_table_name_and_id(self.TB_NAME,
                                                                            self.garage_ids[self.ui.size_comboBox.currentIndex()]))
            self.updateDataFromDB()

    def okPushBtnClk(self):
        """действие при нажатии Добавить или Применить"""
        if self.mainForm: # если добаление платежа в карточку
            if not (self.ui.size_comboBox.currentText() and self.ui.width_lineEdit.text() and self.ui.length_lineEdit.text() and self.ui.height_lineEdit.text()):
                ui.dialogs.onShowError(self, 'Ошибка', 'Вы не заполнили все поля')
                return
            self.garage = GarageSizeStructure()
            self.garage.width = self.ui.width_lineEdit.text()
            self.garage.len = self.ui.length_lineEdit.text()
            self.garage.height = self.ui.height_lineEdit.text()
            self.garage.comment = self.ui.comment_lineEdit.text()

            self.mainForm.contribModel.setItems(self.garage)
            self.close()
            return
        self.db.execute(sqlite_qwer.sql_update_garage_size(self.garage_ids[self.ui.size_comboBox.currentIndex()],
                                                            float(self.ui.width_lineEdit.text().replace(',', '.')),
                                                            float(self.ui.length_lineEdit.text().replace(',', '.')),
                                                            float(self.ui.height_lineEdit.text().replace(',', '.')),
                                                            self.ui.comment_lineEdit.text()))
        self.updateDataFromDB()


@dataclasses
class GarageSizeStructure():
    """Класс информации о размерах гаража"""

    def __init__(self):
        self.id = ''            # id записи
        self.width = ''       # ширина гаража
        self.len = ''       # длина гаража
        self.height = ''     # высота гаража
        self.comment = ''

class AddSizeGarage_front(QtWidgets.QWidget):
    """Виджет для добавления размеров гаража в бд"""

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = addK.Ui_Form()
        self.ui.setupUi(self)

        self.mainForm = None
        self.db = db

        self.initUi()

    def initUi(self):
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.ok_pushButton.clicked.connect(self.okPushBtnClk)
        self.ui.width_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.length_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.height_lineEdit.setValidator(ui.validators.floatValidator())

    def okPushBtnClk(self):
        """нажатие кнопки ок"""
        if self.mainForm:
            if not(self.ui.width_lineEdit.text() and self.ui.length_lineEdit.text() and self.ui.height_lineEdit.text()):
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
                return
            if self.db.connect:
                self.ui.width_lineEdit.setText(self.ui.width_lineEdit.text().replace(',', '.'))
                self.ui.length_lineEdit.setText(self.ui.length_lineEdit.text().replace(',', '.'))
                self.ui.height_lineEdit.setText(self.ui.height_lineEdit.text().replace(',', '.'))
                try:

                    sql = sqlite_qwer.sql_add_new_garage_size(self.ui.width_lineEdit.text(),
                                                              self.ui.length_lineEdit.text(),
                                                              self.ui.height_lineEdit.text(),
                                                              self.ui.comment_lineEdit.text())
                    self.db.execute(sql)
                except Exception as e:
                    ui.dialogs.onShowError(self, constants.ERROR_SQL_QWERY, str(e))
                    return
                self.mainForm.fillGarageSizeFromBase()
            self.close()
