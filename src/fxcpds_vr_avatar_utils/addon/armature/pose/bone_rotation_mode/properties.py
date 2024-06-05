from bpy.props import EnumProperty

from fxcpds_vr_avatar_utils.addon.properties import EphemeralProperties


class BoneRotationPropertyGroup(EphemeralProperties):
    name = 'brmn_props'

    # noinspection PyTypeHints,PyProtocol
    target_rotation_mode: EnumProperty(
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
