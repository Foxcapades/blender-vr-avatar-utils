from .state import FxGlobalStateAccessor


def register() -> None:
    from .properties import FxGlobalProperties
    FxGlobalProperties.register()


def unregister() -> None:
    from .properties import FxGlobalProperties
    FxGlobalProperties.unregister()
