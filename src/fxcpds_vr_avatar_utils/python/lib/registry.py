class Registrable:
    # NOTE: DO NOT NAME THIS METHOD "register", THE BLENDER API CALLS THAT
    #       METHOD IF IT EXISTS.
    @classmethod
    def register_class(cls) -> None:
        import bpy.utils
        bpy.utils.register_class(cls)

    # NOTE: DO NOT NAME THIS METHOD "unregister", THE BLENDER API CALLS THAT
    #       METHOD IF IT EXISTS.
    @classmethod
    def unregister_class(cls) -> None:
        from .xbpy.utils import silent_unregister_class
        silent_unregister_class(cls)
