from PySide6 import QtCore, QtGui, QtWidgets



class CarTableViewModel(QtCore.QAbstractTableModel):
    """
    Модель для отображения данных по автомобилям в TableView
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.items = []

    def returnItems(self):
        return self.items

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
            # if col == 3:
            #     return f'{car_info.owner_id}'
            # if col == 4:
            #     return f'{car_info.active}'

        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:

            return {
                0: 'id',
                1: 'Марка',
                2: 'Гос. номер',
                3: 'Владелец',
                4: 'Телефон'
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

        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


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
        self.header = ['id', 'ФИО', 'Дата рождения', 'Телефон', 'Доп. телефон', 'Собственник']
        self.items = []

    def resetData(self):
        self.beginResetModel()
        self.items.clear()
        self.endResetModel()

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
                return
        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.header[section]

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
        self.header = ['id', 'Тип', 'Номер счетчика', 'Тек. показания (день)', 'Тек. показания (ночь)', 'Расход день',
                       'Расход ночь']
        self.items = []

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return 7

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
            if col == 5:
                return  f'{int(elMeter.curDay) - int(elMeter.prev_day)}'
            if col == 6:
                return  f'{int(elMeter.curNight) - int(elMeter.prev_night)}'
            # как вариант - добавить сюда вывод информации о потребленной ЭЭ
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.header[section]

