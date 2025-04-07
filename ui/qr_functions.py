import os
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
from ui.qr.qr_bankInfo import Ui_Form
import ui.validators
import ui.css
import ui.dialogs
import ui.qr.statusbar
from datetime import datetime
from PySide6 import QtCore, QtWidgets


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
    def __init__(self, parent=None, db=None, garage_id=None):
        super().__init__(parent)
        self.ui = ui.qr.statusbar.Ui_Form()
        self.ui.setupUi(self)
        # переменные класса
        self.css = ui.css  # для красоты
        self.db = db
        self.garage_id = garage_id
        self.qr_thread = TQR_Thread(garage_id=self.garage_id)  # поток с генерацией qr-кода
        self.no_error = None  # для отлова ошибок в потоке
        self.breakByUser = None  # для отображения кто завершил процесс

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
            self.db.execute(sqlite_qwer.sql_select_maxid(constants.OBJ_TABLE))
            maxid = self.db.cursor.fetchone()
            self.ui.progressBar.setMaximum(maxid[0])

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
        self.qr_thread.clearSignal.connect(self.refreshStatus)

    def closeEvent(self, event):
        if ui.dialogs.onShowСonfirmation(self, constants.ATTANTION_TITLE, constants.QUESTION_STOP_GENERATION_QR):
            if self and event.type() == QtCore.QEvent.Type.Close:
                self.breakByUser = True
                self.qr_thread.flag = False
        else:
            event.ignore()

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
                    if self.garage_id:
                        os.startfile(
                            f"{constants.DEFAULT_QR_DIR_PASS}\\QR для гаража {self.garage_id}.docx")
                    else:
                        os.startfile(f"{constants.DEFAULT_QR_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}")
                except Exception as e:
                    ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=str(e))
            self.destroy(True)
        elif self.breakByUser:
            ui.dialogs.onShowOkMessage(self, title=constants.ERROR_TITLE,
                                       msg=constants.ERROR_QR_GENERATION_BREAK_BY_USER)
            self.cleanUp()
            self.destroy()
        else:
            ui.dialogs.onShowOkMessage(self, title=constants.ERROR_TITLE, msg=constants.ERROR_QR_GENERATION)
            self.cleanUp()
            self.destroy()

    def cleanUp(self):
        files = os.listdir(constants.DEFAULT_TMP_DIR_PASS)
        for file in files:
            pass_file = f'{constants.DEFAULT_TMP_DIR_PASS}{file}'
            if os.path.isfile(pass_file):
                try:
                    os.remove(pass_file)
                finally:
                    pass

    def refreshStatus(self, maxValue):
        self.ui.progressBar.reset()
        self.ui.progressBar.setValue(maxValue)


class TQR_Thread(QtCore.QThread):
    """
    поток поиска файлов с рекурсией
    """
    infoSignal = QtCore.Signal(str)
    clearSignal = QtCore.Signal(int)
    statusSignal = QtCore.Signal(int)
    errorSignal = QtCore.Signal(bool)

    def __init__(self, parent=None, db=None, garage_id=None):
        super().__init__(parent)
        self.flag = None  # для возможности остановки процесса

        self.db = db  # ссылка на БД

        self.fileNames = []  # для хранения списка названия файлов
        self.statusbar = None  # для отображения окна со статусбаром
        self.value = 0  # стартовое значение для статусбара
        self.garage_id = garage_id  # id гаража

    def run(self) -> None:
        if self.flag is None:
            self.flag = True
        self.generate_qr()

    def generate_qr(self):
        """Да что за гений писал эту функцию которая генерирует QR коды"""
        timer = 0
        if not os.path.isfile(constants.DEFAULT_QR_TEMPLATE_NAME):
            self.infoSignal.emit('Отсутствует шаблон\nЗакройте окно')
            self.flag = False
            return None

        if self.fileNames:
            self.fileNames = []  # очищаем переменную с названиями файлов чтобы не было дубликатов

        if self.db:
            # Создаем папку для хранения временных файлов
            if not os.path.exists(constants.DEFAULT_TMP_DIR_PASS):
                os.makedirs(constants.DEFAULT_TMP_DIR_PASS, mode=0x777)
            # Создаем папку для хранения qr
            if not os.path.exists(constants.DEFAULT_QR_DIR_PASS):
                os.makedirs(constants.DEFAULT_QR_DIR_PASS, mode=0x777)

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
                if self.garage_id:
                    self.db.execute(sqlite_qwer.sql_select_payment_member_information(id=self.garage_id))
                else:
                    self.db.execute(sqlite_qwer.sql_select_payment_member_information(id=None))
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
                    self.fill_doc_template(paymentMemberInfo.num_bild,
                                           paymentMemberInfo.num_row,
                                           paymentMemberInfo.id)
                except Exception as e:
                    print(e)
                    self.errorSignal.emit(False)

                # Подтираем ненужные фото qr кодов
                for j in range(2):
                    qr_dir = f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}.png" if j == 0 \
                        else f"tmp\\qr_{paymentMemberInfo.num_row}_{paymentMemberInfo.num_bild}_electric.png"
                    os.remove(qr_dir)

                timer += 1
                print(timer)
                # if timer == 1:
                #     break
            if not self.flag:
                return None
            try:
                self.final_output_document(self.fileNames)
            except Exception as e:
                print(e)
                self.errorSignal.emit(False)

    def fill_doc_template(self, num, row, id):
        """Заполняем шаблон с QR кодами"""
        doc = DocxTemplate(constants.DEFAULT_QR_TEMPLATE_NAME)
        qr = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}.png', width=Mm(35), height=Mm(35))
        qr_electric = InlineImage(doc, image_descriptor=f'tmp\\qr_{row}_{num}_electric.png', width=Mm(35),
                                  height=Mm(35))

        try:
            # Вытаскиваем информацию по гаражному кооперативу
            self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS))
            info = self.db.cursor.fetchone()
            paymentInfo = paymentInformation(*info)

            # Вытаскиваем информацию по гаражу
            self.db.execute(sqlite_qwer.sql_select_payment_garage_information(id=id))
            garageInfo = self.db.cursor.fetchone()
            paymentGarageInfo = paymentGarageInformation(*garageInfo)

            # Вытаскиваем информацию по счетчикам
            self.db.execute(sqlite_qwer.sql_select_payment_meter_information(id=id))
            meterInfo = self.db.cursor.fetchone()
            paymentMeterInfo = paymentMeterInformation(*meterInfo)

        except Exception as e:
            ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=constants.ERROR_QR_GENERATION)
            self.flag = False

        # Арифметика для квитанции (Оплата членских взносов)
        raznica = int(paymentGarageInfo.vznos) - int(paymentGarageInfo.tekyschieNachisleniya)
        nachisleno_I = 0 if int(paymentGarageInfo.pereplata) > 0 or (raznica > int(paymentGarageInfo.vznos) / 2) else (
                int(
                    paymentGarageInfo.vznos) / 2 - raznica)  # 0 в начисления если имеется переплата
        if int(paymentGarageInfo.pereplata) > 0:
            nachisleno_II = 0
        elif raznica <= int(paymentGarageInfo.vznos) / 2:
            nachisleno_II = int(paymentGarageInfo.vznos) / 2
        else:
            nachisleno_II = int(paymentGarageInfo.vznos) - raznica
        dop_vznos_I = 1000 if (int(paymentGarageInfo.dolg) > 0 or  # 1000 р штрафа если имеется долг
                               (int(datetime.now().strftime("%m")) > 4 and nachisleno_I > 0)) else 0
        dop_vznos_II = 1000 if (int(paymentGarageInfo.tekyschieNachisleniya) > int(
            paymentGarageInfo.vznos) / 2) and int(
            datetime.now().strftime("%m")) > 9 else 0  # 1000 р штрафа если не оплатили до октября
        summa_k_oplate_I = 0 if int(paymentGarageInfo.pereplata) > 0 else nachisleno_I + dop_vznos_I + float(
            paymentGarageInfo.dolg)  # 0 в начисления если имеется переплата
        summa_k_oplate_II = 0 if int(
            paymentGarageInfo.pereplata) > 0 else nachisleno_II + dop_vznos_II  # 0 в начисления если имеется переплата
        itogo = 0 if int(
            paymentGarageInfo.pereplata) > 0 else summa_k_oplate_I + summa_k_oplate_II  # 0 в начисления если имеется переплата

        # Арифметика для квитанции (Оплата электроэнергии)
        potreb_day_220 = 0 if paymentMeterInfo.num_meter_220 is None else int(paymentMeterInfo.day_220) - int(
            paymentMeterInfo.prev_day_220)
        potreb_night_220 = 0 if paymentMeterInfo.num_meter_220 is None else int(
            paymentMeterInfo.night_220) - int(paymentMeterInfo.prev_night_220)
        potreb_day_380 = 0 if paymentMeterInfo.num_meter_380 is None else int(paymentMeterInfo.day_380) - int(
            paymentMeterInfo.prev_day_380)
        potreb_night_380 = 0 if paymentMeterInfo.num_meter_380 is None else int(
            paymentMeterInfo.night_380) - int(paymentMeterInfo.prev_night_380)
        nachisleno_day_220 = potreb_day_220 * int(paymentMeterInfo.value_day_220)
        nachisleno_night_220 = potreb_night_220 * int(paymentMeterInfo.value_night_220)
        nachisleno_day_380 = potreb_day_380 * int(paymentMeterInfo.value_day_380)
        nachisleno_night_380 = potreb_night_380 * int(paymentMeterInfo.value_night_380)

        context = {'qr_photo': qr,
                   'qr_photo_electric': qr_electric,
                   'num': num,
                   'row': row,
                   'fio': f'{paymentGarageInfo.surname} {paymentGarageInfo.first_name} {paymentGarageInfo.second_name}',
                   'name': paymentInfo.Name,
                   'PayeeINN': paymentInfo.PayeeINN,
                   'KPP': paymentInfo.KPP,
                   'BIC': paymentInfo.BIC,
                   'CorrespAcc': paymentInfo.CorrespAcc,
                   'PersonalAcc': paymentInfo.PersonalAcc,
                   'BankName': paymentInfo.BankName,

                   # Данные для квитанции с общими взносами
                   'year': datetime.now().strftime("%Y"),
                   'vznos': paymentGarageInfo.vznos,
                   'garage_size': f'{paymentGarageInfo.width}x{paymentGarageInfo.length}x{paymentGarageInfo.height}',
                   'dolg': paymentGarageInfo.dolg,
                   'dop_vznos_I': dop_vznos_I,
                   'dop_vznos_II': dop_vznos_II,
                   'nachisleno_I': nachisleno_I,
                   'nachisleno_II': nachisleno_II,
                   'summa_k_oplate_I': summa_k_oplate_I,
                   'summa_k_oplate_II': summa_k_oplate_II,
                   'dop_vznos_sum': dop_vznos_I + dop_vznos_II,
                   'itogo': itogo,

                   'num_meter_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.num_meter_220,
                   # Данные для дневных показаний счетчика 220
                   'prev_day_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.prev_day_220,
                   'day_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.day_220,
                   'potreb_day_220': potreb_day_220,
                   'value_day_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.value_day_220,
                   'nachisleno_day_220': nachisleno_day_220,
                   'itog_day_220': nachisleno_day_220,
                   # Данные для ночных показаний счетчика 220
                   'prev_night_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.prev_night_220,
                   'night_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.night_220,
                   'potreb_night_220': potreb_night_220,
                   'value_night_220': 0 if paymentMeterInfo.num_meter_220 is None else paymentMeterInfo.value_night_220,
                   'nachisleno_night_220': nachisleno_night_220,
                   'itog_night_220': nachisleno_night_220,

                   # Данные для дневных показаний счетчика 380
                   'prev_day_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.prev_day_380,
                   'day_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.day_380,
                   'potreb_day_380': potreb_day_380,
                   'value_day_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.value_day_380,
                   'nachisleno_day_380': nachisleno_day_380,
                   'itog_day_380': nachisleno_day_380,
                   'num_meter_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.num_meter_380,
                   # Данные для ночных показаний счетчика 380
                   'prev_night_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.prev_night_380,
                   'night_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.night_380,
                   'potreb_night_380': potreb_night_380,
                   'value_night_380': 0 if paymentMeterInfo.num_meter_380 is None else paymentMeterInfo.value_night_380,
                   'nachisleno_night_380': nachisleno_night_380,
                   'itog_night_380': nachisleno_night_380,

                   'itogo_meters': nachisleno_day_220 + nachisleno_night_220 + nachisleno_night_380 + nachisleno_day_380
                   }
        doc.render(context)
        doc.save(f"tmp\\Гараж_{row}_{num}.docx")
        self.fileNames.append(f"tmp\\Гараж_{row}_{num}.docx")

    def final_output_document(self, files_list):
        """Создаем итоговый файл с QR кодами"""
        self.infoSignal.emit('Создаем итоговый файл\nОсталось совсем чуть-чуть')
        if self.garage_id:
            if os.path.isfile(
                    f"{constants.DEFAULT_QR_DIR_PASS}\\QR для гаража {self.garage_id}.docx"):
                os.remove(
                    f"{constants.DEFAULT_QR_DIR_PASS}\\QR для гаража {self.garage_id}.docx")
        else:
            if os.path.isfile(f"{constants.DEFAULT_QR_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}"):
                os.remove(f"{constants.DEFAULT_QR_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}")
        number_of_sections = len(files_list)
        # Сбрасываем прогресс бар и устанавливаем новое максимальное значение
        self.clearSignal.emit(number_of_sections)
        master = Document_compose(files_list[0])
        composer = Composer(master)
        for i in range(1, number_of_sections):
            doc_temp = Document_compose(files_list[i])
            composer.append(doc_temp)
            self.statusSignal.emit(i)
            # Проверяем не прервана ли операция пользователем
            if not self.flag:
                if self.garage_id:
                    composer.save(
                        f"{constants.DEFAULT_QR_DIR_PASS}\\QR для гаража {self.garage_id}.docx")
                else:
                    composer.save(f"{constants.DEFAULT_QR_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}")
                return None
        if self.garage_id:
            composer.save(
                f"{constants.DEFAULT_QR_DIR_PASS}\\QR для гаража {self.garage_id}.docx")
        else:
            composer.save(f"{constants.DEFAULT_QR_DIR_PASS}{constants.DEFAUL_QR_FILE_NAME}")
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


@dataclass
class paymentGarageInformation:
    id: str = ''
    surname: str = ''
    first_name: str = ''
    second_name: str = ''
    vznos: str = ''
    width: str = ''
    length: str = ''
    height: str = ''
    dolg: str = ''
    tekyschieNachisleniya: str = ''
    pereplata: str = ''


@dataclass
class paymentMeterInformation:
    id: str = ''
    num_meter_220: str = ''
    prev_day_220: str = ''
    day_220: str = ''
    prev_night_220: str = ''
    night_220: str = ''
    num_meter_380: str = ''
    prev_day_380: str = ''
    day_380: str = ''
    prev_night_380: str = ''
    night_380: str = ''
    value_day_220: str = ''
    value_night_220: str = ''
    value_day_380: str = ''
    value_night_380: str = ''
