from . import _icons

icons = _icons.Icons()


def register(addon_path: str) -> None:
    import os

    # noinspection PyUnresolvedReferences,PyProtectedMember
    icons._init(os.path.join(addon_path, 'assets'))


def unregister() -> None:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    icons._destroy()
