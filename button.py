
from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleButton()

    def setStyleButton(self):
        self.setStyleSheet('font-size: 24px')
        self.setMinimumSize(75, 75)