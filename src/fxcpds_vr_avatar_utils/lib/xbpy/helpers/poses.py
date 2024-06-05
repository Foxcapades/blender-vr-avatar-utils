from bpy.types import Object, Pose

__all__ = ['require_pose']


def require_pose(obj: Object) -> Pose:
    return obj.pose
