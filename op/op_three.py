import bpy

class OT_Operator_Three(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tla.op_three"
    bl_label = "op three"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print ("OP THREE")
        return {'FINISHED'}
