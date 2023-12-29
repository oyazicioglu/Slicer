import bpy

class SceneCreateOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.scene_create_operator"
    bl_label = "Scene Created Operator"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        object = context.object
        object.slicer.target = context.active_object

        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(SceneCreateOperator)

def unregister():
    bpy.utils.unregister_class(SceneCreateOperator)
