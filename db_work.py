import shutil
import sqlite3
from os.path import isfile
from PySide6 import QtCore, QtWidgets, QtGui

import constants
from constants import *
import sqlite_qwer
import ui.dialogs


class Garage_DB():
    """Класс для работы с БД"""

    def __init__(self, db_name: str = DEFAULT_DB_NAME):
        self.db_name = db_name  # имя БД
        self.connect = None  # коннектор БД
        self.cursor = None  # курсор БД

    def __del__(self):
        if self.connect:
            self.connect.close()

    def execute(self, sql: str) -> bool:
        """выполнение sql запроса"""
        if not self.connect:
            self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            print(e)
            self.connect.close()
            return False
        return True

    def create_db(self) -> bool:
        """
        создание новой БД с именем, заданным при создании экземпляра класса
        :return: истина, если БД создана
        также проверяем создана ли бд и переименовываем ее
        """
        if isfile(constants.DEFAULT_DB_NAME):
            try:
                shutil.copy(constants.DEFAULT_DB_NAME, constants.DEFAULT_OLD_DB_NAME)
            except:
                return False
        try:
            self.connect = sqlite3.connect(self.db_name)
            self.cursor = self.connect.cursor()
            for table_name in TABALE_NAMES:
                self.drop_table(table_name)
            for item in BD_SQL_CREATOR:
                try:
                    self.cursor.execute(item)
                except Exception as e:
                    print(item, e)
                    self.connect.close()
                    return False
            return True
        except Exception as e:
            print(e)
            return False

    def check_base(self, new_name: str) -> bool:
        """
        проверка существования базы данных, которую задает пользователь
        :param new_name: имя файла БД
        :return: истина, если файл - БД SQLite
        """
        if os.path.isfile(new_name):
            try:
                con = sqlite3.connect(f'file:{new_name}?mode=rw', uri=True)
                con.close()
                return True
            except Exception as e:
                print(e)
                return False
        return False

    def choose_db(self, new_db: str) -> (bool, str):
        """
        смена имени БД
        :param new_db: имя новой БД
        :return: истина, подключена новая БД
        """
        self.db_name = new_db
        if self.connect:
            self.connect.close()
        try:
            self.connect = sqlite3.connect(self.db_name)
            return (True, f'БД {new_db} успешно подключена')
        except Exception as e:
            return (False, f'Ошибка подключения файла {new_db}. Ошибка: {e}')

    def drop_table(self, table_name: str) -> bool:
        """
        удаление таблицы по имени
        :param table_name: имя удаляемой таблицы
        :return: истина, если все ок
        """
        if self.cursor:
            try:
                self.cursor.execute(sqlite_qwer.drop_table_by_name(table_name))
                return True
            except Exception as e:
                print(e)
                return False
        return False

    def autoConnectBD(self) -> (bool, str):
        if self.check_base(DEFAULT_DB_NAME):
            return self.choose_db(DEFAULT_DB_NAME)
        return (False, f'Файл {DEFAULT_DB_NAME} не найден')
