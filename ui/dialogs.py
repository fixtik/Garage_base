from PySide6 import QtGui, QtCore, QtWidgets


def open_file_dialog(caption: str, filter = str) -> str:
    """
    вызывает диалоговое окно для открытия файла
    :return: имя выбранного файла
    """
    return QtWidgets.QFileDialog.getOpenFileName(caption=caption, filter=filter)


def onShowError(parent, title: str, msg: str, *args):
    """
    Вывод об ошибке
    """
    QtWidgets.QMessageBox.critical(parent, title, msg, *args)

def onShowСonfirmation(parent, title: str, msg: str, *args) -> bool:
    """
    Запрос подтверждения действия
    """
    flags = QtWidgets.QMessageBox.StandardButton.Yes
    flags |= QtWidgets.QMessageBox.StandardButton.No
    resp = QtWidgets.QMessageBox.question(parent, title, msg, flags, *args)
    if resp == QtWidgets.QMessageBox.StandardButton.Yes:
        return True
    return False



