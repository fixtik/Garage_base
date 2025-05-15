import os
from PySide6 import QtWidgets, QtGui, QtCore
from dataclasses import dataclass, fields
from openpyxl import Workbook
from openpyxl.styles import Border, Side, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime

import ui.css
import ui.contribs.vigruzka_contribs
import ui.tableView_Models
import ui.dialogs

import constants
import sqlite_qwer
import datetime
import calendar

import ui.contribute_functions


class Smeta():
    def __init__(self, db, parent=None):
        self.db = db  # БД

    def smeta_action(self):
        # Проверили наличие директории для файла сметы
        if not os.path.isdir(constants.DEFAULT_SMETA_DIR_PASS):  # Проверяем создана директория или нет.
            os.makedirs(constants.DEFAULT_SMETA_DIR_PASS, mode=0o777)  # Создаем директорию.
        wb = Workbook()  # создаем книгу
        ws = wb.active  # делаем единственный лист активным
        ws.title = "Смета"  # меняем название листа
        topik = ['№ п/п', 'Доходная часть сметы', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
                 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        ws.append(topik)
        dict = {
            'id': '',
            'name': '',  # название платежа
            'January': '',
            'February': '',
            'March': '',
            'April': '',
            'May': '',
            'June': '',
            'July': '',
            'August': '',
            'September': '',
            'October': '',
            'November': '',
            'December': ''
        }
        id_name = 0  # номер по порядку
        for i in range(2):  # пробегаем blance_count (влияет/не влияет платеж на баланс гаража)
            if i == 0:
                self.text_plateji(ws, ne='не ')
            if self.db.execute(sqlite_qwer.smeta_reqest(balance_count=i)):
                contribs = self.db.cursor.fetchall()
                for contrib in contribs:  # пробегаем по платежам
                    con = SmetaStructureLite(*contrib)
                    name = con.name + (" (Наличный расчет)" if con.pay_kind == '1' else " (Безналичный расчет)")
                    dict['id'] = id_name  # записываем номер по порядку
                    if dict['name'] != name:  # проверяем не закончились ли платежи с одним названием
                        if id_name != 0:  # пропускаем цикл чтобы не записывать пустую строку
                            ws.append(list(dict.values()))  # записываем данные по платежу
                        id_name += 1  # номер по порядку
                        dict.update({}.fromkeys(dict, 0))  # очищаем словарь
                        if i == 1:
                            self.text_plateji(ws)
                            i += 1  # плюсуем чтобы больше не записывалось
                        dict['name'] = name  # записываем в словарь название платежа
                        if calendar.month_name[int(con.month)] in dict:  # Проверяем есть ли название месяца в словаре
                            # Записываем сумму платежа в нужный месяц
                            dict[calendar.month_name[int(con.month)]] = con.TotalSum
                    else:
                        if calendar.month_name[int(con.month)] in dict:  # Проверяем есть ли название месяца в словаре
                            # Записываем сумму платежа в нужный месяц
                            dict[calendar.month_name[int(con.month)]] = con.TotalSum
        dict['id'] = id_name  # Записываем последний id т.к. он уже приплюсован ранее
        ws.append(list(dict.values()))  # Записываем последний платеж
        file_name = f'{constants.DEFAULT_SMETA_DIR_PASS}Смета_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx'
        self.autoFit(ws=ws)
        wb.save(file_name)  # сохраняем эксель
        # for row in ws.iter_rows(values_only=True):
        #     print(row)

    def text_plateji(self, ws, ne: str = ''):
        ws.append([''])
        ws[f'B{ws.max_row}'].value = f'Платежи {ne}учитываемые в балансе'
        ws.merge_cells(start_row=ws.max_row, start_column=ws.min_column + 1, end_row=ws.max_row,
                       end_column=ws.max_column)  # объединяем ячейки
        ws[f'B{ws.max_row}'].alignment = Alignment(horizontal='center')  # выравниваем посередине

    @staticmethod
    def autoFit(ws):
        for column in ws.iter_cols():
            # автоматическая подгонка ширины столбцов
            name = get_column_letter(column[0].column)
            new_col_length = max(len(str(cell.value)) for cell in column)
            ws.column_dimensions[name].width = new_col_length + 2  # Added an extra bit for padding
            # границы
            thins = Side(border_style="thin", color="000000")
            for cell in column:
                cell.border = Border(top=thins, bottom=thins, left=thins, right=thins)


class Doljnik():
    def __init__(self, db, parent=None):
        self.db = db  # БД

    def doljnik_action(self):
        # Проверили наличие директории для файла должников
        if not os.path.isdir(constants.DEFAULT_DOLJNIKI_DIR_PASS):  # Проверяем создана директория или нет.
            os.makedirs(constants.DEFAULT_DOLJNIKI_DIR_PASS, mode=0o777)  # Создаем директорию.
        wb = Workbook()  # создаем книгу
        ws = wb.active  # делаем единственный лист активным
        ws.title = "Должники"  # меняем название листа
        topik = ['№ п/п', 'Ряд', 'Гараж', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Запасной телефон',
                 'Дата последнего платежа',
                 'Размер долга']
        ws.append(topik)
        row_counter = 1

        # Проверяем корректность дат в БД и меняем их на isoformat в случае чего
        if self.db.execute('SELECT id,pay_date FROM contribution;'):
            s = self.db.cursor.fetchall()
            for i in s:
                try:
                    datetime.date.fromisoformat(i[1])
                except ValueError:
                    update = datetime.datetime.strftime(datetime.datetime.strptime(i[1], '%d.%m.%Y'), '%Y-%m-%d')
                    print(update)
                    self.db.execute(f'UPDATE contribution SET pay_date = "{update}" WHERE id = {i[0]};')

        if self.db.execute(sqlite_qwer.sql_select_doljniki_information()):
            doljniki = self.db.cursor.fetchall()
            for doljnik in doljniki:  # пробегаем по должникам
                stroka = [row_counter]  # заносим счетчик
                dolg = DoljnikStructure(*doljnik)
                dolg.pay_date = datetime.datetime.strftime(datetime.datetime.fromisoformat(dolg.pay_date),
                                                           '%d.%m.%Y') if dolg.pay_date else ''
                for field in fields(dolg):
                    stroka.append(getattr(dolg, field.name))  # добавляем данные датакласса в словарь
                ws.append(stroka)
                row_counter += 1

        file_name = f'{constants.DEFAULT_DOLJNIKI_DIR_PASS}Должники_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx'
        Smeta.autoFit(ws=ws)
        wb.save(file_name)


class Vigruzka_platejei():
    def __init__(self, db, parent=None):
        self.db = db  # БД

    def vigruzka_action(self, garage_id, num_row, num_bild):
        # Проверили наличие директории для файла платежей
        if not os.path.isdir(constants.DEFAULT_PLATEJI_DIR_PASS):  # Проверяем создана директория или нет.
            os.makedirs(constants.DEFAULT_PLATEJI_DIR_PASS, mode=0o777)  # Создаем директорию.
        wb = Workbook()  # создаем книгу
        ws = wb.active  # делаем единственный лист активным
        ws.title = f"Платежи за гараж id{garage_id}"  # меняем название листа
        topik = ['№ п/п', 'Дата платежа', 'Вид платежа', 'Сумма платежа', 'Тип оплаты', 'Комментарий']
        ws.append(topik)
        row_counter = 1

        if self.db.execute(sqlite_qwer.sql_select_contrib_by_object_id(garage_id)):
            conribs = self.db.cursor.fetchall()
            for conrib in conribs:
                con = ui.contribute_functions.Contribution_lite(*conrib)
                con.payDate = datetime.datetime.strftime(datetime.datetime.fromisoformat(con.payDate),
                                                         '%d.%m.%Y') if con.payDate else ''
                con.typePay = "Наличные" if con.typePay == "1" else "Безнал"
                stroka = [row_counter, con.payDate, con.kindPay, con.value, con.typePay, con.comment]
                ws.append(stroka)
                row_counter += 1
        file_name = f'{constants.DEFAULT_PLATEJI_DIR_PASS}Платежи за гараж {num_row}-{num_bild}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx'
        Smeta.autoFit(ws=ws)
        wb.save(file_name)


class Vigruzka_kontrib_ui(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = ui.contribs.vigruzka_contribs.Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector
        self.css = ui.css  # для красоты
        self.obj_model_nal = ui.tableView_Models.PlatejiTableViewModelNal()
        self.obj_model_beznal = ui.tableView_Models.PlatejiTableViewModelBeznal()

        self.initUi()
        self.fill_nal_tableview()
        self.fill_beznaltableview()

    def initUi(self):
        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)

        self.ui.vigruzitNal_pushButton.clicked.connect(self.exel_nal)
        self.ui.vigruzitBeznal_pushButton.clicked.connect(self.exel_nal)

        # устанавливаем дефолтные даты
        self.ui.nachaloPeriodaNal_dateEdit.setDate(datetime.date.today().replace(day=1))
        self.ui.konecPeriodaNal_dateEdit.setDate(datetime.date.today())
        self.ui.nachaloPeriodaBeznal_dateEdit.setDate(datetime.date.today().replace(day=1))
        self.ui.konecPeriodaBeznal_dateEdit.setDate(datetime.date.today())

        # таблица для отображения полей
        self.ui.nal_tableView.setModel(self.obj_model_nal)
        self.ui.nal_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.nal_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                      ResizeToContents)

        self.ui.beznal_tableView.setModel(self.obj_model_beznal)
        self.ui.beznal_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.beznal_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                         ResizeToContents)
        # Обновляем тейблвью при изменении вводных данных
        self.ui.nachaloPeriodaNal_dateEdit.dateChanged.connect(self.fill_nal_tableview)
        self.ui.konecPeriodaNal_dateEdit.dateChanged.connect(self.fill_nal_tableview)
        self.ui.billNumberOt_lineEdit.textEdited.connect(self.fill_nal_tableview)
        self.ui.billNumberDo_lineEdit.textEdited.connect(self.fill_nal_tableview)

        self.ui.nachaloPeriodaBeznal_dateEdit.dateChanged.connect(self.fill_beznaltableview)
        self.ui.konecPeriodaBeznal_dateEdit.dateChanged.connect(self.fill_beznaltableview)

    def fill_nal_tableview(self):
        """заполнение данных tableview"""
        self.ui.nal_tableView.model().clearItemData()
        if self.db:
            sql = sqlite_qwer.sql_selectvigruzka_contrib_nal(self.ui.nachaloPeriodaNal_dateEdit.date().toPython(),
                                                             self.ui.konecPeriodaNal_dateEdit.date().toPython(),
                                                             1,
                                                             self.ui.billNumberOt_lineEdit.text(),
                                                             self.ui.billNumberDo_lineEdit.text())
            cont_id = 1
            if self.db.execute(sql):
                for obj in self.db.cursor.fetchall():
                    contrib = VigruzkaContrib(cont_id, *obj)
                    self.ui.nal_tableView.model().setItems(contrib)
                    cont_id += 1

    def fill_beznaltableview(self):
        self.ui.beznal_tableView.model().clearItemData()
        if self.db:
            sql = sqlite_qwer.sql_selectvigruzka_contrib_nal(self.ui.nachaloPeriodaBeznal_dateEdit.date().toPython(),
                                                             self.ui.konecPeriodaBeznal_dateEdit.date().toPython(),
                                                             2)
            cont_id = 1
            if self.db.execute(sql):
                for obj in self.db.cursor.fetchall():
                    contrib = VigruzkaContrib(cont_id, *obj)
                    self.ui.beznal_tableView.model().setItems(contrib)
                    cont_id += 1

    def exel_nal(self):
        """Выгрузка эксель наличных платежей"""
        # Проверили наличие директории для файла платежей
        if not os.path.isdir(constants.DEFAULT_PLATEJI_DIR_PASS):  # Проверяем создана директория или нет.
            os.makedirs(constants.DEFAULT_PLATEJI_DIR_PASS, mode=0o777)  # Создаем директорию.
        wb = Workbook()  # создаем книгу
        ws = wb.active  # делаем единственный лист активным
        ws.title = "Платежи терминал" if self.sender().objectName() == self.ui.vigruzitNal_pushButton.objectName() else "Платежи безнал"  # меняем название листа
        topik = ['№ п/п', 'Ряд', 'Гараж', 'Дата платежа', 'Номер чека', 'Период', 'Взнос', 'Электричество']
        ws.append(topik)

        contribs = self.ui.nal_tableView.model().items
        for contrib in contribs:
            stroka = [contrib.id, contrib.num_row, contrib.num_bild,
                      datetime.datetime.strptime(contrib.pay_date, "%Y-%m-%d").strftime("%d.%m.%Y"),
                      contrib.bill_number, contrib.period, contrib.vznos, contrib.electric]
            ws.append(stroka)
        if self.sender().objectName() == self.ui.vigruzitNal_pushButton.objectName():
            file_name = f'{constants.DEFAULT_PLATEJI_DIR_PASS}Платежи терминал {datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx'
        else:
            file_name = f'{constants.DEFAULT_PLATEJI_DIR_PASS}Платежи безнал {datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx'

        Smeta.autoFit(ws=ws)
        wb.save(file_name)

        if ui.dialogs.onShowСonfirmation(self, title=constants.INFO_TITLE,
                                         msg=f'{constants.INFO_PLATEJI_GENERATION_OK}'
                                             f'\n{constants.INFO_OPEN_FILE}'):
            try:
                os.startfile(file_name)
            except Exception as e:
                ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=str(e))


@dataclass
class VigruzkaContrib:
    """Класс для работы с данными по наличным платежам"""
    id: int
    num_row: str  # ряд
    num_bild: str  # номер гаража
    pay_date: str  # дата платежа
    bill_number: str  # номер чека
    period: str  # период за который совершен платеж
    vznos: str  # сумма платежа
    electric: str  # сумма платежа за электричество


@dataclass
class DoljnikStructure:
    """Класс для работы с данными по должникам"""
    num_row: str = ''  # ряд
    num_bild: str = ''  # номер гаража
    surname: str = ''  # фамилия
    first_name: str = ''  # имя
    second_name: str = ''  # отчество
    phone_main: str = ''  # номер телефона
    phone_sec: str = ''  # запасной номер
    pay_date: str = ''  # дата последней оплаты
    dolg: str = ''  # сумма долга


@dataclass
class SmetaStructureLite:
    """Класс для работы с данными сметы"""
    name: str = ''  # название платежа
    month: str = ''  # месяц в котором был совершен платеж
    pay_kind: str = ''  # нал(1) / безнал(2)
    TotalSum: str = ''  # итоговая сумма платежей за месяц
