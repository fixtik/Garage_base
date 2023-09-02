STANDART_PATH = ''
DEFAULT_BD_NAME = 'garage.db'

SQL_CREATE_TABLE_GARAGE = 'CREATE TABLE "garage_obj" ( ' \
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                          '	"num_row"	INTEGER NOT NULL,' \
                          '	"num_bild"	INTEGER NOT NULL,' \
                          '	"owner_id"	INTEGER NOT NULL,' \
                          '	"arendator_id"	INTEGER,' \
                          '	"size_type_id"	INTEGER NOT NULL,' \
                          '	"create_year"	TEXT,' \
                          '	"electro_id"	INTEGER' \
                          ');'
SQL_CREATE_TABLE_GARGE_MEMBER = 'CREATE TABLE "garage_member" (' \
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                '	"surname"	TEXT NOT NULL,' \
                                '	"first_name"	TEXT NOT NULL,' \
                                '	"second_name"	TEXT NOT NULL,' \
                                '	"birth_date"	TEXT NOT NULL,' \
                                '	"adress"	TEXT,' \
                                '	"phone_main"	TEXT NOT NULL,' \
                                '	"phone_sec"	TEXT,' \
                                '	"email"	TEXT,' \
                                '	"voa"	TEXT,' \
                                '	"active"	INTEGER NOT NULL,' \
                                '	"photo"	BLOB' \
                                ');'
SQL_CREATE_TABLE_ELECTRIC_METER = 'CREATE TABLE "electric_meter" (' \
                                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                  '	"num_meter"	TEXT NOT NULL,' \
                                  '	"prev_day"	INTEGER,' \
                                  '	"prev_night"	INTEGER,' \
                                  '	"day"	INTEGER,' \
                                  '	"night"	INTEGER' \
                                  ');'
SQL_CREATE_TABLE_TYPE_SIZE = 'CREATE TABLE "type_size" (' \
                             'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                             '	"width"	REAL,' \
                             '	"length"	REAL,' \
                             '	"hight"	REAL,' \
                             '	"comment"	TEXT' \
                             ');'
SQL_CREATE_TABLE_CONTRIBUTION_TYPE = 'CREATE TABLE "contribution_type" (' \
                                     'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                     '	"name"	TEXT,' \
                                     '	"value"	REAL,' \
                                     '	"comment"	TEXT' \
                                     ');'
SQL_CREATE_TABLE_CONTRIBUTION = 'CREATE TABLE "contribution" (' \
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                '	"id_garage"	INTEGER NOT NULL,' \
                                '	"id_cont_type"	INTEGER NOT NULL,' \
                                '	"pay_date"	TEXT NOT NULL,' \
                                '	"period_pay"	TEXT NOT NULL,' \
                                '	"value"	REAL,' \
                                '	FOREIGN KEY("id_cont_type") REFERENCES "contribution_type",' \
                                '	FOREIGN KEY("id_garage") REFERENCES "garage_obj"' \
                                ');'