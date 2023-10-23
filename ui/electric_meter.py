# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'electric_meter.ui'
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
    QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(373, 242)
        self.verticalLayout_9 = QVBoxLayout(Form)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.search_horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.search_horizontalLayout.setObjectName(u"search_horizontalLayout")
        self.search_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.garajeNum_label = QLabel(self.layoutWidget)
        self.garajeNum_label.setObjectName(u"garajeNum_label")

        self.verticalLayout.addWidget(self.garajeNum_label)

        self.row_label = QLabel(self.layoutWidget)
        self.row_label.setObjectName(u"row_label")

        self.verticalLayout.addWidget(self.row_label)


        self.search_horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.garajeNum_lineEdit = QLineEdit(self.layoutWidget)
        self.garajeNum_lineEdit.setObjectName(u"garajeNum_lineEdit")

        self.verticalLayout_2.addWidget(self.garajeNum_lineEdit)

        self.row_lineEdit = QLineEdit(self.layoutWidget)
        self.row_lineEdit.setObjectName(u"row_lineEdit")

        self.verticalLayout_2.addWidget(self.row_lineEdit)


        self.search_horizontalLayout.addLayout(self.verticalLayout_2)

        self.splitter.addWidget(self.layoutWidget)
        self.find_pushButton = QPushButton(self.splitter)
        self.find_pushButton.setObjectName(u"find_pushButton")
        self.splitter.addWidget(self.find_pushButton)

        self.verticalLayout_9.addWidget(self.splitter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.meterType_label = QLabel(Form)
        self.meterType_label.setObjectName(u"meterType_label")

        self.verticalLayout_3.addWidget(self.meterType_label)

        self.meterNum_label = QLabel(Form)
        self.meterNum_label.setObjectName(u"meterNum_label")

        self.verticalLayout_3.addWidget(self.meterNum_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.meterType_comboBox = QComboBox(Form)
        self.meterType_comboBox.addItem("")
        self.meterType_comboBox.addItem("")
        self.meterType_comboBox.setObjectName(u"meterType_comboBox")

        self.verticalLayout_4.addWidget(self.meterType_comboBox)

        self.meterNum_lineEdit = QLineEdit(Form)
        self.meterNum_lineEdit.setObjectName(u"meterNum_lineEdit")

        self.verticalLayout_4.addWidget(self.meterNum_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.meterValues_label = QLabel(Form)
        self.meterValues_label.setObjectName(u"meterValues_label")

        self.verticalLayout_9.addWidget(self.meterValues_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.curDay_label = QLabel(Form)
        self.curDay_label.setObjectName(u"curDay_label")

        self.verticalLayout_5.addWidget(self.curDay_label)

        self.curNight_label = QLabel(Form)
        self.curNight_label.setObjectName(u"curNight_label")

        self.verticalLayout_5.addWidget(self.curNight_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.curDay_lineEdit = QLineEdit(Form)
        self.curDay_lineEdit.setObjectName(u"curDay_lineEdit")

        self.verticalLayout_6.addWidget(self.curDay_lineEdit)

        self.curNight_lineEdit = QLineEdit(Form)
        self.curNight_lineEdit.setObjectName(u"curNight_lineEdit")

        self.verticalLayout_6.addWidget(self.curNight_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.newDay_label = QLabel(Form)
        self.newDay_label.setObjectName(u"newDay_label")

        self.verticalLayout_7.addWidget(self.newDay_label)

        self.newNight_label = QLabel(Form)
        self.newNight_label.setObjectName(u"newNight_label")

        self.verticalLayout_7.addWidget(self.newNight_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.newDay_lineEdit = QLineEdit(Form)
        self.newDay_lineEdit.setObjectName(u"newDay_lineEdit")

        self.verticalLayout_8.addWidget(self.newDay_lineEdit)

        self.newNight_lineEdit = QLineEdit(Form)
        self.newNight_lineEdit.setObjectName(u"newNight_lineEdit")

        self.verticalLayout_8.addWidget(self.newNight_lineEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.horizontalLayout_6.addWidget(self.add_pushButton)

        self.del_pushButton = QPushButton(Form)
        self.del_pushButton.setObjectName(u"del_pushButton")

        self.horizontalLayout_6.addWidget(self.del_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_6.addWidget(self.close_pushButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430", None))
        self.garajeNum_label.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0430\u0436 \u2116", None))
        self.row_label.setText(QCoreApplication.translate("Form", u"\u0420\u044f\u0434 \u2116", None))
        self.find_pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.meterType_label.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430", None))
        self.meterNum_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430", None))
        self.meterType_comboBox.setItemText(0, QCoreApplication.translate("Form", u"220 \u0412\u043e\u043b\u044c\u0442", None))
        self.meterType_comboBox.setItemText(1, QCoreApplication.translate("Form", u"380 \u0412\u043e\u043b\u044c\u0442", None))

        self.meterValues_label.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f:", None))
        self.curDay_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u0434\u0435\u043d\u044c ", None))
        self.curNight_label.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435 \u043d\u043e\u0447\u044c", None))
        self.newDay_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0435 \u0434\u0435\u043d\u044c", None))
        self.newNight_label.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0435 \u043d\u043e\u0447\u044c", None))
        self.add_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.del_pushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

