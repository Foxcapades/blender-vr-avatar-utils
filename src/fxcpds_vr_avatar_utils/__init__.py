bl_info = {
    "name":        "Foxcapades' VR Avatar Utils",
    "description": "Miscellaneous utilities for aiding in work on VR avatars.",
    "author":      "Elizabeth Paige Harper",
    "version":     (0, 2, 1),
    "category":    "Object",
    "blender":     (4, 1, 0),
}

from . import assets, operators, panels, properties, utils


def register() -> None:
    import os

    properties.register_property_group()
    operators.register_operators()
    panels.register_panels()
    assets.register(os.path.dirname(__file__))


def unregister() -> None:
    panels.unregister_panels()
    operators.unregister_operators()
    properties.unregister_property_group()
