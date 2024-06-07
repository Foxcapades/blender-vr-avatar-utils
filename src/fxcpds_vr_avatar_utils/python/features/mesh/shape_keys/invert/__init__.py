from . import ui


ui = ui.UIBox


def register() -> None:
    from . import operation, properties

    properties.InvertPropertyGroup.register_class()
    operation.InvertOperator.register_class()


def unregister() -> None:
    from . import operation, properties

    operation.InvertOperator.unregister_class()
    properties.InvertPropertyGroup.unregister_class()
