from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties
    properties.SyncPropertyGroup.register_class()
    operation.SyncOperator.register_class()


def unregister() -> None:
    from . import operation, properties
    operation.SyncOperator.unregister_class()
    properties.SyncPropertyGroup.unregister_class()
