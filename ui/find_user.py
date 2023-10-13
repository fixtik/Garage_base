# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_user.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(718, 545)
        self.verticalLayout_10 = QVBoxLayout(Form)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.object_radioButton = QRadioButton(Form)
        self.object_radioButton.setObjectName(u"object_radioButton")
        self.object_radioButton.setMinimumSize(QSize(170, 0))

        self.horizontalLayout.addWidget(self.object_radioButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row_label = QLabel(Form)
        self.row_label.setObjectName(u"row_label")
        self.row_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.row_label)

        self.row_lineEdit = QLineEdit(Form)
        self.row_lineEdit.setObjectName(u"row_lineEdit")

        self.verticalLayout.addWidget(self.row_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.number_label = QLabel(Form)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.number_label)

        self.number_lineEdit = QLineEdit(Form)
        self.number_lineEdit.setObjectName(u"number_lineEdit")

        self.verticalLayout_2.addWidget(self.number_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.user_radioButton = QRadioButton(Form)
        self.user_radioButton.setObjectName(u"user_radioButton")
        self.user_radioButton.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_4.addWidget(self.user_radioButton)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.surname_label = QLabel(Form)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.surname_label)

        self.surname_lineEdit = QLineEdit(Form)
        self.surname_lineEdit.setObjectName(u"surname_lineEdit")

        self.verticalLayout_3.addWidget(self.surname_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nem_label = QLabel(Form)
        self.nem_label.setObjectName(u"nem_label")
        self.nem_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.nem_label)

        self.name_lineEdit = QLineEdit(Form)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.verticalLayout_4.addWidget(self.name_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.secondName_label = QLabel(Form)
        self.secondName_label.setObjectName(u"secondName_label")
        self.secondName_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.secondName_label)

        self.secondName_lineEdit = QLineEdit(Form)
        self.secondName_lineEdit.setObjectName(u"secondName_lineEdit")

        self.verticalLayout_5.addWidget(self.secondName_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.phone_label = QLabel(Form)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.phone_label)

        self.phone_lineEdit = QLineEdit(Form)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")

        self.verticalLayout_6.addWidget(self.phone_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.userList_radioButton = QRadioButton(Form)
        self.userList_radioButton.setObjectName(u"userList_radioButton")
        self.userList_radioButton.setMinimumSize(QSize(170, 0))

        self.horizontalLayout_6.addWidget(self.userList_radioButton)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.userList_tableView = QTableView(Form)
        self.userList_tableView.setObjectName(u"userList_tableView")
        self.userList_tableView.setMinimumSize(QSize(0, 122))

        self.horizontalLayout_8.addWidget(self.userList_tableView)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.result_label = QLabel(Form)
        self.result_label.setObjectName(u"result_label")

        self.verticalLayout_7.addWidget(self.result_label)

        self.result_tableView = QTableView(Form)
        self.result_tableView.setObjectName(u"result_tableView")

        self.verticalLayout_7.addWidget(self.result_tableView)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.find_pushButton = QPushButton(Form)
        self.find_pushButton.setObjectName(u"find_pushButton")

        self.horizontalLayout_5.addWidget(self.find_pushButton)

        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.horizontalLayout_5.addWidget(self.add_pushButton)

        self.choose_pushButton = QPushButton(Form)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout_5.addWidget(self.choose_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_5.addWidget(self.close_pushButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u0447\u043b\u0435\u043d\u0430 \u043a\u043e\u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u0430", None))
        self.object_radioButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043d\u043e\u043c\u0435\u0440\u0443 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.row_label.setText(QCoreApplication.translate("Form", u"\u0420\u044f\u0434", None))
        self.number_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.user_radioButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u0434\u0430\u043d\u043d\u044b\u043c \u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0435", None))
        self.surname_label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.nem_label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.secondName_label.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.userList_radioButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430", None))
        self.result_label.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u043c\u044b\u0445 \u043b\u0438\u0446:", None))
        self.find_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

