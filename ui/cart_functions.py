from PySide6 import QtCore, QtWidgets, QtGui


from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions
import ui.electric_meter_func
import ui.member_functions
from ui.new_garage_size_func import GarageSizeStructure
import ui.validators
import sqlite_qwer

from ui.tableView_Models import *



class Cart_frontend(QtWidgets.QWidget):
    TB_NAME = 'type_size'
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.garage_ids = []  # список с id-платежа из БД, индекс соответствует индексу в combobox
        self.db = db          # db-connector

        self.initUi()

        #переменные класса
        self.photoPath = None
        self.addCar_form = None
        self.addContrib_form = None
        self.addUser_form = None
        self.addElectric = None
        self.owner_id = None            # id собственника объекта


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
        self.ui.close_pushButton.clicked.connect(self.close)                        # закрытие формы
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)                  # добавление фото
        self.ui.carAdd_pushButton.clicked.connect(self.showAddCarForm)              # добавление авто
        self.ui.contribAdd_pushButton.clicked.connect(self.showAddContribForm)      # добавление платежки
        self.ui.userAdd_pushButton.clicked.connect(self.showFindUserForm)           # добавление пользрователя
        self.ui.electricAdd_pushButton.clicked.connect(self.showElectricMetr)       # добавленее счетчика
        #self.ui.change_pushButton.clicked.connect()       # внесение изменений в БД

        # установка валидаторов
        self.ui.width_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.len_lineEdit.setValidator(ui.validators.floatValidator())
        self.ui.hight_lineEdit.setValidator(ui.validators.floatValidator())

        #Автоматичкская подгонка столбцов по ширине
        self.ui.contrib_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.auto_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.electric_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.users_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

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

    def showElectricMetr(self):
        self.addElectric = ui.electric_meter_func.Electric_front(self.db)
        self.addElectric.mainForm = self
        if self.ui.change_pushButton.text() == constants.BTN_TEXT_ADD:
            self.addElectric.hideFindePlace()

        self.addElectric.show()

    def showAddCarForm(self):
        """открытие формы добавления авто"""
        self.addCar_form = ui.car_functions.Car_frontend(self.db)
        self.addCar_form.mainForm = self
        self.addCar_form.db = self.db
        self.addCar_form.show()

    def showAddContribForm(self):
        """открытие формы добавления платежа"""
        self.addContrib_form = ui.contribute_functions.AddContrib_front(self.db)
        self.addContrib_form.mainForm = self
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
        self.addUser_form = ui.member_functions.FindMember_front(db=self.db, main_form=self)
        self.addUser_form.show()

    def addRadioButtonToUsersTable(self):
        """Добавление RadioButton в user_tableView"""
        button_group = QtWidgets.QButtonGroup(self)
        for index in range(self.userModel.rowCount()):
            w = QtWidgets.QWidget()
            h_layout = QtWidgets.QHBoxLayout(w)
            h_layout.setContentsMargins(0, 0, 0, 0)
            radio_btn = QtWidgets.QRadioButton("", self)
            radio_btn.clicked.connect(self.get_selected_owner_id)
            h_layout.addWidget(radio_btn, alignment=QtCore.Qt.AlignCenter)
            button_group.addButton(radio_btn)
            self.ui.users_tableView.setIndexWidget(self.ui.users_tableView.model().index(index,
                                                                                        self.userModel.columnCount()-1),
                                                                                         w)



    def get_selected_owner_id(self):
        """изменение данных об id собственника для последующего внесения в БД"""
        button = self.sender()
        index = self.ui.users_tableView.indexAt(button.pos())
        if index.isValid():
            item = self.ui.users_tableView.model().index(index.row(), 0)
            self.owner_id = item.data()









