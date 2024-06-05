import os
import shutil
import sys

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
import ui.statusbar
from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui


class QrBankInfo_frontend(QtWidgets.QWidget):
    def __init__(self, db, status_window, parent=None):
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
        # 1) Перенести кнопку создания файле в главное окно и сделать неюзабельной при отсутствии информации

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
        self.ui.progressBar.setVisible(False)

        self.autofill_PaymentInfo()

    def ok_push_button(self):
        """Отработка кнопки Добавить/Изменить"""
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
        """Автоматическое заполнение платежных данных"""
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


class QR_StatusBar(QtWidgets.QWidget):
    def __init__(self, parent=None, db=None):
        super().__init__(parent)
        self.ui = ui.statusbar.Ui_Form()
        self.ui.setupUi(self)
        # переменные класса
        self.css = ui.css  # для красоты
        self.db = db
        self.qr_thread = TQR_Thread()  # поток с генерацией qr-кода
        self.no_error = None  # для отлова ошибок в потоке

        self.initUi()
        self.initTread()  # инициализация потока

    def initUi(self):
        """Инициализация интерфейса"""
        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)

        # progressBar
        self.ui.progressBar.reset()
        self.ui.progressBar.setMinimum(0)
        try:
            self.db.execute(sqlite_qwer.sql_select_garage_maxid())
            maxid = self.db.cursor.fetchone()
            self.ui.progressBar.setMaximum(maxid[0] + 1)

        except Exception as e:
            ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=constants.ERROR_NO_BASE_CONNECT)
            return None

    def initTread(self):
        """Инициализация потока"""
        self.qr_thread.db = self.db
        self.qr_thread.statusSignal.connect(self.showProcessInStatusBar)
        self.qr_thread.infoSignal.connect(self.show_info)
        self.qr_thread.finished.connect(self.finishHim)
        self.qr_thread.errorSignal.connect(self.result)

    def showProcessInStatusBar(self, stat: int):
        """
        Отображение текущего положения дел в потоке
        :param stat: процесс из потока
        """
        self.ui.progressBar.reset()
        self.ui.progressBar.setValue(stat)

    def start(self):
        self.ui.progressBar.setVisible(True)
        self.ui.label.setVisible(True)
        self.qr_thread.start()  # запуск потока

    def result(self, msg: bool):
        """Отлов ошибок из потока"""
        self.no_error = msg

    def show_info(self, msg: str):
        self.ui.label.setText(msg)

    def finishHim(self):
        if self.no_error:
            self.ui.progressBar.setVisible(False)
            self.ui.label.setText(constants.INFO_QR_GENERATION_OK)
            if ui.dialogs.onShowСonfirmation(self, title=constants.INFO_TITLE, msg=f'{constants.INFO_QR_GENERATION_OK}'
                                                                                   f'\n{constants.INFO_OPEN_FILE}'):
                try:
                    os.startfile(f"{constants.DEFAULT_DOCS_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}")
                except Exception as e:
                    ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=e)

            self.close()

        else:
            ui.dialogs.onShowOkMessage(self, title=constants.ERROR_TITLE, msg=constants.ERROR_QR_GENERATION)
            self.close()


class TQR_Thread(QtCore.QThread):
    """
    поток поиска файлов с рекурсией
    """
    infoSignal = QtCore.Signal(str)
    statusSignal = QtCore.Signal(int)
    errorSignal = QtCore.Signal(bool)

    def __init__(self, parent=None, db=None):
        super().__init__(parent)
        self.flag = None  # для возможности остановки процесса
        self.db = db  # ссылка на БД

        self.fileNames = []  # для хранения списка названия файлов
        self.statusbar = None  # для отображения окна со статусбаром
        self.value = 0  # стартовое значение для статусбара

    def run(self) -> None:
        if self.flag is None:
            self.flag = True
        self.generate_qr()

    def generate_qr(self):
        """Да что за гений писал эту функцию которая генерирует QR коды"""
        timer = 0
        if self.fileNames:
            self.fileNames = []  # очищаем переменную с названиями файлов чтобы не было дубликатов

        if self.db:
            # Создаем папку для хранения временных файлов
            if not os.path.exists(constants.DEFAULT_TMP_DIR_PASS):
                os.mkdir(constants.DEFAULT_TMP_DIR_PASS)

            self.infoSignal.emit('Генерация QR кодов\nПроцесс может занимать до 5 минут')

            # Вытаскиваем инфу по банковским реквизитам
            try:
                self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
                info = self.db.cursor.fetchone()
                paymentInfo = paymentInformation(*info)
            except Exception as e:
                ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=constants.ERROR_QR_GENERATION)
                self.flag = False
                print(e)

            # Вытаскиваем инфу по владельцам гаражей
            try:
                self.db.execute(sqlite_qwer.sql_select_payment_member_information())
                infos = self.db.cursor.fetchall()
            except Exception as e:
                ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=constants.ERROR_QR_GENERATION)
                self.flag = False
                print(e)

            if not self.flag:
                return None
            # обработка данных
            for info in infos:
                if not self.flag:
                    return None
                paymentMemberInfo = paymentMemberInformation(*info)

                fio = f'{paymentMemberInfo.surname} {paymentMemberInfo.first_name} {paymentMemberInfo.second_name}'

                for i in range(2):
                    purpose = f'ПО 31, ряд №{paymentMemberInfo.num_row} гараж №{paymentMemberInfo.num_bild}, задолженность по членскому взносу на {datetime.now().year}' if i == 0 \
                        else f'ПО 31, ряд №{paymentMemberInfo.num_row} гараж №{paymentMemberInfo.num_bild}, {datetime.now().year}. Компенсация электроэнергии'

                    qr_dir = f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}.png" if i == 0 \
                        else f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}_electric.png"

                    qr = f'ST00011|Name={paymentInfo.Name}|PersonalAcc={paymentInfo.PersonalAcc}|' \
                         f'BankName={paymentInfo.BankName}|BIC={paymentInfo.BIC}|' \
                         f'CorrespAcc={paymentInfo.CorrespAcc}|PayeeINN={paymentInfo.PayeeINN}|' \
                         f'LastName={paymentMemberInfo.surname}|FirstName={paymentMemberInfo.first_name}|' \
                         f'MiddleName={paymentMemberInfo.second_name}|Purpose={purpose}||Sum='

                    img = qrcode.make(qr, image_factory=PyPNGImage)
                    img.save(qr_dir)

                # Двигаем шкалу загрузки
                self.value = paymentMemberInfo.id
                self.statusSignal.emit(paymentMemberInfo.id)

                # Создаем документик из шаблона
                try:
                    self.fill_doc_template(paymentMemberInfo.num_bild, paymentMemberInfo.num_row, fio)
                except Exception as e:
                    print(e)
                    self.errorSignal.emit(False)

                # Подтираем ненужные фото qr кодов
                for j in range(2):
                    qr_dir = f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}.png" if j == 0 \
                        else f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}_electric.png"
                    os.remove(qr_dir)

                timer += 1
                if timer == 50:
                    break
            try:
                self.final_output_document(self.fileNames)
            except Exception as e:
                print(e)
                self.errorSignal.emit(False)
            self.value += 1
            self.statusSignal.emit(self.value)

            # Если предложить выбрать открыть или нет, то прога крашится(
            # if ui.dialogs.onShowСonfirmation(self, constants.INFO_TITLE, constants.INFO_OPEN_FILE):
            #     os.startfile(f"{constants.DEFAULT_DOCS_DIR_PASS}\\QR_для оплаты.docx")
            # os.startfile(f"{constants.DEFAULT_DOCS_DIR_PASS}\\QR_для оплаты.docx")

    def fill_doc_template(self, num, row, fio):
        """Заполняем шаблон с QR кодами"""
        doc = DocxTemplate("template.docx")
        qr = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}.png', width=Mm(50), height=Mm(50))
        qr_electric = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}_electric.png', width=Mm(50),
                                  height=Mm(50))
        context = {'qr_photo': qr, 'qr_photo_electric': qr_electric, 'num': num, 'row': row, 'fio': fio}
        doc.render(context)
        doc.save(f"tmp\\Гараж_{row}_{num}.docx")
        self.fileNames.append(f"tmp\\Гараж_{row}_{num}.docx")

    def final_output_document(self, files_list):
        """Создаем итоговый файл с QR кодами"""
        self.infoSignal.emit('Создаем итоговый файл\nОсталось совсем чуть-чуть')

        if os.path.exists(f"{constants.DEFAULT_DOCS_DIR_PASS}\\QR_для оплаты.docx"):
            os.remove(f"{constants.DEFAULT_DOCS_DIR_PASS}\\QR_для оплаты.docx")
        number_of_sections = len(files_list)

        master = Document_compose(files_list[0])
        composer = Composer(master)
        for i in range(1, number_of_sections):
            doc_temp = Document_compose(files_list[i])
            composer.append(doc_temp)

        composer.save(f"{constants.DEFAULT_DOCS_DIR_PASS}\\QR_для оплаты.docx")
        # Подчищаем за собой файлы
        for name in files_list:
            if os.path.exists(f'{os.getcwd()}\\{name}'):
                os.remove(f'{os.getcwd()}\\{name}')
        self.errorSignal.emit(True)


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
