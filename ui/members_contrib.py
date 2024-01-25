# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'members_contrib.ui'
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
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 223)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.typeSize_label = QLabel(Form)
        self.typeSize_label.setObjectName(u"typeSize_label")

        self.verticalLayout.addWidget(self.typeSize_label)

        self.typeSize_comboBox = QComboBox(Form)
        self.typeSize_comboBox.setObjectName(u"typeSize_comboBox")

        self.verticalLayout.addWidget(self.typeSize_comboBox)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.value_label = QLabel(Form)
        self.value_label.setObjectName(u"value_label")

        self.verticalLayout_2.addWidget(self.value_label)

        self.value_lineEdit = QLineEdit(Form)
        self.value_lineEdit.setObjectName(u"value_lineEdit")

        self.verticalLayout_2.addWidget(self.value_lineEdit)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.year_label = QLabel(Form)
        self.year_label.setObjectName(u"year_label")

        self.verticalLayout_3.addWidget(self.year_label)

        self.year_comboBox = QComboBox(Form)
        self.year_comboBox.setObjectName(u"year_comboBox")

        self.verticalLayout_3.addWidget(self.year_comboBox)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.horizontalLayout.addWidget(self.add_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout.addWidget(self.close_pushButton)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0447\u043b\u0435\u043d\u0441\u043a\u0438\u0445 \u0432\u0437\u043d\u043e\u0441\u043e\u0432",
                                                       None))
        self.typeSize_label.setText(QCoreApplication.translate("Form",
                                                               u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0433\u0430\u0440\u0430\u0436\u0430",
                                                               None))
        self.value_label.setText(QCoreApplication.translate("Form",
                                                            u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0433\u043e\u0434\u043e\u0432\u043e\u0433\u043e \u0447\u043b\u0435\u043d\u0441\u043a\u043e\u0433\u043e \u0432\u0437\u043d\u043e\u0441\u0430",
                                                            None))
        self.year_label.setText(QCoreApplication.translate("Form",
                                                           u"\u0413\u043e\u0434 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f",
                                                           None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0435\u0441\u0442\u0438", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi
