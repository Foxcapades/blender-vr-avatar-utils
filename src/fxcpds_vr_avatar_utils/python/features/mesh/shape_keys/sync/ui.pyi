import bpy.types
from ..... import lib

class UIBox(lib.ui.UIComponent):
    @classmethod
    def draw(cls, layout: bpy.types.UILayout, context: lib.xbpy.Context) -> None: pass
