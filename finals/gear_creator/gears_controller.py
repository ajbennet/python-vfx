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
    gearTranslateZList ={}

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
        gearRadius = size.value
        numberOfTeeth = 8 * gearRadius

        translateZValue, previousRotation= self.getSelectedGear()
        print (previousRotation, translateZValue)
        gear = cmds.polyGear(s=numberOfTeeth, radius=gearRadius)
        if translateZValue ==-1:
            translateZValue = 0
        else:
            translateZValue += Controller.TRANSLATECONST * gearRadius
        cmds.setAttr('{GEAR}.translateZ'.format(GEAR=gear[0]), translateZValue)
        Controller.gearTranslateZList[gear[0]] = translateZValue

        if not previousRotation or previousRotation == 'frame':
            frame = Controller.ROTATECOUNTERCLOCKWISE
            rotateYValue = Controller.ROTATEYCONST / gearRadius
            cmds.setAttr('{GEAR}.rotateY'.format(GEAR=gear[0]), rotateYValue)
        else:
            frame = Controller.ROTATECLOCKWISE

        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=2)

        cmds.expression(s='{GEAR}.rotateY={FRAME}'.format(GEAR=gear[0], FRAME=frame))
        Controller.gearFrameList[gear[0]] = frame

    def getSelectedGear(self):
        gear = cmds.ls(selection=True)
        print(not gear)
        if not gear:
            return -1, 0
        else:

            gearZ = Controller.gearTranslateZList.get(gear[0])
            if not gearZ:
                gearZ = cmds.getAttr('{GEAR}.translateZ'.format(GEAR=gear[0]))

            gearFrame = Controller.gearFrameList.get(gear[0])
            print('gearProperty %s', gearFrame)
            # gearExpression = cmds.expression(sn='{GEAR}.rotateY'.format(GEAR=gear[0]), q=True)
            # print('Value of GearZ {GEAR} and gearExpression {EXP}'.format(GEAR=gearZ, EXP=gearExpression))
            return gearZ, gearFrame
