from bpy.types import Operator
from ..lib.registry import Registrable
from ..lib.xbpy import Context


class FxOperator(Operator, Registrable):
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def is_runnable(cls, ctx: Context) -> bool:
        return True
