import sys
import os
from os.path import isfile

from PySide6 import QtCore, QtWidgets, QtGui

import sqlite_qwer
from ui.main_window import Ui_MainWindow
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


class SetIcon(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def icon(self, label=None, window_icon=None):
        if os.path.isfile(constants.DEFAULT_VOA_IMG):
            pix = QtGui.QPixmap(constants.DEFAULT_VOA_IMG)
            pix = pix.scaled(constants.IMG_W, constants.IMG_W, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            if label:
                self.ui.voa_label.setPixmap(pix)
            if window_icon:
                self.setWindowIcon(QtGui.QIcon(pix))
