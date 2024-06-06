from .....lib.xbpy import Context, UIPropsParameters
from ....common.state import FxGlobalStateAccessor
from .properties import SyncPropertyGroup


class State(FxGlobalStateAccessor):
    @property
    def ignore_muted(self) -> bool:
        return self.get_ignore_muted(self.context)

    @staticmethod
    def make_ignore_muted_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'ignore_muted'}

    @staticmethod
    def get_ignore_muted(c: Context) -> bool:
        return _x(c).ignore_muted

    #

    @property
    def ignore_locked(self) -> bool:
        return self.get_ignore_locked(self.context)

    @staticmethod
    def make_ignore_locked_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'ignore_locked'}

    @staticmethod
    def get_ignore_locked(c: Context) -> bool:
        return _x(c).ignore_locked

    #

    @property
    def skp_only_from_selected(self) -> bool:
        return self.get_skp_only_from_selected(self.context)

    @staticmethod
    def make_skp_only_from_selected_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'skp_only_from_selected'}

    @staticmethod
    def get_skp_only_from_selected(c: Context) -> bool:
        return _x(c).skp_only_from_selected

    #

    @property
    def skp_only_to_selected(self) -> bool:
        return self.get_skp_only_to_selected(self.context)

    @staticmethod
    def make_skp_only_to_selected_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'skp_only_to_selected'}

    @staticmethod
    def get_skp_only_to_selected(c: Context) -> bool:
        return _x(c).skp_only_to_selected


def _x(c: Context) -> SyncPropertyGroup:
    return SyncPropertyGroup.get_from(c.window_manager)
