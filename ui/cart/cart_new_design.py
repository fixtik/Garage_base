# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart_new_design.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
                               QGroupBox, QHBoxLayout, QHeaderView, QLabel,
                               QLayout, QLineEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QTabWidget, QTableView, QVBoxLayout,
                               QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(931, 913)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(Form)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.garage_groupBox = QGroupBox(Form)
        self.garage_groupBox.setObjectName(u"garage_groupBox")
        self.garage_groupBox.setMinimumSize(QSize(1, 0))
        self.garage_groupBox.setMaximumSize(QSize(16777215, 99999))
        self.verticalLayout_6 = QVBoxLayout(self.garage_groupBox)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.garage_label = QLabel(self.garage_groupBox)
        self.garage_label.setObjectName(u"garage_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.garage_label.sizePolicy().hasHeightForWidth())
        self.garage_label.setSizePolicy(sizePolicy1)
        self.garage_label.setMaximumSize(QSize(61, 31))

        self.verticalLayout.addWidget(self.garage_label)

        self.row_label = QLabel(self.garage_groupBox)
        self.row_label.setObjectName(u"row_label")
        sizePolicy1.setHeightForWidth(self.row_label.sizePolicy().hasHeightForWidth())
        self.row_label.setSizePolicy(sizePolicy1)
        self.row_label.setMaximumSize(QSize(61, 31))

        self.verticalLayout.addWidget(self.row_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.garage_lineEdit = QLineEdit(self.garage_groupBox)
        self.garage_lineEdit.setObjectName(u"garage_lineEdit")
        self.garage_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_12.addWidget(self.garage_lineEdit)

        self.row_lineEdit = QLineEdit(self.garage_groupBox)
        self.row_lineEdit.setObjectName(u"row_lineEdit")
        self.row_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_12.addWidget(self.row_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_12)


        self.horizontalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buildYear_label = QLabel(self.garage_groupBox)
        self.buildYear_label.setObjectName(u"buildYear_label")
        self.buildYear_label.setMinimumSize(QSize(136, 0))
        self.buildYear_label.setMaximumSize(QSize(16777215, 31))
        self.buildYear_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.buildYear_label)

        self.buildingYear_dateEdit = QDateEdit(self.garage_groupBox)
        self.buildingYear_dateEdit.setObjectName(u"buildingYear_dateEdit")
        self.buildingYear_dateEdit.setMinimumSize(QSize(91, 31))
        self.buildingYear_dateEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_4.addWidget(self.buildingYear_dateEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.kadastr_label = QLabel(self.garage_groupBox)
        self.kadastr_label.setObjectName(u"kadastr_label")
        self.kadastr_label.setMinimumSize(QSize(136, 0))
        self.kadastr_label.setMaximumSize(QSize(16777215, 31))
        self.kadastr_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.kadastr_label)

        self.kadastr_lineEdit = QLineEdit(self.garage_groupBox)
        self.kadastr_lineEdit.setObjectName(u"kadastr_lineEdit")
        self.kadastr_lineEdit.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_16.addWidget(self.kadastr_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.width_label_2 = QLabel(self.garage_groupBox)
        self.width_label_2.setObjectName(u"width_label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.width_label_2.sizePolicy().hasHeightForWidth())
        self.width_label_2.setSizePolicy(sizePolicy2)
        self.width_label_2.setMinimumSize(QSize(119, 22))
        self.width_label_2.setMaximumSize(QSize(9999999, 22))
        self.width_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.width_label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.garage_groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 31))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.addSize_pushButton = QPushButton(self.garage_groupBox)
        self.addSize_pushButton.setObjectName(u"addSize_pushButton")
        self.addSize_pushButton.setMinimumSize(QSize(0, 31))
        self.addSize_pushButton.setMaximumSize(QSize(31, 31))

        self.horizontalLayout_2.addWidget(self.addSize_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_12.addLayout(self.verticalLayout_5)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.photo_label = QLabel(self.garage_groupBox)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.photo_label)

        self.image_pushButton = QPushButton(self.garage_groupBox)
        self.image_pushButton.setObjectName(u"image_pushButton")

        self.verticalLayout_3.addWidget(self.image_pushButton)

        self.horizontalLayout_20.addLayout(self.verticalLayout_3)

        self.verticalLayout_11.addLayout(self.horizontalLayout_20)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ownerFIO_label = QLabel(self.garage_groupBox)
        self.ownerFIO_label.setObjectName(u"ownerFIO_label")
        sizePolicy2.setHeightForWidth(self.ownerFIO_label.sizePolicy().hasHeightForWidth())
        self.ownerFIO_label.setSizePolicy(sizePolicy2)
        self.ownerFIO_label.setMinimumSize(QSize(0, 22))
        self.ownerFIO_label.setMaximumSize(QSize(119, 22))
        self.ownerFIO_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.ownerFIO_label)

        self.ownerFIO_lineEdit = QLineEdit(self.garage_groupBox)
        self.ownerFIO_lineEdit.setObjectName(u"ownerFIO_lineEdit")
        self.ownerFIO_lineEdit.setMinimumSize(QSize(0, 31))
        self.ownerFIO_lineEdit.setMaximumSize(QSize(99999, 16777215))

        self.horizontalLayout_14.addWidget(self.ownerFIO_lineEdit)

        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.ownerPhone_label = QLabel(self.garage_groupBox)
        self.ownerPhone_label.setObjectName(u"ownerPhone_label")
        sizePolicy2.setHeightForWidth(self.ownerPhone_label.sizePolicy().hasHeightForWidth())
        self.ownerPhone_label.setSizePolicy(sizePolicy2)
        self.ownerPhone_label.setMinimumSize(QSize(0, 22))
        self.ownerPhone_label.setMaximumSize(QSize(119, 22))
        self.ownerPhone_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.ownerPhone_label)

        self.ownerPhone_lineEdit = QLineEdit(self.garage_groupBox)
        self.ownerPhone_lineEdit.setObjectName(u"ownerPhone_lineEdit")
        self.ownerPhone_lineEdit.setMinimumSize(QSize(0, 31))
        self.ownerPhone_lineEdit.setMaximumSize(QSize(9999, 16777215))

        self.horizontalLayout_17.addWidget(self.ownerPhone_lineEdit)

        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.electricMeter_label = QLabel(self.garage_groupBox)
        self.electricMeter_label.setObjectName(u"electricMeter_label")
        sizePolicy1.setHeightForWidth(self.electricMeter_label.sizePolicy().hasHeightForWidth())
        self.electricMeter_label.setSizePolicy(sizePolicy1)
        self.electricMeter_label.setMaximumSize(QSize(99999, 31))

        self.verticalLayout_6.addWidget(self.electricMeter_label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.electric_tableView = QTableView(self.garage_groupBox)
        self.electric_tableView.setObjectName(u"electric_tableView")
        self.electric_tableView.setMaximumSize(QSize(16777215, 87))

        self.horizontalLayout_6.addWidget(self.electric_tableView)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_39.setContentsMargins(-1, 20, -1, 20)
        self.electricAdd_pushButton = QPushButton(self.garage_groupBox)
        self.electricAdd_pushButton.setObjectName(u"electricAdd_pushButton")
        self.electricAdd_pushButton.setMaximumSize(QSize(31, 23))

        self.verticalLayout_39.addWidget(self.electricAdd_pushButton)

        self.electricDel_pushButton = QPushButton(self.garage_groupBox)
        self.electricDel_pushButton.setObjectName(u"electricDel_pushButton")
        self.electricDel_pushButton.setMaximumSize(QSize(31, 23))

        self.verticalLayout_39.addWidget(self.electricDel_pushButton)

        self.horizontalLayout_6.addLayout(self.verticalLayout_39)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.users_label = QLabel(self.garage_groupBox)
        self.users_label.setObjectName(u"users_label")
        sizePolicy1.setHeightForWidth(self.users_label.sizePolicy().hasHeightForWidth())
        self.users_label.setSizePolicy(sizePolicy1)
        self.users_label.setMaximumSize(QSize(99999, 31))

        self.verticalLayout_6.addWidget(self.users_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.users_tableView = QTableView(self.garage_groupBox)
        self.users_tableView.setObjectName(u"users_tableView")
        self.users_tableView.setMaximumSize(QSize(16777215, 150))

        self.horizontalLayout_3.addWidget(self.users_tableView)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 52, 0, 52)
        self.userAdd_pushButton = QPushButton(self.garage_groupBox)
        self.userAdd_pushButton.setObjectName(u"userAdd_pushButton")
        self.userAdd_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_37.addWidget(self.userAdd_pushButton)

        self.userDel_pushButton = QPushButton(self.garage_groupBox)
        self.userDel_pushButton.setObjectName(u"userDel_pushButton")
        self.userDel_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_37.addWidget(self.userDel_pushButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout_37)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_14.addWidget(self.garage_groupBox)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabBarAutoHide(False)
        self.contribs = QWidget()
        self.contribs.setObjectName(u"contribs")
        self.gridLayout = QGridLayout(self.contribs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.contrib_tableView = QTableView(self.contribs)
        self.contrib_tableView.setObjectName(u"contrib_tableView")
        self.contrib_tableView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.contrib_tableView, 0, 0, 1, 1)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_4)

        self.contribAdd_pushButton_2 = QPushButton(self.contribs)
        self.contribAdd_pushButton_2.setObjectName(u"contribAdd_pushButton_2")
        self.contribAdd_pushButton_2.setMaximumSize(QSize(31, 31))

        self.verticalLayout_41.addWidget(self.contribAdd_pushButton_2)

        self.contribDel_pushButton_2 = QPushButton(self.contribs)
        self.contribDel_pushButton_2.setObjectName(u"contribDel_pushButton_2")
        self.contribDel_pushButton_2.setMaximumSize(QSize(31, 31))

        self.verticalLayout_41.addWidget(self.contribDel_pushButton_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_12)

        self.gridLayout.addLayout(self.verticalLayout_41, 0, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.prevDebt_label = QLabel(self.contribs)
        self.prevDebt_label.setObjectName(u"prevDebt_label")
        sizePolicy2.setHeightForWidth(self.prevDebt_label.sizePolicy().hasHeightForWidth())
        self.prevDebt_label.setSizePolicy(sizePolicy2)
        self.prevDebt_label.setMinimumSize(QSize(0, 18))
        self.prevDebt_label.setMaximumSize(QSize(999993, 18))
        self.prevDebt_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.prevDebt_label)

        self.prevDebt_lineEdit = QLineEdit(self.contribs)
        self.prevDebt_lineEdit.setObjectName(u"prevDebt_lineEdit")
        self.prevDebt_lineEdit.setMinimumSize(QSize(180, 31))
        self.prevDebt_lineEdit.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_8.addWidget(self.prevDebt_lineEdit)

        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calc_label = QLabel(self.contribs)
        self.calc_label.setObjectName(u"calc_label")
        sizePolicy2.setHeightForWidth(self.calc_label.sizePolicy().hasHeightForWidth())
        self.calc_label.setSizePolicy(sizePolicy2)
        self.calc_label.setMinimumSize(QSize(0, 18))
        self.calc_label.setMaximumSize(QSize(999999, 18))
        self.calc_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.calc_label)

        self.calc_lineEdit = QLineEdit(self.contribs)
        self.calc_lineEdit.setObjectName(u"calc_lineEdit")
        self.calc_lineEdit.setMinimumSize(QSize(180, 31))
        self.calc_lineEdit.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_9.addWidget(self.calc_lineEdit)

        self.horizontalLayout_9.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.balance_label = QLabel(self.contribs)
        self.balance_label.setObjectName(u"balance_label")
        sizePolicy2.setHeightForWidth(self.balance_label.sizePolicy().hasHeightForWidth())
        self.balance_label.setSizePolicy(sizePolicy2)
        self.balance_label.setMinimumSize(QSize(0, 18))
        self.balance_label.setMaximumSize(QSize(999999, 18))
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.balance_label)

        self.balance_lineEdit = QLineEdit(self.contribs)
        self.balance_lineEdit.setObjectName(u"balance_lineEdit")
        self.balance_lineEdit.setMinimumSize(QSize(180, 31))
        self.balance_lineEdit.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_10.addWidget(self.balance_lineEdit)

        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 0, 1, 2)

        self.tabWidget.addTab(self.contribs, "")
        self.auto = QWidget()
        self.auto.setObjectName(u"auto")
        self.gridLayout_3 = QGridLayout(self.auto)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.auto_tableView = QTableView(self.auto)
        self.auto_tableView.setObjectName(u"auto_tableView")

        self.gridLayout_3.addWidget(self.auto_tableView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.auto, "")
        self.documents = QWidget()
        self.documents.setObjectName(u"documents")
        self.gridLayout_4 = QGridLayout(self.documents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.docs_tableView = QTableView(self.documents)
        self.docs_tableView.setObjectName(u"docs_tableView")
        self.docs_tableView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.docs_tableView, 0, 0, 4, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.docsAdd_pushButton = QPushButton(self.documents)
        self.docsAdd_pushButton.setObjectName(u"docsAdd_pushButton")
        self.docsAdd_pushButton.setMaximumSize(QSize(31, 31))

        self.gridLayout_2.addWidget(self.docsAdd_pushButton, 1, 1, 1, 1)

        self.docsDel_pushButton = QPushButton(self.documents)
        self.docsDel_pushButton.setObjectName(u"docsDel_pushButton")
        self.docsDel_pushButton.setMaximumSize(QSize(31, 31))

        self.gridLayout_2.addWidget(self.docsDel_pushButton, 2, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_13, 3, 1, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.documents, "")

        self.verticalLayout_14.addWidget(self.tabWidget)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.change_pushButton = QPushButton(Form)
        self.change_pushButton.setObjectName(u"change_pushButton")
        self.change_pushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.change_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")
        self.close_pushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.close_pushButton)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)

        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430",
                                                       None))
        self.garage_groupBox.setTitle(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0430\u0436", None))
        self.garage_label.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0430\u0436 \u2116", None))
        self.row_label.setText(QCoreApplication.translate("Form", u"\u0420\u044f\u0434 \u2116", None))
        self.buildYear_label.setText(QCoreApplication.translate("Form",
                                                                u"\u0413\u043e\u0434 \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438",
                                                                None))
        self.buildingYear_dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy", None))
        self.kadastr_label.setText(QCoreApplication.translate("Form",
                                                              u"\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440",
                                                              None))
        self.width_label_2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.addSize_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.photo_label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e", None))
        self.image_pushButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.ownerFIO_label.setText(
            QCoreApplication.translate("Form", u"\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a",
                                       None))
        self.ownerPhone_label.setText(
            QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.electricMeter_label.setText(QCoreApplication.translate("Form",
                                                                    u"\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0438:",
                                                                    None))
        self.electricAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.electricDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.users_label.setText(QCoreApplication.translate("Form",
                                                            u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438",
                                                            None))
        self.userAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.userDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.contribAdd_pushButton_2.setText(QCoreApplication.translate("Form", u"+", None))
        self.contribDel_pushButton_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.prevDebt_label.setText(QCoreApplication.translate("Form",
                                                               u"\u0414\u043e\u043b\u0433 \u0437\u0430 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434",
                                                               None))
        self.calc_label.setText(QCoreApplication.translate("Form",
                                                           u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f",
                                                           None))
        self.balance_label.setText(
            QCoreApplication.translate("Form", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0441\u0447\u0435\u0442\u0430",
                                       None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contribs),
                                  QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u0442\u0435\u0436\u0438",
                                                             None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.auto), QCoreApplication.translate("Form",
                                                                                                u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438",
                                                                                                None))
        self.docsAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.docsDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.documents), QCoreApplication.translate("Form",
                                                                                                     u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b",
                                                                                                     None))
        self.change_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

