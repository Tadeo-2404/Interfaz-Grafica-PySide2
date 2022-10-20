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
        MainWindow.resize(535, 383)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BoxContainer = QGroupBox(self.centralwidget)
        self.BoxContainer.setObjectName(u"BoxContainer")
        self.BoxContainer.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(189, 183, 181);\n"
"color: rgb(255, 255, 255);\n"
"padding: 2px;")
        self.gridLayout = QGridLayout(self.BoxContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputBox_peso = QSpinBox(self.BoxContainer)
        self.inputBox_peso.setObjectName(u"inputBox_peso")
        self.inputBox_peso.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.inputBox_peso, 2, 1, 1, 1)

        self.mostrarBtn = QPushButton(self.BoxContainer)
        self.mostrarBtn.setObjectName(u"mostrarBtn")
        self.mostrarBtn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"height: 25px;\n"
"text-transform:uppercase;")

        self.gridLayout.addWidget(self.mostrarBtn, 6, 0, 1, 2)

        self.agregarInicioBtn = QPushButton(self.BoxContainer)
        self.agregarInicioBtn.setObjectName(u"agregarInicioBtn")
        self.agregarInicioBtn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"height: 25px;\n"
"text-transform:uppercase;")

        self.gridLayout.addWidget(self.agregarInicioBtn, 5, 0, 1, 2)

        self.input_id = QLineEdit(self.BoxContainer)
        self.input_id.setObjectName(u"input_id")
        self.input_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.input_id, 0, 1, 1, 1)

        self.label_peso = QLabel(self.BoxContainer)
        self.label_peso.setObjectName(u"label_peso")

        self.gridLayout.addWidget(self.label_peso, 2, 0, 1, 1)

        self.label_destino = QLabel(self.BoxContainer)
        self.label_destino.setObjectName(u"label_destino")

        self.gridLayout.addWidget(self.label_destino, 3, 0, 1, 1)

        self.label_origen = QLabel(self.BoxContainer)
        self.label_origen.setObjectName(u"label_origen")

        self.gridLayout.addWidget(self.label_origen, 1, 0, 1, 1)

        self.input_origen = QLineEdit(self.BoxContainer)
        self.input_origen.setObjectName(u"input_origen")
        self.input_origen.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.input_origen, 1, 1, 1, 1)

        self.input_destino = QLineEdit(self.BoxContainer)
        self.input_destino.setObjectName(u"input_destino")
        self.input_destino.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;")

        self.gridLayout.addWidget(self.input_destino, 3, 1, 1, 1)

        self.agregarFinalBtn = QPushButton(self.BoxContainer)
        self.agregarFinalBtn.setObjectName(u"agregarFinalBtn")
        self.agregarFinalBtn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"height: 25px;\n"
"text-transform:uppercase;")

        self.gridLayout.addWidget(self.agregarFinalBtn, 4, 0, 1, 2)

        self.label_id = QLabel(self.BoxContainer)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.BoxContainer, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 535, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BoxContainer.setTitle(QCoreApplication.translate("MainWindow", u"Vuelo", None))
        self.mostrarBtn.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.agregarInicioBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.label_peso.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.label_destino.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_origen.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.agregarFinalBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
    # retranslateUi

