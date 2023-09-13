STANDART_PATH = ''
DEFAULT_DB_NAME = 'garage.db'



SQL_CREATE_TABLE_GARAGE = 'CREATE TABLE IF NOT EXISTS "garage_obj" ( ' \
                          'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                          '	"num_row"	INTEGER NOT NULL,' \
                          '	"num_bild"	INTEGER NOT NULL,' \
                          '	"kadastr_num" TEXT NOT NULL,' \
                          '	"owner_id"	INTEGER NOT NULL,' \
                          '	"arendator_id"	INTEGER,' \
                          '	"size_type_id"	INTEGER NOT NULL,' \
                          '	"create_year"	TEXT,' \
                          '	"electro_id"	INTEGER,' \
                          'FOREIGN KEY("owner_id") REFERENCES "garage_member"("id"),' \
                          'FOREIGN KEY("size_type_id") REFERENCES "type_size"("id"),' \
                          'FOREIGN KEY("electro_id") REFERENCES "electric_meter"("id")' \
                          ');'

SQL_CREATE_TABLE_GARGE_MEMBER = 'CREATE TABLE IF NOT EXISTS "garage_member" (' \
                                'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                '	"surname"	TEXT NOT NULL,' \
                                '	"first_name"	TEXT NOT NULL,' \
                                '	"second_name"	TEXT,' \
                                '	"birth_date"	TEXT NOT NULL,' \
                                '	"adress"	TEXT,' \
                                '	"phone_main"	TEXT NOT NULL,' \
                                '	"phone_sec"	TEXT,' \
                                '	"email"	TEXT,' \
                                '	"voa"	TEXT,' \
                                '	"active"	INTEGER NOT NULL,' \
                                '	"photo"	BLOB' \
                                ');'

SQL_CREATE_TABLE_ELECTRIC_METER = 'CREATE TABLE IF NOT EXISTS "electric_meter" (' \
                                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                                  '	"num_meter"	TEXT NOT NULL,' \
                                  '	"prev_day"	INTEGER DEFAULT 0,' \
                                  '	"prev_night"	INTEGER DEFAULT 0,' \
                                  '	"day"	INTEGER INTEGER DEFAULT 0,' \
                                  '	"night"	INTEGER INTEGER DEFAULT 0' \
                                  ');'

SQL_CREATE_TABLE_TYPE_SIZE = 'CREATE TABLE IF NOT EXISTS "type_size" (' \
                             'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                             '	"width"	REAL NOT NULL,' \
                             '	"len" REAL NOT NULL,' \
                             '	"hight"	REAL NOT NULL,' \
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
                          'FOREIGN KEY("owner_id") REFERENCES "garage_member"("id")' \
                              ');'

BD_SQL_CREATOR = [SQL_CREATE_TABLE_GARGE_MEMBER, SQL_CREATE_TABLE_ELECTRIC_METER, SQL_CREATE_TABLE_TYPE_SIZE,
                  SQL_CREATE_TABLE_CONTRIBUTION_TYPE, SQL_CREATE_TABLE_GARAGE, SQL_CREATE_TABLE_CONTRIBUTION,
                  SQL_CREATE_TABLE_AUTOMOBILE]