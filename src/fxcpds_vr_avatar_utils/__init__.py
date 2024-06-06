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
    from .python import features
    from .python.lib import assets

    assets.register(os.path.dirname(__file__))
    features.register()


def unregister() -> None:
    from .python import features
    from .python.lib import assets

    features.unregister()
    assets.unregister()
