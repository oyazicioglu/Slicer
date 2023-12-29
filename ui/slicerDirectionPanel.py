import bpy
    
class OBJECT_PT_slice_direction_type(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "OBJECT_PT_slice_direction_type"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label="Slice Direction"
    bl_parent_id="OBJECT_PT_slice"
    bl_options={'HIDE_HEADER'}
    
    @classmethod
    def poll(cls, context):
        return context.object.sceneOptions is not None
        
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.separator()
        col.label(text="Slice Direction")
        col.prop(context.object.directionTypes, "directions")
        