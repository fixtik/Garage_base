import sqlite3
import os
import datetime

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
def sql_add_electric_meter(num_meter: str, cur_day: int, cur_night: int = 0, pr_day: int = 0, pr_night: int = 0,
                           type: int = 220) -> str:
    """
    Запрос на добавление нового электросчетчика
    :param num_meter: номер электросчетчика
    :param cur_day: текущие дневные показания показания
    :param cur_night: текущие ночные показания (по умолчанию 0)
    :param pr_day: предыдущие дневные показания (по умолчанию 0)
    :param pr_night: предыдущие ночные показания (по умолчанию 0)
    :param type: тип счетчика
    :return: sql-запрос
    """
    return f'INSERT INTO electric_meter (num_meter, prev_day, prev_night,' \
           f' day, night, type) VALUES ("{num_meter}", {pr_day}, {pr_night}, {cur_day}, {cur_night}, {type});'


def sql_update_electric_meter_by_id(metr_id: int, cur_day: int, cur_night: int = 0) -> str:
    """
    Запрос на обновление текущих показаний счетчика по id-счетчика
    :param metr_id: id-счетчика
    :param cur_day: текущие дневные показания
    :param cur_night: :param cur_night: текущие ночные показания (по умолчанию 0)
    :return: sql-запрос
    """
    return f'UPDATE electric_meter SET ' \
           f'prev_day = (SELECT day FROM electric_meter WHERE id = {metr_id}), ' \
           f'prev_night =  (SELECT night FROM electric_meter WHERE id = {metr_id}), ' \
           f'day = {cur_day}, night = {cur_night} ' \
           f'WHERE id = {metr_id};'


def sql_get_metr_id_by_num(num_metr: str, type: str = 220) -> str:
    """
    Запрос на получение id счетчика по номеру счетчика
    :param num_metr: номер-счетчика
    :param type: тип счетчика
    :return: sql-запрос
    """
    return f'SELECT id FROM electric_meter WHERE num_meter = "{num_metr}" and type = {type};'


def sql_get_consumed_energi_by_id(metr_id: int) -> str:
    """
    Получение данных по потребленной электроэнергии
    :param metr_id: id счетчика
    :return: sql-запрос
    """
    return f'SELECT day - prev_day, night - prev_night FROM electric_meter WHERE id = {metr_id}'


# запросы на типоразмер
def sql_add_new_type_size(width: float = 4.5, len: float = 6, hight: float = 3.2, comment: str = '') -> str:
    """
    Запрос на добавление нового типоразмера объекта недвижимости
    :param width: ширина объекта (4,5 метра по умолчнанию)
    :param len: длина объекта (6 метров по умолчнанию)
    :param hight: высота объекта (3.2 метра по умолчнанию)
    :return: sql-запрос
    """
    return f'INSERT INTO type_size (width, len, hight, comment) VALUES ({width}, {len}, {hight}, {comment});'


def get_type_size_id_by_size(width: float, len: float, height: float) -> str:
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


def sql_add_new_contrib(id_garage: str, id_cont: str, pay_date: str, pay_kind: int, value: float,
                        comment: str = '', check_photo: str = '') -> str:
    """
    формирование запроса для добавления платежа в БД
    """
    return f"INSERT INTO contribution (id_garage, id_cont_type, pay_date, pay_kind, value, comment, check_photo) " \
           f"VALUES " \
           f"({id_garage}, {id_cont}, '{pay_date}', '{pay_kind}', {value}, '{comment}','{check_photo}');"


def sql_full_update_contrib(cont_id: str, id_garage: str, id_cont: str, pay_date: str,
                            value: float, pay_kind: int,  comment: str = '', check_photo: str = '') -> str:
    """
    формирование запроса для добавления платежа в БД (pay_kind = 1 если нал, 2 - безнал)
    """
    return f"UPDATE contribution SET id_garage={id_garage}, id_cont_type = {id_cont}, pay_date = '{pay_date}', " \
           f" pay_kind = {pay_kind}, value = {value}, comment = '{comment}', check_photo ='{check_photo}' " \
           f"WHERE id = {cont_id};"


def sql_update_contrib_type(contrib_id: int, value: float, pay_kind: int,
                            comment: str = '', check_photo: str = '') -> str:
    """
    обновление заначений полей по id
    """
    return f"UPDATE contribution_type SET value = {value}, pay_kind = {pay_kind}, " \
           f"comment = '{comment}', check_photo ='{check_photo}' WHERE id = {contrib_id};"


# запросы по членам кооператива
def sql_add_new_member(surname: str, first_name: str, birth_date: str, phone_main: str, voa: str,
                       second_name: str = '', address: str = '', second_phone: str = '',
                       email: str = '', photo='') -> str:
    """
    Добавление нового члена кооператива или арендатора
    :param surname: фамилия
    :param first_name: имя
    :param birth_date: дата рождения
    :param phone_main: основной номер телефона
    :param voa: направление ВОА
    :param second_name: отчество (необязательно)
    :param address: адрес проживания (необязательно)
    :param second_phone: запасной телефон (необязательно)
    :param email: адрес электронной почты (необязательно)
    :param photo: фотография (необязательно)
    :return: sql-запрос
    """
    return f"INSERT INTO garage_member (surname, first_name, second_name, birth_date, phone_main," \
           f" phone_sec, address, email, voa, photo) VALUES ('{surname}', '{first_name}', '{second_name}', '{birth_date}', " \
           f"'{phone_main}', '{second_phone}', '{address}', '{email}', '{voa}', '{photo}');"


def sql_get_all_active(table_name: str) -> str:
    """
    возвращает одну запись по id
    """
    return f"SELECT * FROM {table_name} WHERE active = 1;"


# универсальные запросы
def sql_select_all_from_table(table_name: str) -> str:
    """выбор всех значений в таблице table_name"""
    return f"SELECT * FROM {table_name};"


def sql_get_one_record_by_id(table_name: str, id: int) -> str:
    """
    возвращает одну запись по id
    """
    return f"SELECT * FROM {table_name} WHERE id = {id};"


def sql_select_all_by_field_value(table_name: str, field_name: str, value: list) -> str:
    """
    возвращает записи по значению поля
    """
    return f"SELECT * FROM {table_name} WHERE {field_name} IN ({value});"


def sql_select_id_by_field_value(table_name: str, field_name: str, value: str) -> str:
    """
    возвращает записи по значению поля
    """
    return f"SELECT id FROM {table_name} WHERE {field_name} = '{value}';"


def sql_update_field_by_table_name_and_id(table_name: str, rec_id: int, field: str, new_value) -> str:
    """
    Обновление значения любого из полей по id-записи
    :param table_name: имя таблицы
    :param rec_id: id типоразмера
    :param place: имя изменяемого поля
    :param new_value: новое значение
    :return: sql-запрос
    """
    return f'UPDATE {table_name} SET {field} = "{new_value}" WHERE id={rec_id};'


def sql_delete_rec_by_table_name_and_id(table_name: str, rec_id: str) -> str:
    """
    удаление записи по имени таблицы и id
    :param table_name: имя таблицы
    :param rec_id: список удаляемых id через ,
    :return: sql-запрос
    """
    return f'DELETE FROM {table_name} WHERE id IN ({rec_id});'


def drop_table_by_name(table_name: str) -> str:
    """
    Удаление таблицы по имени
    :param table_name: имя таблицы
    :return: sql-запрос
    """
    return f'DROP TABLE IF EXISTS {table_name};'


# автомобильные запросы
def sql_add_new_car(mark: str, gos_num: str, owner_id: int) -> str:
    """
    Добавление нового автомобиля привязанного к id владельца
    :param mark: марка автомобиля
    :param gos_num: номер автомобиля
    :param owner_id: id влядельца автомобиля
    :return: sql-запрос
    """
    return f'INSERT INTO automobile (mark, gos_num, owner_id, active) VALUES ("{mark}", "{gos_num}", "{owner_id}", "1");'


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


def sql_update_car_by_id(id: str, new_mark: str, new_gos_num: str) -> str:
    """
    Обновление марки и номера машины по id авто
    :param id: id авто
    :param new_mark: новая марка автомобиля
    :param new_gos_num: новый гос номер автомобиля
    :return: sql-запрос
    """
    return f"UPDATE automobile SET mark = '{new_mark}', gos_num = '{new_gos_num}'" \
           f"WHERE id = {id};"


def sql_set_inactive_car_by_id(id: str) -> str:
    """
    Перевод в неактивное состояние автомобиля по его id
    :param gos_num: номер владельца автомобиля
    :return: sql-запрос
    """
    return f'UPDATE  automobile ' \
           f'SET active = 0, inactive_date = date() ' \
           f'WHERE id = {id};'


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
    return f"SELECT owner_id FROM automobile WHERE gos_num = '{gos_num}';"


def sql_get_car_by_own_id(own_id: str, active='1') -> str:
    """
    Вывод всех активных авто одного пользователя
    :param own_id: id владельца авто
    :param active: актуальное авто (1), архивное авто (0)
    :return: sql-запрос
    """
    return f"SELECT * FROM automobile WHERE owner_id = '{own_id}'and active = {active};"


def sql_select_garaje_id_by_num_and_row(garage_num: int, row: int) -> str:
    """
    Поиск id гаража по номеру и ряду
    """
    return f'SELECT id FROM garage_obj WHERE num_bild = {garage_num} and num_row = {row};'


def sql_update_garage_member(id: str, surname: str, first_name: str, birth_date: str, phone_main: str, voa: str,
                             second_name: str = '', address: str = '', second_phone: str = '',
                             email: str = '', photo: str = '') -> str:
    """
    Редактирование члена кооператива или арендатора
    :param id: идетификатор члена, которого редактируем
    :param surname: фамилия
    :param first_name: имя
    :param birth_date: дата рождения
    :param phone_main: основной номер телефона
    :param voa: направление ВОА
    :param second_name: отчество (необязательно)
    :param address: адрес проживания (необязательно)
    :param second_phone: запасной телефон (необязательно)
    :param email: адрес электронной почты (необязательно)
    :param photo: фото-путь (необязательно)
    :return: sql-запрос
    """
    return f"UPDATE garage_member SET surname = '{surname}', first_name = '{first_name}', second_name = '{second_name}'," \
           f" birth_date = '{birth_date}', phone_main = '{phone_main}', phone_sec = '{second_phone}', " \
           f"address = '{address}', email = '{email}', voa = '{voa}', photo = '{photo}' WHERE id={id};"


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


def sql_add_new_garage_size(width: float, length: float, height: float, cont_value: float, comment: str = ' ') -> str:
    '''
    Добавление размеров гаража
    :param width: ширина
    :param len: длина
    :param height: высота
    :param cont_value: сумма платежа
    :param comment: комментарий
    :return: sql-запрос
    '''
    return f'INSERT INTO type_size (width, len, height, cont_value, comment) VALUES ({width}, {length}, {height}, ' \
           f'{cont_value}, "{comment}");'


def sql_update_garage_size(size_id: int, width: float, length: float, height: float, cont_value: float,
                           comment: str = ' ') -> str:
    '''
    Запрос на поиск id по типоразмерам
    :param width: ширина
    :param len: длина
    :param height: высота
    :param comment: комментарий
    :return: sql-запрос
    '''
    return f"UPDATE type_size SET width = {width}, len = {length}, height = {height}, cont_value = {cont_value}, comment = '{comment}'" \
           f" WHERE id = {size_id};"


def sql_member_search(surname: str = '', first_name: str = '', second_name: str = '', phone_main: str = '') -> str:
    """Возвращает запрос для вывода всех пользователей по части входных данных"""
    sql_string = 'SELECT * FROM garage_member WHERE '
    if surname:
        sql_string += f"surname LIKE '%{surname}%'"
        if first_name or second_name or phone_main:
            sql_string += ' AND '
    if first_name:
        sql_string += f"first_name LIKE '%{first_name}%'"
        if second_name or phone_main:
            sql_string += ' AND '
    if second_name:
        sql_string += f"second_name LIKE '%{second_name}%'"
        if phone_main:
            sql_string += ' AND '
    if phone_main:
        sql_string += f"phone_main LIKE '%{phone_main}%'"
    sql_string += ';'

    return sql_string


def sql_get_members_by_ogject(row: int = 0, number: int = 0) -> str:
    """
    формирование запроса на получения списка id собственников и арендаторов
    по номеру объекта недвижимости
    """
    sql_string = 'SELECT owner_id, arendator_id FROM garage_obj WHERE '
    if row:
        sql_string += f'num_row={row}'
        sql_string += ' AND ' if number else ''
    sql_string += f'num_bild={number}' if number else ''
    return sql_string


def sql_get_member_by_id_set(ids: str) -> str:
    """формирование запроса на получение данных пользователей по списку id (только активные)"""
    return f'SELECT * FROM garage_member WHERE id IN ({ids}) AND active = 1'


def sql_select_cars_and_own_info_by_owner_id(ids: str):
    """запрос на выборку инфо об авто с данными собственника"""
    return f"SELECT a.id, a.mark, " \
           f" a.gos_num, " \
           f" garage_member.surname, " \
           f" garage_member.first_name, " \
           f" garage_member.second_name, " \
           f" garage_member.phone_main " \
           f" FROM automobile as a " \
           f" INNER JOIN garage_member ON garage_member.id = a.owner_id" \
           f" WHERE a.active = 1 and garage_member.id IN ({ids});"


def sql_gos_num_search(mark: str = '', gos_num: str = '', active: int = 1) -> str:
    """Возвращает запрос для вывода автомобилей по номеру или марке"""
    sql_string = f'SELECT * FROM automobile WHERE active = "{active}" AND '
    if mark:
        sql_string += f"mark LIKE '%{mark}%'"
        if gos_num:
            sql_string += ' AND '
    if gos_num:
        sql_string += f"gos_num LIKE '%{gos_num}%'"
    sql_string += ';'

    return sql_string


# --------------------------------------
# запросы по гаражу
def sql_add_new_garage(row: str, num: str, ownder_id: str, size_id: str, cr_year: str,
                       arenda_ids: str = '', kadastr: str = '', e220: str = '0', e380: str = '0') -> str:
    """
    Формаирование запроса на добавление нового гаража
    :param row: ряд
    :param num: номер
    :param ownder_id: идентификатор собственника
    :param size_id: идентификатор размера
    :param cr_year: год постройки
    :param arenda_ids: список через пробел идентификаторов арендаторов
    :param kadastr: кадастровый номер
    :param e220: идентификатор счетчика 220 В
    :param e380: идентификатор счетчика 380 В1
    :return: sql-запрос
    """
    return f"INSERT INTO garage_obj (num_row, num_bild, kadastr_num, owner_id, arendator_id, size_type_id, " \
           f"create_year, electro220_id, electro380_id) VALUES ({row}, {num}, '{kadastr}', {ownder_id}, " \
           f"'{arenda_ids}', {size_id}, '{cr_year}', {e220}, {e380});"


def sql_full_update_garage(object_id: str, row: str, num: str, ownder_id: str, size_id: str, cr_year: str,
                           arenda_ids: str = '', kadastr: str = '', e220: str = '0', e380: str = '0') -> str:
    """
    Формаирование запроса на изменение данных гаража
    :param object_id: id редактируемого объекта
    :param row: ряд
    :param num: номер
    :param ownder_id: идентификатор собственника
    :param size_id: идентификатор размера
    :param cr_year: год постройки
    :param arenda_ids: список через пробел идентификаторов арендаторов
    :param kadastr: кадастровый номер
    :param e220: идентификатор счетчика 220 В
    :param e380: идентификатор счетчика 380 В1
    :return: sql-запрос
    """
    return f"UPDATE garage_obj SET num_row = {row}, " \
           f"num_bild = {num}, kadastr_num = '{kadastr}', owner_id = {ownder_id}, arendator_id = '{arenda_ids}', " \
           f"size_type_id = {size_id}, create_year ='{cr_year}', electro220_id = {e220}, electro380_id = {e380} " \
           f"WHERE id = {object_id} ;"


def sql_get_all_objects_for_list_by_row_and_num(row: str = '', num: str = ''):
    """
    Формирование запроса на вывод данных из БД в таблицу главного окна
    :param row: ряд объекта
    :param num: номер объекта
    :return: sql-запрос в зависимости от переданных значений
    """
    sql = f'SELECT garage_obj.id, garage_obj.num_row, garage_obj.num_bild, garage_member.surname,' \
          f'garage_member.first_name, garage_member.second_name, garage_member.phone_main, garage_obj.kadastr_num ' \
          f' FROM garage_obj INNER JOIN garage_member ON garage_member.id = garage_obj.owner_id '
    if row and not num:
        sql += f"WHERE garage_obj.num_row = {row} "
    elif not row and num:
        sql += f"WHERE garage_obj.num_bild = {num} "
    elif row and num:
        sql += f"WHERE garage_obj.num_row = {row} and garage_obj.num_bild = {num} "
    sql += f'ORDER BY garage_obj.num_row ASC, garage_obj.num_bild;'
    return sql


def sql_select_contrib_by_object_id(object_id: str) -> str:
    """Запрос на выдачу всех платежей для конкретного гаража"""

    return f"SELECT contribution.id, contribution_type.name, contribution.pay_date, " \
           f" contribution.value, contribution.comment, contribution.pay_kind ,contribution.check_photo" \
           f" FROM main.garage_obj " \
           f" INNER JOIN contribution ON garage_obj.id = contribution.id_garage " \
           f" INNER JOIN contribution_type ON contribution_type.id = contribution.id_cont_type " \
           f" WHERE garage_obj.id = {object_id} " \
           f" ORDER BY contribution.id DESC;"


def sql_find_id_by_filds(*args, table_name: str) -> str:
    """
    Запрос на поиск id записи по полям
    :param args: кортеж (<имя поля> <значение>)
    :param table_name: имя таблицы для поиска
    """
    if args:
        sql = f"SELECT id FROM {table_name} WHERE "
        for i, item in enumerate(args):
            sql += f"{item[0]} = {item[1]}" if str(item[1]).isdigit() else f"{item[0]} = '{item[1]}'"
            if i + 1 < len(args):
                sql += ' AND '
            else:
                sql += ';'
        return sql

    return None


def sql_check_column_exists_in_table(table_name: str, column_name: str) -> str:
    """
    Запрос на проверку наличия поля в таблице
    :param table_name: имя таблицы
    :param column_name: имя поля
    :return: sql-запрос
    """
    return f"SELECT COUNT(*) AS CNTREC FROM pragma_table_info('{table_name}') WHERE name='{column_name}'"


def sql_add_new_meter_payment(type: str = '', value_day: float = 0, value_night: float = 0) -> str:
    return (f'INSERT INTO meter_payment (type, value_day, value_night) '
            f'VALUES ("{type}", {value_day}, {value_night});')


def sql_update_meter_payment(type: str = '', value_day: float = 0, value_night: float = 0) -> str:
    return f"UPDATE meter_payment SET value_day = {value_day}, value_night = {value_night}'" \
           f" WHERE type = '{type}';"


def sql_add_new_object_account(obj_id: int, current_debt: float = 0, calculation: float = 0, balance: float = 0) -> str:
    return (f'INSERT INTO object_account (obj_id, current_debt, calculation, balance) '
            f'VALUES ({obj_id}, {current_debt}, {calculation}, {balance});')


def sql_update_object_account(obj_id: int, current_debt: float = 0, calculation: float = 0,
                              balance: float = 0) -> str:
    return f"UPDATE object_account SET current_debt = {current_debt}, calculation = {calculation}, balance = {balance}" \
           f" WHERE obj_id = {obj_id};"

def sql_select_obj_account_by_object_id(object_id: str) -> str:
    """Запрос на выдачу текущего состояния счета объекта"""
    return f"SELECT * FROM object_account WHERE obj_id = {object_id};"

# тарифы на ЭЭ
def sql_get_current_tarif(meter_type: str):
    """Запрос на получение актуальных тарифов на счетчик"""
    return f"SELECT * FROM meter_payment WHERE type_meter = {meter_type};"

def sql_set_current_tarif(meter_type: str, value_day: str = 0, value_night: str = 0):
    """Запрос на установку актуальных тарифов на счетчик"""
    return f"UPDATE meter_payment SET value_day = {value_day}, " \
                                 f"value_night = {value_night} " \
                            f"WHERE type_meter = {meter_type};"

def sql_add_current_tarif(meter_type: str, value_day: str = 0, value_night: str = 0):
    """Запрос на добавление записи для счетчика"""
    return f"INSERT INTO meter_payment (type_meter, value_day, value_night) VALUES ({meter_type}, {value_day}," \
           f" {value_night}); "

def sql_add_new_members_contrib(size_id: int, value: float, year: int):
    """Запрос на внесение годового членского взноса"""
    return f"INSERT INTO members_contrib (size_id, value, year, date_add) VALUES " \
           f"({size_id}, {value}, {year}, '{datetime.datetime.now().isoformat()}');"

def sql_biling_members_contrib(year: int):
    """Запрос на установку даты выставления счета"""
    return f"UPDATE INTO members_contrib SET date_biling = '{datetime.datetime.now().isoformat()}' WHERE year = {year};"

def sql_get_value_members_contrib(size_id: int, year: int):
    """запрос на получение значений размеров платежа по типоразмеру объекта за определенный год"""
    return f"SELECT value FROM members_contrib WHERE size_id = {size_id} and year = {year};"

def sql_update_value_members_contrib(size_id: int, value: float, year: int):
    """Запрос на установку новго значения счета (при условии, что счет еще не был выставлен ранее)"""
    return  f"UPDATE INTO members_contrib SET value = {value}, date_add = '{datetime.datetime.now().isoformat()}' " \
            f"WHERE year = {year} and size_id = {size_id} and date_biling ='0';"
