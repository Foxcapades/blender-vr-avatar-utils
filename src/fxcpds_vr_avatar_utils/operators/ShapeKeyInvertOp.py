from typing import cast, Callable, Generator

from .aliases import Context, Icon, OperatorReturn
from ..properties import get_property_group, PluginProperties
from ..utils import is_keyed_mesh, select_only

from bpy.types import Menu, Mesh, Object, Operator

import bpy


class ShapeKeyInvertOp(Operator):
    bl_idname = 'fxcpds_vr_avatar_utils.invert_shape_key'
    bl_label = 'Invert Shape Key'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = (
        'Inverts a shape key, turning it into the new basis while creating or '
        'replacing a \'toggle\' shape key'
    )

    @classmethod
    def poll(cls, context: Context) -> bool:
        return _is_valid(context, get_property_group())

    def execute(self, context: Context) -> set[OperatorReturn]:
        props = get_property_group()
        steps: list[str]

        if props.dry_run:
            steps = self._execute_dry_run(context, props)
        else:
            self._execute_live_run(context, props)
            steps = []

        # noinspection PyShadowingNames
        def draw(self: Menu, _):
            col = self.layout.column()

            if len(steps) == 0:
                col.label(text='Done')
            else:
                for i, step in enumerate(steps):
                    col.label(text=f'{i:02} - {step}')

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

    @staticmethod
    def _execute_live_run(context: Context, props: PluginProperties) -> None:
        target = context.object
        if props.shape_key_inversion_create_copy:
            target = _create_duplicate(target, context)
            context.object.hide_set(state=True, view_layer=context.view_layer)

        basis = props.shape_key_inversion_basis_replacement.strip()
        toggle = ShapeKeyInvertOp._get_toggle_shape_key_name(props, target, basis)
        i_ctx = InverterContext(target, context, basis, toggle, props.shape_key_inversion_remove_merged)

        if target.name != context.object.name:
            with context.temp_override(object=target):
                for _, fn in _build_steps(i_ctx):
                    fn(i_ctx)
        else:
            for _, fn in _build_steps(i_ctx):
                fn(i_ctx)

    @staticmethod
    def _execute_dry_run(context: Context, props: PluginProperties) -> list[str]:
        steps: list[str] = []

        target = context.object
        object_name = target.name

        if props.shape_key_inversion_create_copy:
            dup_name = object_name + ".dup"
            steps.append(f"create duplicate of object '{object_name}' ({dup_name})")
            steps.append(f"hide object '{object_name}'")
            object_name = dup_name

        basis = props.shape_key_inversion_basis_replacement.strip()
        toggle = ShapeKeyInvertOp._get_toggle_shape_key_name(props, target, basis)
        i_ctx = InverterContext(target, context, basis, toggle, props.shape_key_inversion_remove_merged)

        for step, _ in _build_steps(i_ctx, object_name):
            steps.append(step)

        return steps

    @staticmethod
    def _get_toggle_shape_key_name(props: PluginProperties, target: Object, basis: str) -> str:
        out = props.shape_key_inversion_toggle.strip()

        if len(out) == 0:
            out = _safe_toggle_shape_key_name(target, basis)

        return out


def _is_valid(ctx: Context, props: PluginProperties) -> bool:
    basis = props.shape_key_inversion_basis_replacement.strip()

    if len(basis) == 0:
        return False

    if not is_keyed_mesh(ctx.object):
        return False

    blocks = cast(Mesh, ctx.object.data).shape_keys.key_blocks

    if len(blocks) < 2:
        return False

    if blocks[0].name == basis:
        return False

    for sk in blocks:
        if sk.name == basis:
            return True

    return False


class InverterContext:
    def __init__(self, obj: Object, ctx: Context, new_basis: str, toggle_name: str, remove_merged: bool):
        self.object = obj
        self.context = ctx
        self.key_blocks = cast(Mesh, obj.data).shape_keys.key_blocks
        self.new_basis = new_basis
        self.toggle_name = toggle_name
        self.remove_merged = remove_merged

        self.duplicate_object: Object | None = None


def _create_duplicate(obj: Object, ctx: Context) -> Object:
    bpy.ops.object.mode_set(mode='OBJECT')
    select_only(obj, ctx)
    bpy.ops.object.duplicate()
    return ctx.active_object


def _zero_shape_keys(obj: Object, toggle_key: str) -> None:
    key = cast(Mesh, obj.data).shape_keys

    for sk in key.key_blocks:
        if sk.name == toggle_key:
            sk.value = sk.slider_max
        else:
            sk.value = 0.0


def _safe_toggle_shape_key_name(obj: Object, new_basis_name: str) -> str:
    toggle_base = 'toggle.' + new_basis_name
    keys = cast(Mesh, obj.data).shape_keys.key_blocks

    if toggle_base not in keys:
        return toggle_base

    n = 1
    while True:
        attempt = toggle_base + f'{n:03}'

        if attempt not in keys:
            return attempt

        n += 1


def _build_steps(
    c: InverterContext,
    object_name: str = None,
) -> Generator[tuple[str, Callable[[InverterContext], None]], None, None]:
    if not object_name:
        object_name = c.object.name

    yield f"create a temporary duplicate of '{object_name}'", __step_make_temp_dup
    yield f"zero irrelevant shape keys on the temp duplicate", __step_zero_shape_keys
    yield f"focus selection on '{object_name}'", __step_select_target_object
    yield f"apply shape key '{c.new_basis}' to '{object_name}' basis", __step_apply_new_basis
    if c.remove_merged:
        yield f"remove shape key '{c.new_basis}' from '{object_name}'", __step_remove_merged
    yield f"apply temp duplicate object as new shape key on object '{object_name}'", __step_apply_dup_as_shape_key
    yield f"rename new shape key to '{c.toggle_name}'", __step_rename_shape_key
    yield f"delete the temp duplicate object", __step_delete_duplicate_object
    yield f"select shape key '{c.toggle_name}' on object '{object_name}'", __step_select_new_shape_key


def __step_make_temp_dup(c: InverterContext) -> None:
    """
    Create a duplicate of our target object.

    This duplicate will become the base value for our toggle key.
    """
    c.duplicate_object = _create_duplicate(c.object, c.context)


def __step_zero_shape_keys(c: InverterContext) -> None:
    """Zero the duplicate's shape keys (except the toggle key, if present)"""
    _zero_shape_keys(c.duplicate_object, c.toggle_name)


def __step_select_target_object(c: InverterContext) -> None:
    """Select the operation target object."""
    select_only(c.object, c.context)


def __step_apply_new_basis(c: InverterContext) -> None:
    # Select the object's basis key
    c.object.active_shape_key_index = 0

    # Go to edit mode so that we can apply the new basis shape to the actual
    # basis shape key
    bpy.ops.object.mode_set(mode='EDIT')

    # Apply the new basis shape to the object basis
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.blend_from_shape(shape=c.new_basis)

    # Switch back to object mode.
    bpy.ops.object.mode_set(mode='OBJECT')


def __step_remove_merged(c: InverterContext) -> None:
    c.object.active_shape_key_index = c.key_blocks.find(c.new_basis)
    bpy.ops.object.shape_key_remove()


def __step_apply_dup_as_shape_key(c: InverterContext) -> None:
    # Add our temp duplicate to the selection.
    c.duplicate_object.select_set(True)

    # Join the duplicate to the target object as a new shape key.
    bpy.ops.object.join_shapes()


def __step_rename_shape_key(c: InverterContext) -> None:
    # Remove the toggle key (if present) so we can safely rename the new toggle
    # key to the target name.
    if c.toggle_name in c.key_blocks:
        c.object.active_shape_key_index = c.key_blocks.find(c.toggle_name)
        bpy.ops.object.shape_key_remove()

    # Rename the new shape key.
    c.key_blocks[len(c.key_blocks) - 1].name = c.toggle_name


def __step_delete_duplicate_object(c: InverterContext) -> None:
    select_only(c.duplicate_object, c.context)
    bpy.ops.object.delete(confirm=False)


def __step_select_new_shape_key(c: InverterContext) -> None:
    select_only(c.object, c.context)
    c.object.active_shape_key_index = len(c.key_blocks) - 1
