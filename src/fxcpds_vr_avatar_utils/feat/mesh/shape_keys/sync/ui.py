from bpy.types import UILayout

from .....utils.aliases import Context
from .....utils import context as ctx, compatibility

from .operator import SyncOperator
from .props import SyncProps


def draw(layout: UILayout, context: Context) -> None:
    key = ctx.current_key(context)

    col = layout.box().column()

    col.label(text='Sync Shape Keys', icon='UV_SYNC_SELECT')

    col.separator()
    SyncProps.draw_ignore_muted(key, col)

    if compatibility.have_shape_keys_plus(context):
        row = col.row()
        SyncProps.draw_skp_only_from_selected(key, row)
        SyncProps.draw_skp_only_to_selected(key, row)
    else:
        SyncProps.draw_ignore_locked(key, col)

    col.separator()
    col.operator(SyncOperator.bl_idname)
