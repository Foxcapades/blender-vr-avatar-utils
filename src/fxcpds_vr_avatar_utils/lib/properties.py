from abc import abstractmethod, ABC
from typing import Generic, Self, TypeVar

from bpy.types import PropertyGroup
from bpy.props import PointerProperty

from .xpy import classproperty
from .registry import Registrable


P = TypeVar('P')


class AddonProperties(PropertyGroup, Registrable, Generic[P], ABC):
    @classproperty
    @abstractmethod
    def target_type(cls) -> type[P]:
        pass

    @classmethod
    def register(cls) -> None:
        from bpy.utils import register_class
        register_class(cls)
        setattr(cls.target_type, cls.name, PointerProperty(type=cls))

    @classmethod
    def unregister(cls) -> None:
        from ..lib.xbpy import silent_unregister_property
        silent_unregister_property(cls, cls.target_type, cls.name)

    @classmethod
    def get_from(cls, kind: P) -> Self:
        return kind[cls.name]
