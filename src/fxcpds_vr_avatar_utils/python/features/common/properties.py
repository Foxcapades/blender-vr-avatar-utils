from bpy.props import BoolProperty
from .. import properties


class FxGlobalProperties(properties.ephemeral.EphemeralProperties):
    name = 'global_props'

    # noinspection PyTypeHints
    dry_run: BoolProperty(
        name='Dry Run',
        description=(
            'Decides whether changes should be performed or if the plugin '
            'should perform a \'dry run\' where it makes no changes and '
            'instead reports the changes it would have made if Dry Run was '
            'disabled'
        ),
        options=set(),
    )

    # noinspection PyTypeHints
    lock_to_scene: BoolProperty(
        name='This Scene Only',
        description=(
            'Whether bulk operations should be locked to objects in the '
            'current scene only.  If disabled, bulk operations will apply to '
            'relevant objects in all scenes'
        ),
        default=True,
        options=set(),
    )
