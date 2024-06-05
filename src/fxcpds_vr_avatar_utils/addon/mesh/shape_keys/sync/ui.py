from bpy.types import UILayout

from .....lib.ui import UIComponent
from .....lib.xbpy import shape_keys, Context
from .....compat import addons

from .operation import SyncOperator
from .state import State


class UIBox(UIComponent):
    title = "Sync Shape Keys"
    icon = "UV_SYNC_SELECT"

    @classmethod
    def should_be_enabled(cls, context: Context) -> bool:
        return shape_keys.count_shape_keys(context.object) > 1

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        layout.prop(**State.make_ignore_muted_draw_args(context))

        if addons.ShapeKeysPlus.is_available(context):
            row = layout.row()
            row.prop(**State.make_skp_only_from_selected_draw_args(context))
            row.prop(**State.make_skp_only_to_selected_draw_args(context))
        else:
            layout.prop(**State.make_ignore_locked_draw_args(context))

        layout.separator()
        layout.operator(SyncOperator.bl_idname)
