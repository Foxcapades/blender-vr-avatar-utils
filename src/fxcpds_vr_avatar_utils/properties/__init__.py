from .PluginProperties import PluginProperties


def register_property_group() -> None:
    import bpy

    bpy.utils.register_class(PluginProperties)
    bpy.types.Scene.bmsk_avi_props = bpy.props.PointerProperty(type=PluginProperties)


def unregister_property_group() -> None:
    import bpy

    del bpy.types.Scene.bmsk_avi_props
    bpy.utils.unregister_class(PluginProperties)


def get_property_group() -> PluginProperties:
    import bpy
    return bpy.context.scene.bmsk_avi_props
