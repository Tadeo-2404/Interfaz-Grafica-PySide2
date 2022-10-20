from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainWindow import Ui_MainWindow
from Aeropuerto import Aeropuerto
from Vuelo import Vuelo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.aeropuerto = Aeropuerto()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarInicioBtn.clicked.connect(self.agregarInicio)
        self.ui.agregarFinalBtn.clicked.connect(self.agregarFinal)
        self.ui.mostrarBtn.clicked.connect(self.mostrar)

    @Slot()
    def agregarInicio(self) :
        id = self.ui.input_id.text()
        origen = self.ui.input_origen.text()
        destino = self.ui.input_destino.text()
        peso = self.ui.inputBox_peso.value()
        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_inicio(vuelo)

    @Slot()
    def agregarFinal(self) :
        id = self.ui.input_id.text()
        origen = self.ui.input_origen.text()
        destino = self.ui.input_destino.text()
        peso = self.ui.inputBox_peso.value()
        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_final(vuelo)

    @Slot()
    def mostrar(self) :
        # self.aeropuerto.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.aeropuerto))
