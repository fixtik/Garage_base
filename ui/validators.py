from PySide6 import QtCore, QtGui

def showHelp(window):
    button = window
    button.setToolTip("Формат: *.*")
    button.setToolTipDuration(3000)

def floatValidator():
    reg_ex = QtCore.QRegularExpression()
    reg_ex.setPattern('[0-9]+[,.]?[0-9]+')
    return QtGui.QRegularExpressionValidator(reg_ex)

def onlyNumValidator():
    """валидатор для ввода только цифр"""
    reg_ex = QtCore.QRegularExpression()
    reg_ex.setPattern('[0-9]+')
    return QtGui.QRegularExpressionValidator(reg_ex)
