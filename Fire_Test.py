import maya.cmds as cmds
#import alembic.Abc as abc
#import alembic.AbcCoreAbstract as abcca
#import alembic.AbcGeom as abcg

def color_selected(*args):
    rgb = cmds.colorSliderButtonGrp(col, q=True, rgb=True)
    cmds.setAttr('fire_test_nParticleShape1.color[0].color_Color', rgb[0], rgb[1], rgb[2],type="double3")
   

def incandescence_selected(*args):
    rgb0 = cmds.colorSliderButtonGrp(inc0, q=True, rgb=True)
    rgb1 = cmds.colorSliderButtonGrp(inc1, q=True, rgb=True)
    rgb2 = cmds.colorSliderButtonGrp(inc2, q=True, rgb=True)
    cmds.setAttr('fire_test_nParticleShape1.incandescence[0].incandescence_Color', rgb0[0], rgb0[1], rgb0[2],type="double3")
    cmds.setAttr('fire_test_nParticleShape1.incandescence[1].incandescence_Color', rgb1[0], rgb1[1], rgb1[2],type="double3")
    cmds.setAttr('fire_test_nParticleShape1.incandescence[2].incandescence_Color', rgb2[0], rgb2[1], rgb2[2],type="double3")
   
   
def size_changed_cb(*args):
    new_size = cmds.floatSliderGrp(sizer, q=True, v=True)        
    cmds.setAttr('fire_test_emitter1.scale', new_size, new_size, new_size, type='double3')  
   
   
def create_ambient_light(*args):
    new_intensity = cmds.floatSliderGrp(ambientLightIntensity, q=True, v=True)
    if cmds.objExists('ambientLight'):
        light = cmds.ambientLight(n='ambientLight', e=True, intensity=new_intensity)
    else:
        light = cmds.ambientLight(n='ambientLight', intensity=new_intensity)    
   
#    print('Size Dragged')

def turbulence_changed_cb(*args):
    mag = cmds.floatSliderGrp(tubulanceMag, q=True, v=True)
    att = cmds.floatSliderGrp(tubulanceAtt, q=True, v=True)
    fre = cmds.floatSliderGrp(tubulanceFre, q=True, v=True)
    cmds.setAttr('FireTurbulence2.magnitude', mag)
    cmds.setAttr('FireTurbulence2.attenuation', att)
    cmds.setAttr('FireTurbulence2.frequency', fre)
   
#   print('Turbulence Dragged')

#part = cmds.nParticle( p=[(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)] )
#print(part)


window = cmds.window(title="Fire Asset Manager", widthHeight=(500,300))
layout = cmds.columnLayout('fireLayout', adjustableColumn=True, parent=window)
#cmds.color(part, rgb=(255,0,0))
#cmds.button(label="Red", parent=layout)
#cmds.button(label="Blue", parent=layout)
#cmds.button(label="Green", parent=layout)
col = cmds.colorSliderButtonGrp( label='Color', buttonLabel='Select', rgb=(0, 0, 0), parent=layout, bc=color_selected)
inc0 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 0', buttonLabel='Select', rgb=(0, 0, 0), parent=layout, bc=incandescence_selected)
inc1 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 1', buttonLabel='Select', rgb=(0, 0, 0), parent=layout, bc=incandescence_selected)
inc2 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 2', buttonLabel='Select', rgb=(0, 0, 0), parent=layout, bc=incandescence_selected)

sizer = cmds.floatSliderGrp(label='Flame Size', field=True, value=1, parent=layout, dc=size_changed_cb)
tubulanceMag = cmds.floatSliderGrp(label=' Turbulence Magnitude' , field=True, value=1, parent=layout, dc=turbulence_changed_cb)
tubulanceAtt = cmds.floatSliderGrp(label=' Turbulence Attenuation' , field=True, value=1, parent=layout, dc=turbulence_changed_cb)
tubulanceFre = cmds.floatSliderGrp(label=' Turbulence Frequency' , field=True, value=1, parent=layout, dc=turbulence_changed_cb)

ambientLightIntensity = cmds.floatSliderButtonGrp( label='Intensity', field=True, value = 0.0, buttonLabel='Create Ambient Light', parent=layout, bc=create_ambient_light)

cmds.showWindow(window)
