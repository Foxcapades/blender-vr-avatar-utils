from bpy.types import UILayout
from ....utils.aliases import Context
from .sync import draw as draw_sync
from .rename import draw as draw_rename


def draw(layout: UILayout, context: Context) -> None:
    draw_sync(layout, context)
    layout.separator()
    draw_rename(layout, context)
