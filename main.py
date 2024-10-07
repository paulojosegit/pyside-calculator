
import sys
import qdarktheme

from PySide6.QtWidgets import QApplication

from window import MainWindow
from display import Display
from buttons_grid import ButtonsGridLayout

app = QApplication(sys.argv)

# Dark Theme
qdarktheme.setup_theme()

window = MainWindow()
display = Display()
window.vlayout.addWidget(display)

buttonsGrid = ButtonsGridLayout()
window.vlayout.addLayout(buttonsGrid)

window.show()
app.exec()