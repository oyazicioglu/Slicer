
import bpy

class SceneOptions(bpy.types.PropertyGroup):
    target: bpy.props.PointerProperty(type=bpy.types.Object, name="target")