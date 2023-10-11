from PySide6 import QtCore, QtWidgets, QtGui

import sqlite_qwer
import ui.new_member
import ui.find_user
import ui.dialogs
import constants
import db_work
import ui.validators


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
            # TODO сделать очистку форм
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TEXT_PLACE_NOT_FILL)



    def addPushBtnClk(self):

        """Проверка данных при нажатии 'Добавить' """
        self.member.surname = self.ui.surname_lineEdit.text()
        self.member.name = self.ui.secondName_lineEdit.text()
        self.member.secondName = self.ui.secondName_lineEdit.text()
        self.member.birthday = self.ui.dateBirdth_dateEdit.date().toPython()
        self.member.phone = self.ui.phone_lineEdit.text()
        self.member.additPhone = self.ui.addPhone_lineEdit.text()
        self.member.email = self.ui.email_lineEdit.text()
        self.member.voa = self.ui.voa_lineEdit.text()
        self.member.address = self.ui.address_lineEdit.text()
        self.addToBase()

class FindMember_front(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.find_user.Ui_Form()
        self.ui.setupUi(self)

        self.db = None          # сслыка на объект БД
        self.member = Member()  #
        self.parentForm = None  # сслыка на форму вызова для возвращения добавленных объектов

        self.initUi()


    def initUi(self):

        self.resize(self.width(), 220)
        #слоты





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
