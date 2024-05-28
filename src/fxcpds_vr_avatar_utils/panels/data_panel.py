from ..operators import BoneRotationNormalizeOp, ShapeKeyInvertOp, ShapeKeyRenameOp, ShapeKeySyncOp
from ..properties import get_property_group, PluginProperties
from ..utils import Compatibility

from .aliases import Context, ObjectType

import bpy


class DataPanel(bpy.types.Panel):
    bl_label = "VR Avatar Utils"
    bl_idname = "OBJECT_PT_bmsk_data_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context: Context):
        return context.object is not None and (context.object.type == 'MESH' or context.object.type == 'ARMATURE')

    def draw(self, context: Context):
        obj = context.object
        props = get_property_group()

        column = self.layout.column()

        _draw_global_options(column, props, obj.type)

        column.separator()

        if obj.type == 'MESH':
            _draw_for_mesh(context, column, props)
        elif obj.type == 'ARMATURE':
            _draw_for_pose(column, props)


def _draw_global_options(layout: bpy.types.UILayout, props: PluginProperties, kind: ObjectType) -> None:
    col = layout.box().column()
    col.label(text='Global Options', icon='WORLD')
    col.separator()

    row = col.row()
    row.prop(data=props, property=PluginProperties.PROP_NAME_GLOBAL_DRY_RUN)

    if kind == 'MESH':
        row.prop(data=props, property=PluginProperties.PROP_NAME_LOCK_TO_SCENE)


def _draw_for_mesh(context: Context, layout: bpy.types.UILayout, props: PluginProperties) -> None:
    _draw_sync_shape_keys(context, layout, props)
    layout.separator()
    _draw_shape_key_inversion(layout, props)
    layout.separator()
    _draw_rename_shape_keys(layout, props)


def _draw_for_pose(column: bpy.types.UILayout, props: PluginProperties):
    col = column.box().column()

    col.label(text='Bone Rotation Mode Normalization', icon='BONE_DATA')
    col.separator()

    row = col.row()
    row.prop(data=props, property=PluginProperties.PROP_NAME_BONE_TARGET_ROTATION_MODE)
    row.operator(BoneRotationNormalizeOp.bl_idname)


def _draw_sync_shape_keys(context: Context, layout: bpy.types.UILayout, props: PluginProperties) -> None:
    col = layout.box().column()

    col.label(text='Sync Shape Keys', icon='UV_SYNC_SELECT')

    col.separator()
    col.prop(data=props, property=PluginProperties.PROP_NAME_SYNC_IGNORE_MUTED)

    if Compatibility.have_shape_keys_plus(context):
        row = col.row()
        row.prop(data=props, property=PluginProperties.PROP_NAME_SYNC_COMPAT_SKP_ONLY_FROM_SELECTED)
        row.prop(data=props, property=PluginProperties.PROP_NAME_SYNC_COMPAT_SKP_ONLY_TO_SELECTED)
    else:
        col.prop(data=props, property=PluginProperties.PROP_NAME_SYNC_IGNORE_LOCKED)

    col.separator()
    col.operator(ShapeKeySyncOp.bl_idname)


def _draw_rename_shape_keys(layout: bpy.types.UILayout, props: PluginProperties) -> None:
    col = layout.box().column()

    col.label(text='Rename Shape Keys', icon='SHAPEKEY_DATA')
    col.separator()

    row = col.row()

    left = row.column()
    left.prop(data=props, property=PluginProperties.PROP_NAME_KEY_RENAME_FROM)
    left.prop(data=props, property=PluginProperties.PROP_NAME_KEY_RENAME_TO)

    right = row.column(align=True)
    right.label()
    right.operator(ShapeKeyRenameOp.bl_idname)


def _draw_shape_key_inversion(layout: bpy.types.UILayout, props: PluginProperties) -> None:
    col = layout.box().column()

    col.label(text='Shape Key Inversion', icon='FILE_REFRESH')
    col.separator()

    col.prop(data=props, property=PluginProperties.PROP_NAME_SK_INVERT_BASIS)
    col.prop(data=props, property=PluginProperties.PROP_NAME_SK_INVERT_TOGGLE)
    col.separator()

    row = col.row()
    row.prop(data=props, property=PluginProperties.PROP_NAME_SK_INVERT_REMOVE_MERGED)
    row.prop(data=props, property=PluginProperties.PROP_NAME_SK_INVERT_CREATE_COPY)
    col.separator()

    col.operator(ShapeKeyInvertOp.bl_idname)
