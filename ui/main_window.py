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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menubar.setDefaultUp(False)
        self.operation_menu = QMenu(self.menubar)
        self.operation_menu.setObjectName(u"operation_menu")
        self.settings_menu = QMenu(self.menubar)
        self.settings_menu.setObjectName(u"settings_menu")
        self.about_menu = QMenu(self.menubar)
        self.about_menu.setObjectName(u"about_menu")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.operation_menu.menuAction())
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.operation_menu.addAction(self.search_action)
        self.operation_menu.addAction(self.add_action)
        self.operation_menu.addSeparator()
        self.operation_menu.addAction(self.exit_action)
        self.settings_menu.addAction(self.chooseBD_action)
        self.settings_menu.addAction(self.createBD_action)
        self.menu.addAction(self.kindPay_action)
        self.menu.addAction(self.member_action)
        self.menu.addAction(self.garage_action)
        self.menu.addAction(self.electric_action)

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
        self.operation_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.settings_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0411\u0414", None))
    # retranslateUi

