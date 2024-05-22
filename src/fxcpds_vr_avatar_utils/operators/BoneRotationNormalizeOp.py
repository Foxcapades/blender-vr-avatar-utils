from ..properties import get_property_group

from .aliases import Context, OperatorReturn

from bpy.types import Menu, Operator

import bpy


class BoneRotationNormalizeOp(Operator):
    bl_idname = 'fxcpds_vr_avatar_utils.pose_normalizer'
    bl_label = 'Normalize Bone Rotations'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = (
        'Sets the rotation mode on all of this armature\'s pose to the '
        'selected rotation type.  WARNING: Changing the rotation mode of pose '
        'bones may cause existing pose assets to no longer apply correctly'
    )

    def execute(self, context: Context) -> set[OperatorReturn]:
        if context.object is None or context.object.type != 'ARMATURE':
            return {'CANCELLED'}

        original_mode = context.object.mode

        bpy.ops.object.mode_set(mode='POSE')

        props = get_property_group()

        change_count = 0

        for pb in context.pose_object.pose.bones.values():
            if pb.rotation_mode != props.target_rotation_mode:
                change_count += 1
                pb.bone.select = True
            else:
                pb.bone.select = False

        if change_count == 0:
            self._render_result(context, 0, props.dry_run)
            bpy.ops.object.mode_set(mode=original_mode)
            return {'CANCELLED'}

        if not props.dry_run:
            bpy.ops.pose.rotation_mode_set(type=props.target_rotation_mode)

        self._render_result(context, change_count, props.dry_run)

        bpy.ops.object.mode_set(mode=original_mode)

        if props.dry_run:
            return {'CANCELLED'}
        else:
            return {'FINISHED'}

    @staticmethod
    def _render_result(context: Context, count: int, dry_mode: bool) -> None:
        if count == 0:
            text = 'Nothing would have changed.' if dry_mode else 'Nothing was changed'
        elif dry_mode:
            text = f'Would have updated the rotation mode of {count} bones.'
        else:
            text = f'Updated the rotation mode of {count} bones.'

        def draw(self: Menu, _):
            self.layout.label(text=text)

        context.window_manager.popup_menu(draw, title='Bone Normalization Result', icon='INFO')
