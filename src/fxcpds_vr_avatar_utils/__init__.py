bl_info = {
    "name":        "Foxcapades' VR Avatar Utils",
    "description": "Miscellaneous utilities for aiding in work on VR avatars.",
    "author":      "Elizabeth Paige Harper",
    "version":     (0, 1, 0),
    "category":    "Object",
    "blender":     (4, 1, 1),
}

from . import operators
from . import panels
from . import properties
from . import utils


def register() -> None:
    properties.register_property_group()
    operators.register_operators()
    panels.register_panels()


def unregister() -> None:
    panels.unregister_panels()
    operators.unregister_operators()
    properties.unregister_property_group()
