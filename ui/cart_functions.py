from PySide6 import QtCore, QtWidgets, QtGui


from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions
import ui.electric_meter_func
import ui.member_functions
import ui.new_garage_size_func
import ui.validators

import sqlite_qwer

from ui.tableView_Models import *



class Cart_frontend(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db          # db-connector

        # переменные класса
        self.photoPath = None
        self.addCar_form = None
        self.addContrib_form = None
        self.addUser_form = None
        self.addElectric = None
        self.addSize = None
        self.owner_id = None  # id собственника объекта
        self.garage_ids = []  # список id типоразмеров

        self.initUi()

    def initUi(self):
        """Инициализация интерфейса"""
        self.setMinimumWidth(1000)
        #self.setMaximumHeight(600)
        #авто табличка
        self.carModel = CarTableViewModel()
        self.ui.auto_tableView.setModel(self.carModel)
        self.ui.auto_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #платежная табличка
        self.contribModel = ContribTableViewModel()
        self.ui.contrib_tableView.setModel(self.contribModel)
        self.ui.contrib_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #пользовательская таблица
        self.userModel = UsersTableViewModel()
        self.ui.users_tableView.setModel(self.userModel)
        self.ui.users_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #табличка счетчиков
        self.elMeterModel = ElectricTableViewModel()
        self.ui.electric_tableView.setModel(self.elMeterModel)
        self.ui.electric_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Обновление комбо бокса сразмерами гаража
        self.updateDataFromDB()              # заполнение данных типоразмера

        # слоты кнопок
        self.ui.close_pushButton.clicked.connect(self.close)                        # закрытие формы
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)                  # добавление фото
        self.ui.carAdd_pushButton.clicked.connect(self.showAddCarForm)              # добавление авто
        self.ui.contribAdd_pushButton.clicked.connect(self.showAddContribForm)      # добавление платежки
        self.ui.userAdd_pushButton.clicked.connect(self.showFindUserForm)           # добавление пользрователя
        self.ui.electricAdd_pushButton.clicked.connect(self.showElectricMetr)       # добавленее счетчика
        self.ui.addSize_pushButton.clicked.connect(self.showSizeEditorForm)

        self.ui.carDel_pushButton.clicked.connect(self.delTbView)                   # удаление выделенной строки
        self.ui.contribDel_pushButton.clicked.connect(self.delTbView)
        self.ui.userDel_pushButton.clicked.connect(self.delTbView)
        self.ui.electricDel_pushButton.clicked.connect(self.delTbView)
        self.ui.change_pushButton.clicked.connect(self.addToBasePushBtnclck)       # внесение изменений в БД

        # валидаторы
        self.ui.garage_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.row_lineEdit.setValidator(ui.validators.onlyNumValidator())

        # установка в readOnly
        self.ui.ownerFIO_lineEdit.setReadOnly(True)
        self.ui.ownerPhone_lineEdit.setReadOnly(True)

        #Автоматичкская подгонка столбцов по ширине
        self.ui.contrib_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.auto_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.electric_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.users_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)



    def fillComboBox(self):
        """Заполнение данных о размере в комбобокс"""
        if self.db:
            self.garage_ids = \
                ui.new_garage_size_func.AddGarageSize_front.fillGarageSizeFromBase(self.db, self.ui.comboBox)[:]


    def itemChanged(self):
        pass
        """изменение данных в полях при изменении выбранной позиции"""
        if self.ui.comboBox.currentIndex() == -1:
            return
        self.db.execute(sqlite_qwer.sql_get_one_record_by_id(ui.new_garage_size_func.AddGarageSize_front.TB_NAME,
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
        """открытие окна для добавления счетчика"""
        self.addElectric = ui.electric_meter_func.Electric_front(self.db)
        self.addElectric.mainForm = self
        if self.ui.change_pushButton.text() == constants.BTN_TEXT_ADD:
            self.addElectric.hideFindePlace()

        self.addElectric.show()

    def showAddCarForm(self):
        """открытие формы добавления авто"""
        self.addCar_form = ui.car_functions.Car_frontend(self.db)
        self.addCar_form.mainForm = self
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

    def showSizeEditorForm(self):
        """открывает форму добавления типоразмера"""
        self.closeChildForm(self.addSize)
        self.addSize = ui.new_garage_size_func.AddGarageSize_front(self.db)
        self.addSize.mainForm = self
        self.addSize.show()

    def destroyChildren(self):
        self.closeChildForm(self.sender())


    @staticmethod
    def closeChildForm(child: QtWidgets.QWidget):
        """уничтожает дочернюю форму (чтобы нельзя было открывать много окон)"""
        if isinstance(child, QtWidgets.QWidget):
            child.destroy()
            return None

    @staticmethod
    def delSelectRowFromTableView(tv: QtWidgets.QTableView):
        """удаление выделенной строки """
        model = tv.model()
        indxs = tv.selectionModel().selectedRows()
        for indx in sorted(indxs):
            model.removeRow(indx.row())

    @staticmethod
    def getDataFromTableView(tv: QtWidgets.QTableView) -> DBTableView:
        """возвращает данные из TableView"""
        model = tv.model()
        return model.items

    def delTbView(self):
        """удаление строки из таблицы"""
        if self.sender().objectName() == self.ui.carDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.auto_tableView)
        elif self.sender().objectName() == self.ui.electricDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.electric_tableView)
        elif self.sender().objectName() == self.ui.userDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.users_tableView)
        elif self.sender().objectName() == self.ui.contribDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.contrib_tableView)
        else:
            pass

    def checkFillAllFields(self):
        if not (self.owner_id):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_OWNER)
            return False
        if not (self.ui.row_lineEdit.text() and self.ui.garage_lineEdit.text()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_DATA_OBJECT)
            return False
        if not (self.ui.electric_tableView.model().items):
            if ui.dialogs.onShowСonfirmation(self, constants.INFO_TITLE, constants.INFO_NO_ELECTRIC_METER_TO_ADD):
                return False
        e_data = self.ui.electric_tableView.model().items
        e220, e380 = None, None
        for item in e_data: # Electric()
            if item.type == constants.TYPE220 and not e220:
                e220 = item.type
            elif item.type == constants.TYPE380 and not e380:
                e380 = item.type
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TOO_MANY_METERS)
                return False
        return True

    def addToBasePushBtnclck(self):
        if self.checkFillAllFields():
            if self.ui.change_pushButton.text() == constants.BTN_TEXT_ADD:
                # формируем запросы на добавление
                pass







    def get_selected_owner_id(self):
        """изменение данных об id собственника для последующего внесения в БД"""
        button = self.sender()
        index = self.ui.users_tableView.indexAt(button.pos())
        if index.isValid():
            item = self.ui.users_tableView.model().index(index.row(), 0)
            self.owner_id = item.data()









