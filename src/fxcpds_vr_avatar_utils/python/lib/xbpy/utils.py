__all__ = ['silent_remove_property', 'silent_unregister_class', 'silent_unregister_property']


def silent_unregister_property(prop_type: type, from_type: type, prop_name: str) -> None:
    silent_remove_property(from_type, prop_name)
    silent_unregister_class(prop_type)


def silent_remove_property(_from: type, name: str) -> None:
    try:
        delattr(_from, name)
    except Exception:
        pass


def silent_unregister_class(cls: type) -> None:
    import bpy.utils
    try:
        bpy.utils.unregister_class(cls)
    except Exception:
        pass

