import bpy
from ..registry import Registrable
from .utils import silent_unregister_class


class Panel(bpy.types.Panel, Registrable):
    @classmethod
    def register(cls) -> None:
        bpy.utils.register_class(cls)

    @classmethod
    def unregister(cls) -> None:
        silent_unregister_class(cls)


__all__ = ['Panel']
