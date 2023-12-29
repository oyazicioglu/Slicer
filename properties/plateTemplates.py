
import bpy

class PlateTemplates(bpy.types.PropertyGroup):
    templates : bpy.props.EnumProperty(items =[
        ("CUSTOM", "Custom", "", 1),
        ("RED", "Red", "", 2),
        ("GREEN", "Green", "", 3),
        ("BLUE", "Blue", "", 4),
        ("YELLOW", "Yellow", "", 5),
    ], name="", default="CUSTOM",options={'ANIMATABLE'})