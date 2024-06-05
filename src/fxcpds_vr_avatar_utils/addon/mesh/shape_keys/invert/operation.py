from typing import Callable, Generator

import bpy
from bpy.types import Key, Object, UIPopupMenu

from .....lib.operators import FxOperator
from .....lib.xbpy import keys, objects, Context, Icon, OperatorReturn
from .....var import op_return
from .state import InvertState


class InvertOperator(FxOperator):
    bl_idname = 'fxcpds_vr_avatar_utils.invert_shape_key'
    bl_label = 'Invert Shape Key'
    bl_description = (
        'Inverts a shape key, turning it into the new basis while creating or '
        'replacing a \'toggle\' shape key'
    )

    def execute(self, context: Context) -> set[OperatorReturn]:
        if not self.is_runnable(context):
            return {op_return.CANCELLED}

        props = InvertState(context)
        ctx = _InversionContext(props, _get_toggle_shape_key_name(keys.require_key(context.object), props))

        messages: list[str]

        if props.dry_run:
            n = 1
            messages = [f"{n:02} - {s[0]}" for s in _build_steps(ctx)]
        else:
            for _, fn in _build_steps(ctx):
                fn(ctx)
            messages = ['Done']

        def draw(s: UIPopupMenu, _: Context):
            col = s.layout.column()
            for msg in messages:
                col.label(text=msg)

        title: str
        icon: Icon
        result: OperatorReturn
        if props.dry_run:
            title = 'Would have performed the following steps:'
            icon = 'QUESTION'
            result = 'CANCELLED'
        else:
            title = 'Shape Key Inversion Result'
            icon = 'INFO'
            result = 'FINISHED'

        context.window_manager.popup_menu(draw, title=title, icon=icon)

        return {result}

    @classmethod
    def is_runnable(cls, ctx: Context) -> bool:
        if (key := keys.require_key(ctx.object)) is None:
            return False

        basis = InvertState.get_new_basis(ctx).strip()

        if len(basis) == 0 or len(key.key_blocks) < 2 or key.key_blocks[0].name == basis:
            return False

        return basis in key.key_blocks


class _InversionContext:
    duplicate_object: Object

    def __init__(self, props: InvertState, toggle_key: str) -> None:
        ctx = props.context
        self.object = ctx.object
        self.key_blocks = keys.require_key(ctx.object).key_blocks
        self.props = props
        self.toggle_key = toggle_key

    @property
    def context(self) -> Context: return self.props.context

    @property
    def basis_key(self) -> str: return self.props.new_basis.strip()

    @property
    def delete_new_basis_key(self) -> bool: return self.props.remove_merged

    @property
    def create_copy(self) -> bool: return self.props.create_copy


def _get_toggle_shape_key_name(key: Key, props: InvertState) -> str:
    out = props.toggle_key.strip()

    if len(out) > 0:
        return out

    out = 'toggle.' + props.new_basis

    n = 1
    while True:
        attempt = out + f".{n:03}"

        if attempt not in key.key_blocks:
            return attempt

        n += 1


def _get_object_clone_name(obj: Object, ctx: Context) -> str:
    n = 1
    while True:
        attempt = obj.name + f".{n:03}"

        if attempt not in ctx.blend_data.objects:
            return attempt


def _build_steps(c: _InversionContext) -> Generator[tuple[str | None, Callable[[_InversionContext], None]], None, None]:
    object_name = c.object.name

    if c.create_copy:
        clone_name = _get_object_clone_name(c.object, c.context)
        yield None, _step_select_current
        yield f"create a working copy of object '{object_name}' ({clone_name})", _step_create_working_copy
        yield None, _step_select_current
        object_name = clone_name

    with c.context.temp_override(object=c.object):
        yield f"create a temporary duplicate of object '{object_name}'", _step_make_temp_duplicate
        yield f"zero out non-target shape keys on temporary duplicate object", _step_zero_shape_keys
        yield None, _step_select_current
        yield f"apply shape key '{c.basis_key}' to basis on object '{object_name}'", _step_apply_new_basis
        if c.delete_new_basis_key:
            yield f"remove shape key '{c.basis_key}' from object '{object_name}'", _step_remove_basis_key
        yield f"apply temporary duplicate object as new shape key on object '{object_name}'", _step_apply_dup
        yield f"delete temporary duplicate object", _step_delete_temp_duplicate
        if c.toggle_key in c.key_blocks:
            yield f"remove current '{c.toggle_key}' shape key from object '{object_name}'", _step_remove_toggle_key
        yield f"rename new shape key to '{c.toggle_key}'", _step_rename_new_shape_key
        yield None, _step_select_new_shape_key


def _step_select_current(c: _InversionContext) -> None:
    objects.select_only(c.object, c.context)


def _step_create_working_copy(c: _InversionContext) -> None:
    c.object = objects.duplicate(c.object, c.context)


def _step_make_temp_duplicate(c: _InversionContext) -> None:
    c.duplicate_object = objects.duplicate(c.object, c.context)


def _step_zero_shape_keys(c: _InversionContext) -> None:
    key = keys.require_key(c.duplicate_object)
    toggle = None if c.basis_key == c.toggle_key else c.toggle_key

    for sk in key.key_blocks:
        if sk.name == toggle:
            sk.value = sk.slider_max
        else:
            sk.value = 0.0


def _step_apply_new_basis(c: _InversionContext) -> None:
    c.object.active_shape_key_index = 0
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.blend_from_shape(shape=c.basis_key)
    bpy.ops.object.mode_set(mode='OBJECT')


def _step_remove_basis_key(c: _InversionContext) -> None:
    c.object.active_shape_key_index = c.key_blocks.find(c.basis_key)
    bpy.ops.object.shape_key_remove()


def _step_apply_dup(c: _InversionContext) -> None:
    c.duplicate_object.select_set(True)
    bpy.ops.object.join_shapes()


def _step_delete_temp_duplicate(c: _InversionContext) -> None:
    objects.select_only(c.duplicate_object, c.context)
    bpy.ops.object.delete(confirm=False)
    objects.select_only(c.object, c.context)


def _step_remove_toggle_key(c: _InversionContext) -> None:
    c.object.active_shape_key_index = c.key_blocks.find(c.toggle_key)
    bpy.ops.object.shape_key_remove()


def _step_rename_new_shape_key(c: _InversionContext) -> None:
    c.key_blocks[len(c.key_blocks) - 1].name = c.toggle_key


def _step_select_new_shape_key(c: _InversionContext) -> None:
    c.object.active_shape_key_index = len(c.key_blocks) - 1
