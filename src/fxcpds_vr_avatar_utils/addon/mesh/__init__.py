from .ui import MeshPanel


def register() -> None:
    from . import shape_keys

    shape_keys.register()


def unregister() -> None:
    from . import shape_keys

    shape_keys.unregister()
