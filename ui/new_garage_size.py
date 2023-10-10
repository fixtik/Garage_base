# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_garage_size1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(357, 281)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 15, 341, 58))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.kindContrib_label_2 = QLabel(self.layoutWidget)
        self.kindContrib_label_2.setObjectName(u"kindContrib_label_2")

        self.verticalLayout_5.addWidget(self.kindContrib_label_2)

        self.size_comboBox = QComboBox(self.layoutWidget)
        self.size_comboBox.setObjectName(u"size_comboBox")

        self.verticalLayout_5.addWidget(self.size_comboBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.addSize_pushButton = QPushButton(self.layoutWidget)
        self.addSize_pushButton.setObjectName(u"addSize_pushButton")
        self.addSize_pushButton.setMaximumSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.addSize_pushButton)

        self.delSize_pushButton = QPushButton(self.layoutWidget)
        self.delSize_pushButton.setObjectName(u"delSize_pushButton")
        self.delSize_pushButton.setMaximumSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.delSize_pushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 140, 341, 47))
        self.comment_verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.comment_verticalLayout_9.setObjectName(u"comment_verticalLayout_9")
        self.comment_verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.commentContrib_label_2 = QLabel(self.verticalLayoutWidget_4)
        self.commentContrib_label_2.setObjectName(u"commentContrib_label_2")

        self.comment_verticalLayout_9.addWidget(self.commentContrib_label_2)

        self.commentContrib_lineEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.commentContrib_lineEdit.setObjectName(u"commentContrib_lineEdit")

        self.comment_verticalLayout_9.addWidget(self.commentContrib_lineEdit)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 341, 51))
        self.horizontalLayoutWidget.setMaximumSize(QSize(16777215, 51))
        self.size_horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.size_horizontalLayout_5.setObjectName(u"size_horizontalLayout_5")
        self.size_horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.width_label = QLabel(self.horizontalLayoutWidget)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_20.addWidget(self.width_label)

        self.width_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setMinimumSize(QSize(0, 20))
        self.width_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.width_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.length_label = QLabel(self.horizontalLayoutWidget)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_21.addWidget(self.length_label)

        self.length_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.length_lineEdit.setObjectName(u"length_lineEdit")
        self.length_lineEdit.setMinimumSize(QSize(0, 20))
        self.length_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_21.addWidget(self.length_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.height__label = QLabel(self.horizontalLayoutWidget)
        self.height__label.setObjectName(u"height__label")
        self.height__label.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_23.addWidget(self.height__label)

        self.height_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.height_lineEdit.setObjectName(u"height_lineEdit")
        self.height_lineEdit.setMinimumSize(QSize(0, 20))
        self.height_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_23.addWidget(self.height_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_23)

        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 230, 341, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.ok_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout_11.addWidget(self.ok_pushButton)

        self.close_pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_11.addWidget(self.close_pushButton)

        QWidget.setTabOrder(self.size_comboBox, self.addSize_pushButton)
        QWidget.setTabOrder(self.addSize_pushButton, self.delSize_pushButton)
        QWidget.setTabOrder(self.delSize_pushButton, self.width_lineEdit)
        QWidget.setTabOrder(self.width_lineEdit, self.length_lineEdit)
        QWidget.setTabOrder(self.length_lineEdit, self.height_lineEdit)
        QWidget.setTabOrder(self.height_lineEdit, self.commentContrib_lineEdit)
        QWidget.setTabOrder(self.commentContrib_lineEdit, self.ok_pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.kindContrib_label_2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440\u044b \u0433\u0430\u0440\u0430\u0436\u0430:", None))
        self.addSize_pushButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.delSize_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.commentContrib_label_2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.width_label.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.length_label.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430:", None))
        self.height__label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

