from typing import Iterable

from bpy.types import UILayout

from ...lib.ui import UIPanelBody, UIComponent
from ...lib.xbpy import shape_keys as sk, Context
from ...var import obj_type
from . import shape_keys


class MeshPanel(UIPanelBody):
    @classmethod
    def ui_components(cls, context: Context) -> Iterable[UIComponent]:
        yield shape_keys.sync_ui
        yield shape_keys.invert_ui
        yield shape_keys.rename_ui

    @classmethod
    def should_be_drawn(cls, context: Context) -> bool:
        return context.object.type == obj_type.MESH

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        if not sk.has_shape_keys(context.object):
            layout.label(text="Add shape keys to this mesh to enabled VR Avatar Util operations.")
        else:
            super().draw(layout, context)
