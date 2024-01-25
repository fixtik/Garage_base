# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bilingForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.year_comboBox = QComboBox(Form)
        self.year_comboBox.setObjectName(u"year_comboBox")

        self.verticalLayout.addWidget(self.year_comboBox)

        self.contrib_tableView = QTableView(Form)
        self.contrib_tableView.setObjectName(u"contrib_tableView")

        self.verticalLayout.addWidget(self.contrib_tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_pushButton = QPushButton(Form)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout.addWidget(self.ok_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout.addWidget(self.close_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0447\u0435\u0442\u0430 (\u0447\u043b\u0435\u043d\u0441\u043a\u0438\u0435 \u0432\u0437\u043d\u043e\u0441\u044b)", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

