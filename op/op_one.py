import bpy

class OT_Operator_One(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "tla.op_one"
    bl_label = "op one"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print ("OP ONE")
        return {'FINISHED'}
