from typing import cast, Protocol

from bpy.types import Key, Mesh, Object

from .aliases import Context

import bpy


# noinspection PyPropertyDefinition
class Keyed(Protocol):
    @property
    def shape_keys(self) -> Key: pass


def require_key(obj: Object) -> Key:
    return cast(Keyed, obj.data).shape_keys


def count_shape_keys(obj: Object) -> int:
    if not (obj is not None and (obj.type == 'MESH' or obj.type == 'LATTICE' or obj.type == 'CURVE')):
        return 0

    data = cast(Keyed, obj.data)

    return len(data.shape_keys.key_blocks)


def has_key(obj: Object) -> bool:
    return (
        obj is not None
        and (obj.type == 'MESH' or obj.type == 'LATTICE' or obj.type == 'CURVE')
        and cast(Keyed, obj.data).shape_keys is not None
    )


def has_shape_keys(obj: Object) -> bool:
    return count_shape_keys(obj) > 0


def is_usable_mesh(obj: Object) -> bool:
    return obj is not None and obj.type == 'MESH'


def is_keyed_mesh(obj: Object) -> bool:
    return is_usable_mesh(obj) and cast(Mesh, obj.data).shape_keys is not None


def is_mesh_with_shape_keys(obj: Object) -> bool:
    if not is_usable_mesh(obj):
        return False

    key = cast(Mesh, obj.data).shape_keys

    return key is not None and len(key.key_blocks) > 0


def select_only(obj: Object, ctx: Context) -> None:
    if ctx.active_object is not None and ctx.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    ctx.view_layer.objects.active = obj
