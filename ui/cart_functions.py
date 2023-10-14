from PySide6 import QtCore, QtWidgets, QtGui

import sqlite_qwer
from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions
import ui.member_functions
from ui.new_garage_size_func import GarageSizeStructure
import ui.validators

from ui.tableView_Models import *



class Cart_frontend(QtWidgets.QWidget):
    TB_NAME = 'type_size'
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.garage_ids = []  # список с id-платежа из БД, индекс соответствует индексу в combobox
        self.db = None

        self.initUi()

        #переменные класса
        self.db = None
        self.photoPath = None
        self.addCar_form = None
        self.addContrib_form = None
        self.addUser_form = None


    def initUi(self):
        """Инициализация интерфейса"""
        self.setMinimumWidth(1000)
        #self.setMaximumHeight(600)
        #авто табличка
        self.carModel = CarTableViewModel()
        self.ui.auto_tableView.setModel(self.carModel)
        #платежная табличка
        self.contribModel = ContribTableViewModel()
        self.ui.contrib_tableView.setModel(self.contribModel)
        #пользовательская таблица
        self.userModel = UsersTableViewModel()
        self.ui.users_tableView.setModel(self.userModel)
        #табличка счетчиков
        self.elMeterModel = ElectricTableViewModel()
        self.ui.electric_tableView.setModel(self.elMeterModel)

        # Обновление комбо бокса сразмерами гаража
        self.ui.comboBox.currentIndexChanged.connect(self.itemChanged)

        # слоты кнопок
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)
        self.ui.carAdd_pushButton.clicked.connect(self.showAddCarForm)
        self.ui.contribAdd_pushButton.clicked.connect(self.showAddContribForm)
        self.ui.userAdd_pushButton.clicked.connect(self.showFindUserForm)

        # установка валидаторов
        self.ui.width_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.len_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.hight_lineEdit.setValidator(ui.validators.floatValidator())

    def fillComboBox(self):
        if self.db:
            self.db.execute(sqlite_qwer.sql_select_all_from_table(self.TB_NAME))
            size = self.db.cursor.fetchall()
            self.garage_ids.clear()
            self.ui.comboBox.clear()
            for item in size:
                cont = GarageSizeStructure()
                cont.id = item[0]
                self.garage_ids.append(cont.id)
                cont.width = format(item[1]).rstrip('0').rstrip('.')
                cont.len = format(item[2]).rstrip('0').rstrip('.')
                cont.height = format(item[3]).rstrip('0').rstrip('.')
                cont.comment = item[4]
                self.ui.comboBox.addItem(str(cont.width) + ' x ' + str(cont.len) + ' x ' + str(cont.height))

            self.itemChanged()

    def itemChanged(self):
        """изменение данных в полях при изменении выбранной позиции"""
        if self.ui.comboBox.currentIndex() == -1:
            return
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(self.TB_NAME,
                                                             self.garage_ids[self.ui.comboBox.currentIndex()]))
        contrib = self.db.cursor.fetchall()

        self.ui.width_lineEdit.setText(str(contrib[0][1]))
        self.ui.len_lineEdit.setText(str(contrib[0][2]))
        self.ui.hight_lineEdit.setText(str(contrib[0][3]))
        self.ui.width_lineEdit_2.setText(contrib[0][4])

    def updateDataFromDB(self):
        """Обновление данных из БД для отображения в полях"""
        self.fillComboBox()

    def choosePhoto(self):
        """выбор фото на карточку"""
        img_path = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_PHOTO, constants.FILTER_PHOTO)[0]
        if img_path:
            pix = QtGui.QPixmap(img_path)
            pix = pix.scaled(constants.PHOTO_W, constants.PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.photo_label.setPixmap(pix)
            self.photoPath = img_path

    def showAddCarForm(self):
        """открытие формы добавления авто"""
        self.addCar_form = ui.car_functions.Car_frontend()
        self.addCar_form.mainForm = self
        self.addCar_form.show()

    def showAddContribForm(self):
        """открытие формы добавления платежа"""
        self.addContrib_form = ui.contribute_functions.AddContrib_front()
        self.addContrib_form.mainForm = self
        self.addContrib_form.db = self.db
        self.addContrib_form.updateDataFromDB()
        self.addContrib_form.show()


    def clearForm(self):
        """удаление текста в EditLine"""
        #гараж
        self.ui.row_lineEdit.setText('')
        self.ui.garage_lineEdit.setText('')
        self.ui.len_lineEdit.setText('')
        self.ui.width_lineEdit.setText('')
        self.ui.hight_lineEdit.setText('')
        # собственник

        # авто
        self.ui.auto_tableView.clearSpans()
        # взносы
        self.ui.contrib_tableView.clearSpans()

    def add_car_to_tableView(self, mark: str, num: str):
        """добавление данных о машине в таблицу"""
        self.ui.auto_tableView.columnCountChanged(0, 3)
        self.ui.auto_tableView.rowCountChanged(0,2)
        #self.ui.auto_tableView.(0,0) = '1'

    def showFindUserForm(self):
        """Открывает форму поиска члена кооператива"""
        self.addUser_form = ui.member_functions.FindMember_front()
        self.addUser_form.db = self.db
        self.addUser_form.show()




