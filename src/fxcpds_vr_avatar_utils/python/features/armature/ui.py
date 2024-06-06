from typing import Iterable

from bpy.types import UILayout

from ...lib.ui import UIPanelBody, UIComponent
from ...lib.xbpy import armatures, Context
from ...var import obj_type
from . import pose


class ArmaturePanelBody(UIPanelBody):
    @classmethod
    def ui_components(cls, _: Context) -> Iterable[UIComponent]:
        yield pose.ui

    @classmethod
    def should_be_drawn(cls, context: Context) -> bool:
        return context.object.type == obj_type.ARMATURE

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        if not armatures.has_bones(context.object):
            layout.label(text="Add bones to this armature to enabled VR Avatar Util operations.")
        else:
            super().draw(layout, context)
