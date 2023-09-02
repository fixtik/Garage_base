import sqlite3
import os


from constants import *




def search_db(path: str, db_name: str = DEFAULT_BD_NAME) -> bool:
    """проверка наличия файла бд по заднному пути"""
    return os.path.isfile(f'{path}{db_name}')


def create_db(path: str, db_name: str = DEFAULT_BD_NAME) -> bool:
    """создает БД по заданному пути"""
    try:
        conn = sqlite3.connect(f'{path}{db_name}')
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False




