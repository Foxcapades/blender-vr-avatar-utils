from bpy.types import UILayout

from .....assets import icons
from .....lib import ui, xbpy
from .operation import BoneRotationOp
from .state import BoneRotationModeState as State


class UIBox(ui.UIComponent):
    title = "Bone Rotation Mode Normalization"
    icon = icons.bone_rotation

    @classmethod
    def draw(cls, layout: UILayout, context: xbpy.Context) -> None:
        row = layout.row()
        row.prop(**State.make_target_rotation_mode_draw_args(context))
        row.operator(BoneRotationOp.bl_idname)
