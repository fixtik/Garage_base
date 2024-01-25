import datetime

from PySide6 import QtCore, QtWidgets, QtGui
from dataclasses import dataclass

import constants
import main
import ui.contrib_add as addW
import ui.contrib_addKind as addK
import ui.dialogs
import ui.cart_functions
import ui.cart_functions
import sqlite_qwer
import ui.validators
import ui.members_contrib
import ui.new_garage_size_func
import ui.bilingForm


class AddContrib_front(QtWidgets.QWidget):
    TB_NAME = 'contribution_type'

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = addW.Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # БД
        self.mainForm = None  # Родительская форма
        self.addKind_form = None  # Форма добавления нового вида платежа
        self.contib = None  # объект для передачи данных в другую форму
        self.contib_ids = []  # список с id-платежа из БД, индекс соответствует индексу в combobox
        self.cur_indx = None  # текущий выбранный индекс в combobox
        self.billPhotoPath = None  # путь фотографии чека

        self.initUi()

    def initUi(self):

        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.ok_pushButton.clicked.connect(self.okPushBtnClk)
        self.ui.addKind_pushButton.clicked.connect(self.addKindContrib)
        # self.ui.delKind_pushButton.clicked.connect(self.delKindContrib) убрали сию функцию
        self.ui.kindContrib_comboBox.currentIndexChanged.connect(self.itemChanged)
        self.ui.card_radioButton.clicked.connect(self.setEnabledChooseCheckProto)
        self.ui.cash_radioButton.clicked.connect(self.setEnabledChooseCheckProto)
        self.ui.chooseCheck_pushButton.clicked.connect(self.chooseBillPhoto)

        # Установка текущей даты при создании платежа
        self.ui.payDate_dateEdit.setDate(datetime.date.today())
        self.ui.cash_radioButton.setChecked(True)

        self.setEnabledChooseCheckProto()

        self.ui.sumContrib_lineEdit.setValidator(ui.validators.floatValidator())

    def updateDataFromDB(self):
        """Обновление данных из БД для отображения в полях"""
        self.fillKindContribFromBase()

    def chooseBillPhoto(self):
        """выбор фото чека"""
        img_path = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_PHOTO, constants.FILTER_PHOTO)[0]
        if img_path:
            self.billPhotoPath = img_path
            self.ui.label.setText(img_path)

    def setEnabledChooseCheckProto(self):
        """изменяет доступность кнопки выбора фото чека"""
        self.ui.chooseCheck_pushButton.setEnabled(self.ui.card_radioButton.isChecked())

    def addKindContrib(self):
        """вызов окна для добавления нового вида платежа"""
        self.addKind_form = AddKindContrib_front(self.db)
        self.addKind_form.mainForm = self
        self.addKind_form.show()

    def delKindContrib(self):
        """удаление вида платежа из базы"""
        q = ui.dialogs.onShowСonfirmation(self, "Подтверждение действия",
                                          "Вы уверены, что хотите удалить выбранный тип платежа?")
        if q:
            self.db.execute(sqlite_qwer.sql_delete_rec_by_table_name_and_id(self.TB_NAME,
                                                                            self.contib_ids[
                                                                                self.ui.kindContrib_comboBox.currentIndex()]))
            self.updateDataFromDB()

    def okPushBtnClk(self):
        """действие при нажатии Добавить или Применить"""
        if self.mainForm:  # если добаление платежа в карточку
            if not (self.ui.kindContrib_comboBox.currentText() and self.ui.sumContrib_lineEdit.text()):
                ui.dialogs.onShowError(self, 'Ошибка', 'Вы не заполнили все поля')
                return
            self.contib = Contribution()
            self.contib.value = self.ui.sumContrib_lineEdit.text()
            self.contib.kindPay = self.ui.kindContrib_comboBox.currentText()
            self.contib.typePay = 1 if self.ui.cash_radioButton.isChecked() else 2

            self.contib.payDate = self.ui.payDate_dateEdit.text()
            self.contib.comment = self.ui.commentContrib_lineEdit.text()
            self.contib.checkPath = self.billPhotoPath
            self.mainForm.contribModel.setItems(self.contib)
            if isinstance(self.mainForm, ui.cart_functions.Cart_frontend):
                self.mainForm.set_new_value_acc(self.contib)
            self.close()
            return
        self.db.execute(
            sqlite_qwer.sql_update_contrib_type(self.contib_ids[self.ui.kindContrib_comboBox.currentIndex()],
                                                float(self.ui.sumContrib_lineEdit.text().replace(',', '.')),
                                                self.ui.commentContrib_lineEdit.text()))
        self.updateDataFromDB()

    def fillKindContribFromBase(self):
        """заполнение данных в combobox с видами платежей из БД """
        if self.db:
            self.db.execute(sqlite_qwer.sql_select_all_from_table(self.TB_NAME))
            contrib = self.db.cursor.fetchall()
            self.contib_ids.clear()
            self.ui.kindContrib_comboBox.clear()
            for item in contrib:
                cont = Cotrib_type(*item)
                self.contib_ids.append(cont.id)
                self.ui.kindContrib_comboBox.addItem(cont.name)
            self.itemChanged()

    def itemChanged(self):
        """изменение данных в полях при изменении выбранной позиции"""
        if self.ui.kindContrib_comboBox.currentIndex() == -1:
            return
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(self.TB_NAME,
                                                             self.contib_ids[
                                                                 self.ui.kindContrib_comboBox.currentIndex()]))
        contrib = self.db.cursor.fetchone()

        self.ui.sumContrib_lineEdit.setText(str(contrib[2]))
        self.ui.commentContrib_lineEdit.setText(contrib[3])

    def hideDateField(self, hidden: bool):
        """скрывает или отображает возможность выбора дат на форме"""
        self.ui.payDate_dateEdit.setVisible(hidden)

        self.ui.payDate_label.setVisible(hidden)
        self.resize(self.width(), 150)
        self.setWindowTitle(constants.CONTRIB_WIN_EDIT_TITLE)

    def closeEvent(self, event) -> bool:
        if isinstance(self.mainForm, main.Form_frontend):
            self.mainForm.typePay = None
        self.mainForm = None
        super().closeEvent()


@dataclass
class Contribution():
    """Класс информации о платеже"""
    id: str = ''  # id платежа
    garage_id: str = ''  # id гаража
    kindPay: str = ''  # вид платежа
    payDate: str = ''  # дата платежа
    value: str = ''  # сумма платежа
    comment: str = ''  # комментарий
    typePay: str = ''  # тип оплаты (нал / безнал)
    checkPath: str = ''  # путь к чеку


@dataclass
class Cotrib_type():
    """Класс доступных видах платежа"""
    id: str = ''
    name: str = ''
    value: str = ''
    comment: str = ''


@dataclass
class Contribution_lite():
    """Класс информации о платеже"""
    id: str = ''  # id платежа
    kindPay: str = ''  # вид платежа
    payDate: str = ''  # дата платежа
    value: str = ''  # сумма платежа
    comment: str = ''
    typePay: str = ''
    checkPath: str = ''


@dataclass
class ObjAccount():
    """класс описания текущего состояния счета"""
    id: str = ''  # id записи (для изменения)
    obj_id: str = ''  # id объекта
    debt: str = ''  # текущая задолжность
    calculation: str = ''  # начисления
    balance: str = ''  # баланс


class AddKindContrib_front(QtWidgets.QWidget):
    """Виджет для добавления платежа в бд"""

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
        self.ui.value_lineEdit.setValidator(ui.validators.floatValidator())

    def okPushBtnClk(self):
        """нажатие кнопки ок"""
        if self.mainForm:
            if not (self.ui.kind_lineEdit.text() and self.ui.value_lineEdit.text()):
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
                return
            if self.db.connect:
                self.ui.value_lineEdit.setText(self.ui.value_lineEdit.text().replace(',', '.'))
                if ui.cart_functions.check_rec_in_base(self.db,
                                                       ('name', self.ui.kind_lineEdit.text()),
                                                       tb_name=constants.CONTRIB_TYPE_TABLE):
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_CONTRIB_TYPE_ALREADY_EXIST)
                    return None
                try:

                    sql = sqlite_qwer.sql_add_new_contrib_type(self.ui.kind_lineEdit.text(),
                                                               self.ui.value_lineEdit.text(),
                                                               self.ui.comment_lineEdit.text())
                    self.db.execute(sql)
                except Exception as e:
                    ui.dialogs.onShowError(self, constants.ERROR_SQL_QWERY, str(e))
                    return
                self.mainForm.fillKindContribFromBase()
            self.close()

    def closeEvent(self, event) -> bool:
        self.mainForm = None
        super().closeEvent(event)


class Member_contrib_ui(QtWidgets.QWidget):
    """класс для отображения окна установки членского взноса"""

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = ui.members_contrib.Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # БД
        self.mainForm = None  # Родительская форма
        self.size_ids = []  # Cписок size_id
        self.initUI()

    def initUI(self):
        self.ui.close_pushButton.clicked.connect(self.close)
        self.get_size_from_db()

        self.ui.year_comboBox.setEditable(True)
        self.ui.year_comboBox.setValidator(ui.validators.onlyNumValidator())
        self.setYear()

        self.ui.value_lineEdit.setValidator(ui.validators.floatValidator())

        self.ui.typeSize_comboBox.currentIndexChanged.connect(self.set_value_to_field)
        self.ui.year_comboBox.currentIndexChanged.connect(self.set_value_to_field)
        self.ui.year_comboBox.currentTextChanged.connect(self.set_value_to_field)
        self.ui.add_pushButton.clicked.connect(self.addButton_pressed)
        self.set_value_to_field()

    def setYear(self):
        """Установка диапазона годов"""

        end_year = int(datetime.datetime.now().year)
        start_year = end_year - 3
        for y in range(start_year, end_year + 3):
            self.ui.year_comboBox.addItem(str(y))
        self.ui.year_comboBox.setCurrentText(str(end_year))

    def set_value_to_field(self):
        value = self.get_value_from_db()
        self.ui.value_lineEdit.setText(str(value))

    def get_size_from_db(self):
        """Заполнение комбобокса с размерами и получение их ids"""
        self.size_ids = \
            ui.new_garage_size_func.AddGarageSize_front.fillGarageSizeFromBase(self.db, self.ui.typeSize_comboBox)

    def get_value_from_db(self) -> str:
        """возвращает значение платежа из БД"""
        value = ''
        if not self.checker(False):
            return value
        if self.db:
            sql = sqlite_qwer.sql_get_value_members_contrib(
                size_id=self.size_ids[self.ui.typeSize_comboBox.currentIndex()],
                year=self.ui.year_comboBox.currentText())
            if self.db.execute(sql):
                value = self.db.cursor.fetchone()
        return value[0] if value else ''

    def get_bilingDate_from_db(self) -> str:
        """возвращает дату выставления счета из БД"""
        bilDate = ''
        if not self.checker(False):
            return bilDate
        if self.db:
            sql = sqlite_qwer.sql_get_biling_members_contrib_date(
                size_id=self.size_ids[self.ui.typeSize_comboBox.currentIndex()],
                year=self.ui.year_comboBox.currentText())
            if self.db.execute(sql):
                bilDate = self.db.cursor.fetchone()
        return bilDate if bilDate != '0' else ''

    def checker(self, value_in: bool) -> bool:
        return (self.ui.year_comboBox.currentText() and self.ui.typeSize_comboBox.currentText() and
                self.ui.value_lineEdit.text()) if value_in else \
            (self.ui.year_comboBox.currentText() and self.ui.typeSize_comboBox.currentText())

    def addButton_pressed(self):
        """действие по нажатию кнопки Внести"""
        if not self.checker(True):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.INFO_DATA_IS_EMPTY)
            return False
        value = self.get_value_from_db()
        if value == self.ui.value_lineEdit.text():
            return False
        if value != 0 and value:
            if not (ui.dialogs.onShowСonfirmation(self, constants.INFO_TITLE, constants.QUESTION_UPDATE_MEMBER_CONT)):
                return False
        if self.get_bilingDate_from_db():
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_CONTRIB_TYPE_ALREADY_BILING)
            return False
        if self.db:
            sql = sqlite_qwer.sql_update_value_members_contrib(
                size_id=self.size_ids[self.ui.typeSize_comboBox.currentIndex()],
                value=self.ui.value_lineEdit.text(),
                year=self.ui.year_comboBox.currentText()
            ) if (value != 0 and value) else sqlite_qwer.sql_add_new_members_contrib(
                size_id=self.size_ids[self.ui.typeSize_comboBox.currentIndex()],
                value=self.ui.value_lineEdit.text(),
                year=self.ui.year_comboBox.currentText())
            if self.db.execute(sql):
                ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_UPDATE_DB_OK)
                return True
        return False

    def closeEvent(self, event):
        if isinstance(self.mainForm, main.Form_frontend):
            self.mainForm.memberCont = None
        self.mainForm = None
        super().closeEvent(event)


class Biling_contrib_ui(QtWidgets.QWidget):
    """класс для отображения выставления счета членского взноса"""

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = ui.bilingForm.Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # БД
        self.mainForm = None

        # todo 1) запрос в БД на выгрузку "годов"
        #      2) запрос в БД на выгрузку "размеров" и размеров платежей
        #      3) модель представления tableview для отображения "размер гаража - сумма членского взноса"
        #      4) проверка ранее выставленных платежей (мало ли нет выставления какому-то из размеров, а остальным есть)
        #      5) проверка и запрет на повторное выставление платежей
