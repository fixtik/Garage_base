import os

STANDART_PATH = ''
DEFAULT_DB_NAME = 'garage.db'
DEFAULT_VOA_IMG = 'photo/voa.png'

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
                                '   "comment" TEXT,' \
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
OBJ_TABLE = 'garage_obj'
ELECTRIC_TABLE = 'electric_meter'
MEMBER_TABLE = 'garage_member'
SIZE_TABLE = 'type_size'
CONTRIB_TYPE_TABLE = 'contribution_type'

OWNER_ID = 'owner_id'

CONTRIB_WIN_EDIT_TITLE = 'Редактирование типа платежа'

PHOTO_H = 100
PHOTO_W = 100
IMG_H = 200
IMG_W = 200
ELECTRIC_HEIGHT_ADD = 170

ERROR_TEXT_PLACE_NOT_FILL = 'Заполните все обязательные поля!'
ERROR_SQL_QWERY = 'Ошибка выполнения запроса'
ERROR_NO_BASE_CONNECT = 'Нет подключенной БД!'
ERROR_ADD_BASE_ERR = "Ошибка при добавлении записи в БД!"
ERROR_NO_OWNER = 'Не выбран собственник для объекта!'
ERROR_NO_SIZE = 'Не выбран размер объекта!'
ERROR_NO_DATA_OBJECT = 'Не заполнены данные об объекте!'
ERROR_TOO_MANY_METERS = 'На объекте могут быть установлены только по одному счетчику разных типов'
ERROR_METER_ALREADY_USE = "Данный счетчик уже используется на другом объекте. Проверьте правильность введенных данных"
ERROR_OBJECT_ALREADY_EXIST = 'Объект уже существует в БД!'
ERROR_MEMBER_ALREADY_EXIST = 'Пользователь с такими данными уже существует в БД! Проверьте правильность введенных ' \
                            'значений'
ERROR_SIZE_ALREADY_EXIST = 'Такой типоразмер уже есть в БД!'
ERROR_CONTRIB_TYPE_ALREADY_EXIST = 'Платеж с таким названием уже существует'

MESSAGE_CHECK_DATA = 'Проверьте корректность введенных данных'
MESSAGE_CHECK_DB_CONNECTIONS = 'Проверьте подключение к БД'

TITLE_SELECT_BD = "Выберите файл БД"
TITLE_EDIT_MODE = 'Редактирование'
ERROR_TITLE = "Ошибка!"

INFO_DATA_IS_EMPTY = "Данных не обнаружено"
INFO_NO_ELECTRIC_METER = 'Для данного объекта нет счетчика'
INFO_NO_ELECTRIC_METER_TO_ADD = 'Вы не ввели данные по электросчетчику! \n Хотите внести сейчас?'
INFO_NO_OBJECT = "Объекта не обнаружено"

INFO_TITLE = "Информация"
ATTANTION_TITLE = 'Внимание!'
ATTANTION_ACCEPT = 'Подтверждение действия'
INFO_SUCCESS_ADDED = 'Данные успешно добавлены в БД'
INFO_SUCCESS_CHANGED = 'Изменения успешно внесены в БД'

QUESTION_WRITE_EL_METER_WHITHOUT_OBJ = 'Хотите добавить запись без привязки к объекту?'
QUESTION_DELETE_TYPE_SIZE = "Вы уверены, что хотите удалить выбранный типоразмер гаража?"

TITLE_SELECT_PHOTO = "Выберите фото для загрузки"

FILTER_PHOTO = '*.jpg *.jpeg'
FILTER_BD = '*.db'

BTN_TEXT_ADD = 'Добавить'
BTN_TEXT_CHANGE = "Изменить"
BTN_TEXT_CHOOSE = "Выбрать"

LABLEL_TEXT_ADD_DBLCLCK = "Добавление - двойным кликом"

TITLE_ADD_NEW = "Режим добавления нового объекта"

DEFAULT_VALUE = '0'

DEFAULT_PHOTO_PASS = os.getcwd() + '\\photo\\member\\'  # os.getcwd() - возвращает текущую директорию
DEFAULT_BILLS_PASS = os.getcwd() + '\\photo\\bills\\'  # os.getcwd() - возвращает текущую директорию

WINDOW_TITLE_ADD_SIZE = 'Редактирование типоразмеров'

TYPE220 = 220
TYPE380 = 380
