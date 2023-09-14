# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart_.ui'
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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(817, 1080)
        self.verticalLayout_35 = QVBoxLayout(Form)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.garage_groupBox = QGroupBox(Form)
        self.garage_groupBox.setObjectName(u"garage_groupBox")
        self.garage_groupBox.setMinimumSize(QSize(1, 0))
        self.garage_groupBox.setMaximumSize(QSize(16777215, 99999))
        self.verticalLayout_32 = QVBoxLayout(self.garage_groupBox)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.garage_label = QLabel(self.garage_groupBox)
        self.garage_label.setObjectName(u"garage_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.garage_label.sizePolicy().hasHeightForWidth())
        self.garage_label.setSizePolicy(sizePolicy)
        self.garage_label.setMaximumSize(QSize(61, 31))

        self.verticalLayout.addWidget(self.garage_label)

        self.row_label = QLabel(self.garage_groupBox)
        self.row_label.setObjectName(u"row_label")
        sizePolicy.setHeightForWidth(self.row_label.sizePolicy().hasHeightForWidth())
        self.row_label.setSizePolicy(sizePolicy)
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


        self.horizontalLayout_17.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

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


        self.horizontalLayout_17.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.photo_label = QLabel(self.garage_groupBox)
        self.photo_label.setObjectName(u"photo_label")
        self.photo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.photo_label)

        self.image_pushButton = QPushButton(self.garage_groupBox)
        self.image_pushButton.setObjectName(u"image_pushButton")

        self.verticalLayout_3.addWidget(self.image_pushButton)


        self.horizontalLayout_17.addLayout(self.verticalLayout_3)


        self.verticalLayout_32.addLayout(self.horizontalLayout_17)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.width_label = QLabel(self.garage_groupBox)
        self.width_label.setObjectName(u"width_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.width_label.sizePolicy().hasHeightForWidth())
        self.width_label.setSizePolicy(sizePolicy1)
        self.width_label.setMinimumSize(QSize(119, 22))
        self.width_label.setMaximumSize(QSize(9999999, 22))
        self.width_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.width_label)

        self.width_lineEdit = QLineEdit(self.garage_groupBox)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_4.addWidget(self.width_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.len_label = QLabel(self.garage_groupBox)
        self.len_label.setObjectName(u"len_label")
        sizePolicy1.setHeightForWidth(self.len_label.sizePolicy().hasHeightForWidth())
        self.len_label.setSizePolicy(sizePolicy1)
        self.len_label.setMinimumSize(QSize(119, 22))
        self.len_label.setMaximumSize(QSize(99999, 22))
        self.len_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.len_label)

        self.len_lineEdit = QLineEdit(self.garage_groupBox)
        self.len_lineEdit.setObjectName(u"len_lineEdit")
        self.len_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_7.addWidget(self.len_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.hight_label = QLabel(self.garage_groupBox)
        self.hight_label.setObjectName(u"hight_label")
        sizePolicy1.setHeightForWidth(self.hight_label.sizePolicy().hasHeightForWidth())
        self.hight_label.setSizePolicy(sizePolicy1)
        self.hight_label.setMinimumSize(QSize(119, 22))
        self.hight_label.setMaximumSize(QSize(99999, 22))
        self.hight_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.hight_label)

        self.hight_lineEdit = QLineEdit(self.garage_groupBox)
        self.hight_lineEdit.setObjectName(u"hight_lineEdit")
        self.hight_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_8.addWidget(self.hight_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.verticalLayout_32.addLayout(self.verticalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetMaximumSize)
        self.elMetric220_label = QLabel(self.garage_groupBox)
        self.elMetric220_label.setObjectName(u"elMetric220_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.elMetric220_label.sizePolicy().hasHeightForWidth())
        self.elMetric220_label.setSizePolicy(sizePolicy2)
        self.elMetric220_label.setMinimumSize(QSize(232, 31))
        self.elMetric220_label.setMaximumSize(QSize(16777215, 31))
        self.elMetric220_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.elMetric220_label)

        self.elMetric220_lineEdit = QLineEdit(self.garage_groupBox)
        self.elMetric220_lineEdit.setObjectName(u"elMetric220_lineEdit")
        self.elMetric220_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_10.addWidget(self.elMetric220_lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.curentValue220_label = QLabel(self.garage_groupBox)
        self.curentValue220_label.setObjectName(u"curentValue220_label")
        sizePolicy.setHeightForWidth(self.curentValue220_label.sizePolicy().hasHeightForWidth())
        self.curentValue220_label.setSizePolicy(sizePolicy)
        self.curentValue220_label.setMaximumSize(QSize(10000, 31))
        self.curentValue220_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.curentValue220_label)

        self.currentValue220_lineEdit = QLineEdit(self.garage_groupBox)
        self.currentValue220_lineEdit.setObjectName(u"currentValue220_lineEdit")
        self.currentValue220_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_5.addWidget(self.currentValue220_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.newValue220_label = QLabel(self.garage_groupBox)
        self.newValue220_label.setObjectName(u"newValue220_label")
        sizePolicy.setHeightForWidth(self.newValue220_label.sizePolicy().hasHeightForWidth())
        self.newValue220_label.setSizePolicy(sizePolicy)
        self.newValue220_label.setMaximumSize(QSize(100000, 31))
        self.newValue220_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.newValue220_label)

        self.newValue220_lineEdit = QLineEdit(self.garage_groupBox)
        self.newValue220_lineEdit.setObjectName(u"newValue220_lineEdit")
        self.newValue220_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_6.addWidget(self.newValue220_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetMinimumSize)
        self.elMetric380_label = QLabel(self.garage_groupBox)
        self.elMetric380_label.setObjectName(u"elMetric380_label")
        sizePolicy2.setHeightForWidth(self.elMetric380_label.sizePolicy().hasHeightForWidth())
        self.elMetric380_label.setSizePolicy(sizePolicy2)
        self.elMetric380_label.setMinimumSize(QSize(232, 31))
        self.elMetric380_label.setMaximumSize(QSize(16777215, 31))
        self.elMetric380_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.elMetric380_label)

        self.elMetric380_lineEdit = QLineEdit(self.garage_groupBox)
        self.elMetric380_lineEdit.setObjectName(u"elMetric380_lineEdit")
        self.elMetric380_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_11.addWidget(self.elMetric380_lineEdit)


        self.verticalLayout_24.addLayout(self.verticalLayout_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.curentValue380_label = QLabel(self.garage_groupBox)
        self.curentValue380_label.setObjectName(u"curentValue380_label")
        sizePolicy.setHeightForWidth(self.curentValue380_label.sizePolicy().hasHeightForWidth())
        self.curentValue380_label.setSizePolicy(sizePolicy)
        self.curentValue380_label.setMaximumSize(QSize(10000, 31))
        self.curentValue380_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.curentValue380_label)

        self.currentValue380_lineEdit = QLineEdit(self.garage_groupBox)
        self.currentValue380_lineEdit.setObjectName(u"currentValue380_lineEdit")
        self.currentValue380_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_22.addWidget(self.currentValue380_lineEdit)


        self.horizontalLayout_6.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.newValue380_label = QLabel(self.garage_groupBox)
        self.newValue380_label.setObjectName(u"newValue380_label")
        sizePolicy.setHeightForWidth(self.newValue380_label.sizePolicy().hasHeightForWidth())
        self.newValue380_label.setSizePolicy(sizePolicy)
        self.newValue380_label.setMaximumSize(QSize(100000, 31))
        self.newValue380_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.newValue380_label)

        self.newValue380_lineEdit = QLineEdit(self.garage_groupBox)
        self.newValue380_lineEdit.setObjectName(u"newValue380_lineEdit")
        self.newValue380_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_23.addWidget(self.newValue380_lineEdit)


        self.horizontalLayout_6.addLayout(self.verticalLayout_23)


        self.verticalLayout_24.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_24)


        self.verticalLayout_32.addLayout(self.horizontalLayout_11)


        self.verticalLayout_35.addWidget(self.garage_groupBox)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.owner_groupBox = QGroupBox(Form)
        self.owner_groupBox.setObjectName(u"owner_groupBox")
        self.verticalLayout_21 = QVBoxLayout(self.owner_groupBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.surname_label = QLabel(self.owner_groupBox)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setMaximumSize(QSize(16777215, 31))
        self.surname_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.surname_label)

        self.surnamename_lineEdit = QLineEdit(self.owner_groupBox)
        self.surnamename_lineEdit.setObjectName(u"surnamename_lineEdit")
        self.surnamename_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_14.addWidget(self.surnamename_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.name_label = QLabel(self.owner_groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMaximumSize(QSize(16777215, 31))
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.owner_groupBox)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_13.addWidget(self.name_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_13)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.secondName_label = QLabel(self.owner_groupBox)
        self.secondName_label.setObjectName(u"secondName_label")
        self.secondName_label.setMaximumSize(QSize(16777215, 31))
        self.secondName_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.secondName_label)

        self.secondName_lineEdit = QLineEdit(self.owner_groupBox)
        self.secondName_lineEdit.setObjectName(u"secondName_lineEdit")
        self.secondName_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_15.addWidget(self.secondName_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)


        self.verticalLayout_21.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.dateBirdth_label = QLabel(self.owner_groupBox)
        self.dateBirdth_label.setObjectName(u"dateBirdth_label")
        self.dateBirdth_label.setMaximumSize(QSize(109, 16777215))
        self.dateBirdth_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.dateBirdth_label)

        self.dateBirdth_dateEdit = QDateEdit(self.owner_groupBox)
        self.dateBirdth_dateEdit.setObjectName(u"dateBirdth_dateEdit")
        self.dateBirdth_dateEdit.setMinimumSize(QSize(0, 31))
        self.dateBirdth_dateEdit.setMaximumSize(QSize(109, 31))
        self.dateBirdth_dateEdit.setMinimumDate(QDate(1900, 1, 1))

        self.verticalLayout_18.addWidget(self.dateBirdth_dateEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_18)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.phone_label = QLabel(self.owner_groupBox)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(0, 31))
        self.phone_label.setMaximumSize(QSize(16777215, 31))
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.phone_label)

        self.phone_lineEdit = QLineEdit(self.owner_groupBox)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_16.addWidget(self.phone_lineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.addPhone_label = QLabel(self.owner_groupBox)
        self.addPhone_label.setObjectName(u"addPhone_label")
        self.addPhone_label.setMinimumSize(QSize(0, 31))
        self.addPhone_label.setMaximumSize(QSize(16777215, 31))
        self.addPhone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.addPhone_label)

        self.addPhone_lineEdit = QLineEdit(self.owner_groupBox)
        self.addPhone_lineEdit.setObjectName(u"addPhone_lineEdit")
        self.addPhone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_17.addWidget(self.addPhone_lineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.address_label = QLabel(self.owner_groupBox)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 31))
        self.address_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_9.addWidget(self.address_label)

        self.address_textEdit = QTextEdit(self.owner_groupBox)
        self.address_textEdit.setObjectName(u"address_textEdit")
        self.address_textEdit.setMinimumSize(QSize(0, 31))
        self.address_textEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_9.addWidget(self.address_textEdit)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_15.addWidget(self.owner_groupBox)

        self.arenda_groupBox = QGroupBox(Form)
        self.arenda_groupBox.setObjectName(u"arenda_groupBox")
        self.verticalLayout_25 = QVBoxLayout(self.arenda_groupBox)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.arendaSurname_label = QLabel(self.arenda_groupBox)
        self.arendaSurname_label.setObjectName(u"arendaSurname_label")
        self.arendaSurname_label.setMaximumSize(QSize(16777215, 31))
        self.arendaSurname_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.arendaSurname_label)

        self.arendaSurnamename_lineEdit = QLineEdit(self.arenda_groupBox)
        self.arendaSurnamename_lineEdit.setObjectName(u"arendaSurnamename_lineEdit")
        self.arendaSurnamename_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_26.addWidget(self.arendaSurnamename_lineEdit)


        self.horizontalLayout_12.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.arendaName_label = QLabel(self.arenda_groupBox)
        self.arendaName_label.setObjectName(u"arendaName_label")
        self.arendaName_label.setMaximumSize(QSize(16777215, 31))
        self.arendaName_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.arendaName_label)

        self.arendaName_lineEdit = QLineEdit(self.arenda_groupBox)
        self.arendaName_lineEdit.setObjectName(u"arendaName_lineEdit")
        self.arendaName_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_27.addWidget(self.arendaName_lineEdit)


        self.horizontalLayout_12.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.arendaSecondName_label = QLabel(self.arenda_groupBox)
        self.arendaSecondName_label.setObjectName(u"arendaSecondName_label")
        self.arendaSecondName_label.setMaximumSize(QSize(16777215, 31))
        self.arendaSecondName_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.arendaSecondName_label)

        self.arendaSecondName_lineEdit = QLineEdit(self.arenda_groupBox)
        self.arendaSecondName_lineEdit.setObjectName(u"arendaSecondName_lineEdit")
        self.arendaSecondName_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_28.addWidget(self.arendaSecondName_lineEdit)


        self.horizontalLayout_12.addLayout(self.verticalLayout_28)


        self.verticalLayout_25.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.arendaDateBirdth_label = QLabel(self.arenda_groupBox)
        self.arendaDateBirdth_label.setObjectName(u"arendaDateBirdth_label")
        self.arendaDateBirdth_label.setMaximumSize(QSize(109, 16777215))
        self.arendaDateBirdth_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.arendaDateBirdth_label)

        self.arendaDateBirdth_dateEdit = QDateEdit(self.arenda_groupBox)
        self.arendaDateBirdth_dateEdit.setObjectName(u"arendaDateBirdth_dateEdit")
        self.arendaDateBirdth_dateEdit.setMinimumSize(QSize(0, 31))
        self.arendaDateBirdth_dateEdit.setMaximumSize(QSize(109, 31))
        self.arendaDateBirdth_dateEdit.setMinimumDate(QDate(1900, 1, 1))

        self.verticalLayout_29.addWidget(self.arendaDateBirdth_dateEdit)


        self.horizontalLayout_13.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.arendaPhone_label = QLabel(self.arenda_groupBox)
        self.arendaPhone_label.setObjectName(u"arendaPhone_label")
        self.arendaPhone_label.setMinimumSize(QSize(0, 31))
        self.arendaPhone_label.setMaximumSize(QSize(16777215, 31))
        self.arendaPhone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.arendaPhone_label)

        self.arendaPhone_lineEdit = QLineEdit(self.arenda_groupBox)
        self.arendaPhone_lineEdit.setObjectName(u"arendaPhone_lineEdit")
        self.arendaPhone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_30.addWidget(self.arendaPhone_lineEdit)


        self.horizontalLayout_13.addLayout(self.verticalLayout_30)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.arendaAddPhone_label = QLabel(self.arenda_groupBox)
        self.arendaAddPhone_label.setObjectName(u"arendaAddPhone_label")
        self.arendaAddPhone_label.setMinimumSize(QSize(0, 31))
        self.arendaAddPhone_label.setMaximumSize(QSize(16777215, 31))
        self.arendaAddPhone_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.arendaAddPhone_label)

        self.arendaAddPhone_lineEdit = QLineEdit(self.arenda_groupBox)
        self.arendaAddPhone_lineEdit.setObjectName(u"arendaAddPhone_lineEdit")
        self.arendaAddPhone_lineEdit.setMinimumSize(QSize(0, 31))

        self.verticalLayout_31.addWidget(self.arendaAddPhone_lineEdit)


        self.horizontalLayout_13.addLayout(self.verticalLayout_31)


        self.verticalLayout_25.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.arendaAddress_label = QLabel(self.arenda_groupBox)
        self.arendaAddress_label.setObjectName(u"arendaAddress_label")
        self.arendaAddress_label.setMinimumSize(QSize(0, 31))
        self.arendaAddress_label.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_14.addWidget(self.arendaAddress_label)

        self.arendaAddress_textEdit = QTextEdit(self.arenda_groupBox)
        self.arendaAddress_textEdit.setObjectName(u"arendaAddress_textEdit")
        self.arendaAddress_textEdit.setMinimumSize(QSize(0, 31))
        self.arendaAddress_textEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_14.addWidget(self.arendaAddress_textEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addWidget(self.arenda_groupBox)


        self.verticalLayout_35.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.auto_label = QLabel(Form)
        self.auto_label.setObjectName(u"auto_label")
        self.auto_label.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout_19.addWidget(self.auto_label)

        self.auto_tableView = QTableView(Form)
        self.auto_tableView.setObjectName(u"auto_tableView")
        self.auto_tableView.setMaximumSize(QSize(16777215, 62))

        self.verticalLayout_19.addWidget(self.auto_tableView)


        self.horizontalLayout_18.addLayout(self.verticalLayout_19)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_2)

        self.carAdd_pushButton = QPushButton(Form)
        self.carAdd_pushButton.setObjectName(u"carAdd_pushButton")
        self.carAdd_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_34.addWidget(self.carAdd_pushButton)

        self.carDel_pushButton = QPushButton(Form)
        self.carDel_pushButton.setObjectName(u"carDel_pushButton")
        self.carDel_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_34.addWidget(self.carDel_pushButton)


        self.horizontalLayout_18.addLayout(self.verticalLayout_34)


        self.verticalLayout_35.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.contrib_label = QLabel(Form)
        self.contrib_label.setObjectName(u"contrib_label")

        self.verticalLayout_20.addWidget(self.contrib_label)

        self.contrib_tableView = QTableView(Form)
        self.contrib_tableView.setObjectName(u"contrib_tableView")

        self.verticalLayout_20.addWidget(self.contrib_tableView)


        self.horizontalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)

        self.conribAdd_pushButton = QPushButton(Form)
        self.conribAdd_pushButton.setObjectName(u"conribAdd_pushButton")
        self.conribAdd_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_33.addWidget(self.conribAdd_pushButton)

        self.contribDel_pushButton = QPushButton(Form)
        self.contribDel_pushButton.setObjectName(u"contribDel_pushButton")
        self.contribDel_pushButton.setMaximumSize(QSize(31, 31))

        self.verticalLayout_33.addWidget(self.contribDel_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_3)


        self.horizontalLayout_19.addLayout(self.verticalLayout_33)


        self.verticalLayout_35.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_10 = QHBoxLayout()
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


        self.verticalLayout_35.addLayout(self.horizontalLayout_10)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.garage_groupBox.setTitle(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0430\u0436", None))
        self.garage_label.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0430\u0436 \u2116", None))
        self.row_label.setText(QCoreApplication.translate("Form", u"\u0420\u044f\u0434 \u2116", None))
        self.buildYear_label.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0434 \u043f\u043e\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.buildingYear_dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy", None))
        self.kadastr_label.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u0440\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.photo_label.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e", None))
        self.image_pushButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.width_label.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.len_label.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.hight_label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.elMetric220_label.setText(QCoreApplication.translate("Form", u"\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0447\u0435\u0442\u0447\u0438\u043a (220 \u0412)", None))
        self.curentValue220_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a. \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.newValue220_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432. \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.elMetric380_label.setText(QCoreApplication.translate("Form", u"\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0447\u0435\u0442\u0447\u0438\u043a (380 \u0412)", None))
        self.curentValue380_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a. \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.newValue380_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432. \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.owner_groupBox.setTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a", None))
        self.surname_label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.secondName_label.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.dateBirdth_label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.addPhone_label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.address_label.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.arenda_groupBox.setTitle(QCoreApplication.translate("Form", u"\u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440", None))
        self.arendaSurname_label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.arendaName_label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.arendaSecondName_label.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.arendaDateBirdth_label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.arendaPhone_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.arendaAddPhone_label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.arendaAddress_label.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.auto_label.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c", None))
        self.carAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.carDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.contrib_label.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
        self.conribAdd_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.contribDel_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.change_pushButton.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

