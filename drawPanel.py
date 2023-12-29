import bpy

class VIEW3D_PT_slicer(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_space_type = 'PROPERTIES'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Slicer"
    bl_label = "Slicer"
    
    def draw(self, context):
        layout = self.layout
        
        if context.object.sceneOptions.created:
            if context.mode == 'OBJECT' and len(context.selected_objects) > 0 and context.active_object.type == "MESH":
                sceneOptions = context.object.sceneOptions
                layout.prop_search(context.scene, sceneOptions.target, context.scene, "objects", text="")
                dimensionProps = context.object.dimentionOptions
                dimensionColumn = layout.column(align=True, heading="Dimensions")
                dimensionColumn.prop(dimensionProps, "width")
                dimensionColumn.prop(dimensionProps, "length")
                dimensionColumn.prop(dimensionProps, "thickness")
            else:
                col = layout.column(align=True)
                col.label(text="Select a mesh object")
        else:
            col = layout.column(align=True)
            layout.operator("object.scene_create_operator", text="Create Slice")
    
    
    
    