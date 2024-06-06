import typing
import bpy.types
from .. import aliases

def count_shape_keys(obj: bpy.types.Object) -> int: pass

def has_shape_keys(obj: bpy.types.Object) -> bool: pass

def non_default_shape_key_search_cb(_, context: aliases.Context, edit_txt: str) -> typing.Iterable[str]:
    """
    Default shape key omitting shape key name search callback.

    Searches through the shape keys on the current context object for any key
    names that start with or contain the input `edit_txt` value, excluding the
    default/basis shape key.

    Key names that start with the input value will be placed higher in the
    result order than key names that contain a match to the input text elsewhere
    in them.

    Args:
        _: Ignored.

        context: Blender context.

        edit_txt: User input text.

    Yields:
        Matching shape key names.

    Returns:
        Either a generator over the matching shape key names, or None if there
        were no matches or the object did not have shape keys present.
    """
    pass

def shape_key_search_cb(_, context: aliases.Context, edit_txt: str) -> typing.Iterable[str]:
    """
    Shape key name search callback.

    Searches through the shape keys on the current context object for any key
    names that start with or contain the input edit_txt value.

    Key names that start with the input text value will be placed higher in the
    result order than key names that contain a match to the input text elsewhere
    in them.

    Args:
        _: Ignored

        context: Blender context.

        edit_txt: User input text.

    Returns:
        A list of zero or more matching shape key names.
    """
    pass
