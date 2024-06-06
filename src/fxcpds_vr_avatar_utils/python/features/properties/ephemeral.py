import typing

from bpy.types import WindowManager

from fxcpds_vr_avatar_utils.python.lib import AddonProperties


class EphemeralPropertyContainer(AddonProperties[WindowManager]):
    name = 'fxcpds_vau_props'
    target_type = WindowManager


class EphemeralProperties(AddonProperties[EphemeralPropertyContainer]):
    target_type = EphemeralPropertyContainer

    @classmethod
    def get_from(cls, w: WindowManager) -> typing.Self:
        return w[EphemeralPropertyContainer.name][cls.name]
