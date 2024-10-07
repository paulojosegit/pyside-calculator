
from PySide6.QtWidgets import QGridLayout
from button import Button

class ButtonsGridLayout(QGridLayout):
    def __init__(self, *args, **kwagrs):
        super().__init__(*args, **kwagrs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.makeGrid()

    def makeGrid(self):
        for numerRow, row in enumerate(self._gridMask):
            for numberColumn, column in enumerate(row):
                button = Button(column)
                self.addWidget(button, numerRow, numberColumn)