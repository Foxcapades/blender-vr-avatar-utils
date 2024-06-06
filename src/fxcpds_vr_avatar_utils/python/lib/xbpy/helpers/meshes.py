from bpy.types import Object
from fxcpds_vr_avatar_utils.python.var import obj_type
from .keys import require_key
from .shape_keys import has_shape_keys

__all__ = ['is_keyed_mesh', 'is_mesh', 'is_mesh_with_shape_keys']


def is_keyed_mesh(obj: Object) -> bool:
    return is_mesh(obj) and require_key(obj) is not None


def is_mesh(obj: Object) -> bool:
    return obj is not None and obj.type == obj_type.MESH


def is_mesh_with_shape_keys(obj: Object) -> bool:
    return is_mesh(obj) and has_shape_keys(obj)

