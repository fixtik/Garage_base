# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_car.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(461, 262)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.carMark_label = QLabel(Form)
        self.carMark_label.setObjectName(u"carMark_label")
        self.carMark_label.setMinimumSize(QSize(80, 31))
        self.carMark_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout.addWidget(self.carMark_label)

        self.carMark_lineEdit = QLineEdit(Form)
        self.carMark_lineEdit.setObjectName(u"carMark_lineEdit")
        self.carMark_lineEdit.setMinimumSize(QSize(0, 31))
        self.carMark_lineEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout.addWidget(self.carMark_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gosNum_label = QLabel(Form)
        self.gosNum_label.setObjectName(u"gosNum_label")
        self.gosNum_label.setMinimumSize(QSize(80, 31))
        self.gosNum_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_2.addWidget(self.gosNum_label)

        self.gosNum_lineEdit = QLineEdit(Form)
        self.gosNum_lineEdit.setObjectName(u"gosNum_lineEdit")
        self.gosNum_lineEdit.setMinimumSize(QSize(0, 31))
        self.gosNum_lineEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_2.addWidget(self.gosNum_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.carInDb_tableView = QTableView(Form)
        self.carInDb_tableView.setObjectName(u"carInDb_tableView")

        self.verticalLayout_2.addWidget(self.carInDb_tableView)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.add_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")
        self.close_pushButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.close_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.carMark_label.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u0440\u043a\u0430 \u0430\u0432\u0442\u043e:", None))
        self.gosNum_label.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0441. \u043d\u043e\u043c\u0435\u0440:", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

