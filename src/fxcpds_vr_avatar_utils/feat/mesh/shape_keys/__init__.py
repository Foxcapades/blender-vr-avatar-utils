from .ui import draw


__all__ = ['draw', 'register', 'unregister']


def register() -> None:
    from . import rename, sync
    rename.register()
    sync.register()


def unregister() -> None:
    from . import rename, sync
    rename.register()
    sync.register()
