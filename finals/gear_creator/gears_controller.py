"""
Class object to create and modify gears
"""
import sys
import importlib
import maya.cmds as cmds
import view
import model

importlib.reload(view)
importlib.reload(model)


class Controller(object):

    ROTATECLOCKWISE = 'frame'
    ROTATECOUNTERCLOCKWISE = '-frame'
    TRANSLATECONST = 2.1
    ROTATEYCONST = 23

    def __init__(self):


    def createSpinningGears(self, numberOfGears=2, gearRadius=2):
        translateZValue = 0
        numberOfTeeth = 8 * gearRadius
        previousFrame = 0

        for gearNumber in range(0, numberOfGears):
            gear = cmds.polyGear(s=numberOfTeeth, radius=gearRadius)
            cmds.setAttr('{GEAR}.translateZ'.format(GEAR=gear[0]), translateZValue)
            translateZValue += Controller.TRANSLATECONST * gearRadius
            if (previousFrame == 0):
                frame = Controller.ROTATECLOCKWISE
                previousFrame = 1
            else:
                frame = Controller.ROTATECOUNTERCLOCKWISE
                previousFrame = 0
                rotateYValue = Controller.ROTATEYCONST / gearRadius
                cmds.setAttr('{GEAR}.rotateY'.format(GEAR=gear[0]), rotateYValue)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)
            cmds.expression(s='{GEAR}.rotateY={FRAME}'.format(GEAR=gear[0], FRAME=frame))



    def addGear(self, size=model.Size.MEDIUM, location=model.Location.RIGHT):

        translateZValue = 0
        numberOfTeeth = 8 * size
        previousFrame = 0
        gear = cmds.polyGear(s=numberOfTeeth, radius=size)
        cmds.setAttr('{GEAR}.translateZ'.format(GEAR=gear[0]), translateZValue)
        translateZValue += Controller.TRANSLATECONST * size

        if (previousFrame == 0):
            frame = Controller.ROTATECLOCKWISE
            previousFrame = 1
        else:
            frame = Controller.ROTATECOUNTERCLOCKWISE
            previousFrame = 0
            rotateYValue = Controller.ROTATEYCONST / size
            cmds.setAttr('{GEAR}.rotateY'.format(GEAR=gear[0]), rotateYValue)

        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

        cmds.expression(s='{GEAR}.rotateY={FRAME}'.format(GEAR=gear[0], FRAME=frame))
