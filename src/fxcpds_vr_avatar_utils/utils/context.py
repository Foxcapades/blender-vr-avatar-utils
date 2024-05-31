import bpy
import fxcpds_vr_avatar_utils


def current_key(context: fxcpds_vr_avatar_utils.utils.aliases.Context) -> bpy.types.Key:
    return fxcpds_vr_avatar_utils.utils.objects.require_key(context)
