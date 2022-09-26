"""
Class object to create and modify gears
"""
import maya.cmds as cmds


class Creator(object):

    def __init__(self):
        self.name = None
        self.transform = None
        self.constructor = None
        self.extrusion = None
        self.length = None
        self.teeth = None
        self.spans = None
        self.width = None
        self.thickness = None

    def create(self, gear_name='gear1', teeth=11, teeth_length=0.2,):
        self.teeth = teeth
        self.spans = self.teeth * 2
        self.length = teeth_length
        self.name = gear_name
        self.transform, self.constructor = cmds.polyPipe(name=gear_name, subdivisionsAxis=self.spans)

        side_faces = range(self.spans * 2, self.spans * 3, 2)

        cmds.select(clear=True)

        for face in side_faces:
            cmds.select('{TRANSFORM}.f[{FACE_NUMBER}]'.format(TRANSFORM=self.transform, FACE_NUMBER=face), add=True)

        self.extrusion = cmds.polyExtrudeFacet(localTranslateZ=teeth_length)
        cmds.select(clear=True)

    '''@property
    def get_transform(self):
        return self.transform
    '''
    def update(self, teeth=None, length=None):
        if teeth:
            self.teeth = teeth
        if length:
            self.length = length
        self.spans = self.teeth * 2
        cmds.polyPipe(self.constructor, edit=True, subdivisionsAxis=self.spans)

        side_faces = range(self.spans * 2, self.spans * 3, 2)
        face_names = list()

        for face in side_faces:
            face_name = 'f[{FACE}]'.format(FACE=face)
            face_names.append(face_name)

        cmds.setAttr('{FACE_NAME}.inputComponents'.format(FACE_NAME=self.extrusion[0]), len(face_names), *face_names,
                     type='componentList')

        cmds.polyExtrudeFacet(self.extrusion, edit=True, localTranslateZ=self.length)
        pass
