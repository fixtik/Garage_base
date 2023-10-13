import sqlite3
import os


from constants import *




def search_db(path: str, db_name: str = DEFAULT_DB_NAME) -> bool:
    """проверка наличия файла бд по заднному пути"""
    return os.path.isfile(f'{path}{db_name}')


def create_db(path: str, db_name: str = DEFAULT_DB_NAME) -> bool:
    """создает БД по заданному пути"""
    try:
        conn = sqlite3.connect(f'{path}{db_name}')
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False

# Запросы на электросчетчик
def sql_add_electric_meter(num_meter: str, cur_day: int, cur_night: int = 0, pr_day: int = 0 , pr_night: int = 0) -> str:
    """
    Запрос на добавление нового электросчетчика
    :param num_meter: номер электросчетчика
    :param cur_day: текущие дневные показания показания
    :param cur_night: текущие ночные показания (по умолчанию 0)
    :param pr_day: предыдущие дневные показания (по умолчанию 0)
    :param pr_night: предыдущие ночные показания (по умолчанию 0)
    :return: sql-запрос
    """
    return f'INSERT INTO electric_meter (num_meter, prev_day, prev_night,' \
           f' day, night) VALUES ({num_meter}, {pr_day}, {pr_night}, {cur_day}, {cur_night});'


def sql_update_electric_meter_by_id(metr_id: int, cur_day: int, cur_night: int = 0) -> str:
    """
    Запрос на обновление текущих показаний счетчика по id-счетчика
    :param metr_id: id-счетчика
    :param cur_day: текущие дневные показания
    :param cur_night: :param cur_night: текущие ночные показания (по умолчанию 0)
    :return: sql-запрос
    """
    return f'UPDATE electric_meter SET' \
           f'prev_day = (SELECT day FROM electric_meter WHERE id = {metr_id}),' \
           f'prev_night =  (SELECT night FROM electric_meter WHERE id = {metr_id}),' \
           f'day = {cur_day}, night = {cur_night} ' \
           f'WHERE id = {metr_id};'


def sql_get_metr_id_by_num(num_metr: str) -> str:
    """
    Запрос на получение id счетчика по номеру счетчика
    :param num_metr: номер-счетчика
    :return: sql-запрос
    """
    return f'SELECT id FROM electric_meter WHERE num_metr = {num_metr});'

def sql_get_consumed_energi_by_id(metr_id: int) -> str:
    """
    Получение данных по потребленной электроэнергии
    :param metr_id: id счетчика
    :return: sql-запрос
    """
    return f'SELECT day - prev_day, night - prev_night FROM electric_meter WHERE id = {metr_id}'


#запросы на типоразмер
def sql_add_new_type_size(width: float = 4.5, len: float = 6, hight: float = 3.2, comment: str ='')-> str:
    """
    Запрос на добавление нового типоразмера объекта недвижимости
    :param width: ширина объекта (4,5 метра по умолчнанию)
    :param len: длина объекта (6 метров по умолчнанию)
    :param hight: высота объекта (3.2 метра по умолчнанию)
    :return: sql-запрос
    """
    return f'INSERT INTO type_size (width, len, hight, comment) VALUES ({width}, {len}, {hight}, {comment});'


def get_type_size_id_by_size(width: float, len:float, height: float) -> str:
    """
    Запрос на поиск id по типоразмерам
    :param width: ширина
    :param len: длина
    :param height: высота
    :return: sql-запрос
    """
    return f"SELECT id FROM type_size WHERE width = {width}, len = {len}, height = {height};"


# запросы на тип взноса
def sql_add_new_contrib_type(contrib_name: str, value: float, comment: str = ' ') -> str:
    """
    добавление нового типа взноса
    :param contrib_name: название взноса
    :param value: размер взноса
    :param comment: комментарий
    :return: sql-запрос
    """

    return f"INSERT INTO contribution_type (name, value, comment) VALUES ('{contrib_name}', {value}, '{comment}');"

def sql_update_contrib_type(contrib_id: int, value: float, comment: str = ' ') -> str:
    """
    обновление заначений полей по id
    """
    return f"UPDATE contribution_type SET value = {value}, comment = '{comment}' WHERE id = {contrib_id};"

def sql_get_one_record_by_id(table_name: str, id: int) -> str:
    """
    возвращает одну запись по id
    """
    return f"SELECT * FROM {table_name} WHERE id = {id};"

# запросы по членам кооператива
def sql_add_new_member(surname: str, first_name: str, birth_date: str, phone_main: str, voa: str,
                       second_name:str ='', adress: str = '', second_phone:str = '',
                       email:str = '', photo ='') -> str:
    """
    Добавление нового члена кооператива или арендатора
    :param surname: фамилия
    :param first_name: имя
    :param birth_date: дата рождения
    :param phone_main: основной номер телефона
    :param voa: направление ВОА
    :param second_name: отчество (необязательно)
    :param adress: адрес проживания (необязательно)
    :param second_phone: запасной телефон (необязательно)
    :param email: адрес электронной почты (необязательно)
    :param photo: фотография (необязательно)
    :return: sql-запрос
    """
    return f"INSERT INTO garage_member (surname, first_name, second_name, birth_date, phone_main," \
           f" phone_sec, adress, email, voa, photo) VALUES ('{surname}', '{first_name}', '{second_name}', {birth_date}," \
           f"'{phone_main}', '{second_phone}', '{adress}', '{email}', '{voa}', '{photo}');"


#универсальные запросы
def sql_select_all_from_table(table_name: str) -> str:
    """выбор всех значений в таблице table_name"""
    return f"SELECT * FROM {table_name};"

def sql_update_field_by_table_name_and_id(table_name: str, rec_id: int, field: str, new_value) -> str:
    """
    Обновление значения любого из полей по id-записи
    :param table_name: имя таблицы
    :param rec_id: id типоразмера
    :param place: имя изменяемого поля
    :param new_value: новое значение
    :return: sql-запрос
    """
    return f'UPDATE {table_name} SET {field} = {new_value} WHERE id={rec_id};'


def sql_delete_rec_by_table_name_and_id(table_name: str, rec_id: int) -> str:
    """
    удаление записи по имени таблицы и id
    :param table_name: имя таблицы
    :param rec_id: id
    :return: sql-запрос
    """
    return f'DELETE FROM {table_name} WHERE id = {rec_id};'

def drop_table_by_name(table_name: str) -> str:
    """
    Удаление таблицы по имени
    :param table_name: имя таблицы
    :return: sql-запрос
    """
    return f'DROP TABLE IF EXISTS {table_name};'


#автомобильные запросы
def sql_add_new_car(mark: str, gos_num: str, owner_id: int) -> str:
    """
    Добавление нового автомобиля привязанного к id владельца
    :param mark: марка автомобиля
    :param gos_num: номер автомобиля
    :param owner_id: id влядельца автомобиля
    :return: sql-запрос
    """
    return f'INSERT INTO automobile (mark, gos_num, owner_id, active) VALUES ({mark}, {gos_num}, {owner_id}, "1");'


def sql_update_car(gos_num: str, new_mark: str, new_gos_num: str) -> str:
    """
    Обновление марки и номера машины по id владельца
    :param gos_num: номер владельца автомобиля
    :param new_mark: новая марка автомобиля
    :param new_gos_num: новый гос номер автомобиля
    :return: sql-запрос
    """
    return f'UPDATE automobile SET mark = {new_mark}, gos_num = {new_gos_num}' \
           f'WHERE id = (SELECT id FROM automobile WHERE gos_num = {gos_num});'


def sql_set_inactive_car(gos_num: str) -> str:
    """
    Перевод в неактивное состояние автомобиля
    :param gos_num: номер владельца автомобиля
    :return: sql-запрос
    """
    return f'UPDATE  automobile' \
           f'SET active = 0, inactive_date = date() ' \
           f'WHERE id = (SELECT id FROM automobile WHERE gos_num = {gos_num});'


def sql_set_inactive_garage_member(surname: str, first_name: str, second_name: str, phone_main: str) -> str:
    """
    Перевод в неактивное состояние пользователя
    :param surname: фамилия пользователя
    :param first_name: имя пользователя
    :param second_name: отчество пользователя
    :param phone_main: телефон пользователя
    :return: sql-запрос
    """
    return f'UPDATE  GARGE_MEMBER' \
           f'SET active = 0, inactive_date = date() ' \
           f'WHERE id = (SELECT id FROM GARGE_MEMBER WHERE surname = {surname}, first_name = {first_name},' \
           f'second_name = {second_name}, phone_main = {phone_main};)'


def sql_get_car(gos_num: str) -> str:
    """
    Поиск id владельца по номеру автомобиля
    :param gos_num: гос номер автомобиля
    :return: sql-запрос
    """
    return f'SELECT owner_id FROM automobile WHERE gos_num = {gos_num};'

def sql_select_garaje_id_by_num_and_row(garage_num: int, row: int) -> str:
    """
    Поиск id гаража по номеру и ряду
    """
    return f'SELECT id FROM garage_obj WHERE num_bild = {garage_num} and num_row = {row};'


'''--------------------------------------------NEW--------------------------------------------------'''

def sql_update_garage_member(surname: str, first_name: str, second_name: str, phone_main: str, change_pole: str, new_value: str) -> str:
    """
    Замена любого поля гаражного члена через id
    :param surname: фамилия пользователя
    :param first_name: имя пользователя
    :param second_name: отчество пользователя
    :param phone_main: телефон пользователя
    :param change_pole: изменяемое поле
    :param new_value: новое значение
    :return: sql-запрос
    """
    return f'UPDATE  garage_member ' \
           f'SET {change_pole} = {new_value} ' \
           f'WHERE id = (SELECT id FROM GARGE_MEMBER WHERE surname = {surname}, first_name = {first_name}, ' \
           f'second_name = {second_name}, phone_main = {phone_main});'

def sql_update_garage(num_row: str, num_bild: str, change_pole: str, new_value: str) -> str:
    """
    Замена любого поля гаражного члена через id
    :param num_row: номер ряда
    :param num_bild: номер гаража
    :param change_pole: изменяемое поле
    :param new_value: новое значение
    :return: sql-запрос
    """
    return f'UPDATE  garage_obj ' \
           f'SET {change_pole} = {new_value} ' \
           f'WHERE id = (SELECT id FROM garage_member WHERE num_row = {num_row}, num_bild = {num_bild});'

'''--------------------------------------------NEW--------------------------------------------------'''

def sql_add_new_garage_size(width: float, length: float, height: float, comment: str = ' ') -> str:
    '''
    Добавление размеров гаража
    :param width: ширина
    :param len: длина
    :param height: высота
    :param comment: комментарий
    :return: sql-запрос
    '''
    return f'INSERT INTO type_size (width, len, height, comment) VALUES ({width}, {length}, {height}, "{comment}");'

def sql_update_garage_size(size_id: int, width: float, length: float, height: float, comment: str = ' ') -> str:
    '''
    Запрос на поиск id по типоразмерам
    :param width: ширина
    :param len: длина
    :param height: высота
    :param comment: комментарий
    :return: sql-запрос
    '''
    return f"UPDATE type_size SET width = {width}, len = {length}, height = {height}, comment = '{comment}'" \
           f" WHERE id = {size_id};"

'''--------------------------------------------NEW--------------------------------------------------'''

def member_search(surname: str, first_name: str, second_name: str, phone_main: str) -> str:
    sql_string = 'SELECT id FROM garage_member WHERE '
    if surname != '':
        sql_string = sql_string + 'surname LIKE \'%' + surname + '%\''
        if first_name != '' or second_name != '' or phone_main != '':
            sql_string += ' AND '
    if first_name != '':
        sql_string = sql_string + 'first_name LIKE \'%' + first_name + '%\''
        if second_name != '' or phone_main != '':
            sql_string += ' AND '
    if second_name != '':
        sql_string = sql_string + 'second_name LIKE \'%' + second_name + '%\''
        if phone_main != '':
            sql_string += ' AND '
    if phone_main != '':
        sql_string = sql_string + 'phone_main LIKE \'%' + phone_main + '%\''
    sql_string += ';'

    return sql_string


