import os
from functools import partial
from PySide2 import QtCore, QtWidgets, QtUiTools


class UI(object):
    def __init__(self, ui_file=None):
        super(UI, self).__init__()
        ui_file = QtCore.QFile(ui_file)
        ui_file.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.__init__widgets()

    def __init__widgets(self):
        self.gearRadius = self.window.findChild(QtWidgets.QLineEdit, 'gearRadius')
        self.button = self.window.findChild(QtWidgets.QPushButton, 'addButton')
        self.button.pressed.connect(partial(self.add_button_label))

    def add_button_label(self):
        print(self.gearRadius.text())


def main():
    parentDir = os.path.split(__file__)[0]
    uiFilePath = os.path.join(parentDir, 'ui/gear-creator.ui')
    interface = UI(uiFilePath)
    return interface.window
