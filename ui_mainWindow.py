# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(225, 307)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 211, 251))
        self.groupBox.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 183, 181);\n"
"color: rgb(255, 255, 255);\n"
"padding: 2px;")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"height: 25px;\n"
"text-transform:uppercase;")

        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 225, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vuelo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
    # retranslateUi

