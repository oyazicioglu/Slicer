
import bpy

class DimensionSettings(bpy.types.PropertyGroup):
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
        default=1.8 
    )
    
