import sys

from PySide2 import QtCore, QtGui, QtWidgets


class UI(QtWidgets.QMainWindow):
    _TITTLE = 'UI'
    _VERSION = 1.0

    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setWindowTitle('{TITTLE} v{VERSION}'.format(TITTLE=self._TITTLE, VERSION=self._VERSION))

        self._init_widgets()
        self._init_addons()
        self._create_layout()

        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setCentralWidget(self.centralWidget)
        self.setStatusBar(self.statusBar)
        self.addToolBar(self.toolBar)
        self.setLayout(self.mainLayout)

    def _init_widgets(self):
        self.centralWidget = QtWidgets.QWidget(self)

        self.menu = self.menuBar()

        self.toolBar = QtWidgets.QToolBar('UI Tools')

        self.tabBar = QtWidgets.QTabWidget()

        self.tabOptions = QtWidgets.QCalendarWidget()

        self.scrollArea = QtWidgets.QScrollArea()

        self.scrollText = QtWidgets.QTextEdit()

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralWidget)

        self.interfaceGroup = QtWidgets.QGroupBox('UI Options :')

        self.interfaceRadioLayout = QtWidgets.QVBoxLayout()

        self.statusBar = QtWidgets.QStatusBar()
        self.interGrabberGroup = QtWidgets.QGroupBox('Text Grabber :')
        self.textGrabberLayout = QtWidgets.QVBoxLayout()
        self.interGrabberGroup.setLayout(self.textGrabberLayout)
        self.textGrabberLayout.addWidget(self.scrollArea)
        self.textGrabberButton = QtWidgets.QPushButton('Grab Text')
        self.textGrabberLayout.addWidget(self.textGrabberButton)


    def _init_addons(self):

        self.fileMenu = self.menu.addMenu('&File')

        self.fileAction = QtWidgets.QAction('File Action', self)
        self.fileMenu.addAction(self.fileAction)
        self.fileMenu.addSeparator()

        self.fileSubMenu = self.fileMenu.addMenu('Sub Menu')

        self.subAction = QtWidgets.QAction('Sub Action', self)
        self.fileSubMenu.addAction(self.subAction)

        self.helpMenu = self.menu.addMenu('&Help')

        self.infoAction = QtWidgets.QAction('Info Action', self)
        self.helpSubMenu = self.helpMenu.addAction(self.infoAction)

        self.combo = QtWidgets.QComboBox()
        self.combo.addItem('Option 1')
        self.combo.addItem('Option 2')
        self.combo.addItem('Option 3')

        self.checkBox = QtWidgets.QCheckBox('Checked')

        self.toolBar.isMovable()
        self.toolBar.toggleViewAction()
        self.toolBar.addWidget(QtWidgets.QLabel('UI Tool Bar'))
        self.toolBar.addWidget(self.combo)
        self.toolBar.addSeparator()
        self.toolBar.layout().setSpacing(25)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.checkBox)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollText)
        self.scrollArea.setViewportMargins(10, 10, 10, 10)

        self.tabBar.setDocumentMode(True)
        self.tabBar.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabBar.setMovable(True)
        self.tabBar.addTab(self.tabOptions, 'Tab 1')
        self.tabBar.addTab(self.interGrabberGroup, 'TextGrabber')

    def _create_layout(self):
        self.radioButton1 = QtWidgets.QRadioButton('&Radio Button 1')
        self.radioButton1.setStatusTip("Radio Button 1")
        self.radioButton1.setChecked(True)
        self.radioButton2 = QtWidgets.QRadioButton('&Radio Button 2')
        self.radioButton2.setStatusTip("Radio Button 2")
        self.radioButton3 = QtWidgets.QRadioButton('&Radio Button 3')
        self.radioButton3.setStatusTip("Radio Button 3")

        self.interfaceRadioLayout.addWidget(self.radioButton1)
        self.interfaceRadioLayout.addWidget(self.radioButton2)
        self.interfaceRadioLayout.addWidget(self.radioButton3)

        self.interfaceGroup.setAlignment(QtCore.Qt.AlignHCenter)
        self.interfaceRadioLayout.setAlignment(QtCore.Qt.AlignHCenter)

        self.interfaceGroup.setLayout(self.interfaceRadioLayout)
        self.mainLayout.addWidget(self.tabBar)
        self.mainLayout.addWidget(self.interfaceGroup)

        self.statusBar.showMessage('UI Layout Set!', 2000)


def main():
    """
    This is Important for ALl UI Testing
    """
    active_window = QtWidgets.QApplication.activeWindow()
    if active_window:
        my_app = UI(parent=active_window)
        my_app.show()

    else:
        app = QtWidgets.QApplication(sys.argv)
        my_app = UI(parent=None)
        my_app.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
