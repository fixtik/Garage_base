from dataclasses import dataclass
from datetime import datetime
import os

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
    def __init__(self, db, main_form: QtWidgets.QWidget, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector

        # переменные класса
        self.mainForm = main_form
        self.photoPath = None
        self.addCar_form = None
        self.addContrib_form = None
        self.addUser_form = None
        self.addElectric = None
        self.addSize = None
        self.owner_id = None  # id собственника объекта
        self.garage_size_ids = []  # список id типоразмеров
        self.e220, self.e380 = None, None  # для id счетчиков
        self.garage_id = None  # id гаража
        self.button_group = None  # QButtonGroup(self)
        self.fullObjInfo = None  # информация об объекте (полная)

        self.initUi()

    def initUi(self):
        """Инициализация интерфейса"""
        self.setMinimumWidth(1000)
        # self.setMaximumHeight(600)
        # авто табличка
        self.carModel = CarTableViewModel()
        self.ui.auto_tableView.setModel(self.carModel)
        self.ui.auto_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # платежная табличка
        self.contribModel = ContribTableViewModel()
        self.ui.contrib_tableView.setModel(self.contribModel)
        self.ui.contrib_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # пользовательская таблица
        self.userModel = UsersTableViewModel()
        self.ui.users_tableView.setModel(self.userModel)
        self.ui.users_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.users_tableView.doubleClicked.connect(self.showEditUserForm)

        # табличка счетчиков
        self.elMeterModel = ElectricTableViewModel()
        self.ui.electric_tableView.setModel(self.elMeterModel)
        self.ui.electric_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.electric_tableView.doubleClicked.connect(self.showEditElectricForm)

        # Обновление комбо бокса сразмерами гаража
        self.updateDataFromDB()  # заполнение данных типоразмера

        # слоты кнопок
        self.ui.close_pushButton.clicked.connect(self.close)  # закрытие формы
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)  # добавление фото

        self.ui.contribAdd_pushButton.clicked.connect(self.showAddContribForm)  # добавление платежки
        self.ui.userAdd_pushButton.clicked.connect(self.showFindUserForm)  # добавление пользрователя
        self.ui.electricAdd_pushButton.clicked.connect(self.showElectricMetr)  # добавленее счетчика
        self.ui.addSize_pushButton.clicked.connect(self.showSizeEditorForm)  # доабвление размеров

        # удаление выделенной строки
        self.ui.contribDel_pushButton.clicked.connect(self.delTbView)
        self.ui.userDel_pushButton.clicked.connect(self.delTbView)
        self.ui.electricDel_pushButton.clicked.connect(self.delTbView)
        # self.ui.change_pushButton.clicked.connect(self.clearCartForm)  # внесение изменений в БД
        self.ui.change_pushButton.clicked.connect(self.addToBasePushBtnclck)  # внесение изменений в БД

        # валидаторы
        self.ui.garage_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.row_lineEdit.setValidator(ui.validators.onlyNumValidator())

        # установка в readOnly
        self.ui.ownerFIO_lineEdit.setReadOnly(True)
        self.ui.ownerPhone_lineEdit.setReadOnly(True)

        # Автоматичкская подгонка столбцов по ширине
        self.ui.contrib_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.auto_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.electric_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.users_tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.auto_label.setMinimumWidth(self.ui.userAdd_pushButton.width())

        self.ui.image_pushButton.setVisible(False)
        self.ui.photo_label.setVisible(False)

    def fillComboBox(self):
        """Заполнение данных о размере в комбобокс"""
        if self.db:
            self.garage_size_ids = \
                ui.new_garage_size_func.AddGarageSize_front.fillGarageSizeFromBase(self.db, self.ui.comboBox)[:]

    def updateDataFromDB(self):
        """Обновление данных из БД для отображения в полях"""
        self.fillComboBox()

    def choosePhoto(self):
        """выбор фото на карточку"""
        imgPath = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_PHOTO, constants.FILTER_PHOTO)[0]
        if imgPath:
            self.ui.photo_label.setVisible(True)
            self.setNewPhoto(imgPath)

    def setNewPhoto(self, image: str):
        """
        установка нового фото
        :param image: путь к фото
        """
        if image:
            self.ui.photo_label.setVisible(True)
            pix = QtGui.QPixmap(image)
            pix = pix.scaled(constants.PHOTO_W, constants.PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.photo_label.setPixmap(pix)
            self.photoPath = image

    def showElectricMetr(self):
        """открытие окна для добавления счетчика cо спрятанным полем поиска"""
        self.addElectric = ui.electric_meter_func.Electric_front(self.db, self)

        self.addElectric.hideFindePlace()
        self.addElectric.show()

    def showAddContribForm(self):
        """открытие формы добавления платежа"""
        self.addContrib_form = ui.contribute_functions.AddContrib_front(self.db)
        self.addContrib_form.mainForm = self
        self.addContrib_form.updateDataFromDB()
        self.addContrib_form.show()

    def clearForm(self):
        """удаление текста в EditLine"""
        # гараж
        self.ui.row_lineEdit.setText('')
        self.ui.garage_lineEdit.setText('')
        # self.ui.len_lineEdit.setText('')
        # self.ui.width_lineEdit.setText('')
        # self.ui.hight_lineEdit.setText('')
        # собственник

        # авто
        self.ui.auto_tableView.clearSpans()
        # взносы
        self.ui.contrib_tableView.clearSpans()
        self.ui.electric_tableView.clearSpans()

    def add_car_to_tableView(self, mark: str, num: str):
        """добавление данных о машине в таблицу"""
        self.ui.auto_tableView.columnCountChanged(0, 3)
        self.ui.auto_tableView.rowCountChanged(0, 2)

    def showFindUserForm(self):
        """Открывает форму поиска члена кооператива"""
        self.addUser_form = ui.member_functions.FindMember_front(db=self.db, main_form=self)
        self.addUser_form.show()

    def showEditElectricForm(self):
        """открывает форму редактирования счетчика"""
        self.addElectric = ui.electric_meter_func.Electric_front(self.db)
        self.addElectric.mainForm = self
        elmeter_id = (
            self.ui.electric_tableView.model().items[self.ui.electric_tableView.selectedIndexes()[0].row()]).id
        self.addElectric.changeFormElectric(elmeter_id=elmeter_id)
        self.addElectric.obj_id = self.fullObjInfo.id
        self.addElectric.hideFindePlace()
        self.addElectric.show()

    def showEditUserForm(self):
        """Открывает форму редактирования данных о пользователе"""
        self.addUser_form = ui.member_functions.Member_front(self.db)
        self.addUser_form.parentForm = self
        mem_id = (self.ui.users_tableView.model().items[self.ui.users_tableView.selectedIndexes()[0].row()]).id
        self.addUser_form.changeFormPr(mem_id=mem_id)
        self.addUser_form.show()

    def addRadioButtonToUsersTable(self):
        """Добавление RadioButton в user_tableView"""
        if self.button_group:
            del self.button_group
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.buttonClicked.connect(self.get_selected_owner_id)

        if self.owner_id:
            # дабы не потерять собственника выбранного
            for indx, item in enumerate(self.userModel.items):
                if item.id == self.owner_id:
                    break

        for index in range(self.userModel.rowCount()):
            w = QtWidgets.QWidget()
            h_layout = QtWidgets.QHBoxLayout(w)
            h_layout.setContentsMargins(0, 0, 0, 0)
            radio_btn = QtWidgets.QRadioButton("", self)
            if self.owner_id and indx == index:
                radio_btn.setChecked(True)

            h_layout.addWidget(radio_btn, alignment=QtCore.Qt.AlignCenter)
            self.button_group.addButton(radio_btn, index)
            self.ui.users_tableView.setIndexWidget(self.ui.users_tableView.model().index(index,
                                                                                         self.userModel.columnCount() - 1),
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

        if self.sender().objectName() == self.ui.electricDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.electric_tableView)
        elif self.sender().objectName() == self.ui.userDel_pushButton.objectName():
            # при удалении пользователя - удаляем и сслыки на его id
            indx = self.ui.users_tableView.selectionModel().selectedRows()
            if indx:
                if self.button_group.checkedId() == indx[0].row():
                    self.owner_id = ''
                    self.ui.ownerPhone_lineEdit.clear()
                    self.ui.ownerFIO_lineEdit.clear()
                    self.ui.photo_label.clear()
                    self.photoPath = ''
            self.del_car_by_fio(self.userModel.items[indx[0].row()].fio)
            self.delSelectRowFromTableView(self.ui.users_tableView)
        elif self.sender().objectName() == self.ui.contribDel_pushButton.objectName():
            self.delSelectRowFromTableView(self.ui.contrib_tableView)
        else:
            pass

    def del_car_by_fio(self, fio: str):
        cars = []
        for indx, item in enumerate(self.carModel.items):
            if fio == item.fio:
                cars.append(indx)
        cars.sort(reverse=True)
        for i in cars:
            self.carModel.removeRow(i)

    def checkFillAllFields(self):
        """проверка заполнения всех полей"""
        if not (self.owner_id):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_OWNER)
            return False
        if not (self.ui.row_lineEdit.text() and self.ui.garage_lineEdit.text()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_DATA_OBJECT)
            return False
        if not (self.ui.electric_tableView.model().items):
            if ui.dialogs.onShowСonfirmation(self, constants.INFO_TITLE, constants.INFO_NO_ELECTRIC_METER_TO_ADD):
                return False
        if not (self.ui.comboBox.currentText()):
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_NO_SIZE)
            return False
        e_data = self.ui.electric_tableView.model().items
        self.e380, self.e220 = None, None
        for item in e_data:  # Electric()
            if int(item.type) == constants.TYPE220 and not self.e220:
                self.e220 = item.id
            elif int(item.type) == constants.TYPE380 and not self.e380:
                self.e380 = item.id
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_TOO_MANY_METERS)

                return False

        self.e220 = '0' if not self.e220 else self.e220
        self.e380 = '0' if not self.e380 else self.e380
        return True

    def getUsersIds(self) -> list:
        """возвращает список с id пользователей объекта без id собственника """
        users = self.ui.users_tableView.model().items
        if self.owner_id:
            return [str(user.id) for user in users if int(self.owner_id) != user.id]
        return [str(user.id) for user in users]

    def add_garage(self) -> bool:
        """добавление в БД данных об объекте"""
        if self.db:
            arenda_ids = self.getUsersIds()
            sql = sqlite_qwer.sql_add_new_garage(row=self.ui.row_lineEdit.text(),
                                                 num=self.ui.garage_lineEdit.text(),
                                                 ownder_id=self.owner_id,
                                                 size_id=self.garage_size_ids[self.ui.comboBox.currentIndex()],
                                                 cr_year=self.ui.buildingYear_dateEdit.date().toPython(),
                                                 arenda_ids=" ".join(arenda_ids),
                                                 kadastr=self.ui.kadastr_lineEdit.text(),
                                                 e220=self.e220,
                                                 e380=self.e380)
            if self.db.execute(sql) and self.db.cursor:
                self.garage_id = self.db.cursor.lastrowid
                return True
        return False

    def updateGarage(self) -> bool:
        if self.db and self.fullObjInfo:
            arenda_ids = self.getUsersIds()
            sql = sqlite_qwer.sql_full_update_garage(object_id=self.fullObjInfo.id, row=self.ui.row_lineEdit.text(),
                                                     num=self.ui.garage_lineEdit.text(),
                                                     ownder_id=self.owner_id,
                                                     size_id=self.garage_size_ids[self.ui.comboBox.currentIndex()],
                                                     cr_year=self.ui.buildingYear_dateEdit.date().toPython(),
                                                     arenda_ids=" ".join(arenda_ids) if arenda_ids else ' ',
                                                     kadastr=self.ui.kadastr_lineEdit.text(),
                                                     e220=self.e220,
                                                     e380=self.e380)
            if self.db.execute(sql):
                return True
        return False

    def nameContribToKinfId(self, name: str) -> int:
        """получает id типа платежа по его названию"""
        if self.db.execute(sqlite_qwer.sql_select_id_by_field_value(constants.CONTRIB_TYPE_TABLE,
                                                                    'name', name)):
            return self.db.cursor.fetchone()[0]
        return -1

    def addContributionToBase(self) -> bool:
        """добавление информации о платежах в БД"""
        if self.db:
            obj_id = self.fullObjInfo.id if self.fullObjInfo else self.garage_id
            # забираем внесенные платежи
            contribs = self.ui.contrib_tableView.model().items
            # формируем список id существующих в БД платежей
            new_cont_ids = {con.id for con in contribs if con.id}
            old_contr_ids = []
            # получаем список id платежей из БД (которые были ранее)
            if self.db.execute(sqlite_qwer.sql_select_contrib_by_object_id(obj_id)):
                old_conts = self.db.cursor.fetchall()
                for o_c in old_conts:
                    old_contr_ids.append(o_c[0])
            # получаем список удаленных платежей и удаляем их из БД
            del_cont_ids = ','.join(str(item) for item in set(old_contr_ids).difference(new_cont_ids) if item)
            if del_cont_ids:
                if not (self.db.execute(sqlite_qwer.sql_delete_rec_by_table_name_and_id(
                        table_name=constants.CONTRIB_TABLE, rec_id=del_cont_ids))):
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_DELETE_QWERY +
                                           constants.CONTRIB_TABLE)

            for contr in contribs:
                type_id = self.nameContribToKinfId(contr.kindPay)
                if type_id == -1:
                    return False
                if contr.id:  # если уже есть в базе - обновляем данные
                    sql = sqlite_qwer.sql_full_update_contrib(cont_id=contr.id,
                                                              id_garage=obj_id,
                                                              id_cont=str(type_id),
                                                              pay_date=contr.payDate,
                                                              period_pay=contr.payPeriod,
                                                              value=contr.value,
                                                              comment=contr.comment if contr.comment else ' '
                                                              )
                else:
                    sql = sqlite_qwer.sql_add_new_contrib(
                        id_garage=obj_id,
                        id_cont=str(type_id),
                        pay_date=contr.payDate,
                        period_pay=contr.payPeriod,
                        value=contr.value,
                        comment=contr.comment if contr.comment else ' '
                    )
                if not (self.db.execute(sql)):
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_ADD_BASE_ERR)
                    return False
            return True

    def checkGarageInDB(self) -> bool:
        """проверка гаража в БД по ряду и номеру"""
        return check_rec_in_base(self.db,
                                 ('num_bild', self.ui.garage_lineEdit.text()),
                                 ('num_row', self.ui.row_lineEdit.text()),
                                 tb_name=constants.OBJ_TABLE
                                 )

    def clearCartForm(self):
        """Очистка данных для заполнения сведений о следующем объекте"""
        self.ui.row_lineEdit.clear()
        self.ui.garage_lineEdit.clear()
        self.ui.users_tableView.model().clearItemData()
        self.ui.auto_tableView.model().clearItemData()
        self.ui.contrib_tableView.model().clearItemData()
        self.ui.electric_tableView.model().clearItemData()
        self.ui.ownerPhone_lineEdit.clear()
        self.ui.ownerFIO_lineEdit.clear()
        self.photoPath, self.addCar_form, self.addContrib_form = None, None, None
        self.addUser_form, self.addElectric, self.addSize = None, None, None
        self.owner_id, self.e220, self.e380 = None, None, None
        self.garage_id = None
        self.ui.photo_label.clear()

    def addToBasePushBtnclck(self):
        if self.checkFillAllFields():
            # добавляем гараж
            objInDb = self.checkGarageInDB() if not self.fullObjInfo else True
            if not objInDb:  # если объекта в БД нет
                if self.add_garage():
                    # добавляем платежи
                    if self.addContributionToBase():
                        ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.INFO_SUCCESS_ADDED)
                        self.clearCartForm()
                        self.mainForm.fill_main_tableview()

            elif objInDb and self.fullObjInfo:  # если обект уже в бд и режим редактирования
                if self.updateGarage():
                    if self.addContributionToBase():
                        ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.INFO_SUCCESS_CHANGED)
                        self.close()


            elif objInDb and not self.fullObjInfo:  # если попытка добавить новый объект как дубликат к существующему
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, f'{constants.ERROR_OBJECT_ALREADY_EXIST}\n'
                                                                    f'{constants.MESSAGE_CHECK_DATA}')
            else:  # если ошибка с подключением к БД
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, f'{constants.ERROR_SQL_QWERY}\n'
                                                                    f'{constants.MESSAGE_CHECK_DB_CONNECTIONS}')

    def get_selected_owner_id(self):
        """изменение данных об id собственника для последующего внесения в БД"""
        index = self.button_group.checkedId()
        item = self.ui.users_tableView.model().items[index]
        self.owner_id = item.id
        self.ui.ownerFIO_lineEdit.setText(item.fio)
        self.ui.ownerPhone_lineEdit.setText(item.phone)

        self.photoPath = constants.DEFAULT_PHOTO_DIR_PASS + str(self.owner_id) + '.jpg'
        self.setNewPhoto(self.photoPath)

    def fillDataForObjectFromDB(self, object_id: str):
        """
        Заполнение формы для объекта при известном id объекта
        :param object_id: id объекта
        """
        if self.db and object_id:
            if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(table_name=constants.OBJ_TABLE, id=int(object_id))):
                oi = self.db.cursor.fetchone()
                self.fullObjInfo = FullObjectInfo(*oi)

                # заполняем поля об объекте
                self.ui.row_lineEdit.setText(f'{self.fullObjInfo.num_row}')
                self.ui.garage_lineEdit.setText(f'{self.fullObjInfo.num_bild}')
                self.ui.kadastr_lineEdit.setText(f'{self.fullObjInfo.kadastr_num}')
                self.ui.buildingYear_dateEdit.setDate(
                    datetime.strptime(self.fullObjInfo.create_year, "%Y-%m-%d").date())
                # заполняем данные о собственнике
                sql = sqlite_qwer.sql_get_one_record_by_id(constants.MEMBER_TABLE, int(self.fullObjInfo.owner_id))
                self.owner_id = self.fullObjInfo.owner_id
                if self.db.execute(sql):
                    usinf = ui.member_functions.Member(*self.db.cursor.fetchone())
                    usinf_lite = ui.member_functions.User_Info()
                    usinf_lite.memberToUserInfo(usinf)
                    self.ui.ownerFIO_lineEdit.setText(usinf_lite.fio)
                    self.ui.ownerPhone_lineEdit.setText(usinf.phone)
                    # вставляем фото
                    usinf.photo = os.getcwd() + usinf.photo  # создаем абсолютный путь
                    if usinf.photo and os.path.isfile(usinf.photo):
                        self.ui.photo_label.setVisible(True)
                        self.setNewPhoto(usinf.photo)
                        self.photoPath = usinf.photo
                    else:
                        self.ui.photo_label.setVisible(False)
                    # заполняем данные данные о арендаторах и их авто
                    ids = f"{(self.fullObjInfo.arendator_id.replace(' ', ','))},{self.owner_id}".lstrip(',')
                    if ui.member_functions.FindMember_front.addUserAndCarsToTV(self.db, ids,
                                                                               self.userModel, self.carModel):
                        self.addRadioButtonToUsersTable()
                    # заполняем данные о счетчиках
                    if self.fullObjInfo.electro220_id != 0:
                        if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(constants.ELECTRIC_TABLE,
                                                                                int(self.fullObjInfo.electro220_id))):
                            self.elMeterModel.setItems(ui.electric_meter_func.ElectricMeter(*self.db.cursor.fetchone()))
                    if self.fullObjInfo.electro380_id != 0:
                        if self.db.execute(sqlite_qwer.sql_get_one_record_by_id(constants.ELECTRIC_TABLE,
                                                                                int(self.fullObjInfo.electro380_id))):
                            self.elMeterModel.setItems(ui.electric_meter_func.ElectricMeter(*self.db.cursor.fetchone()))
                    # заполняем данные о типоразмере
                    if self.fullObjInfo.size_type_id:
                        for indx, id in enumerate(self.garage_size_ids):
                            if id == self.fullObjInfo.size_type_id:
                                self.ui.comboBox.setCurrentIndex(indx)
                                break
                    # заполняем данные о платежах
                    if self.db.execute(sqlite_qwer.sql_select_contrib_by_object_id(self.fullObjInfo.id)):
                        conribs = self.db.cursor.fetchall()
                        for conrib in conribs:
                            con = ui.contribute_functions.Contribution_lite(*conrib)
                            self.contribModel.setItems(con)

    def close(self) -> bool:
        self.mainForm.fill_main_tableview()
        self.mainForm.cartObj = None
        self.mainForm = None
        super().close()




def check_rec_in_base(db: db_work.Garage_DB, *args, tb_name: str) -> (int, None):
    """
    Проверка наличия записи в БД
    :param db: ссылка на БД
    :param args: кортеж (<имя поля> <значение>)
    :param table_name: имя таблицы для поиска
    :return: id записи - если запись обнаружена в БД
    """
    sql = sqlite_qwer.sql_find_id_by_filds(*args, table_name=tb_name)
    if sql:
        if db.execute(sql):
            id = db.cursor.fetchone()
            return id
    return None


@dataclass
class ObjectInfo():
    id: str = ''
    row: str = ''
    number: str = ''
    owner: str = ''
    owner_phone: str = ''
    kadastr: str = ''


@dataclass
class FullObjectInfo():
    id: str = ''
    num_row: str = ''
    num_bild: str = ''
    kadastr_num: str = ""
    owner_id: str = ''
    arendator_id: str = ''
    size_type_id: str = ''
    create_year: str = ''
    electro220_id: str = ''
    electro380_id: str = ''
