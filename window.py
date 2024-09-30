
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cwidget = QWidget()
        self.vlayout = QVBoxLayout()
        
        self.setCentralWidget(self.cwidget)
        self.cwidget.setLayout(self.vlayout)

        self.setWindowTitle('Calculadora básica')
        self.adjustSize()
        self.resize(400, 500)
        self.setFixedSize(self.width(), self.height())