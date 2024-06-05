import re
from typing import cast, Iterable

from bpy.types import Mesh, Object
from .keys import require_key, is_keyed
from ..aliases import Context

__all__ = ['has_shape_keys', 'count_shape_keys']


def count_shape_keys(obj: Object) -> int:
    return len(require_key(obj).key_blocks) if is_keyed(obj) else 0


def has_shape_keys(obj: Object) -> bool:
    return count_shape_keys(obj) > 0


def non_default_shape_key_search_cb(_, context: Context, edit_txt: str) -> Iterable[str]:
    if not is_keyed(context.object):
        return None

    matches = shape_key_search_cb(_, context, edit_txt)

    if matches is None:
        return None

    default = cast(Mesh, context.object.data).shape_keys.key_blocks[0].name

    for match in matches:
        if match != default:
            yield match

    return None


def shape_key_search_cb(_, context: Context, edit_txt: str) -> Iterable[str]:
    if not is_keyed(context.object):
        return None

    mesh = cast(Mesh, context.object.data)

    # Don't count leading/trailing space characters in the matching.
    edit_txt = edit_txt.strip()

    # If the stripped input text is empty, return everything.
    if len(edit_txt) == 0:
        for key in mesh.shape_keys.key_blocks.keys():
            yield key

        return None

    # Do case-insensitive searching.
    edit_txt = edit_txt.lower()

    # Output lists.  High is for high-significance matches, low for everything
    # else.
    matches: list[tuple[int, str]] = []

    # Iterate through the shape key names to find matches.
    for key in mesh.shape_keys.key_blocks.keys():
        if key.startswith(edit_txt):
            matches.append((1, key))
        elif edit_txt in key:
            matches.append((3, key))
        else:
            lk = key.lower()

            if lk.startswith(edit_txt):
                matches.append((2, key))
            elif edit_txt in lk:
                matches.append((4, key))

    if len(matches) == 0 and re.match('^\\w+$', edit_txt):
        for key in mesh.shape_keys.key_blocks.keys():
            lk = re.sub('\\W+', '',  key.lower())

            if lk.startswith(edit_txt):
                matches.append((1, key))
            elif edit_txt in lk:
                matches.append((2, key))

    # Sort the matches.
    matches.sort()

    for _, key in matches:
        yield key

    # Return the combined match lists
    return None
