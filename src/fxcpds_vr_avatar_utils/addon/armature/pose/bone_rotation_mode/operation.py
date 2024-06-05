import bpy
from bpy.types import Object, UIPopupMenu

from .....lib.operators import FxOperator
from .....lib.xbpy import armatures, Context, Icon, ObjectRotationMode, OperatorReturn
from .....var import obj_mode, op_return

from .state import BoneRotationModeState as State


class BoneRotationOp(FxOperator):
    bl_idname = 'fxcpds_vr_avatar_utils.bone_rotation_normalizer'
    bl_label = 'Normalize Bone Rotations'
    bl_description = (
        'Sets the rotation mode on all of this armature\'s pose to the '
        'selected rotation type.  WARNING: Changing the rotation mode of pose '
        'bones may cause existing pose assets to no longer apply correctly'
    )

    def execute(self, context: Context) -> set[OperatorReturn]:
        if not armatures.has_bones(context.object):
            return {op_return.CANCELLED}

        og_mode = context.object.mode

        if og_mode != obj_mode.POSE:
            bpy.ops.object.mode_set(mode=obj_mode.POSE)

        props = State.from_current_context(context)

        title: str
        icon: Icon
        result: OperatorReturn
        messages: list[str | tuple[str, ObjectRotationMode]] = []
        if props.dry_run:
            title = 'Operation Plan'
            icon = 'QUESTION'
            result = op_return.CANCELLED
            messages = _dry_run(context.object, props.target_rotation_mode)
        else:
            title = 'Operation Result'
            icon = 'INFO'
            result = op_return.FINISHED
            if (count := _live_run(context.object, props.target_rotation_mode)) > 0:
                messages = [f"Updated {count} bones to rotation mode '{props.target_rotation_mode}'"]

        if og_mode != obj_mode.POSE:
            bpy.ops.object.mode_set(mode=og_mode)

        # noinspection PyShadowingNames
        def draw(self: UIPopupMenu, _: Context) -> None:
            if len(messages) == 0:
                self.layout.label("No changes necessary")
            elif isinstance(messages[0], str):
                self.layout.label(messages[0])
            else:
                layout = self.layout
                n = 1
                for tup in messages:
                    msg = f"Change rotation mode on bone '{tup[0]}' from '{tup[1]}' to '{props.target_rotation_mode}'"
                    row = layout.row()
                    row.label(text=str(n))
                    row.label(text=msg)

        context.window_manager.popup_menu(draw, title=title, icon=icon)

        return {result}


def _dry_run(obj: Object, target_mode: str) -> list[tuple[str, ObjectRotationMode]]:
    out: list[tuple[str, ObjectRotationMode]] = []

    for pb in obj.pose.bones:
        if pb.rotation_mode != target_mode:
            out.append((pb.name, pb.rotation_mode))

    return out


def _live_run(obj: Object, target_mode: ObjectRotationMode) -> int:
    count = 0
    original_settings: dict[str, bool] = {}

    for pb in obj.pose.bones:
        original_settings[pb.name] = pb.bone.select

        if pb.rotation_mode == target_mode:
            pb.bone.select = False
        else:
            pb.bone.select = True
            count += 1

    bpy.ops.pose.rotation_mode_set(type=target_mode)

    for pb in obj.pose.bones:
        pb.bone.select = original_settings[pb.name]

    return count
