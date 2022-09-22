from functools import partial
from PySide2 import QtWidgets, QtGui, QtCore


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Setting the window with a tittle
        self.setWindowTitle("My App")
        # Method to control the storage of widgets
        self._init_widgets()

    def _init_widgets(self):
        # Basic button
        button = QtWidgets.QPushButton("Press Me!")
        # Signal to close the button
        button.pressed.connect(partial(self.close))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


def main():
    my_app = UI()
    my_app.show()
    return my_app
     
"""   
import week6.handCoded.simpleInterface as interface

reload(interface)

ui = interface.main()

"""
