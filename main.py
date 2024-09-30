
import sys
from window import MainWindow
from display import Display

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

app = QApplication(sys.argv)
window = MainWindow()

display = Display()
window.vlayout.addWidget(display)

window.show()
app.exec()
