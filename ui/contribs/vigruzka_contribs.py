# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vigruzka_contribs.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QTabWidget, QTableView,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(785, 497)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nachaloPeriodaNal_label = QLabel(self.tab)
        self.nachaloPeriodaNal_label.setObjectName(u"nachaloPeriodaNal_label")

        self.horizontalLayout.addWidget(self.nachaloPeriodaNal_label)

        self.nachaloPeriodaNal_dateEdit = QDateEdit(self.tab)
        self.nachaloPeriodaNal_dateEdit.setObjectName(u"nachaloPeriodaNal_dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nachaloPeriodaNal_dateEdit.sizePolicy().hasHeightForWidth())
        self.nachaloPeriodaNal_dateEdit.setSizePolicy(sizePolicy)
        self.nachaloPeriodaNal_dateEdit.setMinimumSize(QSize(80, 0))
        self.nachaloPeriodaNal_dateEdit.setProperty("showGroupSeparator", False)
        self.nachaloPeriodaNal_dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.nachaloPeriodaNal_dateEdit)

        self.konecPeriodaNal_label = QLabel(self.tab)
        self.konecPeriodaNal_label.setObjectName(u"konecPeriodaNal_label")

        self.horizontalLayout.addWidget(self.konecPeriodaNal_label)

        self.konecPeriodaNal_dateEdit = QDateEdit(self.tab)
        self.konecPeriodaNal_dateEdit.setObjectName(u"konecPeriodaNal_dateEdit")
        sizePolicy.setHeightForWidth(self.konecPeriodaNal_dateEdit.sizePolicy().hasHeightForWidth())
        self.konecPeriodaNal_dateEdit.setSizePolicy(sizePolicy)
        self.konecPeriodaNal_dateEdit.setMinimumSize(QSize(80, 0))
        self.konecPeriodaNal_dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.konecPeriodaNal_dateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.billNumberOt_label = QLabel(self.tab)
        self.billNumberOt_label.setObjectName(u"billNumberOt_label")

        self.horizontalLayout_2.addWidget(self.billNumberOt_label)

        self.billNumberOt_lineEdit = QLineEdit(self.tab)
        self.billNumberOt_lineEdit.setObjectName(u"billNumberOt_lineEdit")
        self.billNumberOt_lineEdit.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.billNumberOt_lineEdit)

        self.billNumberDo_label = QLabel(self.tab)
        self.billNumberDo_label.setObjectName(u"billNumberDo_label")

        self.horizontalLayout_2.addWidget(self.billNumberDo_label)

        self.billNumberDo_lineEdit = QLineEdit(self.tab)
        self.billNumberDo_lineEdit.setObjectName(u"billNumberDo_lineEdit")
        self.billNumberDo_lineEdit.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.billNumberDo_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.nal_tableView = QTableView(self.tab)
        self.nal_tableView.setObjectName(u"nal_tableView")

        self.verticalLayout.addWidget(self.nal_tableView)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_3)

        self.vigruzitNal_pushButton = QPushButton(self.tab)
        self.vigruzitNal_pushButton.setObjectName(u"vigruzitNal_pushButton")

        self.horizontalLayout_1.addWidget(self.vigruzitNal_pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nachaloPeriodaBeznal_label = QLabel(self.tab_2)
        self.nachaloPeriodaBeznal_label.setObjectName(u"nachaloPeriodaBeznal_label")

        self.horizontalLayout_4.addWidget(self.nachaloPeriodaBeznal_label)

        self.nachaloPeriodaBeznal_dateEdit = QDateEdit(self.tab_2)
        self.nachaloPeriodaBeznal_dateEdit.setObjectName(u"nachaloPeriodaBeznal_dateEdit")
        sizePolicy.setHeightForWidth(self.nachaloPeriodaBeznal_dateEdit.sizePolicy().hasHeightForWidth())
        self.nachaloPeriodaBeznal_dateEdit.setSizePolicy(sizePolicy)
        self.nachaloPeriodaBeznal_dateEdit.setMinimumSize(QSize(80, 0))
        self.nachaloPeriodaBeznal_dateEdit.setProperty("showGroupSeparator", False)
        self.nachaloPeriodaBeznal_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.nachaloPeriodaBeznal_dateEdit)

        self.konecPeriodaBeznal_label = QLabel(self.tab_2)
        self.konecPeriodaBeznal_label.setObjectName(u"konecPeriodaBeznal_label")

        self.horizontalLayout_4.addWidget(self.konecPeriodaBeznal_label)

        self.konecPeriodaBeznal_dateEdit = QDateEdit(self.tab_2)
        self.konecPeriodaBeznal_dateEdit.setObjectName(u"konecPeriodaBeznal_dateEdit")
        sizePolicy.setHeightForWidth(self.konecPeriodaBeznal_dateEdit.sizePolicy().hasHeightForWidth())
        self.konecPeriodaBeznal_dateEdit.setSizePolicy(sizePolicy)
        self.konecPeriodaBeznal_dateEdit.setMinimumSize(QSize(80, 0))
        self.konecPeriodaBeznal_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.konecPeriodaBeznal_dateEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.beznal_tableView = QTableView(self.tab_2)
        self.beznal_tableView.setObjectName(u"beznal_tableView")

        self.gridLayout.addWidget(self.beznal_tableView, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.vigruzitBeznal_pushButton = QPushButton(self.tab_2)
        self.vigruzitBeznal_pushButton.setObjectName(u"vigruzitBeznal_pushButton")

        self.horizontalLayout_5.addWidget(self.vigruzitBeznal_pushButton)

        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u0442\u0435\u0436\u0438", None))
        self.nachaloPeriodaNal_label.setText(QCoreApplication.translate("Form",
                                                                        u"\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430",
                                                                        None))
        self.konecPeriodaNal_label.setText(QCoreApplication.translate("Form",
                                                                      u"\u043a\u043e\u043d\u0435\u0446 \u043f\u0435\u0440\u0438\u043e\u0434\u0430",
                                                                      None))
        self.billNumberOt_label.setText(
            QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0447\u0435\u043a\u0430 \u043e\u0442",
                                       None))
        self.billNumberDo_label.setText(QCoreApplication.translate("Form", u"\u0434\u043e", None))
        self.vigruzitNal_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c Exel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form",
                                                                                               u"\u041a\u0430\u0441\u0441\u0430 \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b",
                                                                                               None))
        self.nachaloPeriodaBeznal_label.setText(QCoreApplication.translate("Form",
                                                                           u"\u041d\u0430\u0447\u0430\u043b\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430",
                                                                           None))
        self.konecPeriodaBeznal_label.setText(QCoreApplication.translate("Form",
                                                                         u"\u043a\u043e\u043d\u0435\u0446 \u043f\u0435\u0440\u0438\u043e\u0434\u0430",
                                                                         None))
        self.vigruzitBeznal_pushButton.setText(
            QCoreApplication.translate("Form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c Exel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form",
                                                                                                 u"\u041a\u0430\u0441\u0441\u0430 \u0431\u0435\u0437\u043d\u0430\u043b",
                                                                                                 None))
    # retranslateUi
