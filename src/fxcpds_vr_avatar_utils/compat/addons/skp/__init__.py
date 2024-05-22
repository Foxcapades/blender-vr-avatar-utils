from . import v2
from . import interface

import bpy
import sys


class ShapeKeysPlus:
    @staticmethod
    def is_available(context: bpy.context) -> bool:
        return 'shape_keys_plus' in context.preferences.addons

    @staticmethod
    def load(context: bpy.context) -> interface.ShapeKeysPlus:
        info = sys.modules['shape_keys_plus'].bl_info

        if info['version'][0] == 2:
            return v2.ShapeKeysPlusV2(context)

        raise Exception('No compatible version of Shape Keys+ is installed!')
