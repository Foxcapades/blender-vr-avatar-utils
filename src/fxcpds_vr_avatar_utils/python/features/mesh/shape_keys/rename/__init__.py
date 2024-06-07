from . import ui

ui = ui.UIBox


def register() -> None:
    from . import operation, properties
    properties.RenamePropertyGroup.register_class()
    operation.RenameOperator.register_class()


def unregister() -> None:
    from . import operation, properties
    operation.RenameOperator.unregister_class()
    properties.RenamePropertyGroup.unregister_class()
