import bpy

from .data_panel import DataPanel


def register_panels() -> None:
    bpy.utils.register_class(DataPanel)


def unregister_panels() -> None:
    bpy.utils.unregister_class(DataPanel)
