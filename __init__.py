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


class VIEW3D_PT_slicer(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_space_type = 'PROPERTIES'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label = "Slicer"
    
    my_float = bpy.props.FloatProperty(name="Some Floating Point", default=0.0)

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT' and len(context.selected_objects) > 0 and context.active_object.type == "MESH"

    def draw(self, context):
        layout = self.layout
        dimensionProps = context.scene.dimensions
        
        col = layout.column(align=True, heading="Dimensions")
        col.prop(dimensionProps, "width")
        col.prop(dimensionProps, "length")
        col.prop(dimensionProps, "thickness")
    
    
classes = (
    DimensionSettings,
    VIEW3D_PT_slicer,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.dimensions = bpy.props.PointerProperty(type=DimensionSettings)

def unregister():
    del bpy.types.Scene.dimensions
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

