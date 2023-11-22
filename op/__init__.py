if "bpy" in locals():
    import importlib
    importlib.reload(op_one)
    importlib.reload(op_two)

else:
    from . import op_one
    from . import op_two

import bpy

classes = [
        op_one.OT_Operator_One,
        op_two.OT_Operator_Two
        ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
