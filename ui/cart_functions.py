from PySide6 import QtCore, QtWidgets, QtGui

from ui.cart_ import Ui_Form


import constants
import db_work
import ui.dialogs
import ui.car_functions
import ui.contribute_functions

PHOTO_H = 100
PHOTO_W = 100


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


    def initUi(self):
        """Инициализация интерфейса"""
        self.setMinimumWidth(1000)
        self.setMaximumHeight(600)
        #авто табличка
        self.carModel = CarTableViewModel()
        self.ui.auto_tableView.setModel(self.carModel)
        #платежная табличка
        self.contribModel = ContribTableViewModel()
        self.ui.contrib_tableView.setModel(self.contribModel)

        # слоты кнопок
        self.ui.close_pushButton.clicked.connect(self.closeForm)
        self.ui.image_pushButton.clicked.connect(self.choosePhoto)
        self.ui.carAdd_pushButton.clicked.connect(self.showAddCarForm)
        self.ui.conribAdd_pushButton.clicked.connect(self.showAddContribForm)



    def closeForm(self):
        """Закрытие формы"""
        self.close()

    def choosePhoto(self):
        """выбор фото на карточку"""
        img_path = ui.dialogs.open_file_dialog("Выберите фото для загрузки", '*.jpg *.jpeg')[0]
        if img_path:
            pix = QtGui.QPixmap(img_path)
            pix = pix.scaled(PHOTO_W, PHOTO_H, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
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
        self.ui.elMetric220_lineEdit.setText('')
        self.ui.elMetric380_lineEdit.setText('')
        self.ui.len_lineEdit.setText('')
        self.ui.width_lineEdit.setText('')
        self.ui.hight_lineEdit.setText('')
        # собственник
        self.ui.surnamename_lineEdit.setText('')
        self.ui.name_lineEdit.setText('')
        self.ui.secondName_lineEdit.setText('')
        self.ui.phone_lineEdit.setText('')
        self.ui.addPhone_lineEdit.setText('')
        self.ui.address_textEdit.setText('')
        # арендатор
        self.ui.arendaSurnamename_lineEdit.setText('')
        self.ui.arendaName_lineEdit.setText('')
        self.ui.arendaSecondName_lineEdit.setText('')
        self.ui.arendaPhone_lineEdit.setText('')
        self.ui.arendaAddPhone_label.setText('')
        self.ui.arendaAddress_textEdit.setText('')
        # авто
        self.ui.auto_tableView.clearSpans()
        # взносы
        self.ui.contrib_tableView.clearSpans()

    def add_car_to_tableView(self, mark: str, num: str):
        """добавление данных о машине в таблицу"""
        self.ui.auto_tableView.columnCountChanged(0, 3)
        self.ui.auto_tableView.rowCountChanged(0,2)
        #self.ui.auto_tableView.(0,0) = '1'



class CarTableViewModel(QtCore.QAbstractTableModel):
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


