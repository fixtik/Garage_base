from PySide6 import QtCore, QtWidgets


def open_file_dialog() -> str:
    """
    вызывает диалоговое окно для открытия файла
    :return: имя выбранного файла
    """
    return QtWidgets.QFileDialog.getOpenFileName(caption="выберите файл бд", filter='*.db')

