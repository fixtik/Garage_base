# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_garage_size.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(357, 281)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 15, 341, 56))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kindContrib_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.kindContrib_label_2.setObjectName("kindContrib_label_2")
        self.verticalLayout_5.addWidget(self.kindContrib_label_2)
        self.kindContrib_comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.kindContrib_comboBox_2.setObjectName("kindContrib_comboBox_2")
        self.verticalLayout_5.addWidget(self.kindContrib_comboBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addKind_pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.addKind_pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.addKind_pushButton_2.setObjectName("addKind_pushButton_2")
        self.verticalLayout_3.addWidget(self.addKind_pushButton_2)
        self.delKind_pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.delKind_pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.delKind_pushButton_2.setObjectName("delKind_pushButton_2")
        self.verticalLayout_3.addWidget(self.delKind_pushButton_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 140, 341, 47))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.comment_verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.comment_verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.comment_verticalLayout_9.setObjectName("comment_verticalLayout_9")
        self.commentContrib_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.commentContrib_label_2.setObjectName("commentContrib_label_2")
        self.comment_verticalLayout_9.addWidget(self.commentContrib_label_2)
        self.commentContrib_lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.commentContrib_lineEdit_2.setObjectName("commentContrib_lineEdit_2")
        self.comment_verticalLayout_9.addWidget(self.commentContrib_lineEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 341, 51))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(16777215, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.size_horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.size_horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.size_horizontalLayout_5.setObjectName("size_horizontalLayout_5")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.sumContrib_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sumContrib_label_2.setMaximumSize(QtCore.QSize(16777215, 21))
        self.sumContrib_label_2.setObjectName("sumContrib_label_2")
        self.verticalLayout_20.addWidget(self.sumContrib_label_2)
        self.sumContrib_lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sumContrib_lineEdit_2.setMinimumSize(QtCore.QSize(0, 20))
        self.sumContrib_lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sumContrib_lineEdit_2.setObjectName("sumContrib_lineEdit_2")
        self.verticalLayout_20.addWidget(self.sumContrib_lineEdit_2)
        self.size_horizontalLayout_5.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.sumContrib_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sumContrib_label_3.setMaximumSize(QtCore.QSize(16777215, 21))
        self.sumContrib_label_3.setObjectName("sumContrib_label_3")
        self.verticalLayout_21.addWidget(self.sumContrib_label_3)
        self.sumContrib_lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sumContrib_lineEdit_3.setMinimumSize(QtCore.QSize(0, 20))
        self.sumContrib_lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sumContrib_lineEdit_3.setObjectName("sumContrib_lineEdit_3")
        self.verticalLayout_21.addWidget(self.sumContrib_lineEdit_3)
        self.size_horizontalLayout_5.addLayout(self.verticalLayout_21)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.sumContrib_label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sumContrib_label_4.setMaximumSize(QtCore.QSize(16777215, 21))
        self.sumContrib_label_4.setObjectName("sumContrib_label_4")
        self.verticalLayout_23.addWidget(self.sumContrib_label_4)
        self.sumContrib_lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sumContrib_lineEdit_5.setMinimumSize(QtCore.QSize(0, 20))
        self.sumContrib_lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sumContrib_lineEdit_5.setObjectName("sumContrib_lineEdit_5")
        self.verticalLayout_23.addWidget(self.sumContrib_lineEdit_5)
        self.size_horizontalLayout_5.addLayout(self.verticalLayout_23)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 341, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.close_pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.close_pushButton_5.setObjectName("close_pushButton_5")
        self.horizontalLayout_11.addWidget(self.close_pushButton_5)
        self.ok_pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ok_pushButton_5.setObjectName("ok_pushButton_5")
        self.horizontalLayout_11.addWidget(self.ok_pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.kindContrib_comboBox_2, self.addKind_pushButton_2)
        Form.setTabOrder(self.addKind_pushButton_2, self.delKind_pushButton_2)
        Form.setTabOrder(self.delKind_pushButton_2, self.sumContrib_lineEdit_2)
        Form.setTabOrder(self.sumContrib_lineEdit_2, self.sumContrib_lineEdit_3)
        Form.setTabOrder(self.sumContrib_lineEdit_3, self.sumContrib_lineEdit_5)
        Form.setTabOrder(self.sumContrib_lineEdit_5, self.commentContrib_lineEdit_2)
        Form.setTabOrder(self.commentContrib_lineEdit_2, self.close_pushButton_5)
        Form.setTabOrder(self.close_pushButton_5, self.ok_pushButton_5)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.kindContrib_label_2.setText(_translate("Form", "Размеры гаража:"))
        self.addKind_pushButton_2.setText(_translate("Form", "+"))
        self.delKind_pushButton_2.setText(_translate("Form", "-"))
        self.commentContrib_label_2.setText(_translate("Form", "Комментарий:"))
        self.sumContrib_label_2.setText(_translate("Form", "Ширина:"))
        self.sumContrib_label_3.setText(_translate("Form", "Длина:"))
        self.sumContrib_label_4.setText(_translate("Form", "Высота:"))
        self.close_pushButton_5.setText(_translate("Form", "Закрыть"))
        self.ok_pushButton_5.setText(_translate("Form", "Применить"))
