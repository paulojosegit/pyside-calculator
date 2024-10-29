
from PySide6.QtWidgets import QGridLayout
from button import Button
from display import Display
from PySide6.QtCore import Slot
from utils import isValidNumber


class ButtonsGridLayout(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display
        self.makeGrid()

    @Slot()
    def _makeConnectButtonDisplay(self, func, *args, **kwargs):
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertKeyInDisplay(self, button: Button):
        buttonText = button.text()

        if not isValidNumber(buttonText):
            return
        
        self.display.insert(buttonText)
        
        if button == '=':
            self.display.setText()

    def makeGrid(self): 
        for numberRow, row in enumerate(self._gridMask):
            for numberColumn, column in enumerate(row):
                button = Button(column)

                self.addWidget(button, numberRow, numberColumn)
                ButtonSlot = self._makeConnectButtonDisplay(self._insertKeyInDisplay, button)
                button.clicked.connect(ButtonSlot)