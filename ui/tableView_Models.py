from PySide6 import QtCore

import constants


class DBTableView(QtCore.QAbstractTableModel):
    """ Модель с для текущей БД"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = []  # заголовки для столбцов
        self.items = []  # данные для заполнения

    def returnItems(self):
        return self.items

    def resetData(self):
        self.beginResetModel()
        self.items.clear()
        self.endResetModel()

    def setItems(self, items):
        self.beginResetModel()
        self.items.append(items)
        self.endResetModel()

    def removeRows(self, position, rows=1, index=QtCore.QModelIndex):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        self.items = self.items[:position] + self.items[position + rows:]
        self.endRemoveRows()
        return True

    def clearItemData(self):
        self.resetData()
        return True

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        """Заголовок таблицы: Марка Номер"""
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.header[section]

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        return len(self.header)


class CarTableViewModel(DBTableView):
    """
    Модель для отображения данных по автомобилям в TableView
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.header = ['id', 'Марка', 'Гос. номер', 'Владелец', 'Телефон']

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
            if col == 3:
                return f'{car_info.fio}'
            if col == 4:
                return f'{car_info.phone}'

        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


class ContribTableViewModel(DBTableView):
    """
        Модель для отображения данных по платежам в TableView
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = ['id', 'Дата платежа', 'Вид платежа', 'Сумма платежа', 'Тип оплаты', 'Комментарий', 'Чек']

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
                return constants.CASH if int(pay_info.typePay) == 1 else constants.CASHLESS
            if col == 5:
                return f'{pay_info.comment}'
            if col == 6:
                return f'{pay_info.checkPath}'

        elif role == QtCore.Qt.TextAlignmentRole:
            return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


class UsersTableViewModel(DBTableView):
    """
        Модель для отображения данных по пользователям в TableView
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = ['id', 'ФИО', 'Дата рождения', 'Телефон', 'Доп. телефон', 'Собственник']

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


class UsersTableViewModelLite(DBTableView):
    """
        Модель для отображения данных по пользователям в TableView
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = ['id', 'ФИО', 'Дата рождения', 'Телефон', 'Доп. телефон']

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


class ElectricTableViewModel(DBTableView):
    """
        Модель для отображения данных по счетчикам в TableView
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = ['id', 'Тип', 'Номер счетчика', 'Тек. показания (день)', 'Тек. показания (ночь)', 'Расход день',
                       'Расход ночь']

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
                return f'{int(elMeter.curDay) - int(elMeter.prev_day)}'
            if col == 6:
                return f'{int(elMeter.curNight) - int(elMeter.prev_night)}'
            # как вариант - добавить сюда вывод информации о потребленной ЭЭ
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


class ObjectTableViewModel(DBTableView):
    """
        Модель для отображения данных по объектам в TableView
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.header = ['id', 'Ряд', 'Номер', 'Владелец', 'Телефон владельца', 'Кадастровый номер']

    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            obj = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{obj.id}'
            if col == 1:
                return f'{obj.row}'
            if col == 2:
                return f'{obj.number}'
            if col == 3:
                return f'{obj.owner}'
            if col == 4:
                return f'{obj.owner_phone}'
            if col == 5:
                return f'{obj.kadastr}'

            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
