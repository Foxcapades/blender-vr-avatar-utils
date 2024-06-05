from ... import lib

class FxGlobalStateAccessor(lib.state.FxStateAccessor):
    @property
    def dry_run(self) -> bool: pass

    @staticmethod
    def make_dry_run_draw_params(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_dry_run(c: lib.xbpy.Context) -> bool: pass

    @property
    def lock_to_scene(self) -> bool: pass

    @staticmethod
    def make_lock_to_scene_draw_params(c: lib.xbpy.Context) -> lib.xbpy.UIPropsParameters: pass

    @staticmethod
    def get_lock_to_scene(c: lib.xbpy.Context) -> bool: pass
