
from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.numeric_button()

    def numeric_button(self):
        self.setStyleSheet('font-size: 30px')
        self.setMinimumSize(75, 75)
