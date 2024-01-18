import sqlite3
from datetime import datetime
import os
import shutil
import constants
import pandas


def spisok_action():
    if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
        os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.

    print('bomj')


def smeta_action():
    if not os.path.isdir(constants.DEFAULT_DOCS_DIR_PASS):  # Проверяем создана директория или нет.
        os.makedirs(constants.DEFAULT_DOCS_DIR_PASS, mode=0o777)  # Создаем директорию.
    print("suka")
