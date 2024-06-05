from ._icons import icons
del _icons


def register(addon_path: str) -> None:
    import os

    # noinspection PyUnresolvedReferences,PyProtectedMember
    icons._init(os.path.join(addon_path, 'assets'))


def unregister() -> None:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    icons._destroy()
