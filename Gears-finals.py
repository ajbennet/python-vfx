import maya.cmds as cmds
import finals.gear_creator.view as view

import importlib
importlib.reload(view)


ui = view.main()
ui.show()