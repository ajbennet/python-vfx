import maya.cmds as cmds
import week2.gear_creator.gear as gear

#help(gear)

import importlib
importlib.reload(gear)


#gear.modify(constructor, extrusion) 

def createCasette():

    translateYValue = 1
    scaleValue = 10
    numberOfTeeth = 30
    
    for gearNumber in range (1, 10):
        constructor, extrusion, transform = gear.create(teeth=int(numberOfTeeth/gearNumber), teeth_length=0.1)
        numberOfTeeth +=gearNumber
        #if gearNumber != 1:
        cmds.setAttr('{TRANSFORM}.translateY'.format(TRANSFORM=transform), translateYValue)
        translateYValue += 1
        cmds.setAttr('{TRANSFORM}.scaleZ'.format(TRANSFORM=transform), scaleValue)
        cmds.setAttr('{TRANSFORM}.scaleX'.format(TRANSFORM=transform), scaleValue)
        if(gearNumber % 2 != 0):
            rotateValue = -scaleValue;
        else:
            rotateValue = scaleValue;
        cmds.setAttr('{TRANSFORM}.rotateY'.format(TRANSFORM=transform), rotateValue)
        scaleValue -= 1

createCasette()