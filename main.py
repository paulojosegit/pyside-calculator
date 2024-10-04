
import sys
import qdarktheme

from PySide6.QtWidgets import QApplication

from window import MainWindow
from display import Display
from buttons import Button

app = QApplication(sys.argv)

#Dark Theme
# qdarktheme.setup_theme()

window = MainWindow()
display = Display()
numeric_button_0 = Button('0')

window.vlayout.addWidget(display)
window.vlayout.addWidget(numeric_button_0)

window.show()
app.exec()