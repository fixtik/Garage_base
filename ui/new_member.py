# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_member.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(707, 423)
        Form.setMinimumSize(QSize(0, 423))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.surname_label = QLabel(Form)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setMaximumSize(QSize(16777215, 31))
        self.surname_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.surname_label)

        self.surname_lineEdit = QLineEdit(Form)
        self.surname_lineEdit.setObjectName(u"surname_lineEdit")
        self.surname_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_14.addWidget(self.surname_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMaximumSize(QSize(16777215, 31))
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(Form)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_13.addWidget(self.name_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.secondName_label = QLabel(Form)
        self.secondName_label.setObjectName(u"secondName_label")
        self.secondName_label.setMaximumSize(QSize(16777215, 31))
        self.secondName_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.secondName_label)

        self.secondName_lineEdit = QLineEdit(Form)
        self.secondName_lineEdit.setObjectName(u"secondName_lineEdit")
        self.secondName_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_15.addWidget(self.secondName_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.photo_label = QLabel(Form)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.photo_label)

        self.photo_pushButton = QPushButton(Form)
        self.photo_pushButton.setObjectName(u"photo_pushButton")

        self.verticalLayout.addWidget(self.photo_pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.dateBirdth_label = QLabel(Form)
        self.dateBirdth_label.setObjectName(u"dateBirdth_label")
        self.dateBirdth_label.setMaximumSize(QSize(109, 16777215))
        self.dateBirdth_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.dateBirdth_label)

        self.dateBirdth_dateEdit = QDateEdit(Form)
        self.dateBirdth_dateEdit.setObjectName(u"dateBirdth_dateEdit")
        self.dateBirdth_dateEdit.setMinimumSize(QSize(0, 31))
        self.dateBirdth_dateEdit.setMaximumSize(QSize(109, 31))
        self.dateBirdth_dateEdit.setMinimumDate(QDate(1900, 1, 1))

        self.verticalLayout_18.addWidget(self.dateBirdth_dateEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.phone_label = QLabel(Form)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(0, 31))
        self.phone_label.setMaximumSize(QSize(16777215, 31))
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.phone_label)

        self.phone_lineEdit = QLineEdit(Form)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_16.addWidget(self.phone_lineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.addPhone_label = QLabel(Form)
        self.addPhone_label.setObjectName(u"addPhone_label")
        self.addPhone_label.setMinimumSize(QSize(0, 31))
        self.addPhone_label.setMaximumSize(QSize(16777215, 31))
        self.addPhone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.addPhone_label)

        self.addPhone_lineEdit = QLineEdit(Form)
        self.addPhone_lineEdit.setObjectName(u"addPhone_lineEdit")
        self.addPhone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_17.addWidget(self.addPhone_lineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.email_label = QLabel(Form)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(0, 31))
        self.email_label.setMaximumSize(QSize(16777215, 31))
        self.email_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.email_label)

        self.email_lineEdit = QLineEdit(Form)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_2.addWidget(self.email_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.voa_label = QLabel(Form)
        self.voa_label.setObjectName(u"voa_label")
        self.voa_label.setMinimumSize(QSize(0, 31))
        self.voa_label.setMaximumSize(QSize(16777215, 31))
        self.voa_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.voa_label)

        self.voa_lineEdit = QLineEdit(Form)
        self.voa_lineEdit.setObjectName(u"voa_lineEdit")
        self.voa_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_3.addWidget(self.voa_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.address_label = QLabel(Form)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 31))
        self.address_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_9.addWidget(self.address_label)

        self.address_lineEdit = QLineEdit(Form)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_9.addWidget(self.address_lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.car_groupBox = QGroupBox(Form)
        self.car_groupBox.setObjectName(u"car_groupBox")
        self.horizontalLayout_11 = QHBoxLayout(self.car_groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.autoMember_tableView = QTableView(self.car_groupBox)
        self.autoMember_tableView.setObjectName(u"autoMember_tableView")
        self.autoMember_tableView.setMaximumSize(QSize(16777215, 62))

        self.verticalLayout_20.addWidget(self.autoMember_tableView)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_3)

        self.memberCarAdd_pushButton = QPushButton(self.car_groupBox)
        self.memberCarAdd_pushButton.setObjectName(u"memberCarAdd_pushButton")
        self.memberCarAdd_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_35.addWidget(self.memberCarAdd_pushButton)

        self.memberCarDel_pushButton = QPushButton(self.car_groupBox)
        self.memberCarDel_pushButton.setObjectName(u"memberCarDel_pushButton")
        self.memberCarDel_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_35.addWidget(self.memberCarDel_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_2)


        self.horizontalLayout_19.addLayout(self.verticalLayout_35)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_19)


        self.verticalLayout_4.addWidget(self.car_groupBox)

        self.verticalSpacer = QSpacerItem(20, 118, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.add_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")
        self.close_pushButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.close_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0447\u043b\u0435\u043d\u0430 \u043a\u043e\u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u0430", None))
        self.surname_label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f*", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f*", None))
        self.secondName_label.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e*", None))
        self.photo_label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e", None))
        self.photo_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.dateBirdth_label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f*", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d*", None))
        self.addPhone_label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"email", None))
        self.voa_label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0412\u041e\u0410", None))
        self.address_label.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.car_groupBox.setTitle(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438:", None))
        self.memberCarAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.memberCarDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

