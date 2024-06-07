from .state import FxGlobalStateAccessor


def register() -> None:
    from .properties import FxGlobalProperties
    FxGlobalProperties.register_class()


def unregister() -> None:
    from .properties import FxGlobalProperties
    FxGlobalProperties.unregister_class()
