from typing import cast, Generator, Sequence

from .aliases import Context
from .objects import is_keyed_mesh

from bpy.types import Mesh, Object, ShapeKey

import bpy


def shape_key_it(obj: Object) -> Generator[ShapeKey, None, None]:
    if not is_keyed_mesh(obj):
        return None

    key = cast(Mesh, obj.data).shape_keys

    for sk in key.key_blocks:
        yield sk

    return None


def non_default_shape_key_search_cb(_, context: Context, edit_txt: str) -> Generator[str, None, None]:
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
    if not is_keyed_mesh(context.object):
        return None

    matches = shape_key_search_cb(_, context, edit_txt)

    if len(matches) == 0:
        return None

    default = cast(Mesh, context.object.data).shape_keys.key_blocks[0].name

    for match in matches:
        if match != default:
            yield match

    return None


def shape_key_search_cb(_, context: Context, edit_txt: str) -> Sequence[str]:
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
    if not is_keyed_mesh(context.object):
        return []

    mesh = cast(bpy.types.Mesh, context.object.data)

    # Don't count leading/trailing space characters in the matching.
    edit_txt = edit_txt.strip()

    # If the stripped input text is empty, return everything.
    if len(edit_txt) == 0:
        return mesh.shape_keys.key_blocks.keys()

    # Do case-insensitive searching.
    edit_txt = edit_txt.lower()

    # Output lists.  High is for high-significance matches, low for everything
    # else.
    high = []
    low = []

    # Iterate through the shape key names to find matches.
    for key in mesh.shape_keys.key_blocks.keys():
        lk = key.lower()

        if lk.startswith(edit_txt):
            high.append(key)
        elif edit_txt in lk:
            low.append(key)

    # Sort the matches.
    high.sort()
    low.sort()

    # Return the combined match lists
    return high + low
