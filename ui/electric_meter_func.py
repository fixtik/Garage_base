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
        self.ui.meterNum_lineEdit.editingFinished.connect(self.getIdFromBase)
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

    def fillFormPlace(self):
        """Заполнение данных"""
        if self.meter:
            self.ui.meterNum_lineEdit.setText(self.meter.num_meter)
            if self.meter.type == 220:
                self.ui.meterType_comboBox.setCurrentIndex(0)
            else:
                self.ui.meterType_comboBox.setCurrentIndex(1)
            self.ui.curDay_lineEdit.setText(self.meter.prev_day)
            self.ui.curNight_lineEdit.setText(self.meter.prev_night)
            self.ui.newDay_lineEdit.setText(self.meter.day)
            self.ui.newNight_lineEdit.setText(self.meter.night)

        else:
            ui.dialogs.onShowError(self, constants.INFO_TITLE, constants.INFO_NO_ELECTRIC_METER)

    def addPushBtnClk(self):
        """Действия при нажатии кнопки "Добавить" """
        self.meter.number = self.ui.meterNum_lineEdit.text()
        self.meter.type = self.ui.meterType_comboBox.currentText()
        self.meter.prev_day = self.ui.curDay_lineEdit.text()
        self.meter.prev_night = self.ui.curNight_lineEdit.text()
        self.meter.curDay = self.ui.newDay_lineEdit.text()
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

        if self.ui.add_pushButton.text() == constants.BTN_TEXT_ADD:
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

        # это нужно отсюда перенести в более подходящее место
        # if self.meter.id and self.obj_id and self.ui.del_pushButton.isVisible():
        #     field = 'electro220_id' if self.meter.type == '220' else 'electro380_id'
        #     if self.db.execute(sqlite_qwer.sql_update_field_by_table_name_and_id(
        #         table_name=constants.TABALE_NAMES[1],
        #         rec_id=self.obj_id,
        #         field=field,
        #         new_value=self.meter.id)):
        #         print('success')                # TODO добавить уведомление о прекрасном завершении операции

        self.close()


    def changeFormElectric(self, elmeter_id: str):
        """подготовка формы к режиму редактирования данных пользователя"""
        self.setWindowTitle(constants.TITLE_EDIT_MODE)
        self.ui.add_pushButton.setText(constants.BTN_TEXT_CHANGE)
        self.meter.id = elmeter_id
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(table_name=self.TABLE_NAME, id=int(self.meter.id)))
        rec = self.db.cursor.fetchone()
        self.meter = ElectricMeter(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
        self.meter.inBase = True
        self.fillPlace()

    def getIdFromBase(self):
        """поиск счетчика по номеру, если есть в БД - заполняются данные"""
        if self.db.execute(sqlite_qwer.sql_get_metr_id_by_num(self.ui.meterNum_lineEdit.text(),
                                                              self.ui.meterType_comboBox.itemText(
                                                              self.ui.meterType_comboBox.currentIndex()))) \
                and self.db.cursor:
            id = self.db.cursor.fetchone()
            print(id)
            if not id:
                self.meter = None
                return None
            if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(table_name=self.TABLE_NAME, id=id[0])):
                rec = self.db.cursor.fetchone()
                self.meter = ElectricMeter(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
                self.meter.inBase = True
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

    def BlockBoxAndReadings(self):
        """Блокируем комбобокс и текущие показания счетчиков"""
        self.ui.curDay_lineEdit.setReadOnly(True)
        self.ui.curNight_lineEdit.setReadOnly(True)
        self.ui.meterType_comboBox.setItemText(0, str(self.meter.type))
        self.ui.meterType_comboBox.setEnabled(False)
        self.setWindowTitle(constants.TITLE_EDIT_MODE)

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
        if isinstance(self.mainForm, ui.cart_functions.Cart_frontend):
            if self.meter and self.sender() != self.ui.close_pushButton:
                self.mainForm.elMeterModel.resetData()
                if self.mainForm.elMeterModel.returnItems():
                    self.mainForm.elMeterModel.setItems(self.mainForm.elMeterModel.returnItems())
                    print(self.mainForm.elMeterModel.returnItems())
                self.mainForm.elMeterModel.setItems(self.meter)
            super().close()
            self.mainForm.destroyChildren()
        else:
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
