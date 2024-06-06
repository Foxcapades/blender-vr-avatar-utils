import bpy.types
from .. import lib

class FxOperator(bpy.types.Operator, fxcpds_vr_avatar_utils.python.lib.registry.Registrable):
    @classmethod
    def is_runnable(cls, ctx: lib.xbpy.Context) -> bool: pass

    @classmethod
    def register(cls) -> None: pass

    @classmethod
    def unregister(cls) -> None: pass
