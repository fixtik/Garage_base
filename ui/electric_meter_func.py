from PySide6 import QtCore, QtWidgets, QtGui

import db_work
from ui.electric_meter import Ui_Form
import sqlite_qwer
import ui.dialogs
import constants
import ui.validators


class Electric_front(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = db                # db-connector
        self.meter = None
        self.obj_id = None          # id объекта

        self.initUi()

    def initUi(self):
        # слоты
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.find_pushButton.clicked.connect(self.searchObj)
        self.ui.add_pushButton.clicked.connect(self.addPushBtnClk)
        # установка валидаторов
        self.ui.row_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.garajeNum_lineEdit.setValidator(ui.validators.onlyNumValidator())


    def searchObj(self):
        """Поиск счетчика по номеру объекта"""
        if not(self.ui.garajeNum_lineEdit.text() and self.ui.row_lineEdit.text()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
            return
        if self.db:
            if self.db.execute(sqlite_qwer.sql_select_garaje_id_by_num_and_row(
                garage_num = int(self.ui.garajeNum_lineEdit.text()),
                row = int(self.ui.row_lineEdit.text())
                )):
                id = self.db.cursor.fetchone()
                if id:
                    if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(constants.TABALE_NAMES[5], id=id[0])):
                        record = self.db.cursor.fetchone()[0]
                        if record:
                            meter = ElectricMeter()
                            meter.id = record[0]
                            meter.num_meter = record[1]
                            meter.type = record[2]
                            meter.prev_day = record[3]
                            meter.prev_night = record[4]
                            meter.day = record[5]
                            meter.night = record[6]
                            self.meter = meter
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
        if not self.db:
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_BASE_CONNECT)
            return

        if not self.fillElectricMeterObj():
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)
            return

        if not self.obj_id:
            # если объект не указан спрашиваем о добавлении без привязки
            if not(ui.dialogs.onShowСonfirmation(self, constants.ATTANTION_TITLE,
                                                 constants.QUESTION_WRITE_EL_METER_WHITHOUT_OBJ)):
                return
        if self.db.execute(sqlite_qwer.sql_add_electric_meter(
            num_meter=self.meter.num_meter,
            cur_day=self.meter.day,
            cur_night=self.meter.night,
            pr_day=self.meter.prev_day,
            pr_night=self.meter.prev_night)):
            self.meter.id = self.db.cursor.lastrowid
        if self.meter.id and self.obj_id:
            field = 'electro220_id' if self.meter.type == '220' else 'electro380_id'
            if self.db.execute(sqlite_qwer.sql_update_field_by_table_name_and_id(
                table_name=constants.TABALE_NAMES[1],
                rec_id=self.obj_id,
                field=field,
                new_value=self.meter.id)):
                print('success')                # TODO добавить уведомление о прекрасном завершении операции





    def fillElectricMeterObj(self) -> bool:
        """заполнение данных из формы"""
        meter = ElectricMeter()
        meter.num_meter = self.ui.meterNum_lineEdit.text()
        if not meter.num_meter:
            return False
        meter.type = self.ui.meterType_comboBox.itemText(self.ui.meterType_comboBox.currentIndex())
        meter.prev_day = self.ui.curDay_lineEdit.text() if self.ui.curDay_lineEdit.text() else 0
        meter.prev_night = self.ui.curNight_lineEdit.text() if self.ui.curNight_lineEdit.text() else 0
        meter.day = self.ui.newDay_lineEdit.text() if self.ui.newDay_lineEdit.text() else 0
        meter.night = self.ui.newNight_lineEdit.text() if self.ui.newNight_lineEdit.text() else 0
        self.meter = meter
        return True

class ElectricMeter():
    def __init__(self):
        self.id = None
        self.num_meter = None
        self.type = None
        self.prev_day = None
        self.prev_night = None
        self.day = None
        self.night = None




