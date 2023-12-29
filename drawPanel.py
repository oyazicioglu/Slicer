import bpy


class VIEW3D_PT_slicer(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "OBJECT_PT_slice"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label="Slicer"
    
    @classmethod
    def poll(cls, context):
        return context.object and context.object.sceneOptions is not None
    
    def draw(self, context):
        layout = self.layout
        sceneOptions = context.object.sceneOptions
        
        if sceneOptions and sceneOptions.target:
            layout.prop_search(context.object.sceneOptions, "target", context.scene, "objects", text="")
        else:
            col = layout.column(align=True)
            col.operator("object.scene_create_operator", text="Create Slice")
        