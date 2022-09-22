import maya.cmds as cmds


from PySide2 import QtWidgets, QtGui, QtCore

class interface:

    windName = 'TweenerWindow'

    def __init__(self):
        self.slider = None
        self.height = 270
        self.width = 250

    def _build(self):
        # Create an initial column layout to parent the children to
        column = cmds.columnLayout(rowSpacing=10, columnWidth=self.width)

        # Now we create a text label to tell the user how to use our UI
        cmds.text(label=' Use this slider to set the tweening amount', width=250)

        # Making two rows for a slider and a button side by side
        row = cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 50), adjustableColumn=1, parent=column)
        # Creating a floatSlider, setting it's min/max/default/steps, and the function to call
        self.slider = cmds.floatSlider(min=0, max=100, value=50, step=1, parent=row)
        # Now we make our button to reset our UI, it will also call our reset method
        cmds.button(label="Reset", command=self.reset, width=50, parent=row)

        # Change the active parent to the layout and create a close button for the UI
        cmds.button(label='Close', command=self.close, width=260, parent=column)

    # Method used to show the UI
    def show(self):
        # First check to see if the window doesn't already exists
        if cmds.window(self.windName, query=True, exists=True):
            cmds.deleteUI(self.windName)

        # Our create window with our name
        cmds.window(self.windName, widthHeight=(self.width, self.height))

        # Now we call our BuildUI Method to _build out the insides of the UI
        self._build()

        # Finally we want to see the UI
        cmds.showWindow()

    # Setting up our reset button
    def reset(self, *args):
        cmds.floatSlider(self.slider, edit=True, value=50)

    # This will delete out UI and close everything
    def close(self, *args):
        cmds.deleteUI(self.windName)


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.setWindowTitle('Tweener App v0.1')
        self._build()
        self._setupSignals()
        self.setCentralWidget(self.centralWidget)

    def _build(self):
        self.centralWidget = QtWidgets.QGroupBox('Animation Key Tweener')
        self.centralWidget.setAlignment(QtCore.Qt.AlignHCenter)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.sliderLayout = QtWidgets.QHBoxLayout()

        self.sliderLabel = QtWidgets.QLabel('Current Slider Value: ')
        self.sliderValue = QtWidgets.QLineEdit(str(50))
        self.sliderValue.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.slider.setValue(int(self.sliderValue.text()))
        self.setKeyButton = QtWidgets.QPushButton('Tween')
        self.mainLayout.addLayout(self.sliderLayout)
        self.sliderLayout.addWidget(self.sliderLabel)
        self.sliderLayout.addWidget(self.sliderValue)
        self.sliderLayout.addWidget(self.slider)
        self.mainLayout.addWidget(self.setKeyButton)

    def _setupSignals(self):
        self.sliderValue.textEdited.connect(self._setSliderPosition)
        self.slider.sliderMoved.connect(self.setSliderValue)

    def _setSliderPosition(self, value):
        try:
            integerValue = int(value)
            if self.slider.minimum() <= integerValue >= self.slider.maximum():
                raise IOError('Please input a value less then 100 and greater then 0')
            self.slider.setValue(integerValue)
        except ValueError:
            pass

    def setSliderValue(self, value):
        self.sliderValue.textEdited.disconnect()
        self.sliderValue.setText(str(value))
        self.sliderValue.textEdited.connect(self._setSliderPosition)


def main():
    my_app = UI()
    my_app.show()
    return my_app
