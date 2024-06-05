from ...lib.state import FxStateAccessor
from ...lib.xbpy import Context, UIPropsParameters
from .properties import FxGlobalProperties


class FxGlobalStateAccessor(FxStateAccessor):
    @property
    def dry_run(self) -> bool:
        return _x(self.context).dry_run

    @staticmethod
    def make_dry_run_draw_params(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'dry_run'}

    @staticmethod
    def get_dry_run(c: Context) -> bool:
        return _x(c).dry_run

    #

    @property
    def lock_to_scene(self) -> bool:
        return _x(self.context).lock_to_scene

    @staticmethod
    def make_lock_to_scene_draw_params(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'lock_to_scene'}

    @staticmethod
    def get_lock_to_scene(c: Context) -> bool:
        return _x(c).lock_to_scene


def _x(c: Context) -> FxGlobalProperties:
    return FxGlobalProperties.get_from(c.window_manager)
