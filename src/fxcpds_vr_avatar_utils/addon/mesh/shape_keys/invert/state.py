from .....lib.xbpy import Context, UIPropsParameters
from ....common import FxGlobalStateAccessor
from .properties import InvertPropertyGroup


class InvertState(FxGlobalStateAccessor):

    @property
    def new_basis(self) -> str:
        return self.get_new_basis(self.context)

    @staticmethod
    def make_new_basis_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'new_basis'}

    @staticmethod
    def get_new_basis(c: Context) -> str:
        return _x(c).new_basis

    #

    @property
    def toggle_key(self) -> str:
        return self.get_toggle_key(self.context)

    @staticmethod
    def make_toggle_key_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'toggle_key'}

    @staticmethod
    def get_toggle_key(c: Context) -> str: return _x(c).toggle_key

    #

    @property
    def remove_merged(self) -> bool:
        return self.get_remove_merged(self.context)

    @staticmethod
    def make_remove_merged_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'remove_merged'}

    @staticmethod
    def get_remove_merged(c: Context) -> bool:
        return _x(c).remove_merged

    #

    @property
    def create_copy(self) -> bool:
        return self.get_create_copy(self.context)

    @staticmethod
    def make_create_copy_draw_args(c: Context) -> UIPropsParameters:
        return {'data': _x(c), 'property': 'create_copy'}

    @staticmethod
    def get_create_copy(c: Context) -> bool:
        return _x(c).create_copy


def _x(c: Context) -> InvertPropertyGroup:
    return InvertPropertyGroup.get_from(c.window_manager)
