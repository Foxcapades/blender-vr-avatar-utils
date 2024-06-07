from abc import abstractmethod, ABC
from typing import Generic, Self, TypeVar

from bpy.types import PropertyGroup
from bpy.props import PointerProperty

from .xpy import classproperty
from .registry import Registrable


P = TypeVar('P')


class _PropMeta(type(PropertyGroup), type(ABC)): pass


class AddonProperties(PropertyGroup, Registrable, Generic[P], ABC, metaclass=_PropMeta):
    @classproperty
    @abstractmethod
    def target_type(cls) -> type[P]:
        pass

    @classmethod
    def register(cls) -> None:
        """
        This is here just to override the ABC.register classmethod to avoid
        errors from Blender's register_class method calling it.
        """
        pass

    @classmethod
    def register_class(cls) -> None:
        import bpy.utils
        bpy.utils.register_class(cls)
        setattr(cls.target_type, cls.name, PointerProperty(type=cls))

    @classmethod
    def unregister_class(cls) -> None:
        from ..lib.xbpy import silent_unregister_property
        silent_unregister_property(cls, cls.target_type, cls.name)

    @classmethod
    def get_from(cls, kind: P) -> Self:
        return kind[cls.name]
