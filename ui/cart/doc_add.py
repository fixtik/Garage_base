# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doc_add.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(228, 102)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chooseDoc_pushButton = QPushButton(Form)
        self.chooseDoc_pushButton.setObjectName(u"chooseDoc_pushButton")
        self.chooseDoc_pushButton.setMaximumSize(QSize(44, 20))

        self.horizontalLayout.addWidget(self.chooseDoc_pushButton)

        self.docPass_label = QLabel(Form)
        self.docPass_label.setObjectName(u"docPass_label")
        self.docPass_label.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.docPass_label)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.docName_lineEdit = QLineEdit(Form)
        self.docName_lineEdit.setObjectName(u"docName_lineEdit")

        self.gridLayout.addWidget(self.docName_lineEdit, 1, 0, 1, 1)

        self.doc_name_txt_label = QLabel(Form)
        self.doc_name_txt_label.setObjectName(u"doc_name_txt_label")
        self.doc_name_txt_label.setMaximumSize(QSize(16777215, 14))

        self.gridLayout.addWidget(self.doc_name_txt_label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ok_pushButton = QPushButton(Form)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout_2.addWidget(self.ok_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_2.addWidget(self.close_pushButton)

        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430",
                                                       None))
        self.chooseDoc_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.docPass_label.setText("")
        self.doc_name_txt_label.setText(QCoreApplication.translate("Form",
                                                                   u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430",
                                                                   None))
        self.ok_pushButton.setText(
            QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi
