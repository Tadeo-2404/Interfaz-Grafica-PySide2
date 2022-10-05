from PySide2.QtWidgets import QMainWindow, QApplication
from main2 import MainWindow
import sys

app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())