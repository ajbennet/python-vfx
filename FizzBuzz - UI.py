import maya.cmds as cmds


def FizzBuzz(*args): 
    fizz = cmds.intFieldGrp(fizzField, q=True, value1=True)
    buzz = cmds.intFieldGrp(fizzField, q=True, value2=True)
    stop = cmds.intFieldGrp(fizzField, q=True, value3=True)
    for fizzbuzz in range(stop):
        if fizzbuzz % fizz == 0 and fizzbuzz % buzz == 0:
            print("fizzbuzz")
            cmds.scrollField(OutputField,edit=True,insertText='fizzbuzz \n', ip=0)
            continue
        elif fizzbuzz % fizz == 0:
            print("fizz")
            cmds.scrollField(OutputField,edit=True,insertText='fizz \n', ip=0)
            
            continue
        elif fizzbuzz % buzz == 0:
            print("buzz")
            cmds.scrollField(OutputField,edit=True,insertText='buzz \n', ip=0)
            continue
        
        print(fizzbuzz)
        cmds.scrollField(OutputField,edit=True,insertText=fizzbuzz, ip=0)
        cmds.scrollField(OutputField,edit=True,insertText='\n', ip=0)
              

cmds.window()
cmds.paneLayout( configuration='horizontal4' )
fizzField = cmds.intFieldGrp( numberOfFields=3, label='Fizz Buzz', extraLabel='Stop', value1=3, value2=5, value3=20  )
cmds.button(label = 'Fizz Buzz', command=FizzBuzz)
OutputField = cmds.scrollField( editable=True, wordWrap=True )
cmds.showWindow()



