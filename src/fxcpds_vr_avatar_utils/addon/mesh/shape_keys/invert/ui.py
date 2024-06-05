from bpy.types import UILayout

from .....lib.xbpy import shape_keys
from .....lib.ui import UIComponent
from .....lib.xbpy import Context
from .....assets import icons
from .operation import InvertOperator
from .state import InvertState as Props


class UIBox(UIComponent):
    title = "Shape Key Inversion"
    icon = icons.invert

    @classmethod
    def should_be_enabled(cls, context: Context) -> bool:
        return shape_keys.count_shape_keys(context.object) > 1

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        layout.prop(**Props.make_new_basis_draw_args(context))
        layout.prop(**Props.make_toggle_key_draw_args(context))
        layout.separator()

        row = layout.row()
        row.prop(**Props.make_remove_merged_draw_args(context))
        row.prop(**Props.make_create_copy_draw_args(context))
        layout.separator()

        row = layout.row()
        row.operator(InvertOperator.bl_idname)
        row.enabled = InvertOperator.is_runnable(context)
