from bpy.types import Key

from .....lib.xbpy import keys, Context, UIPropsParameters
from ....common import FxGlobalStateAccessor
from .properties import RenamePropertyGroup


class State(FxGlobalStateAccessor):
    def __init__(self, c: Context):
        super().__init__(c)
        self.__key = keys.require_key(c.object)

    #

    @property
    def current_key(self) -> Key:
        # noinspection PyUnresolvedReferences
        return self.__key

    #

    @property
    def rename_from(self) -> str:
        return self.get_rename_from(self.context)

    @staticmethod
    def make_rename_from_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'rename_from'}

    @staticmethod
    def get_rename_from(c: Context) -> str:
        return _x(c).rename_from

    #

    @property
    def rename_to(self) -> str:
        return self.get_rename_to(self.context)

    @staticmethod
    def make_rename_to_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'rename_to'}

    @staticmethod
    def get_rename_to(c: Context) -> str:
        return _x(c).rename_to


def _x(c: Context) -> RenamePropertyGroup:
    return RenamePropertyGroup.get_from(c.window_manager)
