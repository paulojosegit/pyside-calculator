
from PySide6.QtWidgets import QGridLayout
from button import Button
from display import Display
from PySide6.QtCore import Slot






from utils import validDisplay, validatorDisplay
import re

class ButtonsGridLayout(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-',  '0', '.', '='],
        ]

        self.display = display
        self.makeGrid()
        # self.display.setText('0')


    @Slot()
    def _makeConnectButtonDisplay(self, func, *args, **kwargs):
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertKeyInDisplay(self, button: Button):
        buttonText = button.text()

        self.display.insert(buttonText)

        sd = self.display.text()

        if buttonText == 'C':
            self.display.clear()
        
        if buttonText == '=':
            self.display.clear()
            self.display.insert(str(eval(sd)))
            print(sd)
    
    def makeGrid(self): 
        for numberRow, row in enumerate(self._gridMask):
            for numberColumn, column in enumerate(row):
                button = Button(column)

                self.addWidget(button, numberRow, numberColumn)
                ButtonSlot = self._makeConnectButtonDisplay(self._insertKeyInDisplay, button)
                button.clicked.connect(ButtonSlot)