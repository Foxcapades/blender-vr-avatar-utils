from . import icons as _icons


icons = _icons.Icons()


def register(addon_path: str) -> None:
    import os

    global icons

    icons._init(os.path.join(addon_path, 'assets'))

