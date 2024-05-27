# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qr_bankInfo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 439)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_Name = QVBoxLayout()
        self.verticalLayout_Name.setObjectName(u"verticalLayout_Name")
        self.Namel_abel = QLabel(Form)
        self.Namel_abel.setObjectName(u"Namel_abel")

        self.verticalLayout_Name.addWidget(self.Namel_abel)

        self.Name_lineEdit = QLineEdit(Form)
        self.Name_lineEdit.setObjectName(u"Name_lineEdit")
        self.Name_lineEdit.setMinimumSize(QSize(0, 22))

        self.verticalLayout_Name.addWidget(self.Name_lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_Name)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.PersonalAcc_verticalLayout = QVBoxLayout()
        self.PersonalAcc_verticalLayout.setObjectName(u"PersonalAcc_verticalLayout")
        self.PersonalAcc_label = QLabel(Form)
        self.PersonalAcc_label.setObjectName(u"PersonalAcc_label")

        self.PersonalAcc_verticalLayout.addWidget(self.PersonalAcc_label)

        self.PersonalAcc_lineEdit = QLineEdit(Form)
        self.PersonalAcc_lineEdit.setObjectName(u"PersonalAcc_lineEdit")
        self.PersonalAcc_lineEdit.setMinimumSize(QSize(0, 22))

        self.PersonalAcc_verticalLayout.addWidget(self.PersonalAcc_lineEdit)


        self.verticalLayout_3.addLayout(self.PersonalAcc_verticalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.BankName_verticalLayout = QVBoxLayout()
        self.BankName_verticalLayout.setObjectName(u"BankName_verticalLayout")
        self.BankName_label = QLabel(Form)
        self.BankName_label.setObjectName(u"BankName_label")

        self.BankName_verticalLayout.addWidget(self.BankName_label)

        self.BankName_lineEdit = QLineEdit(Form)
        self.BankName_lineEdit.setObjectName(u"BankName_lineEdit")
        self.BankName_lineEdit.setMinimumSize(QSize(0, 22))

        self.BankName_verticalLayout.addWidget(self.BankName_lineEdit)


        self.verticalLayout_3.addLayout(self.BankName_verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout_BIC = QVBoxLayout()
        self.verticalLayout_BIC.setObjectName(u"verticalLayout_BIC")
        self.BIC_label = QLabel(Form)
        self.BIC_label.setObjectName(u"BIC_label")

        self.verticalLayout_BIC.addWidget(self.BIC_label)

        self.BIC_lineEdit = QLineEdit(Form)
        self.BIC_lineEdit.setObjectName(u"BIC_lineEdit")
        self.BIC_lineEdit.setMinimumSize(QSize(0, 22))

        self.verticalLayout_BIC.addWidget(self.BIC_lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_BIC)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_CorrespAcc = QVBoxLayout()
        self.verticalLayout_CorrespAcc.setObjectName(u"verticalLayout_CorrespAcc")
        self.CorrespAcc_label = QLabel(Form)
        self.CorrespAcc_label.setObjectName(u"CorrespAcc_label")

        self.verticalLayout_CorrespAcc.addWidget(self.CorrespAcc_label)

        self.CorrespAcc_lineEdit = QLineEdit(Form)
        self.CorrespAcc_lineEdit.setObjectName(u"CorrespAcc_lineEdit")
        self.CorrespAcc_lineEdit.setMinimumSize(QSize(0, 22))

        self.verticalLayout_CorrespAcc.addWidget(self.CorrespAcc_lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_CorrespAcc)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_PayeeINN = QVBoxLayout()
        self.verticalLayout_PayeeINN.setObjectName(u"verticalLayout_PayeeINN")
        self.PayeeINN_label = QLabel(Form)
        self.PayeeINN_label.setObjectName(u"PayeeINN_label")

        self.verticalLayout_PayeeINN.addWidget(self.PayeeINN_label)

        self.PayeeINN_lineEdit = QLineEdit(Form)
        self.PayeeINN_lineEdit.setObjectName(u"PayeeINN_lineEdit")
        self.PayeeINN_lineEdit.setMinimumSize(QSize(0, 22))

        self.verticalLayout_PayeeINN.addWidget(self.PayeeINN_lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_PayeeINN)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_KPP = QVBoxLayout()
        self.verticalLayout_KPP.setObjectName(u"verticalLayout_KPP")
        self.KPP_label = QLabel(Form)
        self.KPP_label.setObjectName(u"KPP_label")

        self.verticalLayout_KPP.addWidget(self.KPP_label)

        self.KPP_lineEdit = QLineEdit(Form)
        self.KPP_lineEdit.setObjectName(u"KPP_lineEdit")
        self.KPP_lineEdit.setMinimumSize(QSize(0, 22))

        self.verticalLayout_KPP.addWidget(self.KPP_lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_KPP)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancel_pushButton_2 = QPushButton(Form)
        self.cancel_pushButton_2.setObjectName(u"cancel_pushButton_2")

        self.horizontalLayout_2.addWidget(self.cancel_pushButton_2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_pushButton = QPushButton(Form)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMinimumSize(QSize(0, 22))

        self.horizontalLayout.addWidget(self.add_pushButton)

        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setMinimumSize(QSize(0, 22))

        self.horizontalLayout.addWidget(self.cancel_pushButton)

        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
                                                       None))
        self.Namel_abel.setText(QCoreApplication.translate("Form",
                                                           u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
                                                           None))
        self.PersonalAcc_label.setText(QCoreApplication.translate("Form",
                                                                  u"\u0420\u0430\u0441\u0447\u0435\u0442\u043d\u044b\u0439 \u0441\u0447\u0435\u0442",
                                                                  None))
        self.BankName_label.setText(QCoreApplication.translate("Form",
                                                               u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0430\u043d\u043a\u0430",
                                                               None))
        self.BIC_label.setText(QCoreApplication.translate("Form", u"\u0411\u0418\u041a", None))
        self.CorrespAcc_label.setText(
            QCoreApplication.translate("Form", u"\u041a\u043e\u0440\u0440. \u0441\u0447\u0435\u0442", None))
        self.PayeeINN_label.setText(QCoreApplication.translate("Form", u"\u0418\u041d\u041d", None))
        self.KPP_label.setText(QCoreApplication.translate("Form", u"\u041a\u041f\u041f", None))
        self.cancel_pushButton_2.setText(QCoreApplication.translate("Form", u"deGenerate", None))
        self.add_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.cancel_pushButton.setText(
            QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

