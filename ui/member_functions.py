from PySide6 import QtCore, QtWidgets, QtGui

import sqlite_qwer
from ui.new_member import Ui_Form
import ui.dialogs
import constants
import db_work


class Member_front(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.photoPath = None
        self.db = None
        self.member = None

        self.initUi()


    def initUi(self):

        self.resize(self.width(), 220)

        self.ui.photo_pushButton.clicked.connect(self.choosePhoto)
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.add_pushButton.clicked.connect(self.addPushBtnClk)


    def choosePhoto(self):
        """выбор фото на карточку"""
        img_path = ui.dialogs.open_file_dialog("Выберите фото для загрузки", '*.jpg *.jpeg')[0]
        if img_path:
            pix = QtGui.QPixmap(img_path)
            pix = pix.scaled(constants.PHOTO_W, constants.PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.photo_label.setPixmap(pix)
            self.photoPath = img_path

    def addToBase(self):
        """Добавление записи в базу"""
        if self.db:
            if self.member.name and self.member.surname and self.member.birthday and self.member.phone \
                    and self.member.address:
                if self.db.execute(sqlite_qwer.sql_add_new_member(surname=self.member.surname,
                                                               first_name=self.member.name,
                                                               second_name=self.member.secondName,
                                                               birth_date=self.member.birthday,
                                                               phone_main=self.member.phone,
                                                               second_phone=self.member.additPhone,
                                                               email=self.member.email,
                                                               voa=self.member.voa,
                                                               photo=self.photoPath)):
                    print('ok')

    def addPushBtnClk(self):
        """Проверка данных при нажатии 'Добавить' """
        self.member.surname = self.ui.surname_lineEdit.text()
        self.member.name = self.ui.secondName_lineEdit.text()
        self.member.secondName = self.ui.secondName_lineEdit.text()
        self.member.birthday = self.ui.dateBirdth_dateEdit.date()
        self.member.phone = self.ui.phone_lineEdit.text()



class Member():
    def __init__(self):
        self.surname = None
        self.name = None
        self.secondName = ''
        self.birthday = None
        self.address = None
        self.phone = None
        self.additPhone = ''
        self.email = ''
        self.voa = ''