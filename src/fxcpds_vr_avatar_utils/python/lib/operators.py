from bpy.types import Operator
from ..lib.registry import Registrable
from ..lib.xbpy import Context


class FxOperator(Operator, Registrable):
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def is_runnable(cls, ctx: Context) -> bool:
        return True

    @classmethod
    def register(cls) -> None:
        import bpy.utils
        bpy.utils.register_class(cls)

    @classmethod
    def unregister(cls) -> None:
        import fxcpds_vr_avatar_utils.python.lib.xbpy
        fxcpds_vr_avatar_utils.lib.xbpy.silent_unregister_class(cls)
