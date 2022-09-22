import week4.gear_creator.gear as gear

#help(gear)

import importlib
importlib.reload(gear)

#creator = gear.Creator()
#creator.create('cog2', 20, .5)
#creator.update(length =.2)
#print (creator.name)

def createCasette():

    translateYValue = 1
    scaleValue = 10
    numberOfTeeth = 30
    creator = gear.Creator()
    creator.create('cog2', 20, .5)

    
    for gearNumber in range (1, 10):
        creator.create(teeth=int(numberOfTeeth/gearNumber), teeth_length=0.1)
        numberOfTeeth +=gearNumber
        transform = creator.transform
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