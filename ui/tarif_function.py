from dataclasses import dataclass
from PySide6 import QtCore, QtWidgets, QtGui

import constants
import sqlite_qwer
from ui.tarif import Ui_Form
import ui.dialogs

class Tarif_frontend(QtWidgets.QWidget):
    def __init__(self, db, main_form: QtWidgets.QWidget, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db                # db-connector
        self.main_form = main_form
        self.initUi()


    def initUi(self):
        self.ui.meterType_comboBox.addItem('220')
        self.ui.meterType_comboBox.addItem('380')
        for _ in range(0, self.ui.meterType_comboBox.count()):
            self.add_meters_tarif(self.ui.meterType_comboBox.itemText(_))
        self.get_current_value_from_bd()

        self.ui.cancel_pushButton.clicked.connect(self.close)
        self.ui.meterType_comboBox.currentTextChanged.connect(self.get_current_value_from_bd)
        self.ui.ok_pushButton.clicked.connect(self.set_current_value_to_bd)


    def add_meters_tarif(self, meter_type: str) -> bool:
        """первоначальное добалвелние записи тарифа для счетчика с проверкой на наличие записи в БД"""
        if self.db:
            if self.db.execute(sqlite_qwer.sql_select_id_by_field_value(table_name=constants.TARIF_TABLE,
                                                                        field_name='type_meter',
                                                                        value=meter_type)):
                if not self.db.cursor.fetchone()[0]:
                    self.db.execute(sqlite_qwer.sql_add_current_tarif(meter_type))
                return True
        return False

    def get_current_value_from_bd(self):
        """получение текущих значений для счетчика"""
        if self.db:
            if self.db.execute(sqlite_qwer.sql_get_current_tarif(self.ui.meterType_comboBox.currentText())):
                cur_tarif = Tarif(*self.db.cursor.fetchone())
                self.ui.day_lineEdit.setText(str(cur_tarif.value_day))
                self.ui.night_lineEdit.setText(str(cur_tarif.value_night))


    def set_current_value_to_bd(self):
        """установка новых значений тарифа"""
        if self.db:

            if self.db.execute(sqlite_qwer.sql_set_current_tarif(self.ui.meterType_comboBox.currentText(),
                            value_day=self.ui.day_lineEdit.text() if self.ui.day_lineEdit.text() else 0,
                            value_night=self.ui.night_lineEdit.text() if self.ui.night_lineEdit.text() else 0)):
                ui.dialogs.onShowOkMessage(self,constants.INFO_TITLE, constants.MESSAGE_UPDATE_DB_OK)
                return
        ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_UPDATE_DB_FAIL)


    def close(self) -> bool:
        self.main_form = None
        super().close()

@dataclass
class Tarif():
    id: str
    type_meter: str
    value_day: str
    value_night:str