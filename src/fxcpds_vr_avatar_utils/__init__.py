bl_info = {
    "name":        "Foxcapades' VR Avatar Utils",
    "description": "Miscellaneous utilities for aiding in work on VR avatars.",
    "author":      "Elizabeth Paige Harper",
    "version":     (0, 2, 1),
    "category":    "Object",
    "blender":     (4, 1, 0),
}


def register() -> None:
    import os
    from . import assets, addon

    assets.register(os.path.dirname(__file__))
    addon.register()


def unregister() -> None:
    from . import assets, addon

    addon.unregister()
    assets.unregister()
