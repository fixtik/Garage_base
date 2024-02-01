import sqlite3
from datetime import datetime
import os
import shutil
import constants
import pandas as pd
import numpy as np


def set_topik():
    topik = ('№ п/п', 'Доходная часть сметы', 'Сумма доходов Смета', 'Сумма доходов исполнение Сметы',
             'Расхождение', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
             'октябрь', 'ноябрь', 'декабрь')
    print(pd.Series(topik))
    # topik.to_excel("docs/smeta.xlsx")


def smeta_action():
    if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
        os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.
    # smeta_file = open("docs/smeta.xlsx", "w+")
    # smeta_file.to_excel("docs/smeta.xlsx")
    # smeta_file.write("Привет, файл!")
    # smeta_file.close()
    set_topik()
    print("suka")


def spisok_action():
    if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
        os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.

    print('bomj')
