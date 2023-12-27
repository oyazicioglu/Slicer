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

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Slicer"
    bl_idname = "OBJECT_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT' and len(context.selected_objects) > 0 and context.active_object.type == "MESH"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
    
def execute(self, context):
    return {'FINISHED'}
    
def register():
    bpy.utils.register_class(LayoutDemoPanel)

def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)

if __name__ == "__main__":
    register()

