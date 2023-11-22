# SPDX-License-Identifier: GPL-2.0-or-later

import bpy
import math

from bpy.props import PointerProperty

from .properties import MultiFileProperties

from op.op_one import OT_Operator_One
from op.op_two import OT_Operator_Two

class MultiFile_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_multifile_panel"
    bl_label = "Multifile Addon Template"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Toolbox"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        mfa_props = context.scene.multifileaddon_props

        layout.prop(mfa_props, "density", slider=True)
        layout.prop(mfa_props, "radius", slider=True)

        col = layout.column(align=True)
        col.prop(mfa_props, "scale", slider=True)
        col.prop(mfa_props, "random_scale_percentage", text="Randomness", slider=True)

        layout.prop(mfa_props, "use_normal_rotation")
        layout.prop(mfa_props, "rotation", slider=True)
        layout.prop(mfa_props, "normal_offset", text="Offset", slider=True)
        layout.prop(mfa_props, "seed")

        layout.operator('tla.op_one', icon="FUND")
        layout.operator('tla.op_two', icon="KEYTYPE_EXTREME_VEC")

def draw_menu(self, context):
    layout = self.layout
    # layout.operator("object.scatter")

classes = (
    MultiFile_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # bpy.types.Scene.multi_file_properties = PointerProperty(type=MultiFileProperties)
    # bpy.types.VIEW3D_MT_object.append(draw_menu)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # del bpy.types.Scene.multi_file_properties
    # bpy.types.VIEW3D_MT_object.remove(draw_menu)
