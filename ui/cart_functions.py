from PySide6 import QtCore, QtWidgets, QtGui

from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions
import ui.member_functions

from ui.tableView_Models import *



class Cart_frontend(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

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

        # слоты кнопок
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)
        self.ui.carAdd_pushButton.clicked.connect(self.showAddCarForm)
        self.ui.contribAdd_pushButton.clicked.connect(self.showAddContribForm)
        self.ui.userAdd_pushButton.clicked.connect(self.showFindUserForm)



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
        self.addUser_form = ui.member_functions.FindMember_front(self.db)
        self.addUser_form.show()




