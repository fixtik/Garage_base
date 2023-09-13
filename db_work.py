import sqlite3
import os


from constants import *


class Garage_DB:
    """Класс для работы с БД"""

    def __init__(self, db_name: str = DEFAULT_DB_NAME):
        self.db_name = db_name   # имя БД
        self.connect = None      # коннектор БД
        self.cursor = None       # курсор БД

    def __del__(self):
        if self.connect:
            self.connect.close()

    def create_db(self) -> bool:
        """
        создание новой БД с именем, заданным при создании экземпляра класса
        :return: истина, если БД создана
        """
        try:
            self.connect = sqlite3.connect(self.db_name)
            self.cursor = self.connect.cursor()
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
                con = sqlite3.connect('file:aaa.db?mode=rw', uri=True)
                con.close()
                return True
            except Exception:
                return False
        return False

    def choose_db(self, new_db: str) -> bool:
        """
        смена имени БД
        :param new_db: имя новой БД
        :return: истина, подключена новая БД
        """
        if self.check_base(new_db):
            self.db_name = new_db
            if self.connect:
                self.connect.close()
            self.connect = sqlite3.connect(self.db_name)
            return True
        return False

