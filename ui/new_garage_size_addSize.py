# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_garage_size_addSize.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(278, 195)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 251, 141))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout_5.addWidget(self.label_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.width_lineEdit = QLineEdit(self.layoutWidget)
        self.width_lineEdit.setObjectName(u"width_lineEdit")

        self.verticalLayout_6.addWidget(self.width_lineEdit)

        self.length_lineEdit = QLineEdit(self.layoutWidget)
        self.length_lineEdit.setObjectName(u"length_lineEdit")

        self.verticalLayout_6.addWidget(self.length_lineEdit)

        self.height_lineEdit = QLineEdit(self.layoutWidget)
        self.height_lineEdit.setObjectName(u"height_lineEdit")

        self.verticalLayout_6.addWidget(self.height_lineEdit)

        self.comment_lineEdit = QLineEdit(self.layoutWidget)
        self.comment_lineEdit.setObjectName(u"comment_lineEdit")

        self.verticalLayout_6.addWidget(self.comment_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 160, 251, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.ok_pushButton = QPushButton(self.layoutWidget_2)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout_6.addWidget(self.ok_pushButton)

        self.close_pushButton = QPushButton(self.layoutWidget_2)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_6.addWidget(self.close_pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0429\u0438\u0440\u0438\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

