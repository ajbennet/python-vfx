import maya.cmds as cmds
import week5.gear_creator.view as view

import importlib
importlib.reload(view)


ui = view.main()
ui.show()