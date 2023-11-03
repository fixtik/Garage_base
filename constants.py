import os

STANDART_PATH = ''
DEFAULT_DB_NAME = 'garage.db'



SQL_CREATE_TABLE_GARAGE = 'CREATE TABLE IF NOT EXISTS "garage_obj" ( ' \
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                          '	"num_row"	INTEGER NOT NULL,' \
                          '	"num_bild"	INTEGER NOT NULL,' \
                          '	"kadastr_num" TEXT,' \
                          '	"owner_id"	INTEGER NOT NULL,' \
                          '	"arendator_id"	TEXT,' \
                          '	"size_type_id"	INTEGER NOT NULL,' \
                          '	"create_year"	TEXT,' \
                          '	"electro220_id"	INTEGER DEFAULT 0,' \
                          '	"electro380_id"	INTEGER DEFAULT 0,' \
                          'FOREIGN KEY("owner_id") REFERENCES "garage_member"("id"),' \
                          'FOREIGN KEY("size_type_id") REFERENCES "type_size"("id")' \
                          ');'
# так как арендаторов может быть >1 => добавляем список id арендатора через пробел

SQL_CREATE_TABLE_GARGE_MEMBER = 'CREATE TABLE IF NOT EXISTS "garage_member" (' \
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                '	"surname"	TEXT NOT NULL,' \
                                '	"first_name"	TEXT NOT NULL,' \
                                '	"second_name"	TEXT,' \
                                '	"birth_date"	TEXT NOT NULL,' \
                                '	"address"	TEXT,' \
                                '	"phone_main"	TEXT NOT NULL,' \
                                '	"phone_sec"	TEXT,' \
                                '	"email"	TEXT,' \
                                '	"voa"	TEXT,' \
                                '	"active"	INTEGER DEFAULT 1,' \
                                '   "inactive_date"	TEXT,' \
                                '	"photo"	BLOB' \
                                ');'
# с фото подумать - может сделать локальную папку с фотками - имена=id пользователя

SQL_CREATE_TABLE_ELECTRIC_METER = 'CREATE TABLE IF NOT EXISTS "electric_meter" (' \
                                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                  '	"num_meter"	TEXT NOT NULL,' \
                                  '	"type"	INTEGER DEFAULT 220,' \
                                  '	"prev_day"	INTEGER DEFAULT 0,' \
                                  '	"prev_night"	INTEGER DEFAULT 0,' \
                                  '	"day"	INTEGER INTEGER DEFAULT 0,' \
                                  '	"night"	INTEGER INTEGER DEFAULT 0' \
                                  ');'
# добалено поле type для возможности различить по вольтажу

SQL_CREATE_TABLE_TYPE_SIZE = 'CREATE TABLE IF NOT EXISTS "type_size" (' \
                             'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                             '	"width"	REAL NOT NULL,' \
                             '	"len" REAL NOT NULL,' \
                             '	"height"	REAL NOT NULL,' \
                             '	"comment"	TEXT' \
                             ');'

SQL_CREATE_TABLE_CONTRIBUTION_TYPE = 'CREATE TABLE IF NOT EXISTS "contribution_type" (' \
                                     'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                     '	"name"	TEXT,' \
                                     '	"value"	REAL,' \
                                     '	"comment"	TEXT' \
                                     ');'

SQL_CREATE_TABLE_CONTRIBUTION = 'CREATE TABLE IF NOT EXISTS "contribution" (' \
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                '	"id_garage"	INTEGER NOT NULL,' \
                                '	"id_cont_type"	INTEGER NOT NULL,' \
                                '	"pay_date"	TEXT NOT NULL,' \
                                '	"period_pay"	TEXT NOT NULL,' \
                                '	"value"	REAL,' \
                                'FOREIGN KEY("id_garage") REFERENCES "garage_obj"("id"),' \
                                'FOREIGN KEY("id_cont_type") REFERENCES "contribution_type"("id")' \
                                ');'

SQL_CREATE_TABLE_AUTOMOBILE = 'CREATE TABLE IF NOT EXISTS "automobile" ( ' \
                              'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                              '	"mark"	TEXT NOT NULL,' \
                              '	"gos_num"	TEXT NOT NULL,' \
                              '	"owner_id"	INTEGER NOT NULL,' \
                              '	"active"	INTEGER DEFAULT 1,' \
                              '	"inactive_date"	TEXT DEFAULT 0,' \
                              'FOREIGN KEY("owner_id") REFERENCES "garage_member"("id")' \
                              ');'

BD_SQL_CREATOR = [SQL_CREATE_TABLE_GARGE_MEMBER, SQL_CREATE_TABLE_ELECTRIC_METER, SQL_CREATE_TABLE_TYPE_SIZE,
                  SQL_CREATE_TABLE_CONTRIBUTION_TYPE, SQL_CREATE_TABLE_GARAGE, SQL_CREATE_TABLE_CONTRIBUTION,
                  SQL_CREATE_TABLE_AUTOMOBILE]

TABALE_NAMES = ['contribution', 'garage_obj', 'automobile', 'garage_member',
                'contribution_type', 'electric_meter', 'type_size']
CAR_TABLE = 'automobile'
OWNER_ID = 'owner_id'


CONTRIB_WIN_EDIT_TITLE = 'Редактирование типа платежа'

PHOTO_H = 100
PHOTO_W = 100
ELECTRIC_HEIGHT_ADD = 170

ERROR_TEXT_PLACE_NOT_FILL = 'Запоните все обязательные поля!'
ERROR_SQL_QWERY = 'Ошибка выполнения запроса'
ERROR_NO_BASE_CONNECT = 'Нет подключенной БД!'
ERROR_ADD_BASE_ERR = "Ошибка при добавлении записи в БД!"
ERROR_NO_OWNER = 'Не выбран собственник для объекта!'
ERROR_NO_DATA_OBJECT = 'Не заполнены данные об объекте!'
ERROR_TOO_MANY_METERS = 'На объекте могут быть установлены только по одному счетчику разных типов'
TITLE_SELECT_BD = "Выберите файл БД"

INFO_DATA_IS_EMPTY = "Данных не обнаружено"
INFO_NO_ELECTRIC_METER = 'Для данного объекта нет счетчика'
INFO_NO_ELECTRIC_METER_TO_ADD = 'Вы не ввели данные по электросчетчику! \n ' \
                                'Хотите ли внести сейчас, или сделаете это позже?'
INFO_NO_OBJECT = "Объекта не обнаружено"

INFO_TITLE = "Информация"
ATTANTION_TITLE = 'Внимание!'
ATTANTION_ACCEPT = 'Подтверждение действия'
ERROR_TITLE = "Ошибка!"

QUESTION_WRITE_EL_METER_WHITHOUT_OBJ = 'Хотите добавить запись без привязки к объекту?'
QUESTION_DELETE_TYPE_SIZE = "Вы уверены, что хотите удалить выбранный типоразмер гаража?"

TITLE_SELECT_PHOTO = "Выберите фото для загрузки"

FILTER_PHOTO = '*.jpg *.jpeg'
FILTER_BD = '*.db'

BTN_TEXT_ADD = 'Добавить'
BTN_TEXT_CHANGE = "Изменить"

TITLE_ADD_NEW = "Режим добавления нового объекта"

DEFAULT_VALUE = '0'

DEFAULT_PHOTO_PASS = os.getcwd() + '\\photo\\member\\'  # os.getcwd() - возвращает текущую директорию
DEFAULT_BILLS_PASS = os.getcwd() + '\\photo\\bills\\'  # os.getcwd() - возвращает текущую директорию

WINDOW_TITLE_ADD_SIZE = 'Редактирование типоразмеров'

TYPE220 = 220
TYPE380 = 380