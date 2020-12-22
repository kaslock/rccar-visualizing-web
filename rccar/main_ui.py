# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 502)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 240, 71, 61))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 310, 71, 61))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 380, 71, 61))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(230, 310, 71, 61))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 310, 71, 61))
        self.text = QPlainTextEdit(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(20, 20, 361, 201))
        self.sens_text = QPlainTextEdit(self.centralwidget)
        self.sens_text.setObjectName(u"sens_text")
        self.sens_text.setGeometry(QRect(400, 20, 361, 201))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 250, 191, 181))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 785, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.clickedGo)
        self.pushButton_4.clicked.connect(MainWindow.clickedRight)
        self.pushButton_5.clicked.connect(MainWindow.clickedMid)
        self.pushButton_3.clicked.connect(MainWindow.clickedBack)
        self.pushButton_2.clicked.connect(MainWindow.clickedLeft)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.label.setText("")
    # retranslateUi

