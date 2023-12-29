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

from .settings.settings import Settings
from .ui.drawPanel import VIEW3D_PT_slicer
from .operators.sceneCreated import SceneCreateOperator
from .ui.dimensionPanel import VIEW3D_PT_dimensions
from .ui.sliceDirectionPanel import OBJECT_PT_slice_direction_type

classes = (
    VIEW3D_PT_slicer,
    Settings,
    SceneCreateOperator,
    VIEW3D_PT_dimensions,
    OBJECT_PT_slice_direction_type,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Object.slicer = bpy.props.PointerProperty(type=Settings)

def unregister():
    del bpy.types.Object.slicer
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()