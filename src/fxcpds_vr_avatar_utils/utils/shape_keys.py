from typing import cast, Sequence

import bpy


def shape_key_search_cb(_, context: bpy.context, edit_txt: str) -> Sequence[str]:
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

    # How did we even get here if this is true?
    if context.object is None or context.object.type != 'MESH':
        return []

    mesh = cast(bpy.types.Mesh, context.object.data)

    # If the mesh has no shape keys, there can be no matches.
    if mesh.shape_keys is None:
        return []

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
