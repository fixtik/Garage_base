import os.path

from PySide6 import QtWidgets, QtGui, QtCore

import ui.css
import ui.main.about
import constants


class About_frontend(QtWidgets.QWidget):
    def __init__(self, db, parent=None):
        super().__init__(parent)

        self.ui = ui.main.about.Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector
        self.css = ui.css  # для красоты

        self.initUi()

    def initUi(self):
        # self.ui.about_textBrowser.

        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)
        self.setText()

    def setText(self):
        if os.path.isfile(constants.DEFAULT_ABOUT_NAME):
            with open(constants.DEFAULT_ABOUT_NAME, 'r', encoding='utf-8') as file:
                self.ui.about_textBrowser.append(file.read())
                self.ui.about_textBrowser.moveCursor(QtGui.QTextCursor.Start)
#
