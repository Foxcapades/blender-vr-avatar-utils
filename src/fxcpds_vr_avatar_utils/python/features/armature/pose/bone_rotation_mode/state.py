from typing import cast

from .....lib.xbpy import Context, ObjectRotationMode, UIPropsParameters
from ....common import FxGlobalStateAccessor
from .properties import BoneRotationPropertyGroup


class BoneRotationModeState(FxGlobalStateAccessor):
    target_rotation_mode: ObjectRotationMode = property(
        lambda self: self.get_props(self.context.window_manager).target_rotation_mode)

    @staticmethod
    def make_target_rotation_mode_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'target_rotation_mode'}

    @staticmethod
    def get_target_rotation_mode(c: Context) -> ObjectRotationMode:
        return cast(ObjectRotationMode, _x(c).target_rotation_mode)


def _x(c: Context) -> BoneRotationPropertyGroup:
    return BoneRotationPropertyGroup.get_from(c.window_manager)
