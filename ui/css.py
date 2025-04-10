import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui

import constants


class SetIcon(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def icon(self, label=None, window_icon=None):
        if os.path.isfile(constants.DEFAULT_VOA_IMG):  # если запускаем из пайчарма
            pix = QtGui.QPixmap(constants.DEFAULT_VOA_IMG)
            pix = pix.scaled(constants.IMG_W, constants.IMG_W, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            if label:
                self.ui.voa_label.setPixmap(pix)
            if window_icon:
                self.setWindowIcon(QtGui.QIcon(pix))
        else:  # если запускаем скомпилированный exe
            bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            path_to_yml = os.path.abspath(os.path.join(bundle_dir, constants.DEFAULT_VOA_IMG))
            pix = QtGui.QPixmap(path_to_yml)
            pix = pix.scaled(constants.IMG_W, constants.IMG_W, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            if label:
                self.ui.voa_label.setPixmap(pix)
            if window_icon:
                self.setWindowIcon(QtGui.QIcon(pix))
