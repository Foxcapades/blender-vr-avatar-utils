from bpy.types import Object
from .keys import require_key, is_keyed

__all__ = ['has_shape_keys', 'count_shape_keys']


def count_shape_keys(obj: Object) -> int:
    return len(require_key(obj).key_blocks) if is_keyed(obj) else 0


def has_shape_keys(obj: Object) -> bool:
    return count_shape_keys(obj) > 0
