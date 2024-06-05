from .invert import ui as invert_ui
from .rename import ui as rename_ui
from .sync import ui as sync_ui


def register() -> None:
    invert.register()
    rename.register()
    sync.register()


def unregister() -> None:
    invert.unregister()
    rename.unregister()
    sync.unregister()
