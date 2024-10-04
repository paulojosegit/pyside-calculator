
import sys
import qdarktheme

from PySide6.QtWidgets import QApplication

from window import MainWindow
from display import Display
from buttons import Button
from buttons_grid import ButtonsGridLayout

app = QApplication(sys.argv)
# Dark Theme
qdarktheme.setup_theme()
window = MainWindow()

display = Display()
window.vlayout.addWidget(display)

buttonsGrid = ButtonsGridLayout()
window.vlayout.addLayout(buttonsGrid)

numeric_button_0 = Button('0')
numeric_button_1 = Button('1')
buttonsGrid.addWidget(numeric_button_0, 0,0)    
buttonsGrid.addWidget(numeric_button_1, 0,1)




window.show()
app.exec()