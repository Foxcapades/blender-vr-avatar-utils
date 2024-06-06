import bpy.types
from ..... import lib
from .... import common

class State(common.FxGlobalStateAccessor):
    @property
    def current_key(self) -> bpy.types.Key: pass

    @property
    def rename_from(self) -> str: pass

    @staticmethod
    def make_rename_from_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_rename_from(c: lib.xbpy.Context) -> str: pass

    @property
    def rename_to(self) -> str: pass

    @staticmethod
    def make_rename_to_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_rename_to(c: lib.xbpy.Context) -> str: pass
