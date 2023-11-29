import weakref
from dataclasses import dataclass

from PySide6 import QtCore, QtWidgets, QtGui

import db_work
from ui.electric_meter import Ui_Form
import sqlite_qwer
import ui.dialogs
import constants
import ui.validators
import ui.cart_functions
from ui.tableView_Models import *


class Electric_front(QtWidgets.QWidget):
    TABLE_NAME = "electric_meter"

    def __init__(self, db, mainForm: QtWidgets.QWidget = None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # db-connector
        self.meter = ElectricMeter()
        self.obj_id = None  # id объекта
        self.mainForm = mainForm  # ссылка на главную форму

        self.initUi()

    def initUi(self):
        # слоты
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.find_pushButton.clicked.connect(self.searchObj)
        self.ui.add_pushButton.clicked.connect(self.addPushBtnClk)
        self.ui.del_pushButton.clicked.connect(self.chooseMeter)
        self.ui.meterNum_lineEdit.editingFinished.connect(self.getIdFromBase)
        self.ui.meterType_comboBox.currentIndexChanged.connect(self.getIdFromBase)
        # установка валидаторов
        self.ui.row_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.garajeNum_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.curDay_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.newDay_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.newNight_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.curNight_lineEdit.setValidator(ui.validators.onlyNumValidator())

    def searchObj(self):
        """Поиск счетчика по номеру объекта"""
        if not (self.ui.garajeNum_lineEdit.text() and self.ui.row_lineEdit.text()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
            return
        if self.db:
            if self.db.execute(sqlite_qwer.sql_select_garaje_id_by_num_and_row(
                    garage_num=int(self.ui.garajeNum_lineEdit.text()),
                    row=int(self.ui.row_lineEdit.text())
            )):
                id = self.db.cursor.fetchone()
                if id:
                    if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(self.TABLE_NAME, id=id[0])):
                        record = self.db.cursor.fetchone()[0]
                        if record:
                            self.meter = ElectricMeter(record[0], record[1], record[2], record[3],
                                                       record[4], record[5], record[6])

                    self.fillFormPlace()
                else:
                    ui.dialogs.onShowError(self, constants.INFO_TITLE, constants.INFO_NO_OBJECT)

    def disable_current_lineEdit(self, flag: bool):
        """Открывает или закрывает возможность установки первоначальных значений"""
        self.ui.curDay_lineEdit.setEnabled(flag)
        self.ui.curNight_lineEdit.setEnabled(flag)
        self.ui.meterNum_lineEdit.setEnabled(flag)
        self.ui.del_pushButton.setVisible(not flag)
        if flag:
            self.ui.add_pushButton.setText(constants.BTN_TEXT_ADD)
        else:
            self.ui.add_pushButton.setText(constants.BTN_TEXT_CHANGE)
            self.ui.del_pushButton.setText(constants.BTN_TEXT_CHOOSE)
            # self.setWindowTitle(constants.TITLE_EDIT_MODE)

    def fillFormPlace(self):
        """Заполнение данных"""
        if self.meter:
            self.ui.meterNum_lineEdit.setText(self.meter.number)
            self.ui.meterType_comboBox.setItemText(0, str(self.meter.type))
            self.ui.curDay_lineEdit.setText(self.meter.prev_day)
            self.ui.curNight_lineEdit.setText(self.meter.prev_night)
            self.ui.newDay_lineEdit.setText(self.meter.curDay)
            self.ui.newNight_lineEdit.setText(self.meter.curNight)

        else:
            ui.dialogs.onShowError(self, constants.INFO_TITLE, constants.INFO_NO_ELECTRIC_METER)

    def addPushBtnClk(self):
        """Действия при нажатии кнопки "Добавить" """
        if not self.ui.meterNum_lineEdit.text():
            return
        if not self.meter:
            self.meter = ElectricMeter()
        self.meter.number = self.ui.meterNum_lineEdit.text()
        self.meter.type = self.ui.meterType_comboBox.currentText()
        self.meter.prev_day = self.ui.curDay_lineEdit.text()
        self.meter.prev_night = self.ui.curNight_lineEdit.text()
        if int(self.ui.curDay_lineEdit.text()) > int(self.ui.newDay_lineEdit.text()):
            self.meter.curDay = self.ui.curDay_lineEdit.text()
        else:
            self.meter.curDay = self.ui.newDay_lineEdit.text()

        if int(self.ui.curNight_lineEdit.text()) > int(self.ui.newNight_lineEdit.text()):
            self.meter.curNight = self.ui.curNight_lineEdit.text()
        else:
            self.meter.curNight = self.ui.newNight_lineEdit.text()

        if not self.db:
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_BASE_CONNECT)
            return

        if not self.obj_id and self.ui.del_pushButton.isVisible():
            # если объект не указан спрашиваем о добавлении без привязки
            if not (ui.dialogs.onShowСonfirmation(self, constants.ATTANTION_TITLE,
                                                  constants.QUESTION_WRITE_EL_METER_WHITHOUT_OBJ)):
                return

            # если счетчика в БД нет ->
        if not self.meter and not (self.fillElectricMeterObj() and self.setDefaultValue()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
            return

        if not self.meter.id:
            if not self.meter.inBase:
                self.db.execute(sqlite_qwer.sql_add_electric_meter(
                    num_meter=self.meter.number,
                    cur_day=int(self.meter.curDay),
                    cur_night=int(self.meter.curNight),
                    pr_day=int(self.meter.prev_day),
                    pr_night=int(self.meter.prev_night),
                    type=int(self.meter.type)))
                self.meter.id = self.db.cursor.lastrowid
        else:
            self.db.execute(sqlite_qwer.sql_update_electric_meter_by_id(
                metr_id=int(self.meter.id),
                cur_day=int(self.meter.curDay),
                cur_night=int(self.meter.curNight)))
            ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.INFO_SUCCESS_CHANGED)
        self.close()

    def chooseMeter(self):
        """работа кнопки удалить или выбрать"""
        if self.ui.del_pushButton.text() == constants.BTN_TEXT_CHOOSE:
            self.close()

    def changeFormElectric(self, elmeter_id: str):
        """подготовка формы к режиму редактирования данных пользователя"""
        self.setWindowTitle(constants.TITLE_EDIT_MODE)
        self.ui.add_pushButton.setText(constants.BTN_TEXT_CHANGE)
        self.ui.meterType_comboBox.setEnabled(False)
        self.meter.id = elmeter_id
        self.disable_current_lineEdit(False)
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(table_name=self.TABLE_NAME, id=int(self.meter.id)))
        rec = self.db.cursor.fetchone()
        self.fill_from_db(rec)

        self.fillPlace()

    def fill_from_db(self, rec: list):
        """заполнение данных по счетчику из БД"""
        self.meter = ElectricMeter(*rec)
        self.meter.inBase = True
        self.ui.meterType_comboBox.setItemText(0, str(self.meter.type))

    def getIdFromBase(self):
        """поиск счетчика по номеру, если есть в БД - заполняются данные"""
        if self.db.execute(sqlite_qwer.sql_get_metr_id_by_num(self.ui.meterNum_lineEdit.text(),
                                                              self.ui.meterType_comboBox.itemText(
                                                                  self.ui.meterType_comboBox.currentIndex()))) \
                and self.db.cursor:
            id = self.db.cursor.fetchone()
            if not id:
                self.meter = None
                self.disable_current_lineEdit(True)
                self.setDefaultValue()
                return None
            if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(table_name=self.TABLE_NAME, id=id[0])):
                rec = self.db.cursor.fetchone()
                self.fill_from_db(rec)
                self.meter.inBase = True

                self.disable_current_lineEdit(False)
                self.fillPlace()

    def fillPlace(self):
        """заполнение полей карточки если счетчик найден в БД"""
        self.ui.meterNum_lineEdit.setText(str(self.meter.number))
        self.ui.curDay_lineEdit.setText(str(self.meter.curDay))
        self.ui.curNight_lineEdit.setText(str(self.meter.curNight))
        # здесь пишем одинаковые значения, так как нет логики - зачем выводить предыдущие значения при внесении новых
        self.ui.newDay_lineEdit.setText(str(self.meter.curDay))
        self.ui.newNight_lineEdit.setText(str(self.meter.curNight))

    def fillElectricMeterObj(self) -> bool:
        """заполнение данных из формы"""
        self.meter = ElectricMeter()
        self.meter.number = self.ui.meterNum_lineEdit.text()
        if not self.meter.number:
            return False
        self.meter.type = self.ui.meterType_comboBox.itemText(self.ui.meterType_comboBox.currentIndex())
        self.meter.prev_day = self.ui.curDay_lineEdit.text() if self.ui.curDay_lineEdit.text() else 0
        self.meter.prev_night = self.ui.curNight_lineEdit.text() if self.ui.curNight_lineEdit.text() else 0
        self.meter.curDay = self.ui.newDay_lineEdit.text() if self.ui.newDay_lineEdit.text() else 0
        self.meter.curNight = self.ui.newNight_lineEdit.text() if self.ui.newNight_lineEdit.text() else 0

        return True

    def hideFindePlace(self, visible: bool = False):
        """Скрывает или показывает формы для поиска счетчика"""
        self.ui.row_lineEdit.setVisible(visible)
        self.ui.row_label.setVisible(visible)
        self.ui.garajeNum_lineEdit.setVisible(visible)
        self.ui.garajeNum_label.setVisible(visible)
        self.ui.find_pushButton.setVisible(visible)
        self.ui.del_pushButton.setVisible(visible)
        if not visible:
            self.setFixedHeight(constants.ELECTRIC_HEIGHT_ADD)
            self.setWindowTitle(constants.TITLE_ADD_NEW)

    def setDefaultValue(self) -> bool:
        """Установка значений по умолчанию, если пользователь поленился ввести данные"""
        if not self.ui.curDay_lineEdit.text():
            self.ui.curDay_lineEdit.setText(constants.DEFAULT_VALUE)
        if not self.ui.curNight_lineEdit.text():
            self.ui.curNight_lineEdit.setText(constants.DEFAULT_VALUE)
        if not self.ui.newNight_lineEdit.text():
            self.ui.newNight_lineEdit.setText(constants.DEFAULT_VALUE)
        if not self.ui.newDay_lineEdit.text():
            self.ui.newDay_lineEdit.setText(constants.DEFAULT_VALUE)
        return int(self.ui.newDay_lineEdit.text()) >= int(self.ui.curDay_lineEdit.text()) and \
            int(self.ui.newNight_lineEdit.text()) >= int(self.ui.curNight_lineEdit.text())

    def close(self) -> bool:
        dublicate = False
        if isinstance(self.mainForm, ui.cart_functions.Cart_frontend):
            if self.meter and self.sender() != self.ui.close_pushButton:
                # проверка по счетчику - не используется ли он на других объектах
                if ui.cart_functions.check_rec_in_base(self.db, ('electro220_id', self.meter.id),
                                                       tb_name=constants.OBJ_TABLE) or \
                        ui.cart_functions.check_rec_in_base(self.db, ('electro380_id', self.meter.id),
                                                            tb_name=constants.OBJ_TABLE):
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_METER_ALREADY_USE)
                    return
                # проверка по уже введенным данным - не добавлен ли счетчик в таблицу
                if (self.sender() == self.ui.del_pushButton and \
                    self.ui.del_pushButton.text() == constants.BTN_TEXT_CHOOSE) or \
                        (self.sender() == self.ui.add_pushButton and \
                         self.ui.add_pushButton.text() == constants.BTN_TEXT_ADD):
                    for item in self.mainForm.elMeterModel.items:
                        if item.id == self.meter.id:
                            dublicate = True
                            break
                    if not dublicate:
                        self.mainForm.elMeterModel.setItems(self.meter)

                else:
                    # обновление данных после редактирования
                    for index, item in enumerate(self.mainForm.ui.electric_tableView.model().items):
                        if item.id == self.meter.id:
                            self.mainForm.ui.electric_tableView.model().items[index] = self.meter
                            self.mainForm.ui.electric_tableView.setModel(self.mainForm.carModel)
                            self.mainForm.ui.electric_tableView.setModel(self.mainForm.elMeterModel)
                            break
        #
        self.mainForm.addElectric = None
        self.mainForm = None
        super().close()


@dataclass
class ElectricMeter():
    id: str = ''
    number: str = ''
    type: str = ''
    prev_day: str = ''
    prev_night: str = ''
    curDay: str = ''
    curNight: str = ''
    inBase: bool = False
