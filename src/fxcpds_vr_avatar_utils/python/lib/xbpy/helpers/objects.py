import bpy.ops.object
from bpy.types import Object
from ..aliases import Context

__all__ = ['duplicate', 'select_only']


def duplicate(obj: Object, ctx: Context, select_new: bool = True) -> Object:
    og_mode = obj.mode
    if og_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    select_only(obj, ctx)
    bpy.ops.object.duplicate()

    new_object = ctx.active_object
    select_only(new_object if select_new else obj, ctx)

    if og_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode=og_mode)

    return new_object


def select_only(obj: Object, ctx: Context) -> None:
    if ctx.active_object is not None and ctx.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    ctx.view_layer.objects.active = obj
