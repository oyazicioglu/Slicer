import bpy

class LineerSliceOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.lineer_slice_operator"
    bl_label = "Lineer Slice Operator"
    bl_options={'TOGGLE'}
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        object = context.object
        object.slicer.sliceType = 1

        return {'FINISHED'}
    
class RadialSliceOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.radial_slice_operator"
    bl_label = "Radial Slice Operator"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        object = context.object
        object.slicer.sliceType = 2

        return {'FINISHED'}

def register():
    bpy.utils.register_class(LineerSliceOperator)
    bpy.utils.register_class(RadialSliceOperator)

def unregister():
    bpy.utils.unregister_class(LineerSliceOperator)
    bpy.utils.unregister_class(RadialSliceOperator)
