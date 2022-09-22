import maya.cmds as cmds
import gear
import tweener


class Base(object):
   
    windowName = "baseWindow"
    
    def show(self): # Rgua method is for showing and deleting the UI only

        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName, widthHeight=(250, 100))
        
        self.buildUI() # separate this from the show to encourage good practices and keep it modular

        cmds.showWindow()

    def buildUI(self): # build the basic structure of the UI 
        pass # need to make this more generic

    def reset(self, *args): # use *args to capture any remaining parameters that are given like by a button
        pass

    def close(self, *args): # Closing out the UI with another button to close it down separate from the above delete
        cmds.deleteUI(self.windowName)


class TweenerUI(Base):

    windowName = 'TweenerWindow'
    width = 250

    def buildUI(self): # build the basic structure of the UI 
        # Create an initial column layout to parent the children to
        column = cmds.columnLayout(rowSpacing=10, columnWidth=self.width)

        # Now we create a text label to tell the user how to use our UI
        cmds.text(label=' Use this slider to set the tweening amount', width=250)

        # Making two rows for a slider and a button side by side
        row = cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 50), adjustableColumn=1, parent=column)
        # Creating a floatSlider, setting it's min/max/default/steps, and the function to call
        self.slider = cmds.floatSlider(min=0, max=100, value=50, step=1, changeCommand=tweener.core, parent=row)
        # Now we make our button to reset our UI, it will also call our reset method
        cmds.button(label="Reset", command=self.reset, width=50, parent=row)

        # Change the active parent to the layout and create a close button for the UI
        cmds.button(label='Close', command=self.close, width=260, parent=column)


    def reset(self, *args): # use *args to capture any remaining parameters that are given like by a button
        #print "Reseting UI"
        #print args

        cmds.floatSlider(self.slider, edit=True, value=50)


class GearUI(Base):

    windowName = 'GearWindow'

    def __init__(self):
        
        self.gear = None

    def buildUI(self):

        column = cmds.columnLayout()
        cmds.text(label= "Use the slider to modify the gear")

        cmds.rowLayout(numberOfColumns=4)
        self.label = cmds.text(label="10")

        self.slider = cmds.intSlider(min=5, max=30, value=10, step=1, dragCommand=self.modifyGear)
        cmds.button(label='Make Gear', command=self.makeGear)
        cmds.button(label='Reset', command=self.reset)

        cmds.setParent(column)
        cmds.button(label='Close', command=self.close)

    def makeGear(self, *args):
        teeth = cmds.intSlider(self.slider, query=True, value=True)
        self.gear = gear.Gear()
        self.gear.creates(teeth=teeth)

    def modifyGear(self, teeth):
        if self.gear:
            self.gear.changeTeeths(teeth=teeth)

        cmds.text(self.label, edit=True, label=teeth)

    def reset(self, *args):
        self.gear = None
        cmds.intSlider(self.slider, edit=True, value=10)
        cmds.text(self.label, edit=True, label=10)
