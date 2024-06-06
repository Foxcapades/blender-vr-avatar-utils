from ..... import lib
from .... import common

class InvertState(common.FxGlobalStateAccessor):
    @property
    def new_basis(self) -> str: pass

    @staticmethod
    def make_new_basis_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_new_basis(c: lib.xbpy.Context) -> str: pass

    @property
    def toggle_key(self) -> str: pass

    @staticmethod
    def make_toggle_key_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_toggle_key(c: lib.xbpy.Context) -> str: pass

    @property
    def remove_merged(self) -> bool: pass

    @staticmethod
    def make_remove_merged_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_remove_merged(c: lib.xbpy.Context) -> bool: pass

    @property
    def create_copy(self) -> bool: pass

    @staticmethod
    def make_create_copy_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_create_copy(c: lib.xbpy.Context) -> bool: pass
