def register() -> None:
    from . import common, armature, mesh, ui
    common.register()
    armature.register()
    mesh.register()
    ui.FxPropsPanel.register_class()


def unregister() -> None:
    from . import common, armature, mesh, ui
    ui.FxPropsPanel.unregister_class()
    mesh.unregister()
    armature.unregister()
    common.unregister()
