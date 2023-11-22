
if "bpy" in locals():
    import importlib
    importlib.reload(version_utils)
    importlib.reload(file_utils)

else:
    from . import version_utils
    from . import file_utils

import bpy
