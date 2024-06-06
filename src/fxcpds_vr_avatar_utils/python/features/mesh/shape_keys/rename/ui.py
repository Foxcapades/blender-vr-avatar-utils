from bpy.types import UILayout

from .....lib.ui import UIComponent
from .....lib.xbpy import Context
from .operation import RenameOperator
from .state import State


class UIBox(UIComponent):
    title = "Rename Shape Keys"
    icon = "SHAPEKEY_DATA"

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        row = layout.row()

        left = row.column()
        left.prop(**State.make_rename_from_draw_args(context))
        left.prop(**State.make_rename_to_draw_args(context))

        right = row.column(align=True)
        right.operator(RenameOperator.bl_idname)
        right.scale_y = 2.0
        right.enabled = RenameOperator.is_runnable(context)
