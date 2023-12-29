import bpy

class SceneCreateOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.scene_create_operator"
    bl_label = "Scene Created Operator"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        print(context)
        object = context.object
        sceneOptions = object.sceneOptions
        sceneOptions.target = context.active_object
        sceneOptions.created = True

        return {'FINISHED'}