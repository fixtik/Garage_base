# import sqlite3
# from datetime import datetime
# from dataclasses import dataclass
# import os
# import shutil
# import constants
# import pandas as pd
# import numpy as np
#
# import sqlite_qwer
# import db_work
#
#
# def set_topik():
#     topik = ('№ п/п', 'Доходная часть сметы', 'Сумма доходов Смета', 'Сумма доходов исполнение Сметы',
#              'Расхождение', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
#              'октябрь', 'ноябрь', 'декабрь')
#     print(pd.Series(topik))
#     # topik.to_excel("docs/smeta.xlsx")
#
#
# class Smeta():
#     def __init__(self, db, parent=None):
#         self.db = db  # БД
#
#     def smeta_action(self):
#         if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
#             os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.
#         print('2')
#         if self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.CONTRIB_TABLE)):
#             conribs = self.db.cursor.fetchall()
#             for conrib in conribs:
#                 print(conrib)
#                 # con = ui.contribute_functions.Contribution_lite(*conrib)
#                 # 'SELECT * FROM contribution WHERE date(pay_date, 'start of year') = date(datetime('now'), 'start of year');'
#
#
# def spisok_action():
#     if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
#         os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.
#     print('bomj')
#
#
# @dataclass
# class SmetaStructure:
#     """Класс для работы с данными сметы"""
#     id: int = ''
#     size_id: str = ''  # вид типоразмера
#     width: str = ''  # размеры
#     length: str = ''
#     height: str = ''
#     year: str = ''  # год за который платят1
#     value: str = ''  # сумма взноса
#     bilingDate: str = ''  # дата выставления счета
