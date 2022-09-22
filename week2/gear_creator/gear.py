import maya.cmds as cmds


def create(gear_name='gear1', teeth=11, teeth_length=0.2):
    """
    Creates a single gear
    :return: None
    """

    spans = teeth * 2

    transform, constructor = cmds.polyPipe(name=gear_name, subdivisionsAxis=spans)

    side_faces = range(spans * 2, spans * 3, 2)

    cmds.select(clear=True)

    for face in side_faces:
        cmds.select('{TRANSFORM}.f[{FACE_NUMBER}]'.format(TRANSFORM=transform, FACE_NUMBER=face), add=True)

    extrusion = cmds.polyExtrudeFacet(localTranslateZ=teeth_length)
    cmds.select(clear=True)

    return constructor, extrusion, transform


def modify(constructor, extrusion, teeth=32, teeth_length=0.2):
    """
    modifies a gear
    """

    spans = teeth * 2
    cmds.polyPipe(constructor, edit=True, subdivisionsAxis=spans)

    side_faces = range(spans * 2, spans * 3, 2)
    face_names = list()

    for face in side_faces:
        face_name = 'f[{FACE}]'.format(FACE=face)
        face_names.append(face_name)

    cmds.setAttr('{FACE_NAME}.inputComponents'.format(FACE_NAME=extrusion[0]), len(face_names), *face_names,
                 type='componentList')

    cmds.polyExtrudeFacet(extrusion, edit=True, localTranslateZ=teeth_length)

    pass
