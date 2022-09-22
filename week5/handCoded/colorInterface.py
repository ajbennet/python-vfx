from functools import partial
from PySide2 import QtWidgets, QtGui, QtCore


class UI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)

        self.setWindowTitle('My App')
        self._init_widgets()
        self._init_layout()
        self.setCentralWidget(self.centralWidget)
        self.setLayout(self.mainLayout)

    def _init_widgets(self):
        self.centralWidget = QtWidgets.QGroupBox('Color Button Options :', self)
        self.label = QtWidgets.QLabel('Select A Color')
        self.combo = QtWidgets.QComboBox()
        self.combo.addItem('Red')
        self.combo.addItem('Green')
        self.combo.addItem('Blue')
        self.combo.addItem('Black')

        self.button = QtWidgets.QPushButton('Press Me')
        self.button.setToolTip('This button will reset its color')
        self.originalColor = self.button.palette().color(self.button.backgroundRole())
        self.textColor = self.button.palette().color(self.button.foregroundRole())

        # signals
        self.combo.activated.connect(self.set_button_color)
        self.button.pressed.connect(self.reset_button_color)

    def _init_layout(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.combo)
        self.mainLayout.addWidget(self.button)

    def set_button_color(self, *args):
        selection_text = self.combo.currentText()
        print selection_text
        if selection_text == 'Red':
            color = QtCore.Qt.red
        elif selection_text == 'Green':
            color = QtCore.Qt.green
        elif selection_text == 'Blue':
            color = QtCore.Qt.blue
        elif selection_text == 'Black':
            color = QtCore.Qt.black

        button_palette = self.button.palette()
        button_palette.setColor(self.button.backgroundRole(), color)
        self.button.setPalette(button_palette)

    def reset_button_color(self):
        button_palette = self.button.palette()
        button_palette.setColor(self.button.backgroundRole(), self.originalColor.toRgb())
        self.button.setPalette(button_palette)


def main():
    my_app = UI()
    my_app.show()
    return my_app

"""
import week6.handCoded.colorInterface as interface

reload(interface)


ui = interface.main()
"""
