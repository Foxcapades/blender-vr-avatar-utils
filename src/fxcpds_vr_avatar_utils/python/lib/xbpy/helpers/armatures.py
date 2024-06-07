from typing import cast
from bpy.types import Armature, Object
from ....var import obj_type

__all__ = ['is_armature', 'is_usable_armature', 'has_bones', 'to_armature']


def is_armature(obj: Object) -> bool:
    return obj is not None and obj.type == obj_type.ARMATURE


def is_usable_armature(obj: Object) -> bool:
    return is_armature(obj) and obj.data is not None and cast(Armature, obj.data).bones is not None


def has_bones(obj: Object) -> bool:
    return is_usable_armature(obj) and len(to_armature(obj).bones) > 0


def to_armature(obj: Object) -> Armature:
    return cast(Armature, obj.data)
