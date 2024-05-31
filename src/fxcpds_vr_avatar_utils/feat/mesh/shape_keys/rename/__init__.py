from .ui import draw


__all__ = ['draw', 'register', 'unregister']


def register() -> None:
    from . import props, operator
    props.register()
    operator.unregister()


def unregister() -> None:
    from . import props, operator
    props.unregister()
    operator.unregister()
