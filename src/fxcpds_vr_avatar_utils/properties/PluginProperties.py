import bpy

from ..utils.shape_keys import non_default_shape_key_search_cb, shape_key_search_cb


# noinspection PyTypeHints
class PluginProperties(bpy.types.PropertyGroup):

    # region Global Options
    #

    PROP_NAME_GLOBAL_DRY_RUN = 'dry_run'

    dry_run: bpy.props.BoolProperty(
        name='Dry Run',
        description=(
            'Decides whether changes should be performed or if the plugin '
            'should perform a \'dry run\' where it makes no changes and '
            'instead reports the changes it would have made if Dry Run was '
            'disabled'
        ),
        options=set(),
    )

    #
    # endregion Global Options

    # region Scene Scoped Options
    #

    PROP_NAME_LOCK_TO_SCENE = 'lock_to_scene'

    lock_to_scene: bpy.props.BoolProperty(
        name='This Scene Only',
        description=(
            'Whether bulk operations should be locked to objects in the '
            'current scene only.  If disabled, bulk operations will apply to '
            'relevant objects in all scenes'
        ),
        default=True,
        options=set(),
    )

    #
    # endregion Scene Scoped Options

    # region Shape Key Renaming
    #

    PROP_NAME_KEY_RENAME_FROM = 'key_rename_from'

    key_rename_from: bpy.props.StringProperty(
        name='From',
        description=(
            'Original shape key name that will be changed to the value of the '
            '\'To\' field'
        ),
        options=set(),
        search=shape_key_search_cb,
        search_options=set(),
    )

    PROP_NAME_KEY_RENAME_TO = 'key_rename_to'

    key_rename_to: bpy.props.StringProperty(
        name='To',
        description=(
            'New shape key name that will be used as the replacement for the '
            '\'From\' field value'
        ),
        options=set()
    )

    #
    # endregion Shape Key Renaming

    # region Shape Key Inversion
    #

    PROP_NAME_SK_INVERT_BASIS = 'shape_key_inversion_basis_replacement'

    shape_key_inversion_basis_replacement: bpy.props.StringProperty(
        name='New Basis',
        description=(
            'Shape key that will be used to form the new basis.  This key\'s'
            'value will be applied to the object\'s actual basis'
        ),
        options=set(),
        search=non_default_shape_key_search_cb,
        search_options=set()
    )

    PROP_NAME_SK_INVERT_TOGGLE = 'shape_key_inversion_toggle'

    shape_key_inversion_toggle: bpy.props.StringProperty(
        name='Toggle Key',
        description=(
            'Name of the key that will be used as or become the the toggling '
            'shape key that can be used to restore the object to a former or '
            'alternative state.  If the key already exists, then it\'s current '
            'value will be used as the toggle value.  If the key does not '
            'already exist, a new key will be created with the default object '
            'state (with no shape keys) will be used as the toggle value'
        ),
        options=set(),
        search=non_default_shape_key_search_cb,
    )

    PROP_NAME_SK_INVERT_REMOVE_MERGED = 'shape_key_inversion_remove_merged'

    shape_key_inversion_remove_merged: bpy.props.BoolProperty(
        name="Remove 'New Basis'",
        description=(
            'Whether the \'New Basis\' shape key should be removed from this '
            'object once the invert operation has been successfully completed'
        ),
        options=set(),
        default=True,
    )

    PROP_NAME_SK_INVERT_CREATE_COPY = 'shape_key_inversion_create_copy'

    shape_key_inversion_create_copy: bpy.props.BoolProperty(
        name='Create New Object',
        description=(
            'Whether this operation should create a new object on which to '
            'perform the changes, leaving this object unchanged'
        ),
        options=set(),
        default=True,
    )

    #
    # endregion Shape Key Inversion

    # region Shape Key Sync
    #

    PROP_NAME_SYNC_IGNORE_MUTED = 'key_sync_ignore_muted'

    key_sync_ignore_muted: bpy.props.BoolProperty(
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

    PROP_NAME_SYNC_IGNORE_LOCKED = 'key_sync_ignore_locked'

    key_sync_ignore_locked: bpy.props.BoolProperty(
        name='Ignore Locked',
        description=(
            'Whether locked shape keys on other objects in this scene should '
            'be ignored when synchronizing shape key values from this object'
        ),
        default=True,
        options=set(),
    )

    #
    # Shape Key Synchronization: Shape Keys+ Compatibility
    #

    PROP_NAME_SYNC_COMPAT_SKP_ONLY_FROM_SELECTED = 'key_sync_skp_only_from_selected'

    key_sync_skp_only_from_selected: bpy.props.BoolProperty(
        name='Only from Selected',
        description=(
            'Only synchronize values from those currently selected on this mesh'
        ),
        options=set(),
    )

    PROP_NAME_SYNC_COMPAT_SKP_ONLY_TO_SELECTED = 'key_sync_skp_only_to_selected'

    key_sync_skp_only_to_selected: bpy.props.BoolProperty(
        name='Only to Selected',
        description=(
            'Only synchronize values to those currently selected on other '
            'meshes'
        ),
        options=set(),
    )

    #
    # endregion Shape Key Sync

    # region Bone Rotation Normalization
    #

    PROP_NAME_BONE_TARGET_ROTATION_MODE = 'target_rotation_mode'

    target_rotation_mode: bpy.props.EnumProperty(
        items=[
            ('QUATERNION', 'Quaternion', 'No Gimbal Lock'),
            ('XYZ', 'XYZ Euler', 'XYZ Rotation Order - prone to Gimbal Lock'),
            ('XZY', 'XZY Euler', 'XZY Rotation Order - prone to Gimbal Lock'),
            ('YXZ', 'YXZ Euler', 'YXZ Rotation Order - prone to Gimbal Lock'),
            ('YZX', 'YZX Euler', 'YZX Rotation Order - prone to Gimbal Lock'),
            ('ZXY', 'ZXY Euler', 'ZXY Rotation Order - prone to Gimbal Lock'),
            ('ZYX', 'ZYX Euler', 'ZYX Rotation Order - prone to Gimbal Lock'),
            (
                'AXIS_ANGLE',
                'Axis Angle',
                'Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector'
            ),
        ],
        name='Rotation Mode',
        description='New rotation mode to set on all bones in a target armature',
        options=set(),
    )

    #
    # endregion Bone Rotation Normalization
