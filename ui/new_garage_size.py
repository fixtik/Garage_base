# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_garage_size.ui'
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
        Form.resize(357, 224)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.size_label = QLabel(Form)
        self.size_label.setObjectName(u"size_label")

        self.verticalLayout_5.addWidget(self.size_label)

        self.size_comboBox = QComboBox(Form)
        self.size_comboBox.setObjectName(u"size_comboBox")
        self.size_comboBox.setMinimumSize(QSize(0, 30))
        self.size_comboBox.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.size_comboBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.delSize_pushButton = QPushButton(Form)
        self.delSize_pushButton.setObjectName(u"delSize_pushButton")
        self.delSize_pushButton.setMinimumSize(QSize(0, 30))
        self.delSize_pushButton.setMaximumSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.delSize_pushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.size_horizontalLayout_5 = QHBoxLayout()
        self.size_horizontalLayout_5.setObjectName(u"size_horizontalLayout_5")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.sumContrib_label_2 = QLabel(Form)
        self.sumContrib_label_2.setObjectName(u"sumContrib_label_2")
        self.sumContrib_label_2.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_20.addWidget(self.sumContrib_label_2)

        self.width_lineEdit = QLineEdit(Form)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setMinimumSize(QSize(0, 20))
        self.width_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.width_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.sumContrib_label_3 = QLabel(Form)
        self.sumContrib_label_3.setObjectName(u"sumContrib_label_3")
        self.sumContrib_label_3.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_21.addWidget(self.sumContrib_label_3)

        self.length_lineEdit = QLineEdit(Form)
        self.length_lineEdit.setObjectName(u"length_lineEdit")
        self.length_lineEdit.setMinimumSize(QSize(0, 20))
        self.length_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_21.addWidget(self.length_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_21)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.sumContrib_label_4 = QLabel(Form)
        self.sumContrib_label_4.setObjectName(u"sumContrib_label_4")
        self.sumContrib_label_4.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_23.addWidget(self.sumContrib_label_4)

        self.height_lineEdit = QLineEdit(Form)
        self.height_lineEdit.setObjectName(u"height_lineEdit")
        self.height_lineEdit.setMinimumSize(QSize(0, 20))
        self.height_lineEdit.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_23.addWidget(self.height_lineEdit)


        self.size_horizontalLayout_5.addLayout(self.verticalLayout_23)


        self.verticalLayout_2.addLayout(self.size_horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comment_verticalLayout_9 = QVBoxLayout()
        self.comment_verticalLayout_9.setObjectName(u"comment_verticalLayout_9")
        self.contrib_label = QLabel(Form)
        self.contrib_label.setObjectName(u"contrib_label")

        self.comment_verticalLayout_9.addWidget(self.contrib_label)

        self.contrib_lineEdit = QLineEdit(Form)
        self.contrib_lineEdit.setObjectName(u"contrib_lineEdit")

        self.comment_verticalLayout_9.addWidget(self.contrib_lineEdit)


        self.horizontalLayout.addLayout(self.comment_verticalLayout_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comment_label = QLabel(Form)
        self.comment_label.setObjectName(u"comment_label")

        self.verticalLayout.addWidget(self.comment_label)

        self.comment_lineEdit = QLineEdit(Form)
        self.comment_lineEdit.setObjectName(u"comment_lineEdit")

        self.verticalLayout.addWidget(self.comment_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.ok_pushButton = QPushButton(Form)
        self.ok_pushButton.setObjectName(u"ok_pushButton")

        self.horizontalLayout_11.addWidget(self.ok_pushButton)

        self.change_pushButton = QPushButton(Form)
        self.change_pushButton.setObjectName(u"change_pushButton")

        self.horizontalLayout_11.addWidget(self.change_pushButton)

        self.close_pushButton = QPushButton(Form)
        self.close_pushButton.setObjectName(u"close_pushButton")

        self.horizontalLayout_11.addWidget(self.close_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        QWidget.setTabOrder(self.size_comboBox, self.delSize_pushButton)
        QWidget.setTabOrder(self.delSize_pushButton, self.width_lineEdit)
        QWidget.setTabOrder(self.width_lineEdit, self.length_lineEdit)
        QWidget.setTabOrder(self.length_lineEdit, self.height_lineEdit)
        QWidget.setTabOrder(self.height_lineEdit, self.contrib_lineEdit)
        QWidget.setTabOrder(self.contrib_lineEdit, self.close_pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.size_label.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440\u044b \u0433\u0430\u0440\u0430\u0436\u0430:", None))
        self.delSize_pushButton.setText(QCoreApplication.translate("Form", u"-", None))
        self.sumContrib_label_2.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.sumContrib_label_3.setText(QCoreApplication.translate("Form", u"\u0414\u043b\u0438\u043d\u0430:", None))
        self.sumContrib_label_4.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.contrib_label.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u043b\u0430\u0442\u0435\u0436\u0430:", None))
        self.comment_label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.ok_pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439", None))
        self.change_pushButton.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.close_pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

