import qrcode
from dataclasses import dataclass
from qrcode.image.pure import PyPNGImage

import constants
import sqlite_qwer
from ui.qr_bankInfo import Ui_Form
import ui.validators
import ui.css
import ui.dialogs
from PySide6 import QtCore, QtWidgets, QtGui


class QrBankInfo_frontend(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector

        # переменные класса
        self.css = ui.css  # для красоты

        self.initUi()

    def initUi(self):
        """Инициализация интерфейса"""
        self.setFixedWidth(400)

        # todo
        # 1) Проверить еще раз первичное добавление информации
        # 2) Добавить генерацию qr по гаражам

        self.ui.add_pushButton.clicked.connect(self.ok_push_button)
        self.ui.cancel_pushButton.clicked.connect(self.close)

        # валидаторы
        self.ui.PersonalAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.BIC_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.CorrespAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.PayeeINN_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.KPP_lineEdit.setValidator(ui.validators.onlyNumValidator())

        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)

        self.autofill_PaymentInfo()

    def ok_push_button(self):
        if self.db and self.ui.add_pushButton.text() == 'Добавить':
            sql = sqlite_qwer.sql_add_new_payment_details(Name=self.ui.Name_lineEdit.text(),
                                                          PersonalAcc=self.ui.PersonalAcc_lineEdit.text(),
                                                          BankName=self.ui.BankName_lineEdit.text(),
                                                          BIC=self.ui.BIC_lineEdit.text(),
                                                          CorrespAcc=self.ui.CorrespAcc_lineEdit.text(),
                                                          PayeeINN=self.ui.PayeeINN_lineEdit.text(),
                                                          KPP=self.ui.KPP_lineEdit.text())
            if self.db.execute(sql):
                ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_PAYMENT_INSERT_OK)
                self.close()
                return True
        elif self.db and self.ui.add_pushButton.text() == 'Изменить':
            sql = sqlite_qwer.sql_update_payment_details(Name=self.ui.Name_lineEdit.text(),
                                                         PersonalAcc=self.ui.PersonalAcc_lineEdit.text(),
                                                         BankName=self.ui.BankName_lineEdit.text(),
                                                         BIC=self.ui.BIC_lineEdit.text(),
                                                         CorrespAcc=self.ui.CorrespAcc_lineEdit.text(),
                                                         PayeeINN=self.ui.PayeeINN_lineEdit.text(),
                                                         KPP=self.ui.KPP_lineEdit.text())
            if self.db.execute(sql):
                ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_PAYMENT_UPDATE_OK)
                self.close()
                return True
        return False

    def autofill_PaymentInfo(self):
        if self.db:
            # self.db.execute(sqlite_qwer.sql_select_first_id_paymentdetails())
            self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
            info = self.db.cursor.fetchone()
            if info is not None:
                paymentInfo = paymentInformation(*info)
                print(paymentInfo)
                self.ui.Name_lineEdit.setText(f'{paymentInfo.Name}')
                self.ui.PersonalAcc_lineEdit.setText(f'{paymentInfo.PersonalAcc}')
                self.ui.BankName_lineEdit.setText(f'{paymentInfo.BankName}')
                self.ui.BIC_lineEdit.setText(f'{paymentInfo.BIC}')
                self.ui.CorrespAcc_lineEdit.setText(f'{paymentInfo.CorrespAcc}')
                self.ui.PayeeINN_lineEdit.setText(f'{paymentInfo.PayeeINN}')
                self.ui.KPP_lineEdit.setText(f'{paymentInfo.KPP}')
            else:
                self.ui.add_pushButton.setText('Добавить')

    def generate_qr(self):
        self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
        info = self.db.cursor.fetchone()
        paymentInfo = paymentInformation(*info)
        print(paymentInfo)
        # Name = 'Всеволжская районная организация общественной организации ВОА'
        # PersonalAcc = '40703810655410003535'
        # BankName = 'СЕВЕРО-ЗАПАДНЫЙ БАНК ПАО СБЕРБАНК'
        # BIC = '044030653'
        # CorrespAcc = '30101810500000000653'

        # todo
        # select garage_number, fio, current_year, payment_sum
        # SELECT id,
        # 	num_row,
        # 	num_bild,
        # 	(SELECT surname FROM garage_member WHERE id = owner_id) as surname,
        # 	(SELECT first_name FROM garage_member WHERE id = owner_id) as first_name,
        # 	(SELECT second_name FROM garage_member WHERE id = owner_id) as second_name
        # FROM garage_obj

        # LastName = 'Елизоветенков'
        # FirstName = 'Никита'
        # MiddleName = 'Александрович'
        # # {LastName} {FirstName} {MiddleName},
        # Sum = 10000  # сумма в копейках (рубли * 100)
        # Purpose = f'ПО 31,ряд №гараж, за 2020'
        # PayeeINN = '4703035967'
        # KPP = '470301001'
        #
        # qr = f'ST00011|Name={Name}|PersonalAcc={PersonalAcc}|BankName={BankName}|BIC={BIC}\
        # |CorrespAcc={CorrespAcc}|PayeeINN={PayeeINN}|LastName={LastName}|FirstName={FirstName}|MiddleName\
        # ={MiddleName}|Purpose={Purpose}||Sum={Sum}'
        #
        # img = qrcode.make(qr, image_factory=PyPNGImage)
        # img.save("qr.png")


@dataclass
class paymentInformation:
    id: str = ''
    Name: str = ''
    PersonalAcc: str = ''
    BankName: str = ''
    BIC: str = ''
    CorrespAcc: str = ''
    PayeeINN: str = ''
    KPP: str = ''


@dataclass
class paymentMemberInformation:
    id: str = ''
    num_row: = ''
    # 	num_bild,
    # 	(SELECT surname FROM garage_member WHERE id = owner_id) as surname,
    # 	(SELECT first_name FROM garage_member WHERE id = owner_id) as first_name,
    # 	(SELECT second_name FROM garage_member WHERE id = owner_id) as second_name
