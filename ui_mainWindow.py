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
        MainWindow.resize(534, 372)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla_container = QTabWidget(self.centralwidget)
        self.tabla_container.setObjectName(u"tabla_container")
        self.tabla_container.setEnabled(True)
        self.tabla_container.setLayoutDirection(Qt.LeftToRight)
        self.tabla_container.setStyleSheet(u"background-color: rgb(228, 229, 232);\n"
"padding: 5px;")
        self.tabla_container.setTabPosition(QTabWidget.North)
        self.tabla_container.setIconSize(QSize(16, 16))
        self.tabla_container.setTabsClosable(False)
        self.tabla_container.setTabBarAutoHide(False)
        self.agregar_tab = QWidget()
        self.agregar_tab.setObjectName(u"agregar_tab")
        self.agregar_tab.setAutoFillBackground(False)
        self.agregar_tab.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.agregar_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BoxContainer = QGroupBox(self.agregar_tab)
        self.BoxContainer.setObjectName(u"BoxContainer")
        self.BoxContainer.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(115, 171, 255);\n"
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
"padding: 1px;\n"
"")

        self.gridLayout.addWidget(self.input_origen, 1, 1, 1, 1)

        self.input_destino = QLineEdit(self.BoxContainer)
        self.input_destino.setObjectName(u"input_destino")
        self.input_destino.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"color: rgb(0, 0, 0);\n"
"padding: 1px;\n"
"")

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

        self.plainTextEdit = QPlainTextEdit(self.agregar_tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabla_container.addTab(self.agregar_tab, "")
        self.tabla_tab = QWidget()
        self.tabla_tab.setObjectName(u"tabla_tab")
        self.gridLayout_4 = QGridLayout(self.tabla_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tabla_tab)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.tabla_input = QLineEdit(self.tabla_tab)
        self.tabla_input.setObjectName(u"tabla_input")
        self.tabla_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.tabla_input, 1, 0, 1, 1)

        self.tabla_buscarBtn = QPushButton(self.tabla_tab)
        self.tabla_buscarBtn.setObjectName(u"tabla_buscarBtn")
        self.tabla_buscarBtn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"text-transform:uppercase;\n"
"color: white;")

        self.gridLayout_4.addWidget(self.tabla_buscarBtn, 1, 1, 1, 1)

        self.tabla_mostrarBtn = QPushButton(self.tabla_tab)
        self.tabla_mostrarBtn.setObjectName(u"tabla_mostrarBtn")
        self.tabla_mostrarBtn.setStyleSheet(u"outline: none;\n"
"border: none;\n"
"background-color: rgb(0, 0, 255);\n"
"text-transform:uppercase;\n"
"color: white;")

        self.gridLayout_4.addWidget(self.tabla_mostrarBtn, 1, 2, 1, 1)

        self.tabla_container.addTab(self.tabla_tab, "")

        self.gridLayout_3.addWidget(self.tabla_container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 534, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabla_container.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.BoxContainer.setTitle(QCoreApplication.translate("MainWindow", u"Vuelo", None))
        self.mostrarBtn.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.agregarInicioBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.input_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID del Vuelo", None))
        self.label_peso.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.label_destino.setText(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_origen.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.input_origen.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Origen del Vuelo", None))
        self.input_destino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destino del Vuelo", None))
        self.agregarFinalBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.tabla_container.setTabText(self.tabla_container.indexOf(self.agregar_tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.tabla_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo del Vuelo", None))
        self.tabla_buscarBtn.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabla_mostrarBtn.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabla_container.setTabText(self.tabla_container.indexOf(self.tabla_tab), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

