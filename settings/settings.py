
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
        ("NONE", "None", "", 1),
        ("LINEER", "Lineer", "", 2),
        ("RADIAL", "Radial", "", 3),
    ], name="", default="NONE", options={'ANIMATABLE'})
