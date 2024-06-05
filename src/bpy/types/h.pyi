from bpy.types.base import bpy_struct

from bpy.types.r import RegionType
from bpy.types.s import SpaceType
from bpy.types.u import UILayout

import bpy


# noinspection PyPropertyDefinition
class Header(bpy_struct):
    bl_idname: str
    bl_region_type: RegionType
    bl_space_type: SpaceType

    @property
    def layout(self) -> UILayout: pass

    def draw(self, context: bpy.context): pass
