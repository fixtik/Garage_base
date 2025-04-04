import os
import sys
import datetime

from os.path import isfile

from PySide6 import QtWidgets
from PySide6 import QtCore

import sqlite_qwer
from ui.main.main_window import Ui_MainWindow
import constants
import db_work
import ui.dialogs
import ui.cart_functions
import ui.contribute_functions
import ui.member_functions
import ui.electric_meter_func
import ui.new_garage_size_func
import ui.tableView_Models
import ui.validators
import ui.tarif_function
import ui.vigruzki_functions
import ui.css
import ui.qr_functions
import ui.main.about
import ui.about_functions

from pro import checker

if getattr(sys, 'frozen', False):
    import pyi_splash


class Form_frontend(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = db_work.Garage_DB()
        self.cartObj = None  # для отображения формы с карточкой объекта
        self.typePay = None  # для отображения формы редактирования видов платежей
        self.newMember = None  # для отображения формы добавления нового члена
        self.elMeter = None  # для отображения формы со счетчиком
        self.garageSize = None  # для отображения формы размера гаража
        self.tarif = None  # для отображения формы редактирования тарифа счетчика
        self.memberCont = None  # для отображения формы добавления членского взноса
        self.bilingCont = None  # для отображения формы выставления счета
        self.qrBankInfo = None  # для отображения формы заполнения банковских реквизитов
        self.progress = None  # для отображения прогресс бара
        self.about = None  # для отображения информации об обновлениях
        self.obj_model = ui.tableView_Models.ObjectTableViewModel()
        self.taskBarHeight = (
                self.screen().geometry().height() - self.screen().availableGeometry().height())  # Храним высоту экрана

        self.css = ui.css  # для красоты

        self.initUi()
        if not checker(constants.WINDOW_TITLE):
            ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=constants.ERROR_NO_KEY)
            self.hideObjectUI(False)
        else:
            if self.autoconnet():
                self.hideObjectUI(True)
                self.fill_main_tableview()
                self.autocheck()

            # self.set_disable_qr()

    def autoconnet(self) -> bool:
        """подключение БД с имененм по умолчанию"""
        res, msg = self.db.autoConnectBD()  # пробуем подключиться к БД по умолчанию
        self.showStatusBarMessage(msg)
        self.hideObjectUI(res)
        return res

    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.createBD_action.triggered.connect(self.create_db)  # создание новой бд
        self.ui.chooseBD_action.triggered.connect(self.openDB)  # выбор существующей бд
        self.ui.openBase_pushButton.clicked.connect(self.openDB)
        self.ui.search_action.triggered.connect(self.showCartObject)  # отображение главной карточки объекта
        self.ui.updateBD_action.triggered.connect(self.updateDB)
        self.ui.search_action.setVisible(False)
        self.ui.exit_action.triggered.connect(self.close)
        self.ui.kindPay_action.triggered.connect(
            self.showKindPayWindow)  # отображение окна редактирования типов платежей
        self.ui.member_action.triggered.connect(self.showAddMemberWindow)  # окно добавления нового члена
        self.ui.electric_action.triggered.connect(self.showElMeterWindow)
        self.ui.garage_action.triggered.connect(self.showGarageSizeWindow)  # окно добавления размеров гаража
        self.ui.add_action.triggered.connect(self.showFullAddCart)  # окно добавления всех данных
        self.ui.tarif_e.triggered.connect(self.showTarifMeter)  # окно редактирования тарифа
        self.ui.add_action.triggered.connect(self.showFullAddCart)  # окно добавления всех данных
        self.ui.tarif_e.triggered.connect(self.showTarifMeter)  # окно редактирования тарифа
        self.ui.memberCont_action.triggered.connect(self.showMemberCont)  # окно редатирования членского взноса
        self.ui.bilingContrib_action.triggered.connect(self.showBilingCont)  # окно выставления счета
        self.ui.bank_info.triggered.connect(self.showQrBankInfo)  # окно добавления банковской информации
        self.ui.about_action.triggered.connect(self.show_about_information)
        # Устанавливаем версию из файла about
        if os.path.isfile(constants.DEFAULT_ABOUT_NAME):
            first_line = open(constants.DEFAULT_ABOUT_NAME, encoding='utf-8').readline().strip('\n')[4:-5]
            self.ui.version_label.setText(first_line)
        else:
            self.ui.version_label.setText('ver 1.04')
        self.ui.version_label.setToolTip('Посмотрите изменения во вкладке "О программе"')

        # ------------- Выгрузки excel ------------- #
        # self.ui.vigruzki.setDisabled(True)
        # self.ui.spisok_action.triggered.connect(ui.vigruzki_functions.spisok_action())
        self.ui.smeta_action.triggered.connect(self.smeta)
        self.ui.spisok_action.setDisabled(True)
        self.ui.qr_action.triggered.connect(self.show_qr_statusbar)
        self.ui.doljniki_action.triggered.connect(self.doljniki)
        # -------------
        # таблица для отображения полей
        self.ui.tableView.setModel(self.obj_model)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.
                                                                  ResizeToContents)
        self.ui.tableView.doubleClicked.connect(self.showCartObject_EditMode)

        self.ui.num_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.row_lineEdit.setValidator(ui.validators.onlyNumValidator())
        self.ui.row_lineEdit.textEdited.connect(self.fill_main_tableview)
        self.ui.num_lineEdit.textEdited.connect(self.fill_main_tableview)
        self.ui.fam_lineEdit.textEdited.connect(self.fill_main_tableview)

        # add a little bit of spice
        self.css.SetIcon.icon(self, label=1, window_icon=1)

    def hideObjectUI(self, flag):
        """Скрывает или показывает объекты интерфейса"""
        self.ui.voa_label.setVisible(not flag)
        self.ui.openBase_pushButton.setVisible(not flag)
        self.ui.row_label.setVisible(flag)
        self.ui.row_lineEdit.setVisible(flag)
        self.ui.num_label.setVisible(flag)
        self.ui.num_lineEdit.setVisible(flag)
        self.ui.tableView.setVisible(flag)
        self.ui.fam_label.setVisible(flag)
        self.ui.fam_lineEdit.setVisible(flag)
        if flag:
            self.ui.horizontalLayout.removeItem(self.ui.verticalLayout)
            self.ui.horizontalLayout.removeItem(self.ui.horizontalSpacer)
            self.ui.horizontalLayout.removeItem(self.ui.horizontalSpacer_2)

    def openDB(self):
        new_name = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_BD, constants.FILTER_BD)[0]
        if new_name:
            if self.db.choose_db(new_name):
                if not self.db:
                    self.db = db_work.Garage_DB(new_name)
                else:
                    self.db.choose_db(new_name)
                self.hideObjectUI(True)
                self.fill_main_tableview()
                self.showStatusBarMessage(f"Файл БД {new_name} открыт")
                self.autocheck()

    def showStatusBarMessage(self, msg: str):
        """вывод сообщения в статус бар"""
        self.ui.statusbar.showMessage(msg)

    def create_db(self):
        if isfile(constants.DEFAULT_DB_NAME):
            if ui.dialogs.onShowСonfirmation(self, constants.INFO_TITLE, constants.INFO_CREATE_DB):
                return False
        if self.db.create_db():
            self.hideObjectUI(True)
            self.fill_main_tableview()

    def showCartObject(self):
        """Отображение окна карточки объекта"""
        self.cartObj = ui.cart_functions.Cart_frontend(db=self.db)
        self.cartObj.show()

    def showCartObject_EditMode(self):
        """Отображение окна карточки редактирования объекта"""
        self.cartObj = ui.cart_functions.Cart_frontend(db=self.db, main_form=self)
        self.cartObj.resize(int(self.cartObj.width()),
                            self.screen().availableSize().height() - self.taskBarHeight)
        self.cartObj.show()
        self.cartObj.move(self.screen().geometry().center() - self.cartObj.geometry().center())

        self.cartObj.fillDataForObjectFromDB(self.obj_model.items[self.ui.tableView.selectedIndexes()[0].row()].id)

    def showKindPayWindow(self):
        """Отображение окна редактирования вида платежа"""
        self.typePay = ui.contribute_functions.AddContrib_front(db=self.db)
        self.typePay.updateDataFromDB()
        self.typePay.hideDateField(False)
        self.typePay.show()

    def showGarageSizeWindow(self):
        """Отображение окна добавления размеров гаража"""
        self.garageSize = ui.new_garage_size_func.AddGarageSize_front(db=self.db)
        self.garageSize.updateDataFromDB()
        self.garageSize.show()

    def showAddMemberWindow(self):
        """Отображение окна добавления нового члена"""
        self.newMember = ui.member_functions.Member_front(db=self.db)
        self.newMember.show()

    def showElMeterWindow(self):
        """Отображение окна работы с эл. счетчкиами"""
        self.elMeter = ui.electric_meter_func.Electric_front(db=self.db)
        self.elMeter.show()

    def showFullAddCart(self):
        """Отображение окна для добавления всех данных одновременно (на основе карточки объекта)"""
        self.cartObj = ui.cart_functions.Cart_frontend(db=self.db, main_form=self)
        self.cartObj.ui.change_pushButton.setText(constants.BTN_TEXT_ADD)
        self.cartObj.show()
        self.cartObj.clearCartForm()

    def showTarifMeter(self):
        """Отображение окна для добавления всех данных одновременно (на основе карточки объекта)"""
        self.tarif = ui.tarif_function.Tarif_frontend(db=self.db, main_form=self)

        self.tarif.show()

    def fill_main_tableview(self):
        """заполнение данных tableview"""
        self.ui.tableView.model().clearItemData()
        if self.db:
            sql = sqlite_qwer.sql_get_all_objects_for_list_by_row_and_num(row=self.ui.row_lineEdit.text(),
                                                                          num=self.ui.num_lineEdit.text(),
                                                                          surname=self.ui.fam_lineEdit.text())
            if self.db.execute(sql):
                for obj in self.db.cursor.fetchall():
                    item = ui.cart_functions.ObjectInfo(obj[0], obj[1], obj[2], f'{obj[3]} {obj[4]} {obj[5]}',
                                                        obj[6],
                                                        obj[7])
                    self.obj_model.setItems(item)

    def showMemberCont(self):
        if self.db:
            self.memberCont = ui.contribute_functions.Member_contrib_ui(db=self.db)
            self.memberCont.mainForm = self
            self.memberCont.show()

    def showBilingCont(self):
        if self.db:
            self.bilingCont = ui.contribute_functions.Biling_contrib_ui(db=self.db)
            self.bilingCont.mainForm = self
            self.bilingCont.show()

    def smeta(self):
        """Генерируем смету"""
        if self.db:
            ui.vigruzki_functions.Smeta(db=self.db).smeta_action()
            if ui.dialogs.onShowСonfirmation(self, title=constants.INFO_TITLE,
                                             msg=f'{constants.INFO_SMETA_GENERATION_OK}'
                                                 f'\n{constants.INFO_OPEN_FILE}'):
                try:
                    os.startfile(
                        f'{constants.DEFAULT_SMETA_DIR_PASS}Смета_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx')
                except Exception as e:
                    # todo эти эксепшены с ошибками вообще работают?
                    ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=e)
            # ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_SMETA_OK)

    def doljniki(self):
        '''Генерируем список должников'''
        if self.db:
            ui.vigruzki_functions.Doljnik(db=self.db).doljnik_action()
            if ui.dialogs.onShowСonfirmation(self, title=constants.INFO_TITLE,
                                             msg=f'{constants.INFO_DOLJNIKI_GENERATION_OK}'
                                                 f'\n{constants.INFO_OPEN_FILE}'):
                try:
                    os.startfile(
                        f'{constants.DEFAULT_DOLJNIKI_DIR_PASS}Должники_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")}.xlsx')
                except Exception as e:
                    # todo эти эксепшены с ошибками вообще работают?
                    ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=e)

    def autocheck(self):
        """Автоматическая напоминалка чтобы не забвали обновить БД если нет новой таблицы"""
        if self.db:
            for table in constants.TABLE_NAMES:
                try:
                    if self.db.execute(sqlite_qwer.sql_check_table_exist_in_bd(table_name=table)):
                        _ = self.db.cursor.fetchone()
                        if not _:
                            ui.dialogs.onShowOkMessage(self, 'БД', 'Не забудьте обновить базу данных')
                            break
                except Exception as e:
                    ui.dialogs.onShowError(self, title=constants.ERROR_TITLE, msg=e)

    def showQrBankInfo(self):
        """Отображение окна добавления банковских реквизитов"""
        self.qrBankInfo = ui.qr_functions.QrBankInfo_frontend(db=self.db, status_window=None)
        self.qrBankInfo.show()

    def show_qr_statusbar(self):
        """Отображение окна с прогрессбаром при создании qr кода"""
        self.progress = ui.qr_functions.QR_StatusBar(db=self.db)
        self.progress.show()
        self.progress.start()

    def show_about_information(self):
        self.progress = ui.about_functions.About_frontend(db=self.db)
        self.progress.show()

    # Оставим до лучших времен, а то получается что надо делать еще миллион проверок (на смету, на платежную информацию) и немного геморно
    # def set_disable_qr(self):
    #     """Отключаем кнопку генерации QR если нет данных об организации"""
    #     if self.db:
    #         if self.db.execute(sqlite_qwer.sql_select_all_from_table(constants.PAYMENT_DETAILS)):
    #             _ = self.db.cursor.fetchone()
    #             if not _:
    #                 self.ui.vigruzki.setEnabled(False)

    def updateDB(self):
        if self.db:
            try:
                self.db.execute(sqlite_qwer.SQL_CREATE_TABLE_DOCS_INFO)
                # for name in constants.ALTER_TABLES_UPDATE_COLUMN_NAME:
                #     self.db.execute(name)
                if self.db.execute(
                        sqlite_qwer.sql_check_column_exists_in_table(constants.CONTRIB_TABLE, 'payment_time')):
                    _ = self.db.cursor.fetchone()[0]
                    if not _:
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS5)
                self.db.execute(sqlite_qwer.SQL_CREATE_TABLE_PAYMENT_DETAILS)
                # self.db.execute(sqlite_qwer.fixBug_updateTypeSizeId())  # typesize_id = 1
                try:
                    self.db.execute(sqlite_qwer.update_contribution())
                except:
                    print('zazzaza lalka')
                if self.db.execute(
                        sqlite_qwer.sql_check_column_exists_in_table(constants.CONTRIB_TABLE, 'balance_count')):
                    _ = self.db.cursor.fetchone()[0]
                    if not _:
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS4)
                        self.db.execute(sqlite_qwer.update_contribution())
                if self.db.execute(sqlite_qwer.sql_check_column_exists_in_table(constants.CONTRIB_TABLE, 'pay_kind')):
                    _ = self.db.cursor.fetchone()[0]
                    if not _:
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS)
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS1)
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS2)

                if self.db.execute(
                        sqlite_qwer.sql_check_column_exists_in_table(constants.CONTRIB_TYPE_TABLE, 'electric')):
                    _ = self.db.cursor.fetchone()[0]
                    if not _:
                        self.db.execute(constants.SQL_ALTER_TABLE_CONTRIBUTIONS3)

                if self.db.execute(sqlite_qwer.sql_check_column_exists_in_table(constants.SIZE_TABLE, 'cont_value')):
                    _ = self.db.cursor.fetchone()[0]
                    if not _:
                        self.db.execute(constants.SQL_ALTER_TABLE_TYPE_SIZE)
                if self.db.execute(constants.SQL_CREATE_TABLE_METER_PAYMENT) and \
                        self.db.execute(constants.SQL_CREATE_TABLE_OBJECT_ACCOUNT) and \
                        self.db.execute(constants.SQL_CREATE_TABLE_MEMBERS_CONTRIB):
                    if self.db.execute(sqlite_qwer.sql_gel_all_obj_ids()):
                        ids = self.db.cursor.fetchall()
                        for id in ids:
                            if self.db.execute(sqlite_qwer.sql_get_item_whithout_accaunt(id[0])):
                                f = self.db.cursor.fetchall()
                                if not f:
                                    self.db.execute(sqlite_qwer.sql_set_default_value_to_account(id[0]))

                    ui.dialogs.onShowOkMessage(self, constants.INFO_TITLE, constants.MESSAGE_UPDATE_DB_OK)
            except Exception as e:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_UPDATE_DB_FAIL)


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        pyi_splash.close()

    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt
    # if not checker():
    #     exit()
    myWindow = Form_frontend()  # Создаём объект окна
    myWindow.show()  # Показываем окно
    myWindow.resize(int(myWindow.width()), int(myWindow.height() * 1.3))
    # myWindow.move(myWindow.screen().geometry().center() - myWindow.geometry().center())
    # myWindow.resize(int(myWindow.width()), myWindow.screen().availableSize().height() - myWindow.taskBarHeight)
    # myWindow.show()

    # Локализация приложения на русский, чтобы не было в сплывающих окошках выбора Yes|No
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.path(QtCore.QLibraryInfo.LibraryPath.TranslationsPath)
    translator.load('qt_%s' % locale, path)
    app.installTranslator(translator)

    sys.exit(app.exec())  # Если exit, то код дальше не исполняется
