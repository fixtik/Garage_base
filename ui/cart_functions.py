from PySide6 import QtCore, QtWidgets, QtGui

from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions
import ui.member_functions




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
        self.addUser_form = ui.member_functions.FindMember_front()
        self.addUser_form.db = self.db
        self.addUser_form.show()





class CarTableViewModel(QtCore.QAbstractTableModel):
    """
    Модель для отображения данных по автомобилям в TableView
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 3

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            car_info = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{car_info.id}'
            if col == 1:
                return f'{car_info.mark}'
            if col == 2:
                return f'{car_info.gos_num}'

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'Марка',
                2: 'Гос. номер'
            }.get(section)

class ContribTableViewModel(QtCore.QAbstractTableModel):
    """
        Модель для отображения данных по платежам в TableView
        """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 5

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            pay_info = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{pay_info.id}'
            if col == 1:
                return f'{pay_info.payDate}'
            if col == 2:
                return f'{pay_info.kindPay}'
            if col == 3:
                return f'{pay_info.value}'
            if col == 4:
                return f'{pay_info.payPeriod}'


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'Дата платежа',
                2: 'Вид платежа',
                3: 'Сумма платежа',
                4: 'Период оплаты',
            }.get(section)

class UsersTableViewModel(QtCore.QAbstractTableModel):
    """
        Модель для отображения данных по пользователям в TableView
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 6

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            user_info = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{user_info.id}'
            if col == 1:
                return f'{user_info.fio}'
            if col == 2:
                return f'{user_info.brDay}'
            if col == 3:
                return f'{user_info.phone}'
            if col == 4:
                return f'{user_info.addPhone}'
            if col == 5:
                return f'{user_info.role}'


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'ФИО',
                2: 'Дата рождения',
                3: 'Телефон',
                4: 'Доп. телефон',
                5: 'Отношение к объекту'
            }.get(section)

class ElectricTableViewModel(QtCore.QAbstractTableModel):
    """
        Модель для отображения данных по счетчикам в TableView
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 5

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            elMeter = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{elMeter.id}'
            if col == 1:
                return f'{elMeter.type}'
            if col == 2:
                return f'{elMeter.number}'
            if col == 3:
                return f'{elMeter.curDay}'
            if col == 4:
                return f'{elMeter.curNight}'
            # как вариант - добавить сюда вывод информации о потребленной ЭЭ


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'Тип',
                2: 'Номер счетчика',
                3: 'Тек. показания (день)',
                4: 'Тек. показания (ночь)'
            }.get(section)
