import maya.cmds as cmds


class Gear:
    def __init__(self):
        self.shape = None
        self.transform = None
        self.constructor = None
        self.extrudes = None
        #self.teeth would it be better to add these here?
        #self.length or in the methods below?

    def creates(self, teeth=10, length=0.3): 
        """
        This function will create and modify a procedural gear using Class structure
        Args:
            teeth: the number of teeth on the gear
            length: the length of the teeth

        Result:
            A tuple of variable used for the following methods or subclasses

        """
        spans = teeth * 2
        self.createPipes(spans)

        # We need to call the make teeth method to grab the face selection
        self.makeTeeths(teeth=teeth, length=length)

    def createPipes(self, spans):
        # We set the transform and the shape to the class variables
        self.transform, self.shape = cmds.polyPipe(subdivisionsAxis=spans)

        for node in cmds.listConnections('{}.inMesh'.format(self.transform)):
            if cmds.objectType(node) == 'polyPipe':
                self.constructor = node
                break

    def makeTeeths(self, teeth=10, length=0.3):
        # The logic similar to the way it was in the function
        cmds.select(cl=True)
        faces = self.getTeethFaces(teeth)
        for face in faces:
            cmds.select('{}.{}'.format(self.transform, face), add=True)

        self.extrudes = cmds.polyExtrudeFacet(ltz=length)[0]
        cmds.select(clear=True)

    def getTeethFaces(self, teeth=10, length=0.3):
        spans = teeth * 2

        sideFaces = range(spans*2, spans*3, 2)
        faces = []
        for face in sideFaces:
            faces.append('f[{}]'.format(face))
        return faces

    def changeTeeths(self, teeth=10, length=0.3):
        # We know what the constructor is, we can refer to it directly
        cmds.polyPipe(self.constructor, edit=True, subdivisionsAxis=teeth * 2)
        # Then we can just call the makeTeeth directly
        self.modifyExtrudes(teeth=teeth, length=length)

    def modifyExtrudes(self, teeth=10, length=0.3):
        faces = self.getTeethFaces(teeth)
        cmds.setAttr('{}.inputComponents'.format(self.extrudes), len(faces), *faces, type='componentList')

        # Finally we modify the length
        self.changeLengths(length=length)

    def changeLengths(self, length=0.3):
        # This method will change the extrusion of the faces when called
        cmds.polyExtrudeFacet(self.extrudes, edit=True, ltz=length)