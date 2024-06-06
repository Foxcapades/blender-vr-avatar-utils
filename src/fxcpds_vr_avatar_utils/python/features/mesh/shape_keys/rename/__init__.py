from . import ui

ui = ui.UIBox


def register() -> None:
    from . import operation, properties
    properties.RenamePropertyGroup.register()
    operation.RenameOperator.register()


def unregister() -> None:
    from . import operation, properties
    operation.RenameOperator.unregister()
    properties.RenamePropertyGroup.unregister()
