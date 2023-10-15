from PySide6 import QtCore, QtGui, QtWidgets





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

class UsersTableViewModelLite(UsersTableViewModel):
    """
        Модель для отображения данных по пользователям в TableView
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def columnCount(self, *args, **kwargs) -> int:
        return 5

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


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'ФИО',
                2: 'Дата рождения',
                3: 'Телефон',
                4: 'Доп. телефон',
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
