bl_info = {
    "name": "multi-file-addon-template",
    "author": "Pete <pete@vertexape.io>",
    "version": (0, 0, 1),
    "blender": (3, 6, 0),
    "location": "3D View > Toolbox",
    "description": "A collection of handy tools",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "The Line",
}

if "bpy" in locals():
    import importlib
    importlib.reload(op)
    importlib.reload(ui)
    importlib.reload(properties)
    importlib.reload(preferences)
else:
    import bpy
    from . import op
    from . import ui
    from . import properties
    from . import preferences

def register():
    preferences.register()
    properties.register()
    ui.register()
    op.register()

def unregister():
    preferences.unregister()
    properties.unregister()
    ui.unregister()
    op.unregister()
