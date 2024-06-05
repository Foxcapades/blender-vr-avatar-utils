from . import ui

ui = ui.ArmaturePanelBody


def register() -> None:
    from . import pose
    pose.register()


def unregister() -> None:
    from . import pose
    pose.unregister()
