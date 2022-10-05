from PySide2.QtWidgets import QPushButton, QApplication
import sys

app = QApplication()
button = QPushButton('Hola')
button.show()
sys.exit(app.exec_())