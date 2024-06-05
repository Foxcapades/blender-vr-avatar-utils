from ..... import lib
from .... import common

class BoneRotationModeState(common.FxGlobalStateAccessor):
    target_rotation_mode: lib.xbpy.ObjectRotationMode

    @staticmethod
    def make_target_rotation_mode_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_target_rotation_mode(c: lib.xbpy.Context) -> lib.xbpy.ObjectRotationMode: pass
