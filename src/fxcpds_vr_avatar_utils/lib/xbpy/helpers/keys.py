from typing import cast, Protocol
from bpy.types import Key, Object
from ....var import obj_type

__all__ = ['is_keyed', 'require_key']


# noinspection PyPropertyDefinition
class _Keyed(Protocol):
    @property
    def shape_keys(self) -> Key: pass


def is_keyed(obj: Object) -> bool:
    return obj is not None and (
        obj.type == obj_type.MESH
        or obj.type == obj_type.LATTICE
        or obj.type == obj_type.CURVE
    ) and require_key(obj) is not None


def require_key(obj: Object) -> Key:
    return cast(_Keyed, obj.data).shape_keys
