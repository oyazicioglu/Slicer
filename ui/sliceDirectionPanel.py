import bpy
    
class OBJECT_PT_slice_direction_type(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "OBJECT_PT_slice_direction_type"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label="Slice Type"
    bl_parent_id="OBJECT_PT_slice"
    bl_options={'HIDE_HEADER'}
    
    @classmethod
    def poll(cls, context):
        return context.object.slicer.target is not None and context.object.type == 'MESH' 
        
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.separator()
        col.label(text="Slice Type", icon="NODE_SIDE")
        col.prop(context.object.slicer, "directions")
        
        if(context.object.slicer.directions == 'LINEER'):
            directionRow = layout.row(heading="Axis")
            directionRow.prop(context.object.slicer, "directionAxies", expand=True)