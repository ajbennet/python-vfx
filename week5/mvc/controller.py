import sys

from PySide2 import QtWidgets

import view as view
import model as model

reload(view)
reload(model)


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
        self.view.textGrabberButton.clicked.connect(lambda: self._getTextAndPassItAlong())

    def _getTextAndPassItAlong(self):
        currentText = self.view.scrollText.toPlainText()
        self.view.statusBar.showMessage(currentText, 5000)
        returnValue = self.model.userTypedThis(currentText, extra)
        self.view.scrollText.Text()


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
