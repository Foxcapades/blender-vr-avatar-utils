from bpy.types import UILayout

from .....utils.aliases import Context
from .....utils import context as ctx

from .operator import RenameOperator
from .props import RenameProps


def draw(layout: UILayout, context: Context) -> None:
    key = ctx.current_key(context)
    col = layout.box().column()

    col.label(text='Rename Shape Keys', icon='SHAPEKEY_DATA')
    col.separator()

    row = col.row()

    left = row.column()
    RenameProps.draw_rename_from(key, left)
    RenameProps.draw_rename_to(key, left)

    right = row.column(align=True)
    right.operator(RenameOperator.bl_idname)
    right.scale_y = 2.0
    right.enabled = RenameOperator.is_runnable(key)
