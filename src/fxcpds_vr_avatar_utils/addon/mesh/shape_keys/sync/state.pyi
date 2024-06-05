from ..... import lib
from .... import common

class State(common.state.FxGlobalStateAccessor):
    @property
    def ignore_muted(self) -> bool: pass

    @staticmethod
    def make_ignore_muted_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_ignore_muted(c: lib.xbpy.Context) -> bool: pass

    @property
    def ignore_locked(self) -> bool: pass

    @staticmethod
    def make_ignore_locked_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_ignore_locked(c: lib.xbpy.Context) -> bool: pass

    @property
    def skp_only_from_selected(self) -> bool: pass

    @staticmethod
    def make_skp_only_from_selected_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_skp_only_from_selected(c: lib.xbpy.Context) -> bool: pass

    @property
    def skp_only_to_selected(self) -> bool: pass

    @staticmethod
    def make_skp_only_to_selected_draw_args(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_skp_only_to_selected(c: lib.xbpy.Context) -> bool: pass
