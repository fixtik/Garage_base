import time

from PySide6 import QtWidgets
from dataclasses import dataclass
from datetime import datetime
import os

from ui.cart.doc_add import Ui_Form
import sqlite_qwer
import ui.css
import ui.dialogs
import constants
import ui.cart_functions
import db_work
import ui.cart.cart_new_design
import ui.member_functions


class Docs_frontend(QtWidgets.QWidget):
    def __init__(self, db, garage_id, mainForm, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db  # db-connector
        self.garage_id = garage_id
        self.mainForm = mainForm
        self.moveBillPhoto = ui.member_functions.Member_front(db)

        # переменные класса
        self.css = ui.css  # для красоты
        self.doc_pass = None

        self.initUi()

    def initUi(self):
        """Инициализация объектов интерфейса"""
        # слоты
        self.ui.chooseDoc_pushButton.clicked.connect(self.chooseDoc_pushButton)
        self.ui.close_pushButton.clicked.connect(self.close)
        self.ui.ok_pushButton.clicked.connect(self.ok_pushButton)
        # add a little bit of spice
        self.css.SetIcon.icon(self, window_icon=1)

    def chooseDoc_pushButton(self):
        """Выбор файла"""
        doc_path = ui.dialogs.open_file_dialog(constants.TITLE_SELECT_DOC, None)[0]
        if doc_path:
            self.doc_pass = doc_path
            self.ui.docPass_label.setText(doc_path)

    def ok_pushButton(self):
        if self.ui.docName_lineEdit.text():
            if self.ui.docName_lineEdit.text().rstrip():
                if self.doc_pass:
                    if self.db:
                        doc = DocsInfo()
                        doc.name = self.ui.docName_lineEdit.text().lstrip().rstrip()
                        doc.date_add = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        doc.doc_pass = self.doc_pass
                        doc.garage_id = self.garage_id
                        self.db.execute(sqlite_qwer.sql_add_new_doc_info(name=doc.name,
                                                                         date_add=doc.date_add,
                                                                         doc_pass=doc.doc_pass,
                                                                         garage_id=doc.garage_id
                                                                         ))
                        doc.id = self.db.cursor.lastrowid
                        self.moveBillPhoto.move_photo(self, docPhotoPath=doc.doc_pass)
                        extension = doc.doc_pass.split('.').pop()  # Запоминаем расширение файла
                        # Запоминаем название файла чтобы потом добавить к названию id
                        name = doc.doc_pass.split('/').pop().split('.')[0]
                        doc.doc_pass = f'{constants.DEFAULT_DOCS_PASS}{name}_{str(self.db.cursor.lastrowid)}.{extension}'
                        doc.date_add = datetime.strptime(doc.date_add, "%Y-%m-%d %H:%M:%S").strftime(
                            '%d.%m.%Y %H:%M:%S')
                        self.mainForm.docsModel.setItems(doc)
                        self.close()
                else:
                    ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_DOC_NO_FILE)
            else:
                ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_DOC_FILE_NAME_SPACE)
        else:
            ui.dialogs.onShowError(self, constants.ERROR_TITLE, constants.ERROR_DOC_NO_FILE_NAME)


@dataclass
class DocsInfo():
    id: str = ''
    name: str = ''
    date_add: str = ''
    doc_pass: str = ''
    garage_id: str = ''
