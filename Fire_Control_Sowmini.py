import maya.cmds as cmds

#Getting the existing colors from the scene and assigning it to the controls
fire_inc_rgb0 = cmds.getAttr('nParticle_fire.color[0].color_Color')
embers_inc_rgb0 = cmds.getAttr('nParticle_embers.color[0].color_Color')
smoke_inc_rgb0 = cmds.getAttr('nParticle_smoke.color[0].color_Color')



def fire_color_selected(*args):
    rgb = cmds.colorSliderButtonGrp(fire_col, q=True, rgb=True)
    #Dont change the value if its the same as the previous rgb value
    if rgb != fire_inc_rgb0[0]:
        fire_inc_rgb0[0] = rgb
        cmds.setAttr('nParticle_fire.color[0].color_Color', rgb[0], rgb[1], rgb[2],type="double3")
        print('Changed fire color to ', rgb)
    else:
        print('Didnt change fire color because it was the same color as before') 

def fire_incandescence_selected(*args):
    rgb0 = cmds.colorSliderButtonGrp(fire_inc0, q=True, rgb=True)
    rgb1 = cmds.colorSliderButtonGrp(fire_inc1, q=True, rgb=True)
    rgb2 = cmds.colorSliderButtonGrp(fire_inc2, q=True, rgb=True)
    cmds.setAttr('nParticle_fire.incandescence[0].incandescence_Color', rgb0[0], rgb0[1], rgb0[2],type="double3")
    cmds.setAttr('nParticle_fire.incandescence[1].incandescence_Color', rgb1[0], rgb1[1], rgb1[2],type="double3")
    cmds.setAttr('nParticle_fire.incandescence[2].incandescence_Color', rgb2[0], rgb2[1], rgb2[2],type="double3")
    print('Changed fire incandescence gradient to',  rgb0, rgb1, rgb2 )
   
def fire_size_changed_cb(*args):
    new_size = cmds.floatSliderGrp(fire_sizer, q=True, v=True)        
    cmds.setAttr('emitter_fire.scale', new_size, new_size, new_size, type='double3')  
    print('Changed fire size to ', new_size)
    

def fire_size_button_cb(*args):
    new_size = cmds.floatSliderGrp(fire_sizer, q=True, v=True) 
    i=1
    #increasing size gradually to demonstrate while loop
    while i<=new_size:
        print('increasing size gradually ,', i)  
        cmds.setAttr('emitter_fire.scale', new_size, new_size, new_size, type='double3')
        i += 1  
    print('Button clicked - Changed fire size to ', new_size)
   
   
def fire_turbulence_changed_cb(*args):
    mag = cmds.floatSliderGrp(fire_tubulanceMag, q=True, v=True)
    att = cmds.floatSliderGrp(fire_tubulanceAtt, q=True, v=True)
    fre = cmds.floatSliderGrp(fire_tubulanceFre, q=True, v=True)
    cmds.setAttr('turbulenceField2.magnitude', mag)
    cmds.setAttr('turbulenceField2.attenuation', att)
    cmds.setAttr('turbulenceField2.frequency', fre)
    print('Changed turbulence magnitude to :',mag, ' attenuation to: ', att, ' frequency to:', fre)  


def embers_color_selected(*args):
    rgb = cmds.colorSliderButtonGrp(embers_col, q=True, rgb=True)
    #Dont change the value if its the same as the previous rgb value
    if rgb != embers_inc_rgb0[0]:
        embers_inc_rgb0[0] = rgb
        cmds.setAttr('nParticle_embers.color[0].color_Color', rgb[0], rgb[1], rgb[2],type="double3")
        print('Changed embers color to ', rgb)
    else:
        print('Didnt change embers color because it was the same color as before') 
   

def embers_incandescence_selected(*args):
    rgb0 = cmds.colorSliderButtonGrp(embers_inc0, q=True, rgb=True)
    rgb1 = cmds.colorSliderButtonGrp(embers_inc1, q=True, rgb=True)
    rgb2 = cmds.colorSliderButtonGrp(embers_inc2, q=True, rgb=True)
    cmds.setAttr('nParticle_embers.incandescence[0].incandescence_Color', rgb0[0], rgb0[1], rgb0[2],type="double3")
    cmds.setAttr('nParticle_embers.incandescence[1].incandescence_Color', rgb1[0], rgb1[1], rgb1[2],type="double3")
    cmds.setAttr('nParticle_embers.incandescence[2].incandescence_Color', rgb2[0], rgb2[1], rgb2[2],type="double3")
    print('Changed embers incandescence gradient to',  rgb0, rgb1, rgb2 )
   
def embers_size_changed_cb(*args):
    new_size = cmds.floatSliderGrp(embers_sizer, q=True, v=True)        
    cmds.setAttr('emitter_embers.scale', new_size, new_size, new_size, type='double3')  
    print('Changed embers size to ', new_size)
   
   
def embers_turbulence_changed_cb(*args):
    mag = cmds.floatSliderGrp(embers_tubulanceMag, q=True, v=True)
    att = cmds.floatSliderGrp(embers_tubulanceAtt, q=True, v=True)
    fre = cmds.floatSliderGrp(embers_tubulanceFre, q=True, v=True)
    cmds.setAttr('turbulenceField1.magnitude', mag)
    cmds.setAttr('turbulenceField1.attenuation', att)
    cmds.setAttr('turbulenceField1.frequency', fre)
    print('Changed embers turbulence magnitude to :',mag, ' attenuation to: ', att, ' frequency to:', fre)  

    
  
def smoke_color_selected(*args):
    rgb = cmds.colorSliderButtonGrp(smoke_col, q=True, rgb=True)
    #Dont change the value if its the same as the previous rgb value
    if rgb != fire_inc_rgb0[0]:
        smoke_inc_rgb0[0] = rgb
        cmds.setAttr('nParticle_smoke.color[0].color_Color', rgb[0], rgb[1], rgb[2],type="double3")
        print('Changed smoke color to ', rgb)
    else:
        print('Didnt change smoke color because it was the same color as before') 

def smoke_incandescence_selected(*args):
    rgb0 = cmds.colorSliderButtonGrp(smoke_inc0, q=True, rgb=True)
    rgb1 = cmds.colorSliderButtonGrp(smoke_inc1, q=True, rgb=True)
    rgb2 = cmds.colorSliderButtonGrp(smoke_inc2, q=True, rgb=True)
    cmds.setAttr('nParticle_smoke.incandescence[0].incandescence_Color', rgb0[0], rgb0[1], rgb0[2],type="double3")
    cmds.setAttr('nParticle_smoke.incandescence[1].incandescence_Color', rgb1[0], rgb1[1], rgb1[2],type="double3")
    cmds.setAttr('nParticle_smoke.incandescence[2].incandescence_Color', rgb2[0], rgb2[1], rgb2[2],type="double3")
    print('Changed smoke incandescence gradient to',  rgb0, rgb1, rgb2 )
   
def smoke_size_changed_cb(*args):
    new_size = cmds.floatSliderGrp(smoke_sizer, q=True, v=True)        
    cmds.setAttr('emitter_smoke.scale', new_size, new_size, new_size, type='double3')  
    print('Changed smoke size to ', new_size) 
   
   
   
def smoke_turbulence_changed_cb(*args):
    mag = cmds.floatSliderGrp(smoke_tubulanceMag, q=True, v=True)
    att = cmds.floatSliderGrp(smoke_tubulanceAtt, q=True, v=True)
    fre = cmds.floatSliderGrp(smoke_tubulanceFre, q=True, v=True)
    cmds.setAttr('turbulenceField4.magnitude', mag)
    cmds.setAttr('turbulenceField4.attenuation', att)
    cmds.setAttr('turbulenceField4.frequency', fre)  
    print('Changed smoke turbulence magnitude to :',mag, ' attenuation to: ', att, ' frequency to:', fre)  


window = cmds.window( widthHeight=(550, 250) )
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
#Fire tab
fireLayout = cmds.rowColumnLayout('fireLayout', numberOfColumns=1)
fire_col = cmds.colorSliderButtonGrp( label='Fire Color', buttonLabel='Select', rgb=fire_inc_rgb0[0], parent=fireLayout, bc=fire_color_selected)
fire_inc0 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 0', buttonLabel='Select', rgb=(0, 0, 0), parent=fireLayout, bc=fire_incandescence_selected)
fire_inc1 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 1', buttonLabel='Select', rgb=(0, 0, 0), parent=fireLayout, bc=fire_incandescence_selected)
fire_inc2 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 2', buttonLabel='Select', rgb=(0, 0, 0), parent=fireLayout, bc=fire_incandescence_selected)

fire_sizer = cmds.floatSliderButtonGrp(label='Flame Size', field=True, buttonLabel='Change', value=1, parent=fireLayout, dc=fire_size_changed_cb, bc=fire_size_button_cb )
fire_tubulanceMag = cmds.floatSliderGrp(label=' Turbulence Magnitude' , field=True, value=1, parent=fireLayout, dc=fire_turbulence_changed_cb)
fire_tubulanceAtt = cmds.floatSliderGrp(label=' Turbulence Attenuation' , field=True, value=1, parent=fireLayout, dc=fire_turbulence_changed_cb)
fire_tubulanceFre = cmds.floatSliderGrp(label=' Turbulence Frequency' , field=True, value=1, parent=fireLayout, dc=fire_turbulence_changed_cb)

cmds.setParent( '..' )

#Embers tab
embersLayout = cmds.rowColumnLayout('embersLayout', numberOfColumns=1)
embers_col = cmds.colorSliderButtonGrp( label='Embers Color', buttonLabel='Select', rgb=embers_inc_rgb0[0], parent=embersLayout, bc=embers_color_selected)
embers_inc0 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 0', buttonLabel='Select', rgb=(0, 0, 0), parent=embersLayout, bc=embers_incandescence_selected)
embers_inc1 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 1', buttonLabel='Select', rgb=(0, 0, 0), parent=embersLayout, bc=embers_incandescence_selected)
embers_inc2 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 2', buttonLabel='Select', rgb=(0, 0, 0), parent=embersLayout, bc=embers_incandescence_selected)

embers_sizer = cmds.floatSliderGrp(label='Flame Size', field=True, value=1, parent=embersLayout, dc=size_changed_cb)
embers_tubulanceMag = cmds.floatSliderGrp(label=' Turbulence Magnitude' , field=True, value=1, parent=embersLayout, dc=embers_turbulence_changed_cb)
embers_tubulanceAtt = cmds.floatSliderGrp(label=' Turbulence Attenuation' , field=True, value=1, parent=embersLayout, dc=embers_turbulence_changed_cb)
embers_tubulanceFre = cmds.floatSliderGrp(label=' Turbulence Frequency' , field=True, value=1, parent=embersLayout, dc=embers_turbulence_changed_cb)

cmds.setParent( '..' )


#Smoke tab
smokeLayout = cmds.rowColumnLayout('smokeLayout', numberOfColumns=1)
smoke_col = cmds.colorSliderButtonGrp( label='Smoke Color', buttonLabel='Select', rgb=smoke_inc_rgb0[0], parent=smokeLayout, bc=smoke_color_selected)
smoke_inc0 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 0', buttonLabel='Select', rgb=(0, 0, 0), parent=smokeLayout, bc=smoke_incandescence_selected)
smoke_inc1 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 1', buttonLabel='Select', rgb=(0, 0, 0), parent=smokeLayout, bc=smoke_incandescence_selected)
smoke_inc2 = cmds.colorSliderButtonGrp( label='Incandescence Gradient 2', buttonLabel='Select', rgb=(0, 0, 0), parent=smokeLayout, bc=smoke_incandescence_selected)

smoke_sizer = cmds.floatSliderGrp(label='Flame Size', field=True, value=1, parent=smokeLayout, dc=smoke_size_changed_cb)
smoke_tubulanceMag = cmds.floatSliderGrp(label=' Turbulence Magnitude' , field=True, value=1, parent=smokeLayout, dc=smoke_turbulence_changed_cb)
smoke_tubulanceAtt = cmds.floatSliderGrp(label=' Turbulence Attenuation' , field=True, value=1, parent=smokeLayout, dc=smoke_turbulence_changed_cb)
smoke_tubulanceFre = cmds.floatSliderGrp(label=' Turbulence Frequency' , field=True, value=1, parent=smokeLayout, dc=smoke_turbulence_changed_cb)

cmds.setParent( '..' )

cmds.tabLayout( tabs, edit=True, tabLabel=((fireLayout, 'Fire'), (embersLayout, 'Embers'), (smokeLayout, 'Smoke')) )

cmds.showWindow(window)
