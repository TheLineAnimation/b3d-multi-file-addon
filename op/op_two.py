import bpy

class OT_Operator_Two(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tla.op_two"
    bl_label = "op two"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print ("OP TWO")
        return {'FINISHED'}
