"""
Class object to create and modify gears
"""
import importlib
import maya.cmds as cmds
from . import view as view
from . import model as model

importlib.reload(view)
importlib.reload(model)


class Controller(object):
    ROTATECLOCKWISE = 'frame'
    ROTATECOUNTERCLOCKWISE = '-frame'
    TRANSLATECONST = 2.1
    ROTATEYCONST = 23
    gearFrameList = {}
    gearTranslateZList = {}
    gearTranslateXList = {}
    gearRadiusList = {}

    def addGear(self, size=model.Size.Medium, location=model.Location.Right, height=1):
        gearRadius = size.value
        translateZValue = 0
        translateXValue = 0
        numberOfTeeth = 8 * gearRadius
        previousXValue, previousZValue, previousRotation, previousRadius = self.getSelectedGear()
        gear = cmds.polyGear(s=numberOfTeeth, radius=gearRadius, height=height)
        Controller.gearRadiusList[gear[0]] = gearRadius
        changeX = True
        changeZ = True
        # When there are no other gears, set the default values for these variables
        if previousRadius == -1:
            previousRadius = gearRadius
        else:
            if location == model.Location.Right:
                translateZValue = previousZValue + (Controller.TRANSLATECONST * gearRadius / 2) + (
                    Controller.TRANSLATECONST * previousRadius / 2)
                translateXValue = previousXValue
            if location == model.Location.Left:
                translateZValue = previousZValue - ((Controller.TRANSLATECONST * gearRadius / 2) + (
                        Controller.TRANSLATECONST * previousRadius / 2))
                translateXValue = previousXValue
            if location == model.Location.Top:
                translateXValue = previousXValue + (Controller.TRANSLATECONST * gearRadius / 2) + (
                    Controller.TRANSLATECONST * previousRadius / 2)
                translateZValue = previousZValue
            if location == model.Location.Bottom:
                translateXValue = previousXValue - ((Controller.TRANSLATECONST * gearRadius / 2) + (
                        Controller.TRANSLATECONST * previousRadius / 2))
                translateZValue = previousZValue
        print(previousXValue, '-', previousZValue, '-', translateXValue, '-', translateZValue)

        #cmds.setAttr('{GEAR}.scaleY'.format(GEAR=gear[0]), height)
        cmds.setAttr('{GEAR}.translateZ'.format(GEAR=gear[0]), translateZValue)
        Controller.gearTranslateZList[gear[0]] = translateZValue
        cmds.setAttr('{GEAR}.translateX'.format(GEAR=gear[0]), translateXValue)
        Controller.gearTranslateXList[gear[0]] = translateXValue

        if not previousRotation or previousRotation == 'frame':
            frame = Controller.ROTATECOUNTERCLOCKWISE
            rotateYValue = Controller.ROTATEYCONST / gearRadius
            cmds.setAttr('{GEAR}.rotateY'.format(GEAR=gear[0]), rotateYValue)
        else:
            frame = Controller.ROTATECLOCKWISE

        # freeze the transformation for the gears, so the starting positions are aligned for the gears.
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

        cmds.expression(s='{GEAR}.rotateY={FRAME}/{RADIUS}*2'.format(GEAR=gear[0], FRAME=frame, RADIUS=gearRadius))
        Controller.gearFrameList[gear[0]] = frame

    def getSelectedGear(self):
        gear = cmds.ls(selection=True)
        print(not gear)
        if not gear:
            return -1, -1, 0, -1
        else:
            gearZ = Controller.gearTranslateZList.get(gear[0])
            if not gearZ:
                gearZ = cmds.getAttr('{GEAR}.translateZ'.format(GEAR=gear[0]))
            gearX = Controller.gearTranslateXList.get(gear[0])
            if not gearX:
                gearX = cmds.getAttr('{GEAR}.translateX'.format(GEAR=gear[0]))

            gearFrame = Controller.gearFrameList.get(gear[0])
            gearRadius = Controller.gearRadiusList.get(gear[0])
            print('get Selected Gear properties', gearX, '-', gearZ, '-', gearFrame, '-', gearRadius)
            return gearX, gearZ, gearFrame, gearRadius

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
