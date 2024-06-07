import typing
import bpy.types
import fxcpds_vr_avatar_utils.python.lib.properties

class EphemeralPropertyContainer(fxcpds_vr_avatar_utils.python.lib.properties.AddonProperties): pass

class EphemeralProperties(fxcpds_vr_avatar_utils.python.lib.properties.AddonProperties[EphemeralPropertyContainer]):
    @classmethod
    def get_from(cls, w: bpy.types.WindowManager) -> typing.Self: pass
