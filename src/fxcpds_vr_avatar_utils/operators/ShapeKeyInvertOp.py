from typing import cast

from .aliases import Context, OperatorReturn
from ..properties import get_property_group, PluginProperties
from ..utils import is_keyed_mesh, select_only

from bpy.types import Mesh, Object, Operator

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
        _execute(InverterContext(context, get_property_group()))

        # noinspection PyShadowingNames
        def draw(self, _):
            self.layout.column().label(text='Done')

        context.window_manager.popup_menu(draw, title="Shape Key Invert Result", icon='INFO')

        return {'FINISHED'}


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
    def __init__(self, ctx: Context, props: PluginProperties):
        self.context = ctx

        self.object = _create_duplicate(ctx.object, ctx) if props.shape_key_inversion_create_copy else ctx.object
        self.key_blocks = cast(Mesh, self.object.data).shape_keys.key_blocks

        self.new_basis = props.shape_key_inversion_basis_replacement.strip()
        self.toggle_name = props.shape_key_inversion_toggle.strip()

        if len(self.toggle_name):
            self.toggle_name = _safe_toggle_shape_key_name(ctx.object, self.new_basis)

        self.remove_merged = props.shape_key_inversion_remove_merged


def _create_duplicate(obj: Object, ctx: Context) -> Object:
    bpy.ops.object.mode_set(mode='OBJECT')
    select_only(obj, ctx)
    bpy.ops.object.duplicate()
    return ctx.object


def _execute(c: 'InverterContext') -> None:
    # Create a duplicate of our target object.  This duplicate will become
    # the base value for our toggle key.
    duplicate_object = _create_duplicate(c.object, c.context)

    # Zero the duplicate's shape keys (except the toggle key, if present)
    _zero_shape_keys(duplicate_object, c.toggle_name)

    # Reselect just the target object
    select_only(c.object, c.context)

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

    if c.remove_merged:
        c.object.active_shape_key_index = c.key_blocks.find(c.new_basis)
        bpy.ops.object.shape_key_remove()

    # Add our temp duplicate to the selection.
    duplicate_object.select_set(True)

    # Join the duplicate to the target object as a new shape key.
    bpy.ops.object.join_shapes()

    # Rename the new shape key.
    new_key_idx = len(c.key_blocks) - 1
    c.key_blocks[new_key_idx].name = c.toggle_name

    # Remove the temp duplicate
    select_only(duplicate_object, c.context)
    bpy.ops.object.delete(confirm=False)

    # Select the target object again.
    select_only(c.object, c.context)

    # Select the new toggle shape key.
    c.object.active_shape_key_index = new_key_idx


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
