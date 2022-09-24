import maya.cmds as cmds
import finals.gear_creator.view as view

import importlib
importlib.reload(view)

rotateClockwise = 'frame'
rotateCounterClockwise = '-frame'
incrementalTranslateZconst = 2.1
rotateYconst = 23
def createSpinningGears(numberOfGears = 2, gearRadius = 2):
    translateZValue = 0
    translateXValue = 0
    numberOfTeeth = 8*gearRadius
    previousFrame = 0
    
    for gearNumber in range (0, numberOfGears):
       
        gear = cmds.polyGear( s=numberOfTeeth, radius = gearRadius)
        cmds.setAttr('{GEAR}.translateZ'.format(GEAR=gear[0]), translateZValue)
        translateZValue+=incrementalZValue*gearRadius
            
        
        if(previousFrame == 0):
            frame =rotateClockwise
            previousFrame = 1
        else:
            frame =rotateCounterClockwise
            previousFrame = 0
            rotateYValue=rotateYconst/gearRadius
            cmds.setAttr('{GEAR}.rotateY'.format(GEAR=gear[0]), rotateYValue)
            
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    
        cmds.expression( s='{GEAR}.rotateY={FRAME}'.format(GEAR=gear[0],FRAME=frame))
    
    
createSpinningGears(2,1)

# List all selected objects
print (cmds.ls( selection=True ))
ui = view.main()
ui.show()
