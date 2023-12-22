# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tarif.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(232, 259)
        Form.setMinimumSize(QSize(232, 259))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MeterType_label = QLabel(Form)
        self.MeterType_label.setObjectName(u"MeterType_label")
        self.MeterType_label.setMinimumSize(QSize(161, 0))

        self.verticalLayout.addWidget(self.MeterType_label)

        self.meterType_comboBox = QComboBox(Form)
        self.meterType_comboBox.setObjectName(u"meterType_comboBox")
        self.meterType_comboBox.setMinimumSize(QSize(161, 0))

        self.verticalLayout.addWidget(self.meterType_comboBox)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.day_label = QLabel(Form)
        self.day_label.setObjectName(u"day_label")
        self.day_label.setMinimumSize(QSize(161, 0))

        self.verticalLayout_2.addWidget(self.day_label)

        self.day_lineEdit = QLineEdit(Form)
        self.day_lineEdit.setObjectName(u"day_lineEdit")
        self.day_lineEdit.setMinimumSize(QSize(161, 0))

        self.verticalLayout_2.addWidget(self.day_lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.night_label = QLabel(Form)
        self.night_label.setObjectName(u"night_label")
        self.night_label.setMinimumSize(QSize(161, 0))

        self.verticalLayout_3.addWidget(self.night_label)

        self.night_lineEdit = QLineEdit(Form)
        self.night_lineEdit.setObjectName(u"night_lineEdit")
        self.night_lineEdit.setMinimumSize(QSize(161, 0))

        self.verticalLayout_3.addWidget(self.night_lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_pushButton = QPushButton(Form)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout.addWidget(self.ok_pushButton)

        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.horizontalLayout.addWidget(self.cancel_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u0430\u0440\u0438\u0444\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430", None))
        self.MeterType_label.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430", None))
        self.day_label.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0440\u0438\u0444 \u0434\u0435\u043d\u044c (\u0437\u0430 \u043a\u0412\u0442*\u0447)", None))
        self.night_label.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0440\u0438\u0444 \u043d\u043e\u0447\u044c (\u0437\u0430 \u043a\u0412\u0442*\u0447)", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0435\u0441\u0442\u0438", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

