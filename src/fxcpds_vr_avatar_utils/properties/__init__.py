import bpy

from .PluginProperties import PluginProperties
from .scene import FxScenePropertyGroup, FxSceneProps


def register_property_group() -> None:
    from . import scene

    bpy.utils.register_class(PluginProperties)
    bpy.types.Scene.bmsk_avi_props = bpy.props.PointerProperty(type=PluginProperties)

    scene.register()


def unregister_property_group() -> None:
    from . import scene

    del bpy.types.Scene.bmsk_avi_props
    bpy.utils.unregister_class(PluginProperties)

    scene.unregister()


def get_property_group() -> PluginProperties:
    return bpy.context.scene.bmsk_avi_props
