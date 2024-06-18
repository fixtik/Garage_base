import os.path

from PySide6 import QtWidgets, QtGui, QtCore

import ui.css
import ui.main.about


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
        text = '<h4>Версия 1.03</h4>\
                1. Обновлен дизайн карточки гаража (Платежи\Автомобили\Документы)<br/>\
                2. Добавлена форма с документами и соответствующий функционал (добавление, удаление, просмотр файлов при двойном нажатии)<br/>\
                3. Добавлен лейбл с версией программы <br/>\
                4. При добавлении чеков и документов сохраняется исходное расширение файлов и их название<br/>\
                5. Исправлена ошибка возникающая при редактировании пользователя без фотографии<br/>\
                6. Исправлена ошибка возникающая при попытке изменить сумму и комментарий платежа \
                <h4>Версия 1.02</h4>\
                1. Добавлена генерация QR_кодов на оплату<br/>\
                2. Добавлена форма с банковскими реквизитами<br/>\
                3. Добавлена возможность полного удаления счетчика<br/>\
                4. Добавлена генерация сметы<br/>'

        self.ui.about_textBrowser.append(text)
        self.ui.about_textBrowser.moveCursor(QtGui.QTextCursor.Start)
        # if os.path.isfile('about.txt'):
        #     file = open('about.txt', 'r', encoding='utf-8')
        #     self.ui.about_textBrowser.append(file.read())
        #     self.ui.about_textBrowser.moveCursor(QtGui.QTextCursor.Start)
