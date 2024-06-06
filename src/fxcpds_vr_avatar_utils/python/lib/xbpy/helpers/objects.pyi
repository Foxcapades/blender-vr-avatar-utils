import bpy.types
from ... import xbpy

def duplicate(obj: bpy.types.Object, ctx: xbpy.Context, select_new: bool = True) -> bpy.types.Object:
    """
    Duplicates a target object, returning the newly created copy.

    Args:
        obj: Object to duplicate.

        ctx: Blender context.

        select_new: Whether the new object should be selected after creation.

    Returns:
        The newly created duplicate object.
    """
    pass

def select_only(obj: bpy.types.Object, ctx: xbpy.Context) -> None:
    """
    Ensures that the given object is the only object selected in the current
    view layer.

    Args:
        obj: Object to select.

        ctx: Blender context.
    """
    pass
