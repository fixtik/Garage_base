# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.search_action = QAction(MainWindow)
        self.search_action.setObjectName(u"search_action")
        self.add_action = QAction(MainWindow)
        self.add_action.setObjectName(u"add_action")
        self.chooseBD_action = QAction(MainWindow)
        self.chooseBD_action.setObjectName(u"chooseBD_action")
        self.createBD_action = QAction(MainWindow)
        self.createBD_action.setObjectName(u"createBD_action")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.kindPay_action = QAction(MainWindow)
        self.kindPay_action.setObjectName(u"kindPay_action")
        self.member_action = QAction(MainWindow)
        self.member_action.setObjectName(u"member_action")
        self.garage_action = QAction(MainWindow)
        self.garage_action.setObjectName(u"garage_action")
        self.electric_action = QAction(MainWindow)
        self.electric_action.setObjectName(u"electric_action")
        self.updateBD_action = QAction(MainWindow)
        self.updateBD_action.setObjectName(u"updateBD_action")
        self.tarif_e = QAction(MainWindow)
        self.tarif_e.setObjectName(u"tarif_e")
        self.smeta_action = QAction(MainWindow)
        self.smeta_action.setObjectName(u"smeta_action")
        self.spisok_action = QAction(MainWindow)
        self.spisok_action.setObjectName(u"spisok_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.voa_label = QLabel(self.centralwidget)
        self.voa_label.setObjectName(u"voa_label")

        self.verticalLayout.addWidget(self.voa_label)

        self.openBase_pushButton = QPushButton(self.centralwidget)
        self.openBase_pushButton.setObjectName(u"openBase_pushButton")

        self.verticalLayout.addWidget(self.openBase_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.row_label = QLabel(self.centralwidget)
        self.row_label.setObjectName(u"row_label")

        self.horizontalLayout_2.addWidget(self.row_label)

        self.row_lineEdit = QLineEdit(self.centralwidget)
        self.row_lineEdit.setObjectName(u"row_lineEdit")

        self.horizontalLayout_2.addWidget(self.row_lineEdit)

        self.num_label = QLabel(self.centralwidget)
        self.num_label.setObjectName(u"num_label")

        self.horizontalLayout_2.addWidget(self.num_label)

        self.num_lineEdit = QLineEdit(self.centralwidget)
        self.num_lineEdit.setObjectName(u"num_lineEdit")

        self.horizontalLayout_2.addWidget(self.num_lineEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setDefaultUp(False)
        self.operation_menu = QMenu(self.menubar)
        self.operation_menu.setObjectName(u"operation_menu")
        self.settings_menu = QMenu(self.menubar)
        self.settings_menu.setObjectName(u"settings_menu")
        self.about_menu = QMenu(self.menubar)
        self.about_menu.setObjectName(u"about_menu")
        self.rabota_with_BD = QMenu(self.menubar)
        self.rabota_with_BD.setObjectName(u"rabota_with_BD")
        self.vigruzki = QMenu(self.menubar)
        self.vigruzki.setObjectName(u"vigruzki")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.operation_menu.menuAction())
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())
        self.menubar.addAction(self.rabota_with_BD.menuAction())
        self.menubar.addAction(self.vigruzki.menuAction())
        self.operation_menu.addAction(self.search_action)
        self.operation_menu.addAction(self.add_action)
        self.operation_menu.addSeparator()
        self.operation_menu.addAction(self.exit_action)
        self.settings_menu.addAction(self.chooseBD_action)
        self.settings_menu.addAction(self.createBD_action)
        self.settings_menu.addAction(self.updateBD_action)
        self.rabota_with_BD.addAction(self.kindPay_action)
        self.rabota_with_BD.addAction(self.member_action)
        self.rabota_with_BD.addAction(self.garage_action)
        self.rabota_with_BD.addAction(self.electric_action)
        self.rabota_with_BD.addAction(self.tarif_e)
        self.vigruzki.addAction(self.spisok_action)
        self.vigruzki.addAction(self.smeta_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" \u0412\u0441\u0435\u0432\u043e\u043b\u043e\u0436\u0441\u043a\u0438\u0439 \u0420.\u0421. \u0412\u041e\u0410", None))
        self.search_action.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.add_action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.chooseBD_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0411\u0414", None))
        self.createBD_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0411\u0414", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.kindPay_action.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u043b\u0430\u0442\u0435\u0436\u0430", None))
        self.member_action.setText(QCoreApplication.translate("MainWindow", u"\u0427\u043b\u0435\u043d \u043a\u043e\u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u0430", None))
        self.garage_action.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0430\u0440\u0430\u0436", None))
        self.electric_action.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0447\u0435\u0442\u0447\u0438\u043a", None))
        self.updateBD_action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0411\u0414", None))
        self.tarif_e.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0442\u0430\u0440\u0438\u0444\u0430\u043c", None))
        self.smeta_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0442\u0430", None))
        self.spisok_action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a", None))
        self.voa_label.setText("")
        self.openBase_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.row_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u044f\u0434", None))
        self.num_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.operation_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.settings_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.rabota_with_BD.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0411\u0414", None))
        self.vigruzki.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
    # retranslateUi

