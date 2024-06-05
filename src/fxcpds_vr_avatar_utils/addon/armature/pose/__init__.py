from .bone_rotation_mode import ui


def register() -> None:
    from . import bone_rotation_mode as brm
    brm.register()


def unregister() -> None:
    from . import bone_rotation_mode as brm
    brm.unregister()
