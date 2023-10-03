from PySide6 import QtCore, QtGui







def onlyNumValidator():
    """валидатор для ввода только цифр"""
    reg_ex = QtCore.QRegularExpression()
    reg_ex.setPattern('[0-9]+')
    return QtGui.QRegularExpressionValidator(reg_ex)
