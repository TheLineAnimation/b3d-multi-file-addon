import bpy
from bpy.types import AddonPreferences

class MFA_Preferences(bpy.types.AddonPreferences):
    """Preferences class: Preferences for this add-on"""

    bl_idname = __package__

    # bl_idname = __name__
    category: bpy.props.StringProperty(
        name="Unfold Panel Category", 
        description="Category in 3D View Toolbox where the Unfold panel is displayed",
        default="Paper" 
    )

    project_name: bpy.props.StringProperty(
        name="Export Panel Category", 
        description="Category in 3D View Toolbox where the Export panel is displayed",
        default="Paper"
    )

    # enable to add features to built-in menu
    toggle_builtin_menu: bpy.props.BoolProperty(
        name="Built-in Menu",
        description="Enable built-in menu",
        default=True
    )

    # enable debug mode
    toggle_debug_mode:  bpy.props.BoolProperty(
        name="Debug Mode",
        description="Enable debugging mode",
        default=False
    )

    def draw(self, _):
        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False


        col = self.layout.column(align=True)
        # col.label(text="Parameters:")

        col.prop(self, "category", text="Category")
        col.prop(self, "project_name", text="Project")

        col.separator()

        box = col.box()
        box.label(text="Options:")
        box.prop(self, "toggle_builtin_menu", text="Built-in Menu")
        box.prop(self, "toggle_debug_mode", text="Debug Mode")

        def text_row (parent, label):
            split = parent.split(factor=0.4)
            split.label(text="")
            split.label(text=label)

        text_row(box, "WAAAAATTT")

        # sub.prop(self, "toggle_builtin_menu", text="WAT")
        # sub.prop(self, "toggle_debug_mode")


def register():
    # for cls in classes:
    bpy.utils.register_class(MFA_Preferences)

def unregister():
    #   for cls in classes:
    bpy.utils.unregister_class(MFA_Preferences)

    
