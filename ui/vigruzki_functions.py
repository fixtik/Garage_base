import os
from dataclasses import dataclass
from openpyxl import Workbook
from openpyxl.styles import Border, Side, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime

import constants
import sqlite_qwer
import datetime
import calendar


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
                            i += 1  # плюсуем чтобы больще не записывалось
                        dict['name'] = name  # записываем в словарь название платежа
                        if calendar.month_name[int(con.month)] in dict:  # Проверяем есть ли название месяца в словаре
                            # Записываем сумму платежа в нужный месяц
                            dict[calendar.month_name[int(con.month)]] = con.TotalSum
                    else:
                        if calendar.month_name[int(con.month)] in dict:  # Проверяем есть ли название месяца в словаре
                            # Записываем сумму платежа в нужный месяц
                            dict[calendar.month_name[int(con.month)]] = con.TotalSum
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

    def autoFit(self, ws):
        for column in ws.iter_cols():
            # автоматическая подгонка ширины столбцов
            name = get_column_letter(column[0].column)
            new_col_length = max(len(str(cell.value)) for cell in column)
            ws.column_dimensions[name].width = new_col_length + 2  # Added an extra bit for padding
            # границы
            thins = Side(border_style="thin", color="000000")
            for cell in column:
                cell.border = Border(top=thins, bottom=thins, left=thins, right=thins)


@dataclass
class SmetaStructureLite:
    """Класс для работы с данными сметы"""
    name: str = ''  # название платежа
    month: str = ''  # месяц в котором был совершен платеж
    pay_kind: str = ''  # нал(1) / безнал(2)
    TotalSum: str = ''  # итоговая сумма платежей за месяц


def spisok_action():
    if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
        os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.
    print('bomj')
