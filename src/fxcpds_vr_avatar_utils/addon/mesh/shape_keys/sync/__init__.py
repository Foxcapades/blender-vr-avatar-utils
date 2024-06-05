from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties
    properties.SyncPropertyGroup.register()
    operation.SyncOperator.register()


def unregister() -> None:
    from . import operation, properties
    operation.SyncOperator.unregister()
    properties.SyncPropertyGroup.unregister()
