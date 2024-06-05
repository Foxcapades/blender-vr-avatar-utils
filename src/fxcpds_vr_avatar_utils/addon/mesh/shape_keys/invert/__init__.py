from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties

    properties.InvertPropertyGroup.register()
    operation.InvertOperator.register()


def unregister() -> None:
    from . import operation, properties

    operation.InvertOperator.unregister()
    properties.InvertPropertyGroup.unregister()
