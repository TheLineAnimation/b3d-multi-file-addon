import bpy

from bpy.props import (
    BoolProperty,
    IntProperty,
    FloatProperty,
    PointerProperty
)


class MultiFileProperties(bpy.types.PropertyGroup):
    seed: IntProperty(
        name="Seed",
        default=0,
        description="Change it to get a different scatter pattern",
    )

    density: FloatProperty(
        name="Density",
        default=10,
        min=0,
        soft_max=50,
        description="The amount of objects per unit on the line",
    )

    radius: FloatProperty(
        name="Radius",
        default=1,
        min=0,
        soft_max=5,
        subtype='DISTANCE',
        unit='LENGTH',
        description="Maximum distance of the objects to the line",
    )

    scale: FloatProperty(
        name="Scale",
        default=0.3,
        min=0.00001,
        soft_max=1,
        description="Size of the generated objects",
    )

    random_scale_percentage: FloatProperty(
        name="Random Scale Percentage",
        default=80,
        min=0,
        max=100,
        subtype='PERCENTAGE',
        precision=0,
        description="Increase to get a larger range of sizes",
    )



    normal_offset: FloatProperty(
        name="Normal Offset",
        default=0,
        soft_min=-1.0,
        soft_max=1.0,
        description="Distance from the surface",
    )

    use_normal_rotation: BoolProperty(
        name="Use Normal Rotation",
        default=True,
        description="Rotate the instances according to the surface normals",
    )

def register():
    bpy.utils.register_class(MultiFileProperties)
    bpy.types.Scene.multifileaddon_props = PointerProperty(type=MultiFileProperties)

def unregister():
    bpy.utils.unregister_class(MultiFileProperties)
    del bpy.types.Scene.multifileaddon_props


