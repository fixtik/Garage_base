import os
import shutil
import sys
import time

from dataclasses import dataclass

# Для создания ворда
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
from docxcompose.composer import Composer
from docx import Document as Document_compose

# Для генерации qr кода
import qrcode
from qrcode.image.pure import PyPNGImage

import constants
import sqlite_qwer
from ui.qr_bankInfo import Ui_Form
import ui.validators
import ui.css
import ui.dialogs
from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui


class QrBankInfo_frontend(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector

        # переменные класса
        self.css = ui.css  # для красоты
        self.fileNames = []  # для хранения списка названия файлов

        self.initUi()

    def initUi(self):
        """Инициализация интерфейса"""
        self.setFixedWidth(400)

        # todo
        # 1) Проверить еще раз первичное добавление информации

        self.ui.add_pushButton.clicked.connect(self.ok_push_button)
        self.ui.cancel_pushButton.clicked.connect(self.close)
        self.ui.cancel_pushButton_2.clicked.connect(self.generate_qr)

        # валидаторы
        self.ui.PersonalAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.BIC_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.CorrespAcc_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.PayeeINN_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.KPP_lineEdit.setValidator(ui.validators.onlyNumValidator())

        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)
        self.ui.progressBar.setVisible(False)

        self.autofill_PaymentInfo()

    # self.generate_qr()

    def ok_push_button(self):
        if self.db and self.ui.add_pushButton.text() == 'Добавить':
            sql = sqlite_qwer.sql_add_new_payment_details(name=self.ui.Name_lineEdit.text(),
                                                          personal_acc=self.ui.PersonalAcc_lineEdit.text(),
                                                          bank_name=self.ui.BankName_lineEdit.text(),
                                                          bic=self.ui.BIC_lineEdit.text(),
                                                          corresp_acc=self.ui.CorrespAcc_lineEdit.text(),
                                                          payee_inn=self.ui.PayeeINN_lineEdit.text(),
                                                          kpp=self.ui.KPP_lineEdit.text())
            if self.db.execute(sql):
                ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_PAYMENT_INSERT_OK)
                self.close()
                return True
        elif self.db and self.ui.add_pushButton.text() == 'Изменить':
            sql = sqlite_qwer.sql_update_payment_details(name=self.ui.Name_lineEdit.text(),
                                                         personal_acc=self.ui.PersonalAcc_lineEdit.text(),
                                                         bank_name=self.ui.BankName_lineEdit.text(),
                                                         bic=self.ui.BIC_lineEdit.text(),
                                                         corresp_acc=self.ui.CorrespAcc_lineEdit.text(),
                                                         payee_inn=self.ui.PayeeINN_lineEdit.text(),
                                                         kpp=self.ui.KPP_lineEdit.text())
            if self.db.execute(sql):
                ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_PAYMENT_UPDATE_OK)
                self.close()
                return True
        return False

    def autofill_PaymentInfo(self):
        if self.db:
            # self.db.execute(sqlite_qwer.sql_select_first_id_payment_details())
            self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
            info = self.db.cursor.fetchone()
            if info is not None:
                paymentInfo = paymentInformation(*info)
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
        timer = 0
        if self.fileNames:
            self.fileNames = []  # очищаем переменную с названиями файлов чтобы не было дубликатов

        if self.db:
            self.ui.progressBar.setVisible(True)
            self.ui.progressBar.reset()
            self.ui.progressBar.setMinimum(0)

            # Создаем папку для хранения временных файлов
            if not os.path.exists(constants.DEFAULT_TMP_DIR_PASS):
                os.mkdir(constants.DEFAULT_TMP_DIR_PASS)

            # Вытаскиваем максимальный id гаража для максимального значения статус бара
            self.db.execute(sqlite_qwer.sql_select_garage_maxid())
            maxid = self.db.cursor.fetchone()
            self.ui.progressBar.setMaximum(maxid[0])

            # Вытаскиваем инфу по банковским реквизитам
            self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
            info = self.db.cursor.fetchone()
            paymentInfo = paymentInformation(*info)

            # Вытаскиваем инфу по владельцам гаражей
            self.db.execute(sqlite_qwer.sql_select_payment_member_information())
            infos = self.db.cursor.fetchall()

            for info in infos:
                paymentMemberInfo = paymentMemberInformation(*info)
                fio = f'{paymentMemberInfo.surname} {paymentMemberInfo.first_name} {paymentMemberInfo.second_name}'

                for i in range(2):
                    Purpose = f'ПО 31, ряд №{paymentMemberInfo.num_row} гараж №{paymentMemberInfo.num_bild}, за {datetime.now().year}' if i == 0 \
                        else f'ПО 31, ряд №{paymentMemberInfo.num_row} гараж №{paymentMemberInfo.num_bild}, за {datetime.now().year}. Электричество'

                    qr_dir = f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}.png" if i == 0 \
                        else f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}_electric.png"

                    qr = f'ST00011|Name={paymentInfo.Name}|PersonalAcc={paymentInfo.PersonalAcc}|' \
                         f'BankName={paymentInfo.BankName}|BIC={paymentInfo.BIC}|' \
                         f'CorrespAcc={paymentInfo.CorrespAcc}|PayeeINN={paymentInfo.PayeeINN}|' \
                         f'LastName={paymentMemberInfo.surname}|FirstName={paymentMemberInfo.first_name}|' \
                         f'MiddleName={paymentMemberInfo.second_name}|Purpose={Purpose}||Sum='

                    img = qrcode.make(qr, image_factory=PyPNGImage)
                    img.save(qr_dir)

                # Двигаем шкалу загрузки
                self.ui.progressBar.setValue(paymentMemberInfo.id)
                # Создаем документик из шаблона
                self.fill_doc_template(paymentMemberInfo.num_bild, paymentMemberInfo.num_row, fio)

                # Подтираем ненужные фото qr кодов
                for j in range(2):
                    qr_dir = f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}.png" if j == 0 \
                        else f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}_electric.png"
                    os.remove(qr_dir)

                timer += 1
                if timer == 5:
                    break

            self.final_output_document(self.fileNames)
            # Убираем статус бар после окончания работы функции
            self.ui.progressBar.setVisible(False)

    def fill_doc_template(self, num, row, fio):
        doc = DocxTemplate("template.docx")
        qr = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}.png', width=Mm(50), height=Mm(50))
        qr_electric = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}_electric.png', width=Mm(50),
                                  height=Mm(50))
        context = {'qr_photo': qr, 'qr_photo_electric': qr_electric, 'num': num, 'row': row, 'fio': fio}
        doc.render(context)
        doc.save(f"tmp\\Гараж_{row}_{num}.docx")
        self.fileNames.append(f"tmp\\Гараж_{row}_{num}.docx")

    def final_output_document(self, files_list):
        if os.path.exists(f"{constants.DEFAULT_DOCS_DIR_PASS}\\Output.docx"):
            os.remove(f"{constants.DEFAULT_DOCS_DIR_PASS}\\Output.docx")
        number_of_sections = len(files_list)
        master = Document_compose(files_list[0])
        composer = Composer(master)
        for i in range(1, number_of_sections):
            doc_temp = Document_compose(files_list[i])
            composer.append(doc_temp)
        composer.save(f"{constants.DEFAULT_DOCS_DIR_PASS}\\Output.docx")

        # Подчищаем за собой файлы
        for name in files_list:
            if os.path.exists(f'{os.getcwd()}\\{name}'):
                os.remove(f'{os.getcwd()}\\{name}')


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
    num_row: str = ''
    num_bild: str = ''
    surname: str = ''
    first_name: str = ''
    second_name: str = ''
