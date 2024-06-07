from bpy.props import StringProperty

from .....lib.xbpy import shape_keys
from ....properties import ephemeral


class RenamePropertyGroup(ephemeral.EphemeralProperties):
    name = "sk_rename_form"

    # noinspection PyTypeHints
    rename_from: StringProperty(
        name='From',
        description=(
            'Original shape key name that will be changed to the value of the '
            '\'To\' field'
        ),
        options=set(),
        search=shape_keys.shape_key_search_cb,
        search_options=set(),
    )

    # noinspection PyTypeHints
    rename_to: StringProperty(
        name='To',
        description=(
            'New shape key name that will be used as the replacement for the '
            '\'From\' field value'
        ),
        options=set()
    )
