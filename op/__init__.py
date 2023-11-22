"""
    import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module

import sys, inspect
def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)

"""



if "bpy" in locals():
    import importlib
    importlib.reload(op_one)
    importlib.reload(op_two)
    importlib.reload(op_three)


else:
    from . import op_one
    from . import op_two
    from . import op_three

import bpy

classes = [
        op_one.OT_Operator_One,
        op_two.OT_Operator_Two,
        op_three.OT_Operator_Three
        ]

import sys, inspect
def print_classes():

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.ismodule(obj):
            print( f'FOUND {name} : {obj}')

def register():
    # print( 'OP INIT REGISTER')
    print_classes()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
