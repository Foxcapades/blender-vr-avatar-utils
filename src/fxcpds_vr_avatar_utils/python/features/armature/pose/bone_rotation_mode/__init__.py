from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties

    properties.BoneRotationPropertyGroup.register()
    operation.BoneRotationOp.register()


def unregister() -> None:
    from . import operation, properties

    operation.BoneRotationOp.unregister()
    properties.BoneRotationPropertyGroup.unregister()
