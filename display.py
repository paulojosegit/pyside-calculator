
import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display = QLineEdit()
        self.configDisplay()

    def configDisplay(self):
        self.setStyleSheet('font-size: 40px;')
        self.setMinimumHeight(80)
        self.setMinimumWidth(21)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(6,4,6,4)
        self.setPlaceholderText('0')

        regex = QRegularExpression('^[0-9/*\-+\.**◀]+$')
        regexValidator = QRegularExpressionValidator(regex, self)
        self.setValidator(regexValidator)