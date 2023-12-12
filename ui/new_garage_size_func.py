from dataclasses import dataclass

from PySide6 import QtCore, QtWidgets, QtGui

import constants
import db_work
import ui.new_garage_size as addWid

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
        self.ui.change_pushButton.clicked.connect(self.okPushBtnClk)
        self.ui.delSize_pushButton.clicked.connect(self. delGarageSize)


        # валидаторы
        self.ui.width_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.length_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.height_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.contrib_lineEdit.setValidator(ui.validators.floatValidator())
        # заголовки
        self.setWindowTitle(constants.WINDOW_TITLE_ADD_SIZE)

        self.updateDataFromDB()
        self.ui.size_comboBox.currentIndexChanged.connect(self.itemChanged)


    @staticmethod
    def fillGarageSizeFromBase(db: db_work.Garage_DB, comboBox: QtWidgets.QComboBox) -> list:
        """
        заполнение данных в комбобокс из базы
        :param db: ссылка на БД
        :param comboBox: комбобокс - приемник
        :return список с id размеров
        """
        garage_ids = []
        if db:
            db.execute(sqlite_qwer.sql_select_all_from_table(AddGarageSize_front.TB_NAME))
            size = db.cursor.fetchall()
            garage_ids.clear()
            comboBox.clear()
            for item in size:
                cont = GarageSizeStructure(*item)

                garage_ids.append(cont.id)
                cont.comment = f'({cont.comment})' if cont.comment else ''
                # cont.width = format(item[1]).rstrip('0').rstrip('.')
                # cont.len = format(item[2]).rstrip('0').rstrip('.')
                # cont.height = format(item[3]).rstrip('0').rstrip('.')
                # cont.comment = f'({item[4]})' if item[4] else ''
                comboBox.addItem(f'{cont.width} x {cont.len} x {cont.height} {cont.comment}')

        return garage_ids


    def itemChanged(self):
        """изменение данных в полях при изменении выбранной позиции"""
        if not self.garage_ids:
            return
        if self.ui.size_comboBox.currentIndex() == -1 or self.ui.ok_pushButton.text() == constants.BTN_TEXT_ADD:
            return

        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(self.TB_NAME,
                                                             self.garage_ids[self.ui.size_comboBox.currentIndex()]))
        g = GarageSizeStructure(*self.db.cursor.fetchone())
        self.ui.width_lineEdit.setText(str(g.width))
        self.ui.length_lineEdit.setText(str(g.len))
        self.ui.height_lineEdit.setText(str(g.height))
        self.ui.comment_lineEdit.setText(g.comment)
        self.ui.contrib_lineEdit.setText(str(g.contrib))

    def updateDataFromDB(self):
        """Обновление данных из БД для отображения в полях"""
        self.garage_ids = self.fillGarageSizeFromBase(self.db, self.ui.size_comboBox)[:]
        self.itemChanged()
        # кнопка Изменить доступна только тогда, когда есть хоть одна запись в комбобоксе
        self.ui.change_pushButton.setEnabled(self.ui.size_comboBox.count())

    def delGarageSize(self):
        """удаление размеров гаража из базы"""
        if not self.ui.size_comboBox.itemText(self.ui.size_comboBox.currentIndex()):
            return
        q = ui.dialogs.onShowСonfirmation(self, constants.ATTANTION_ACCEPT, constants.QUESTION_DELETE_TYPE_SIZE)
        if q:
            self.db.execute(sqlite_qwer.sql_delete_rec_by_table_name_and_id(self.TB_NAME,
                                                                            self.garage_ids[self.ui.size_comboBox.currentIndex()]))
            self.updateDataFromDB()

    def okPushBtnClk(self):
        """действие при нажатии Добавить или Применить"""
        if self.mainForm:
            if not (self.ui.width_lineEdit.text() and self.ui.length_lineEdit.text() and self.ui.height_lineEdit.text()):
                ui.dialogs.onShowError(self, 'Ошибка', 'Вы не заполнили все поля')
                return
            self.garage = GarageSizeStructure()
            self.garage.width = self.ui.width_lineEdit.text().replace(',', '.')
            self.garage.len = self.ui.length_lineEdit.text().replace(',', '.')
            self.garage.height = self.ui.height_lineEdit.text().replace(',', '.')
            self.garage.contrib = self.ui.contrib_lineEdit.text().replace(',', '.')
            self.garage.comment = self.ui.comment_lineEdit.text()

            if self.sender() == self.ui.ok_pushButton:
                if ui.cart_functions.check_rec_in_base(self.db,
                                                       ('width', float(self.garage.width)),
                                                       ('len', float(self.garage.len)),
                                                       ('height', float(self.garage.height)),
                                                       tb_name=constants.SIZE_TABLE):
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_SIZE_ALREADY_EXIST)
                    return None
                # добавляем новый размер
                sql = sqlite_qwer.sql_add_new_garage_size(float(self.garage.width),
                                                          float(self.garage.len),
                                                          float(self.garage.height),
                                                          float(self.garage.contrib),
                                                          self.garage.comment)

            else:
                # изменяем выбранный
                sql = sqlite_qwer.sql_update_garage_size(self.garage_ids[self.ui.size_comboBox.currentIndex()],
                                                         float(self.garage.width),
                                                         float(self.garage.len),
                                                         float(self.garage.height),
                                                         float(self.garage.contrib),
                                                         self.garage.comment)
            self.db.execute(sql)
            self.updateDataFromDB()

    def close(self) -> bool:
        if isinstance(self.mainForm, ui.cart_functions.Cart_frontend):
            self.mainForm.updateDataFromDB()

        self.mainForm = None
        super().close()



@dataclass
class GarageSizeStructure():
    """Класс информации о размерах гаража"""

    id: str = ''             # id записи
    width: str = ''       # ширина гаража
    len: str = ''       # длина гаража
    height: str = ''     # высота гаража
    comment: str = ''   # комментарий
    contrib: str = ''  # размер платы за год