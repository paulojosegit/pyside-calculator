
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

from window import MainWindow
from display import Display

app = QApplication(sys.argv)
window = MainWindow()

display = Display()
window.vlayout.addWidget(display)

window.show()
app.exec()