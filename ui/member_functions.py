import os
import shutil
from dataclasses import dataclass

import constants
import db_work
import sqlite_qwer
import ui.dialogs
import ui.find_user
import ui.new_member
import ui.validators
import ui.car_functions
from ui.tableView_Models import *


class Member_front(QtWidgets.QWidget):

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = ui.new_member.Ui_Form()
        self.ui.setupUi(self)

        self.photoPath = None  # путь к фото
        self.db = db  # сслыка на объект БД
        self.member = Member()  #
        self.car = CarInfo
        self.parentForm = None  # сслыка на форму вызова для возвращения добавленных объектов
        self.addCar_form = None

        self.initUi()


    def initUi(self):

        self.resize(self.width(), 220)
        # слоты
        self.ui.photo_pushButton.clicked.connect(self.choosePhoto)
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.add_pushButton.clicked.connect(self.addPushBtnClk)
        self.ui.memberCarAdd_pushButton.clicked.connect(self.showAddCarForm)
        # валидаторы
        self.ui.phone_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.addPhone_lineEdit.setValidator(ui.validators.onlyNumValidator())

        self.carInDbModel = CarTableViewModel()
        self.ui.autoMember_tableView.setModel(self.carInDbModel)

    def showAddCarForm(self):
        """открытие формы добавления авто"""
        self.addCar_form = ui.car_functions.Car_frontend(self.db)
        self.addCar_form.mainForm = self
        self.addCar_form.show()

    def choosePhoto(self):
        """выбор фото на карточку"""
        img_path = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_PHOTO, constants.FILTER_PHOTO)[0]
        if img_path:
            pix = QtGui.QPixmap(img_path)
            pix = pix.scaled(constants.PHOTO_W, constants.PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.photo_label.setPixmap(pix)
            self.photoPath = img_path  # todo здесь продумать как хранить фото: в БД или в отдельном каталоге, где имя файла = id пользователя
            # во втором случае - написать функцию копирования файла в директорию после присвоения записи id

    def addToBase(self):
        """Добавление записи о пользователе в базу"""
        if self.db:
            if self.member.name and self.member.surname and self.member.birthday and self.member.phone \
                    and self.member.address:
                self.db.execute(sqlite_qwer.sql_add_new_member(surname=self.member.surname,
                                                               first_name=self.member.name,
                                                               second_name=self.member.secondName,
                                                               birth_date=self.member.birthday,
                                                               phone_main=self.member.phone,
                                                               second_phone=self.member.additPhone,
                                                               email=self.member.email,
                                                               voa=self.member.voa,
                                                               address=self.member.address,
                                                               photo=self.photoPath))
                self.member.id = self.db.cursor.lastrowid
                print(self.member.id)
                cars = self.carInDbModel.returnItems()
                for car in cars:
                    self.db.execute(sqlite_qwer.sql_add_new_car(mark=str(car.mark),
                                                                gos_num=str(car.gos_num),
                                                                owner_id=int(self.member.id)))
                self.clearLineEdits()
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)

    def clearLineEdits(self):
        """Очистка формы"""
        self.ui.surname_lineEdit.clear()
        self.ui.name_lineEdit.clear()
        self.ui.secondName_lineEdit.clear()
        self.ui.dateBirdth_dateEdit.clear()
        self.ui.phone_lineEdit.clear()
        self.ui.addPhone_lineEdit.clear()
        #self.ui.email_lineEdit.clear()
        #self.ui.voa_lineEdit.clear()
        self.ui.address_lineEdit.clear()

    def move_photo(self):
        '''Перемещение фото в директорию'''
        if not os.path.isdir(constants.DEFAULT_PHOTO_PASS):  # Проверяем создана директория или нет.
            os.makedirs(constants.DEFAULT_PHOTO_PASS, mode=0o777)  # Создаем директорию.
        if self.photoPath is not None:
            shutil.copy(self.photoPath, constants.DEFAULT_PHOTO_PASS + str(
                self.db.cursor.lastrowid) + '.jpg')  # Перемещаем фотографию и сразу переименовываем
            # Обновляем путь в бд после переноса фотографии
            self.db.execute(sqlite_qwer.sql_update_field_by_table_name_and_id('garage_member',
                                                                              self.db.cursor.lastrowid,
                                                                              'photo',
                                                                              constants.DEFAULT_PHOTO_PASS + str(
                                                                                  self.db.cursor.lastrowid) + '.jpg'))

    def addPushBtnClk(self):

        """Проверка данных при нажатии 'Добавить' """
        self.member.surname = self.ui.surname_lineEdit.text()
        self.member.name = self.ui.name_lineEdit.text()
        self.member.secondName = self.ui.secondName_lineEdit.text()
        self.member.birthday = self.ui.dateBirdth_dateEdit.date().toPython()
        self.member.phone = self.ui.phone_lineEdit.text()
        self.member.additPhone = self.ui.addPhone_lineEdit.text()
        #self.member.email = self.ui.email_lineEdit.text()
        #self.member.voa = self.ui.voa_lineEdit.text()
        self.member.address = self.ui.address_lineEdit.text()
        self.addToBase()
        self.move_photo()
        # смотрим, кто вызывал
        if isinstance(self.parentForm, FindMember_front):
            userInfo = User_Info(self.member)
            self.parentForm.userModel.setItems(userInfo)
            self.close()


class FindMember_front(QtWidgets.QWidget):
    TB_NAME = 'garage_member'

    def __init__(self, db: db_work.Garage_DB, main_form: QtWidgets.QWidget, parent=None):
        super().__init__(parent)
        self.ui = ui.find_user.Ui_Form()
        self.ui.setupUi(self)

        self.db = db  # сслыка на объект БД
        self.member = Member()  #
        self.parentForm = main_form  # сслыка на форму вызова для возвращения добавленных объектов
        self.addForm = None  # ссылка на добавление нового члена
        self.addIdsUsers = []  # список id добавляемых пользователей

        self.initUi()

    def initUi(self):

        self.resize(self.width(), 220)
        # слоты
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.user_radioButton.clicked.connect(self.setEnableds)
        self.ui.object_radioButton.clicked.connect(self.setEnableds)
        self.ui.add_pushButton.clicked.connect(self.addNewMemberPshBtn)
        self.ui.userList_tableView.doubleClicked.connect(self.addToResultTable)
        self.ui.choose_pushButton.clicked.connect(self.addToMainForm)

        # модель для результирующей таблицы
        self.userModel = UsersTableViewModelLite()
        self.ui.result_tableView.setModel(self.userModel)

        # модель для юзерлист
        self.userListModel = UsersTableViewModelLite()
        self.ui.userList_tableView.setModel(self.userListModel)
        self.ui.userList_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Автоматичкская подгонка столбцов по ширине
        self.ui.userList_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                           ResizeToContents)
        self.ui.result_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                         ResizeToContents)

        self.ui.object_radioButton.click()
        self.getUsersListFromDB()

        # моментальное обновление userList_tableView после ввода символов
        self.ui.surname_lineEdit.textChanged.connect(self.liveUpdateRequest)
        self.ui.name_lineEdit.textChanged.connect(self.liveUpdateRequest)
        self.ui.secondName_lineEdit.textChanged.connect(self.liveUpdateRequest)
        self.ui.phone_lineEdit.textChanged.connect(self.liveUpdateRequest)
        self.ui.number_lineEdit.textChanged.connect(self.liveUpdateRequest)
        self.ui.row_lineEdit.textChanged.connect(self.liveUpdateRequest)

    def liveUpdateRequest(self):
        """Заполнение таблицы существующих пользователей из БД"""
        if not (self.ui.surname_lineEdit.text() or self.ui.name_lineEdit.text() or self.ui.secondName_lineEdit.text() or
                self.ui.phone_lineEdit.text() or self.ui.row_lineEdit.text() or self.ui.number_lineEdit.text()):
            self.getUsersListFromDB()
        else:
            # готовим запрос исходя из выбора пользователя
            if self.ui.user_radioButton.isChecked():  # поиск по введенным данным пользователя
                sql = sqlite_qwer.sql_member_search(self.ui.surname_lineEdit.text(),
                                                    self.ui.name_lineEdit.text(),
                                                    self.ui.secondName_lineEdit.text(),
                                                    self.ui.phone_lineEdit.text())

            if self.ui.object_radioButton.isChecked():  # поиск по номеру объекта
                sql = sqlite_qwer.sql_get_members_by_ogject(row=self.ui.row_lineEdit.text(),
                                                            number=self.ui.number_lineEdit.text())
                # получаем все id пользователей
                if self.db.execute(sql) and self.db.cursor:
                    records = self.db.cursor.fetchall()
                    ids = []
                    for rec in records:
                        ids.append(rec[0])
                        if len(rec) > 1: ids.extend([int(i) for i in rec[1].split()])
                    # теперь получаем всех пользователей по id из списка:
                    if not ids:
                        self.userListModel.resetData()
                        return  # если в базе нет записей для этого ряда или номера
                    sql = sqlite_qwer.sql_get_member_by_id_set(ids)

            if self.db.execute(sql) and self.db.cursor:

                users = self.db.cursor.fetchall()
                self.userListModel.resetData()
                self.ui.userList_tableView.clearSpans()
                for user in users:
                    us_info = User_Info(user[0], f'{user[1]} {user[2]} {user[3]}', user[4], user[6], user[7])
                    self.userListModel.setItems(us_info)

    def setEnableds(self):
        """устанавливает или запрещает доступ к объектам интерфейса в зависимости от radioButton"""
        flag_user = self.ui.user_radioButton.isChecked()
        flag_obj = self.ui.object_radioButton.isChecked()
        # закрываем или открываем поиск по объекту
        self.ui.row_lineEdit.setEnabled(flag_obj)
        self.ui.number_lineEdit.setEnabled(flag_obj)
        # закрываем или открываем поиск по пользователю
        self.ui.surname_lineEdit.setEnabled(flag_user)
        self.ui.name_lineEdit.setEnabled(flag_user)
        self.ui.secondName_lineEdit.setEnabled(flag_user)
        self.ui.phone_lineEdit.setEnabled(flag_user)

    def addNewMemberPshBtn(self):
        """открытие формы добавления нового члена в БД"""
        if not self.addForm:
            self.addForm = Member_front(self.db)
            self.addForm.parentForm = self
            self.addForm.show()
        else:
            self.addForm.destroy()
            self.addForm = None
            self.addNewMemberPshBtn()

    def getUsersListFromDB(self):
        """Заполнение таблицы существующих пользователей из БД"""
        if self.db:
            if self.db.execute(sqlite_qwer.sql_get_all_active(self.TB_NAME)) and self.db.cursor:
                users = self.db.cursor.fetchall()
                for user in users:
                    us_info = User_Info(user[0], f'{user[1]} {user[2]} {user[3]}', user[4], user[6], user[7])
                    self.userListModel.setItems(us_info)

    def addToResultTable(self):
        """Отработка двойного клика на таблице со списком всех пользователей"""
        rows = {index.row() for index in self.ui.userList_tableView.selectionModel().selectedIndexes()}
        for row in rows:
            row_data = []
            for column in range(self.ui.userList_tableView.model().columnCount()):
                index = self.ui.userList_tableView.model().index(row, column)
                row_data.append(index.data())
        if row_data[0] in self.addIdsUsers:  # если уже добавлялся - выходим
            return
        self.addIdsUsers.append(row_data[0])
        self.userModel.setItems(User_Info(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4]))

    def addToMainForm(self):
        if self.addIdsUsers and self.db:
            ids = [str(i) for i in self.addIdsUsers]
            ids = ",".join(ids)
            if self.db.execute(sqlite_qwer.sql_get_member_by_id_set(ids)) and self.db.cursor:
                users = self.db.cursor.fetchall()
                for user in users:
                    us_info = User_Info(user[0], f'{user[1]} {user[2]} {user[3]}', user[4], user[6], user[7])
                    self.parentForm.userModel.setItems(us_info)
                    self.parentForm.addRadioButtonToUsersTable()
                self.close()
                return
        ui.dialogs.onShowError(self, constants.ATTANTION_TITLE, constants.INFO_DATA_IS_EMPTY)


@dataclass
class Member():
    """Поля для БД на каждого члена"""
    id: str = None
    surname: str = None
    name: str = None
    secondName: str = ''
    birthday: str = None
    address: str = None
    phone: str = None
    additPhone: str = ''
    email: str = ''
    voa: str = ''

@dataclass
class CarInfo:
    """Класс с инфорамцией об авто"""
    id: str = ''
    own_id: str = ''
    mark: str = ''
    gos_num: str = ''
    owner_id: str = ''
    active: str = ''
    inactive_date: str = ''

@dataclass
class User_Info():
    """Класс для описания пользователя в табличку Карточка объекта"""
    id: str = ''
    fio: str = ''
    brDay: str = ''
    phone: str = ''
    addPhone: str = ''
    role = ''  # todo придумать механизм привязки роли (?) может через отдельный запрос к БД
