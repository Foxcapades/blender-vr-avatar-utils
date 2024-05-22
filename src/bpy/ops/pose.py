from typing import Literal

from bpy.types.c import ConstraintType
from bpy.types.m import MotionpathBakeLocation, MotionpathDisplayType, MotionpathRange
from bpy.types.o import ObjectRotationMode, OperatorReturn


# noinspection PyUnusedLocal
def armature_apply(selected: bool = False) -> set[OperatorReturn]:
    """
    Apply the current pose as the new rest pose

    Args:
        selected: Only apply the selected bones (with propagation to children)

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def autoside_names(axis: Literal['XAXIS', 'YAXIS', 'ZAXIS'] = 'XAXIS') -> set[OperatorReturn]:
    """
    Automatically renames the selected bones according to which side of the target axis they fall on

    Args:
        axis: Axis, Axis to tag names with

            XAXIS: X-Axis – Left/Right.

            YAXIS: Y-Axis – Front/Back.

            ZAXIS: Z-Axis – Top/Bottom.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def blend_to_neighbor(
    factor: float = 0.5,
    prev_frame: int = 0,
    next_frame: int = 0,
    channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'] = 'ALL',
    axis_lock: Literal['FREE', 'X', 'Y', 'Z'] = 'FREE',
) -> set[OperatorReturn]:
    """
    Blend from current position to previous or next keyframe

    Args:
        factor: Weighting factor for which keyframe is favored more

            [0, 1]

        prev_frame: Frame number of keyframe immediately before the current
            frame.

            [-1048574, 1048574]

        next_frame: Frame number of keyframe immediately after the current
            frame.

            [-1048574, 1048574]

        channels: Set of properties that are affected

            ALL: All properties, including transforms, bendy bone shape, and custom properties.

            LOC: Location only.

            ROT: Rotation only.

            SIZE: Scale only.

            BBONE: Bendy Bone shape properties.

            CUSTOM: Custom properties.

        axis_lock: Transform axis to restrict effects to

            FREE: All axes are affected.

            X: Only X-axis transforms are affected.

            Y: Only Y-axis transforms are affected.

            Z: Only Z-axis transforms are affected.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def blend_with_rest(
    factor: float = 0.5,
    prev_frame: int = 0,
    next_frame: int = 0,
    channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'] = 'ALL',
    axis_lock: Literal['FREE', 'X', 'Y', 'Z'] = 'FREE',
) -> set[OperatorReturn]:
    """
    Make the current pose more similar to, or further away from, the rest pose

    Args:
        factor: Weighting factor for which keyframe is favored more.

            [0, 1]

        prev_frame: Frame number of keyframe immediately before the current
            frame.

            [-1048574, 1048574]

        next_frame: Frame number of keyframe immediately after the current
            frame.

            [-1048574, 1048574]

        channels: Set of properties that are affected

            ALL: All properties, including transforms, bendy bone shape, and
                custom properties.

            LOC: Location only.

            ROT: Rotation only.

            SIZE: Scale only.

            BBONE: Bendy Bone shape properties.

            CUSTOM: Custom properties.

        axis_lock: Transform axis to restrict effects to

            FREE: All axes are affected.

            X: Only X-axis transforms are affected.

            Y: Only Y-axis transforms are affected.

            Z: Only Z-axis transforms are affected.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def breakdown(
    factor: float = 0.5,
    prev_frame: int = 0,
    next_frame: int = 0,
    channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'] = 'ALL',
    axis_lock: Literal['FREE', 'X', 'Y', 'Z'] = 'FREE'
) -> set[OperatorReturn]:
    """
    Create a suitable breakdown pose on the current frame

    Args:
        factor: Weighting factor for which keyframe is favored more.

            [0, 1]

        prev_frame: Frame number of keyframe immediately before the current
            frame.

            [-1048574, 1048574]

        next_frame: Frame number of keyframe immediately after the current
            frame.

            [-1048574, 1048574]

        channels: Set of properties that are affected

            ALL: All properties, including transforms, bendy bone shape, and custom properties.

            LOC: Location only.

            ROT: Rotation only.

            SIZE: Scale only.

            BBONE: Bendy Bone shape properties.

            CUSTOM: Custom properties.

        axis_lock: Transform axis to restrict effects to

            FREE: All axes are affected.

            X: Only X-axis transforms are affected.

            Y: Only Y-axis transforms are affected.

            Z: Only Z-axis transforms are affected.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def constraint_add(type: ConstraintType = '') -> set[OperatorReturn]:
    """
    Add a constraint to the active bone

    Args:
        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def constraint_add_with_targets(type: ConstraintType = '') -> set[OperatorReturn]:
    """
    Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    Args:
        type:

    Returns:
        Operation result.
    """
    pass


def constraints_clear() -> set[OperatorReturn]:
    """
    Clear all constraints from the selected bones

    Returns:
        Operation result.
    """
    pass


def constraints_copy() -> set[OperatorReturn]:
    """
    Copy constraints to other selected bones

    Returns:
        Operation result.
    """
    pass


def copy() -> set[OperatorReturn]:
    """
    Copy the current pose of the selected bones to the internal clipboard

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def flip_names(do_strip_numbers: bool = False) -> set[OperatorReturn]:
    """
    Flips (and corrects) the axis suffixes of the names of selected bones

    Args:
        do_strip_numbers: Strip Numbers.  Try to remove right-most dot-number
            from flipped names.Warning: May result in incoherent naming in some
            cases

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def hide(unselected: bool = False) -> set[OperatorReturn]:
    """
    Tag selected bones to not be visible in Pose Mode

    Args:
        unselected:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def ik_add(with_targets: bool = True) -> set[OperatorReturn]:
    """
    Add IK Constraint to the active Bone

    Args:
        with_targets: Assign IK Constraint with targets derived from the select
            bones/objects.

    Returns:
        Operation result.
    """
    pass


def ik_clear() -> set[OperatorReturn]:
    """
    Remove all IK Constraints from selected bones

    Returns:
        Operation result.
    """
    pass


def loc_clear() -> set[OperatorReturn]:
    """
    Reset locations of selected bones to their default values

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def paste(flipped: bool = False, selected_mask: bool = False) -> set[OperatorReturn]:
    """
    Paste the stored pose on to the current pose

    Args:
        flipped: Paste the stored pose flipped on to current pose

        selected_mask: Only paste the stored pose on to selected bones in the
            current pose.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def paths_calculate(
    display_type: MotionpathDisplayType = 'RANGE',
    range: MotionpathRange = 'SCENE',
    bake_location: MotionpathBakeLocation = 'HEADS',
) -> set[OperatorReturn]:
    """
    Calculate paths for the selected bones

    Args:
        display_type: Display type

        range (enum in  Items, (optional)) – Computation Range

        bake_location: Which point on the bones is used when calculating paths.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def paths_clear(only_selected: bool = False) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        only_selected: Only clear motion paths of selected bones.

    Returns:
        Operation result.
    """
    pass


def paths_range_update() -> set[OperatorReturn]:
    """
    Update frame range for motion paths from the Scene’s current frame range.

    Returns:
        Operation result.
    """
    pass


def paths_update() -> set[OperatorReturn]:
    """
    Recalculate paths for bones that already have them

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def propagate(
    mode: Literal[
        'NEXT_KEY',
        'LAST_KEY',
        'BEFORE_FRAME',
        'BEFORE_END',
        'SELECTED_KEYS',
        'SELECTED_MARKERS',
    ] = 'NEXT_KEY',
    end_frame: float = 250.0,
) -> set[OperatorReturn]:
    """
    Copy selected aspects of the current pose to subsequent poses already keyframed

    Args:
        mode: Terminate Mode.  Method used to determine when to stop propagating
            pose to keyframes

            NEXT_KEY: To Next Keyframe – Propagate pose to first keyframe
                following the current frame only.

            LAST_KEY: To Last Keyframe – Propagate pose to the last keyframe
                only (i.e. making action cyclic).

            BEFORE_FRAME: Before Frame – Propagate pose to all keyframes between
                current frame and ‘Frame’ property.

            BEFORE_END: Before Last Keyframe – Propagate pose to all keyframes
                from current frame until no more are found.

            SELECTED_KEYS: On Selected Keyframes – Propagate pose to all
                selected keyframes.

            SELECTED_MARKERS: On Selected Markers – Propagate pose to all
                keyframes occurring on frames with Scene Markers after the
                current frame.

        end_frame: Frame to stop propagating frames to (for ‘Before Frame’ mode)

            [1.17549e-38, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def push(
    factor: float = 0.5,
    prev_frame: int = 0,
    next_frame: int = 0,
    channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'] = 'ALL',
    axis_lock: Literal['FREE', 'X', 'Y', 'Z'] = 'FREE'
) -> set[OperatorReturn]:
    """
    Exaggerate the current pose in regards to the breakdown pose

    Args:
        factor: Weighting factor for which keyframe is favored more.

            [0, 1]

        prev_frame: Frame number of keyframe immediately before the current
            frame.

            [-1048574, 1048574]

        next_frame: Frame number of keyframe immediately after the current
            frame.

            [-1048574, 1048574]

        channels: Set of properties that are affected

            ALL: All properties, including transforms, bendy bone shape, and custom properties.

            LOC: Location only.

            ROT: Rotation only.

            SIZE: Scale only.

            BBONE: Bendy Bone shape properties.

            CUSTOM: Custom properties.

        axis_lock: Transform axis to restrict effects to

            FREE: All axes are affected.

            X: Only X-axis transforms are affected.

            Y: Only Y-axis transforms are affected.

            Z: Only Z-axis transforms are affected.

    Returns:
        Operation result.
    """
    pass


def quaternions_flip() -> set[OperatorReturn]:
    """
    Flip quaternion values to achieve desired rotations, while maintaining the
    same orientations.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def relax(
    factor: float = 0.5,
    prev_frame: int = 0,
    next_frame: int = 0,
    channels: Literal['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'] = 'ALL',
    axis_lock: Literal['FREE', 'X', 'Y', 'Z'] = 'FREE',
) -> set[OperatorReturn]:
    """
    Make the current pose more similar to its breakdown pose

    Args:
        factor: Weighting factor for which keyframe is favored more.

            [0, 1]

        prev_frame: Frame number of keyframe immediately before the current
            frame.

            [-1048574, 1048574]

        next_frame: Frame number of keyframe immediately after the current
            frame.

            [-1048574, 1048574]

        channels: Set of properties that are affected

            ALL: All properties, including transforms, bendy bone shape, and custom properties.

            LOC: Location only.

            ROT: Rotation only.

            SIZE: Scale only.

            BBONE: Bendy Bone shape properties.

            CUSTOM: Custom properties.

        axis_lock: Transform axis to restrict effects to

            FREE: All axes are affected.

            X: Only X-axis transforms are affected.

            Y: Only Y-axis transforms are affected.

            Z: Only Z-axis transforms are affected.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def reveal(select: bool = True) -> set[OperatorReturn]:
    """
    Reveal all bones hidden in Pose Mode

    Args:
        select:

    Returns:
        Operation result.
    """
    pass


def rot_clear() -> set[OperatorReturn]:
    """
    Reset rotations of selected bones to their default values

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def rotation_mode_set(type: ObjectRotationMode = 'QUATERNION') -> set[OperatorReturn]:
    """
    Set the rotation representation used by selected bones

    Args:
        type: Rotation Mode

    Returns:
        Operation result.
    """
    pass


def scale_clear() -> set[OperatorReturn]:
    """
    Reset scaling of selected bones to their default values

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_all(action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'] = 'TOGGLE') -> set[OperatorReturn]:
    """
    Toggle selection status of all bones

    Args:
        action: Selection action to execute

            TOGGLE: Toggle selection for all elements.

            SELECT: Select all elements.

            DESELECT: Deselect all elements.

            INVERT: Invert selection of all elements.

    Returns:
        Operation result.
    """
    pass


def select_constraint_target() -> set[OperatorReturn]:
    """
    Select bones used as targets for the currently selected bones

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_grouped(
    extend: bool = False,
    type: Literal['COLLECTION', 'COLOR', 'KEYINGSET'] = 'COLLECTION',
) -> set[OperatorReturn]:
    """
    Select all visible bones grouped by similar properties

    Args:
        extend: Extend selection instead of deselecting everything first.

        type: Type

            COLLECTION: Same collections as the active bone.

            COLOR: Same color as the active bone.

            KEYINGSET: All bones affected by active Keying Set.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_hierarchy(direction: Literal['PARENT', 'CHILD'] = 'PARENT', extend: bool = False) -> set[OperatorReturn]:
    """
    Select immediate parent/children of selected bones

    Args:
        direction:

        extend: Extend the selection

    Returns:
        Operation result.
    """
    pass


def select_linked() -> set[OperatorReturn]:
    """
    Select all bones linked by parent/child connections to the current
    selection.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_linked_pick(extend: bool = False) -> set[OperatorReturn]:
    """
    Select bones linked by parent/child connections under the mouse cursor.

    Args:
        extend: Extend selection instead of deselecting everything first.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_mirror(only_active: bool = False, extend: bool = False) -> set[OperatorReturn]:
    """
    Mirror the bone selection

    Args:
        only_active: Only operate on the active bone.

        extend: Extend the selection.

    Returns:
        Operation result.
    """
    pass


def select_parent() -> set[OperatorReturn]:
    """
    Select bones that are parents of the currently selected bones

    Returns:
        Operation result.
    """
    pass


def transforms_clear() -> set[OperatorReturn]:
    """
    Reset location, rotation, and scaling of selected bones to their default values

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def user_transforms_clear(only_selected: bool = True) -> set[OperatorReturn]:
    """
    Reset pose bone transforms to keyframed state

    Args:
        only_selected: Only visible/selected bones.

    Returns:
        Operation result.
    """
    pass


def visual_transform_apply() -> set[OperatorReturn]:
    """
    Apply final constrained position of pose bones to their transform

    Returns:
        Operation result.
    """
    pass
