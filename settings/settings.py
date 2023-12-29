
import bpy

    
class Settings(bpy.types.PropertyGroup):
    width: bpy.props.FloatProperty(
        name='Width',
        default=2200.0 
    )

    length: bpy.props.FloatProperty(
        name='Length',
        default=1700.0 
    )

    thickness: bpy.props.FloatProperty(
        name='Thickness',
        default=18 
    )
    
    target: bpy.props.PointerProperty(type=bpy.types.Object, name="target")

    directions : bpy.props.EnumProperty(items =[
        ("LINEER", "Lineer", "", 1),
        ("RADIAL", "Radial", "", 2),
    ], name="", default="LINEER", options={'ANIMATABLE'})
    
    directionAxies : bpy.props.EnumProperty(items =(('0','X',''),('1','Y',''),('1','Z','')))