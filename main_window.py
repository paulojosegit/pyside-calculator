
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)

        self.setWindowTitle('Calculadora básica')        
        self.setCentralWidget(self.central_widget)

        button_send = QPushButton('ENVIAR')
        button_send.setStyleSheet('font-size: 26px')

        button_cancel = QPushButton('CANCELAR')
        button_cancel.setStyleSheet('font-size: 26px')

        self.v_layout.addWidget(button_send)
        self.v_layout.addWidget(button_cancel)

        self.adjustSize()
        self.resize(400, 500)
        self.setFixedSize(self.width(), self.height())


if __name__ == '__main__':
    app = QApplication()

    mw = MainWindow()
    mw.show()

    app.exec()

