import sys
import importlib

from PySide2 import QtWidgets

from . import view as view
from . import model as model

importlib.reload(view)
importlib.reload(model)


class Connect(object):
    def __init__(self, parent=None):
        super(Connect, self).__init__()
        self.view = view.UI(parent=parent)
        self.model = model.Core()
        self.link_model_view()

    def link_model_view(self):
        self.view.subAction.hovered.connect(lambda: self.model.found_sub())
        self.view.infoAction.triggered.connect(lambda: self.model.print_button())

        self.view.combo.currentIndexChanged[str].connect(lambda option: self.model.option(option))
        self.view.combo.currentIndexChanged[str].connect(lambda option: self.view.statusBar.showMessage('{OPTION}'.format(OPTION=option), 500))

        self.view.radioButton2.clicked.connect(lambda: self.model.radio_button2())


def main():
    """
    This is Important for ALl UI Testing
    """
    active_window = QtWidgets.QApplication.activeWindow()
    if active_window:
        my_app = Connect(parent=active_window)
        my_app.view.show()

    else:
        app = QtWidgets.QApplication(sys.argv)
        my_app = Connect(parent=None)
        my_app.view.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
