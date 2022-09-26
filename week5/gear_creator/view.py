import os
import importlib
from functools import partial
from PySide2 import QtCore, QtWidgets, QtUiTools
import week5.gear_creator.gear as gear
import maya.cmds as cmds

importlib.reload(gear)



class UI(object):
    def __init__(self, ui_file=None):
        super(UI, self).__init__()
        ui_file = QtCore.QFile(ui_file)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        self.__init__widgets()
        # initialize the controller
        self.creator = gear.Creator()

    def __init__widgets(self):
        self.teethHeight = self.window.findChild(QtWidgets.QLineEdit, 'teethHeight')
        self.teethHeight.setPlaceholderText('0.1')
        self.noOfGears = self.window.findChild(QtWidgets.QLineEdit, 'noOfGears')
        self.noOfGears.setPlaceholderText('10')
        self.button = self.window.findChild(QtWidgets.QPushButton, 'createGears')
        self.button.pressed.connect(partial(self.create_gears_button))

    def create_gears_button(self):
        teethHeight = 0.1
        try:
            teethHeight = int(float(self.teethHeight.text()))
        except ValueError:
            teethHeight = 0.1

        noOfGears = 10
        try:
            noOfGears = int(float(self.noOfGears.text()))
        except ValueError:
            noOfGears = 10

        self.createCasette(numberOfTeeth=30, teeth_height=teethHeight, numberOfGears=noOfGears)

    def createCasette(self, numberOfTeeth = 30, teeth_height = 0.1, numberOfGears = 10):

        translateYValue = 1
        scaleValue = 10
        self.creator.create('cog2', 20, .5)

        for gearNumber in range(1, numberOfGears):
            self.creator.create(teeth=int(numberOfTeeth / gearNumber), teeth_length=teeth_height)
            numberOfTeeth += gearNumber
            transform = self.creator.transform
            cmds.setAttr('{TRANSFORM}.translateY'.format(TRANSFORM=transform), translateYValue)
            translateYValue += 1
            cmds.setAttr('{TRANSFORM}.scaleZ'.format(TRANSFORM=transform), scaleValue)
            cmds.setAttr('{TRANSFORM}.scaleX'.format(TRANSFORM=transform), scaleValue)
            if (gearNumber % 2 != 0):
                rotateValue = -scaleValue;
            else:
                rotateValue = scaleValue;
            cmds.setAttr('{TRANSFORM}.rotateY'.format(TRANSFORM=transform), rotateValue)
            scaleValue -= 1



def main():
    parentDir = os.path.split(__file__)[0]
    uiFilePath = os.path.join(parentDir, 'gear_creator.ui')
    interface = UI(uiFilePath)
    return interface.window
