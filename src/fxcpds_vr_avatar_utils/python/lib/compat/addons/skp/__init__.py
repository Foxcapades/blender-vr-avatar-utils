from . import v2
from . import interface

import sys

from fxcpds_vr_avatar_utils.python.lib.xbpy import Context


class ShapeKeysPlus:
    @staticmethod
    def is_available(context: Context) -> bool:
        return 'shape_keys_plus' in context.preferences.addons

    @staticmethod
    def load(context: Context) -> interface.ShapeKeysPlus:
        info = sys.modules['shape_keys_plus'].bl_info

        if info['version'][0] == 2:
            return v2.ShapeKeysPlusV2(context)

        raise Exception('No compatible version of Shape Keys+ is installed!')
