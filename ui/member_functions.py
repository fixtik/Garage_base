import os
import shutil

import constants
import db_work
import sqlite_qwer
import ui.dialogs
import ui.find_user
import ui.new_member
import ui.validators
from ui.tableView_Models import *


class Member_front(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.new_member.Ui_Form()
        self.ui.setupUi(self)

        self.photoPath = None   # путь к фото
        self.db = None          # сслыка на объект БД
        self.member = Member()  #
        self.parentForm = None  # сслыка на форму вызова для возвращения добавленных объектов

        self.initUi()


    def initUi(self):

        self.resize(self.width(), 220)
        #слоты
        self.ui.photo_pushButton.clicked.connect(self.choosePhoto)
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.add_pushButton.clicked.connect(self.addPushBtnClk)
        #валидаторы
        self.ui.phone_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.addPhone_lineEdit.setValidator(ui.validators.onlyNumValidator())



    def choosePhoto(self):
        """выбор фото на карточку"""
        img_path = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_PHOTO, constants.FILTER_PHOTO)[0]
        if img_path:
            pix = QtGui.QPixmap(img_path)
            pix = pix.scaled(constants.PHOTO_W, constants.PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.photo_label.setPixmap(pix)
            self.photoPath = img_path # todo здесь продумать как хранить фото: в БД или в отдельном каталоге, где имя файла = id пользователя
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
                                                               adress=self.member.address,
                                                               photo=self.photoPath))
                self.member.id = self.db.cursor.lastrowid
                self.clearLineEdits()
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)


    def clearLineEdits(self):
        self.ui.surname_lineEdit.clear()
        self.ui.name_lineEdit.clear()
        self.ui.secondName_lineEdit.clear()
        self.ui.dateBirdth_dateEdit.clear()
        self.ui.phone_lineEdit.clear()
        self.ui.addPhone_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.voa_lineEdit.clear()
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
        self.member.email = self.ui.email_lineEdit.text()
        self.member.voa = self.ui.voa_lineEdit.text()
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
    def __init__(self, db: db_work.Garage_DB, parent=None):
        super().__init__(parent)
        self.ui = ui.find_user.Ui_Form()
        self.ui.setupUi(self)

        self.db = db          # сслыка на объект БД
        self.member = Member()  #
        self.parentForm = None  # сслыка на форму вызова для возвращения добавленных объектов
        self.addForm = None # ссылка на добавление нового члена

        self.initUi()


    def initUi(self):

        self.resize(self.width(), 220)
        #слоты
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.user_radioButton.clicked.connect(self.setEnableds)
        self.ui.object_radioButton.clicked.connect(self.setEnableds)
        self.ui.userList_radioButton.clicked.connect(self.setEnableds)
        self.ui.add_pushButton.clicked.connect(self.addNewMemberPshBtn)

        #модель для результирующей таблицы
        self.userModel = UsersTableViewModel()
        self.ui.result_tableView.setModel(self.userModel)
        #модель для юзерлист
        self.userListModel = UsersTableViewModelLite()
        self.ui.userList_tableView.setModel(self.userListModel)
        self.ui.userList_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.ui.object_radioButton.click()
        self.getUsersListFromDB()

    def setEnableds(self):
        """устанавливает или запрещает доступ к объектам интерфейса в зависимости от radioButton"""
        flag_user= self.ui.user_radioButton.isChecked()
        flag_obj = self.ui.object_radioButton.isChecked()
        flag_uList = self.ui.userList_radioButton.isChecked()
        # закрываем или открываем поиск по объекту
        self.ui.row_lineEdit.setEnabled(flag_obj)
        self.ui.number_lineEdit.setEnabled(flag_obj)
        # закрываем или открываем поиск по пользователю
        self.ui.surname_lineEdit.setEnabled(flag_user)
        self.ui.name_lineEdit.setEnabled(flag_user)
        self.ui.secondName_lineEdit.setEnabled(flag_user)
        self.ui.phone_lineEdit.setEnabled(flag_user)
        # закрываем или открываем таблицу с результатом
        self.ui.userList_tableView.setEnabled(flag_uList)
        self.ui.find_pushButton.setVisible(not flag_uList)

    def addNewMemberPshBtn(self):
        """открытие формы добавления нового члена в БД"""
        self.addForm = Member_front()
        self.addForm.db = self.db
        self.addForm.parentForm = self
        self.addForm.show()

    def getUsersListFromDB(self):
        """Заполнение таблицы существующих пользователей из БД"""
        if self.db:
            self.db.execute(sqlite_qwer.sql_get_all_active(self.TB_NAME))
            if self.db.cursor:
                member = Member()
                users =  self.db.cursor.fetchall()
                for user in users:
                    member.id = user[0]
                    member.surname = user[1]
                    member.name = user[2]
                    member.secondName = user[3]
                    member.birthday = user[4]
                    member.phone = user[6]
                    member.additPhone = user[7]
                    toTable = User_Info(member)
                    self.userListModel.setItems(toTable)








class Member():
    """Поля для БД на каждого члена"""
    def __init__(self):
        self.id = None
        self.surname = None
        self.name = None
        self.secondName = ''
        self.birthday = None
        self.address = None
        self.phone = None
        self.additPhone = ''
        self.email = ''
        self.voa = ''

class User_Info():
    """Класс для описания пользователя в табличку Карточка объекта"""
    def __init__(self, user: Member):
        self.id = user.id
        self.fio = f'{user.surname} {user.name} {user.secondName}'
        self.brDay = user.birthday
        self.phone = user.phone
        self.addPhone = user.additPhone
        self.role = '' # todo придумать механизм привязки роли (?) может через отдельный запрос к БД
