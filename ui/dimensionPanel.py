import bpy

class VIEW3D_PT_dimensions(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "OBJECT_PT_dimensions"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label="Plate Dimensions"
    bl_parent_id="OBJECT_PT_slice"
    bl_options={'HIDE_HEADER'}
    
    @classmethod
    def poll(cls, context):
        return context.object.slicer is not None and context.object.type == 'MESH' 
        
    def draw(self, context):
        if context.object.slicer.target:
            layout = self.layout
            dimensionProps = context.object.slicer
            dimensionColumn = layout.column(align=True)
            dimensionColumn.label(text="Dimensions", icon="ORIENTATION_GLOBAL")
            dimensionColumn.prop(dimensionProps, "width")
            dimensionColumn.prop(dimensionProps, "length")
            dimensionColumn.prop(dimensionProps, "thickness")