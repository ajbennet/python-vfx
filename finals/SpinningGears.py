import maya.cmds as cmds
import finals.gear_creator.view as view

import importlib
importlib.reload(view)


# List all selected objects
print (cmds.ls( selection=True ))
ui = view.main()
ui.show()
