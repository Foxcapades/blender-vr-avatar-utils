from bpy.props import BoolProperty, StringProperty

from .....lib import shape_keys
from ....properties import EphemeralProperties


class InvertPropertyGroup(EphemeralProperties):
    name = 'sk_inversion_form'

    # noinspection PyTypeHints
    new_basis: StringProperty(
        name='New Basis Key',
        description=(
            'Shape key that will be used to form the new basis.  This key\'s'
            'value will be applied to the object\'s actual basis'
        ),
        options=set(),
        search=shape_keys.non_default_shape_key_search_cb,
        search_options=set()
    )

    # noinspection PyTypeHints
    toggle_key: StringProperty(
        name='Toggle Key',
        description=(
            'Name of the key that will be used as or become the the toggling '
            'shape key that can be used to restore the object to a former or '
            'alternative state.  If the key already exists, then its current '
            'value will be used as the toggle value UNLESS the specified key '
            'is the same as the \'New Basis Key\'.  If the key does not '
            'already exist, a new key will be created with the default object '
            'state (with no shape keys) will be used as the toggle value'
        ),
        options=set(),
        search=shape_keys.non_default_shape_key_search_cb,
    )

    # noinspection PyTypeHints
    remove_merged: BoolProperty(
        name="Remove 'New Basis Key'",
        description=(
            'Whether the \'New Basis Key\' shape key should be removed from '
            'this object once the invert operation has been successfully '
            'completed'
        ),
        options=set(),
        default=True,
    )

    # noinspection PyTypeHints
    create_copy: BoolProperty(
        name='Create New Object',
        description=(
            'Whether this operation should create a new object on which to '
            'perform the changes, leaving the original object unchanged'
        ),
        options=set(),
        default=True,
    )
