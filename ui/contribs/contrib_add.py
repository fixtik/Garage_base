# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contrib_add.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(349, 349)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.kindContrib_label = QLabel(Form)
        self.kindContrib_label.setObjectName(u"kindContrib_label")

        self.verticalLayout_4.addWidget(self.kindContrib_label)

        self.kindContrib_comboBox = QComboBox(Form)
        self.kindContrib_comboBox.setObjectName(u"kindContrib_comboBox")

        self.verticalLayout_4.addWidget(self.kindContrib_comboBox)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addKind_pushButton = QPushButton(Form)
        self.addKind_pushButton.setObjectName(u"addKind_pushButton")
        self.addKind_pushButton.setMaximumSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.addKind_pushButton)

        self.delKind_pushButton = QPushButton(Form)
        self.delKind_pushButton.setObjectName(u"delKind_pushButton")
        self.delKind_pushButton.setMaximumSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.delKind_pushButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sumContrib_label = QLabel(Form)
        self.sumContrib_label.setObjectName(u"sumContrib_label")

        self.verticalLayout_2.addWidget(self.sumContrib_label)

        self.sumContrib_lineEdit = QLineEdit(Form)
        self.sumContrib_lineEdit.setObjectName(u"sumContrib_lineEdit")

        self.verticalLayout_2.addWidget(self.sumContrib_lineEdit)

        self.commentContrib_label = QLabel(Form)
        self.commentContrib_label.setObjectName(u"commentContrib_label")

        self.verticalLayout_2.addWidget(self.commentContrib_label)

        self.commentContrib_lineEdit = QLineEdit(Form)
        self.commentContrib_lineEdit.setObjectName(u"commentContrib_lineEdit")

        self.verticalLayout_2.addWidget(self.commentContrib_lineEdit)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.typePay_label = QLabel(Form)
        self.typePay_label.setObjectName(u"typePay_label")

        self.verticalLayout_3.addWidget(self.typePay_label)

        self.cash_radioButton = QRadioButton(Form)
        self.cash_radioButton.setObjectName(u"cash_radioButton")

        self.verticalLayout_3.addWidget(self.cash_radioButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.card_radioButton = QRadioButton(Form)
        self.card_radioButton.setObjectName(u"card_radioButton")

        self.horizontalLayout_2.addWidget(self.card_radioButton)

        self.chooseCheck_pushButton = QPushButton(Form)
        self.chooseCheck_pushButton.setObjectName(u"chooseCheck_pushButton")
        self.chooseCheck_pushButton.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.chooseCheck_pushButton)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.nonBalance_checkBox = QCheckBox(Form)
        self.nonBalance_checkBox.setObjectName(u"nonBalance_checkBox")

        self.verticalLayout_5.addWidget(self.nonBalance_checkBox)

        self.payDate_horizontalLayout = QHBoxLayout()
        self.payDate_horizontalLayout.setObjectName(u"payDate_horizontalLayout")
        self.payDate_label = QLabel(Form)
        self.payDate_label.setObjectName(u"payDate_label")

        self.payDate_horizontalLayout.addWidget(self.payDate_label)

        self.payDate_dateEdit = QDateEdit(Form)
        self.payDate_dateEdit.setObjectName(u"payDate_dateEdit")

        self.payDate_horizontalLayout.addWidget(self.payDate_dateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.payDate_horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5.addLayout(self.payDate_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

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

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043b\u0430\u0442\u0435\u0436\u0430",
                                                       None))
        self.kindContrib_label.setText(
            QCoreApplication.translate("Form", u"\u0412\u0438\u0434 \u043f\u043b\u0430\u0442\u0435\u0436\u0430:", None))
        self.addKind_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.delKind_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.sumContrib_label.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u043c\u043c\u0430:", None))
        self.commentContrib_label.setText(
            QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:",
                                       None))
        self.typePay_label.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0430:", None))
        self.cash_radioButton.setText(
            QCoreApplication.translate("Form", u"\u043d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.card_radioButton.setText(
            QCoreApplication.translate("Form", u"\u0431\u0435\u0437\u043d\u0430\u043b\u0438\u0447\u043d\u0430\u044f",
                                       None))
        self.chooseCheck_pushButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label.setText("")
        self.nonBalance_checkBox.setText(QCoreApplication.translate("Form",
                                                                    u"\u041d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u0432 \u0431\u0430\u043b\u0430\u043d\u0441\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430",
                                                                    None))
        self.payDate_label.setText(
            QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430:",
                                       None))
        self.ok_pushButton.setText(
            QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi
