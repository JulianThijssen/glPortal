import bpy
from bpy.props import *

glpTypes = [
    ("none" ,"None" , "No special property"),
    ("wall" ,"Wall" , "Wall"),
    ("door" ,"Door" , "Door"),         
    ("trigger" , "Trigger" , "trigger")
]

glpWallTypes = [
    ("default" ,"Default" , "Nothing special just a painted concrete wall"),
    ("invisible" ,"Invisible" , "Invisible (Not implemented)"),    
    ("glass" ,"Glass" , "Glass (Not implemented)"),
    ("portable" ,"Portable" , "Portable Wall")
]

glpTriggerTypes = [
    ("none" ,"None" , "No special property"), 
    ("win" , "Trigger Win" , "Area triggers win"), 
    ("death" , "Trigger Death" , "Area triggers death"),
    ("radiation" , "Trigger Radiation" , "Area triggers rad"),
    ("portable" , "Portable" , "Set Wall Portable")
]

def setTypes():
    bpy.types.Object.glpTypes = EnumProperty(
        items = glpTypes,
        name = "Type")

def setTriggerTypes():
    bpy.types.Object.glpTriggerTypes = EnumProperty(
        items = glpTriggerTypes,
        name = "Trigger Type")    

def setWallTypes():
    bpy.types.Object.glpWallTypes = EnumProperty(
        items = glpWallTypes,
        name = "Wall Type")    

    
setTypes()
setTriggerTypes();
setWallTypes();
