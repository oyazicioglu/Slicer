
import bpy

class SceneSettings(bpy.types.PropertyGroup):
    created: bpy.props.BoolProperty(
        name='Created',
        default=False
    )
    
    target: bpy.props.PointerProperty(type=bpy.types.Object)