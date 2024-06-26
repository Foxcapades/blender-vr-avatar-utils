import abc
import typing
import bpy

from . import registry


P = typing.TypeVar('P')


class AddonProperties(bpy.types.PropertyGroup, registry.Registrable, typing.Generic[P], abc.ABC):
    target_type: type[P]

    @classmethod
    def register_class(cls) -> None: pass

    @classmethod
    def unregister_class(cls) -> None: pass

    @classmethod
    def get_from(cls, kind: P) -> typing.Self: pass
