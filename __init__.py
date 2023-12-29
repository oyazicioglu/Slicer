bl_info = {
    "name": "Slicer",
    "description": "Slice wood panel",
    "author": "Ömer YAZICIOĞLU",
    "version": (0, 0, 1),
    "blender": (4, 0, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }
    
import bpy

from .properties.sliceDirectionType import SliceDirectionType
from .properties.dimensionSettings import DimensionSettings
from .drawPanel import VIEW3D_PT_slicer
from .properties.sceneSettings import SceneOptions
from .operators.sceneCreated import SceneCreateOperator
from .ui.dimensionPanel import VIEW3D_PT_dimensions
from .ui.slicerDirectionPanel import OBJECT_PT_slice_direction_type

classes = (
    VIEW3D_PT_slicer,
    DimensionSettings,
    SceneOptions,
    SceneCreateOperator,
    VIEW3D_PT_dimensions,
    OBJECT_PT_slice_direction_type,
    SliceDirectionType
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Object.dimentionOptions = bpy.props.PointerProperty(type=DimensionSettings)
    bpy.types.Object.sceneOptions = bpy.props.PointerProperty(type=SceneOptions)
    bpy.types.Object.directionTypes = bpy.props.PointerProperty(type=SliceDirectionType)

def unregister():
    del bpy.types.Object.dimentionOptions
    del bpy.types.Object.sceneOptions
    del bpy.types.Object.directionTypes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()