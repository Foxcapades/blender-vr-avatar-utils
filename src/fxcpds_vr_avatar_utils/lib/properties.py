import typing
import bpy

from .registry import Registrable


P = typing.TypeVar('P')


class AddonProperties(bpy.types.PropertyGroup, Registrable, typing.Generic[P]):
    target_type: type[P]

    @classmethod
    def register(cls) -> None:
        bpy.utils.register_class(cls)
        setattr(cls.target_type, cls.name, bpy.props.PointerProperty(type=cls))

    @classmethod
    def unregister(cls) -> None:
        from ..lib.xbpy import silent_unregister_property
        silent_unregister_property(cls, cls.target_type, cls.name)

    @classmethod
    def get_from(cls, kind: P) -> typing.Self:
        return kind[cls.name]
