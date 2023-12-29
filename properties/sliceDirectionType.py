
import bpy

class SliceDirectionType(bpy.types.PropertyGroup):
    directions : bpy.props.EnumProperty(items =[
        ("NONE", "None", "", 1),
        ("LINEER", "Lineer", "", 2),
        ("RADIAL", "Radial", "", 3),
    ], name="", default="NONE", options={'ANIMATABLE'})