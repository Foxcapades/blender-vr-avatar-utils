from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties

    properties.BoneRotationPropertyGroup.register_class()
    operation.BoneRotationOp.register_class()


def unregister() -> None:
    from . import operation, properties

    operation.BoneRotationOp.unregister_class()
    properties.BoneRotationPropertyGroup.unregister_class()
