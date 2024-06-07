import bpy
from ..registry import Registrable


class Panel(bpy.types.Panel, Registrable): pass


__all__ = ['Panel']
