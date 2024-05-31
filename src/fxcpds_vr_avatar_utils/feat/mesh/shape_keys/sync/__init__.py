from .ui import draw


def register() -> None:
    from . import operator, props
    props.register()
    operator.register()


def unregister() -> None:
    from . import operator, props
    operator.unregister()
    props.unregister()


operator = None
props = None
ui = None
