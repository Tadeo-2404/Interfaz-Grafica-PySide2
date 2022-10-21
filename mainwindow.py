from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        self.ui.actionAbrir.triggered.connect(self.abrirArchivo)
        self.ui.actionGuardar.triggered.connect(self.guardarArchivo)

        self.ui.tabla_mostrarBtn.clicked.connect(self.tablaMostrar)
        self.ui.tabla_buscarBtn.clicked.connect(self.tablaBuscar)

    @Slot()
    def tablaBuscar(self):
        id = self.ui.tabla_input.text()
        encontrado = False
        for vuelo in self.aeropuerto:
            if(id == vuelo.getID):
                self.ui.tabla.clear()
                id_widget = QTableWidgetItem(vuelo.getID)
                origen_widget = QTableWidgetItem(vuelo.getOrigen)
                destino_widget = QTableWidgetItem(vuelo.getDestino)
                peso_widget = QTableWidgetItem(str(vuelo.getPeso))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_widget)
                self.ui.tabla.setItem(0, 2, destino_widget)
                self.ui.tabla.setItem(0, 3, peso_widget)

                encontrado = True
                return
        if(not encontrado):
            QMessageBox.warning(
                self,
                "Advertencia",
                f'El vuelo con el ID "{id}" no fue encontrado',
            )

    @Slot()
    def tablaMostrar(self):
        self.ui.tabla.setColumnCount(4)
        headers = ["ID", "Origen", "Destino", "Peso"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.aeropuerto))

        row = 0
        for vuelo in self.aeropuerto:
            id = QTableWidgetItem(vuelo.getID)
            origen = QTableWidgetItem(vuelo.getOrigen)
            destino = QTableWidgetItem(vuelo.getDestino)
            peso = QTableWidgetItem(str(vuelo.getPeso))

            self.ui.tabla.setItem(row, 0, id)
            self.ui.tabla.setItem(row, 1, origen)
            self.ui.tabla.setItem(row, 2, destino)
            self.ui.tabla.setItem(row, 3, peso)
            row += 1


    @Slot()
    def abrirArchivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)',
        )[0]
        if self.aeropuerto.abrirArchivo(ubicacion):
            QMessageBox.accept(
                self,
                "Exito",
                "Se ha abierto exitosamente " + ubicacion
            ) 
        else: QMessageBox.critical(
            self,
            "Fracaso", 
            "No se pudo abrir " + ubicacion
        )

    @Slot()
    def guardarArchivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)',
        )[0]
        if self.aeropuerto.guardarArchivo(ubicacion):
            QMessageBox.accept(
                self,
                "Exito",
                "Se ha creado exitosamente " + ubicacion
            ) 
        else: QMessageBox.critical(
            self,
            "Fracaso", 
            "No se pudo crear " + ubicacion
        )

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
