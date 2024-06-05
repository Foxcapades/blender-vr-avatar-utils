from bpy.props import BoolProperty

from ....properties import EphemeralProperties


class SyncPropertyGroup(EphemeralProperties):
    # noinspection PyTypeHints
    ignore_muted: BoolProperty(
        name='Ignore Muted',
        description=(
            'Whether muted shape keys on this object should be ignored when '
            'synchronizing shape key values to other objects in the scene.  If '
            'a shape key on this object is muted, it will not be considered '
            'when synchronizing values to other objects.  Shape keys that are '
            'muted on other objects in this scene may still be updated'
        ),
        default=True,
        options=set(),
    )

    # noinspection PyTypeHints
    ignore_locked: BoolProperty(
        name='Ignore Locked',
        description=(
            'Whether locked shape keys on other objects in this scene should '
            'be ignored when synchronizing shape key values from this object'
        ),
        default=True,
        options=set(),
    )

    # noinspection PyTypeHints
    skp_only_from_selected: BoolProperty(
        name='Only from Selected',
        description=(
            'Only synchronize values from those currently selected on this mesh'
        ),
        options=set(),
    )

    # noinspection PyTypeHints
    skp_only_to_selected: BoolProperty(
        name='Only to Selected',
        description=(
            'Only synchronize values to those currently selected on other '
            'meshes'
        ),
        options=set(),
    )
