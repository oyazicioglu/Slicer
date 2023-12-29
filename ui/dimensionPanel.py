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
        return context.object.sceneOptions is not None
        
    def draw(self, context):
        if context.object.sceneOptions.target:
            layout = self.layout
            dimensionProps = context.object.dimentionOptions
            dimensionColumn = layout.column(align=True, heading="Plane Dimensions")
            dimensionColumn.prop(dimensionProps, "width")
            dimensionColumn.prop(dimensionProps, "length")
            dimensionColumn.prop(dimensionProps, "thickness")