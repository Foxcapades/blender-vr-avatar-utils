from typing import Literal

from base import bpy_prop_collection, bpy_struct

from a import AnimData, AnimViz
from c import Collection, CollisionSettings, CyclesObjectSettings
from d import Depsgraph
from f import FieldSettings
from i import ID, ImageUser
from m import Macro, Material, MaterialSlot, Modifier, MotionPath
from p import ParticleSystems, Pose, PoseBone
from r import RigidBodyConstraint, RigidBodyObject
from s import Scene, ShapeKey, SoftBodySettings, SpaceView3D
from u import UILayout
from v import VertexGroups, ViewLayer
from w import WindowCursor, WmReportType

import mathutils
import bpy


ObjectAxis = Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']

ObjectEmptyDrawtype = Literal[
    'PLAIN_AXES',
    'ARROWS',
    'SINGLE_ARROW',
    'CIRCLE',
    'CUBE',
    'SPHERE',
    'CONE',
    'IMAGE',
]

ObjectMode = Literal[
    'OBJECT',
    'EDIT',
    'POSE',
    'SCULPT',
    'VERTEX_PAINT',
    'WEIGHT_PAINT',
    'TEXTURE_PAINT',
    'PARTICLE_EDIT',
    'EDIT_GPENCIL',
    'SCULPT_GPENCIL',
    'PAINT_GPENCIL',
    'WEIGHT_GPENCIL',
    'VERTEX_GPENCIL',
    'SCULPT_CURVES',
    'PAINT_GREASE_PENCIL',
]

ObjectModifierType = Literal[
    'DATA_TRANSFER',
    'MESH_CACHE',
    'MESH_SEQUENCE_CACHE',
    'NORMAL_EDIT',
    'WEIGHTED_NORMAL',
    'UV_PROJECT',
    'UV_WARP',
    'VERTEX_WEIGHT_EDIT',
    'VERTEX_WEIGHT_MIX',
    'VERTEX_WEIGHT_PROXIMITY',
    'GREASE_PENCIL_COLOR',
    'GREASE_PENCIL_TINT',
    'GREASE_PENCIL_OPACITY',
    'ARRAY',
    'BEVEL',
    'BOOLEAN',
    'BUILD',
    'DECIMATE',
    'EDGE_SPLIT',
    'NODES',
    'MASK',
    'MIRROR',
    'MESH_TO_VOLUME',
    'MULTIRES',
    'REMESH',
    'SCREW',
    'SKIN',
    'SOLIDIFY',
    'SUBSURF',
    'TRIANGULATE',
    'VOLUME_TO_MESH',
    'WELD',
    'WIREFRAME',
    'GREASE_PENCIL_SUBDIV',
    'GREASE_PENCIL_MIRROR',
    'ARMATURE',
    'CAST',
    'CURVE',
    'DISPLACE',
    'HOOK',
    'LAPLACIANDEFORM',
    'LATTICE',
    'MESH_DEFORM',
    'SHRINKWRAP',
    'SIMPLE_DEFORM',
    'SMOOTH',
    'CORRECTIVE_SMOOTH',
    'LAPLACIANSMOOTH',
    'SURFACE_DEFORM',
    'WARP',
    'WAVE',
    'VOLUME_DISPLACE',
    'GREASE_PENCIL_NOISE',
    'GREASE_PENCIL_OFFSET',
    'GREASE_PENCIL_SMOOTH',
    'GREASE_PENCIL_THICKNESS',
    'CLOTH',
    'COLLISION',
    'DYNAMIC_PAINT',
    'EXPLODE',
    'FLUID',
    'OCEAN',
    'PARTICLE_INSTANCE',
    'PARTICLE_SYSTEM',
    'SOFT_BODY',
    'SURFACE',
]

ObjectRotationMode = Literal[
    'QUATERNION',
    'XYZ',
    'XZY',
    'YXZ',
    'YZX',
    'ZXY',
    'ZYX',
    'AXIS_ANGLE',
]

ObjectType = Literal[
    'MESH',
    'CURVE',
    'SURFACE',
    'META',
    'FONT',
    'CURVES',
    'POINTCLOUD',
    'VOLUME',
    'GPENCIL',
    'GREASEPENCIL',
    'ARMATURE',
    'LATTICE',
    'EMPTY',
    'LIGHT',
    'LIGHT_PROBE',
    'CAMERA',
    'SPEAKER',
]

ObjectTypeCurve = Literal['CURVE', 'SURFACE', 'FONT']

OperatorReturn = Literal['RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH', 'INTERFACE']

OperatorTypeFlag = Literal[
    'REGISTER',
    'UNDO',
    'UNDO_GROUPED',
    'BLOCKING',
    'MACRO',
    'GRAB_CURSOR',
    'GRAB_CURSOR_X',
    'GRAB_CURSOR_Y',
    'DEPENDS_ON_CURSOR',
    'PRESET',
    'INTERNAL',
]


# TODO: incomplete, messing methods
# noinspection PyPropertyDefinition
class Object(ID):  # NEW REGEX
    active_material: Material
    active_material_index: int
    active_shape_key_index: int
    add_rest_position_attribute: bool
    color: tuple[float, float, float, float]
    data: ID
    delta_location: mathutils.Vector
    delta_rotation_euler: mathutils.Euler
    delta_rotation_quaternion: mathutils.Quaternion
    delta_scale: mathutils.Vector
    dimensions: mathutils.Vector
    display_bounds_type: Literal['BOX', 'SPHERE', 'CYLINDER', 'CONE', 'CAPSULE']
    display_type: Literal['BOUNDS', 'WIRE', 'SOLID', 'TEXTURED']
    empty_display_size: float
    empty_display_type: ObjectEmptyDrawtype
    empty_image_depth: Literal['DEFAULT', 'FRONT', 'BACK']
    empty_image_offset: tuple[float, float]
    empty_image_side: Literal['DOUBLE_SIDED', 'FRONT', 'BACK']
    hide_probe_plane: bool
    hide_probe_sphere: bool
    hide_probe_volume: bool
    hide_render: bool
    hide_select: bool
    hide_viewport: bool
    instance_collection: Collection
    instance_faces_scale: float
    instance_type: Literal['NONE', 'VERTS', 'FACES', 'COLLECTION']
    is_holdout: bool
    is_shadow_catcher: bool
    lightgroup: str
    location: mathutils.Vector
    lock_location: tuple[bool, bool, bool]
    lock_rotation: tuple[bool, bool, bool]
    lock_rotation_w: bool
    lock_rotations_4d: bool
    lock_scale: tuple[bool, bool, bool]
    matrix_basis: mathutils.Matrix
    matrix_local: mathutils.Matrix
    matrix_parent_inverse: mathutils.Matrix
    matrix_world: mathutils.Matrix
    parent: 'Object'
    parent_bone: str
    parent_type: Literal['OBJECT', 'ARMATURE', 'LATTICE', 'VERTEX', 'VERTEX_3', 'BONE']
    parent_vertices: tuple[int, int, int]
    pass_index: int
    rotation_axis_angle: tuple[float, float, float, float]
    rotation_euler: mathutils.Euler
    rotation_mode: ObjectRotationMode
    rotation_quaternion: mathutils.Quaternion
    scale: mathutils.Vector
    show_all_edges: bool
    show_axis: bool
    show_bounds: bool
    show_empty_image_only_axis_aligned: bool
    show_empty_image_orthographic: bool
    show_empty_image_perspective: bool
    show_in_front: bool
    show_instancer_for_render: bool
    show_instancer_for_viewport: bool
    show_name: bool
    show_only_shape_key: bool
    show_texture_space: bool
    show_transparent: bool
    show_wire: bool
    track_axis: ObjectAxis
    up_axis: Literal['X', 'Y', 'Z']
    use_camera_lock_parent: bool
    use_empty_image_alpha: bool
    use_grease_pencil_lights: bool
    use_instance_faces_scale: bool
    use_instance_vertices_rotation: bool
    use_mesh_mirror_x: bool
    use_mesh_mirror_y: bool
    use_mesh_mirror_z: bool
    use_shape_key_edit_mode: bool
    use_simulation_cache: bool
    visible_camera: bool
    visible_diffuse: bool
    visible_glossy: bool
    visible_shadow: bool
    visible_transmission: bool
    visible_volume_scatter: bool

    @property
    def active_shape_key(self) -> ShapeKey: pass

    @property
    def animation_data(self) -> AnimData: pass

    @property
    def animation_visualization(self) -> AnimViz: pass

    @property
    def bound_box(self) -> tuple[
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
        tuple[float, float, float],
    ]: pass

    @property
    def collision(self) -> CollisionSettings: pass

    @property
    def constraints(self) -> 'ObjectConstraints': pass

    @property
    def cycles(self) -> CyclesObjectSettings: pass

    @property
    def display(self) -> 'ObjectDisplay': pass

    @property
    def field(self) -> FieldSettings: pass

    @property
    def grease_pencil_modifiers(self) -> 'ObjectGpencilModifiers': pass

    @property
    def image_user(self) -> ImageUser: pass

    @property
    def is_from_instancer(self) -> bool: pass

    @property
    def is_from_set(self) -> bool: pass

    @property
    def is_instancer(self) -> bool: pass

    @property
    def light_linking(self) -> 'ObjectLightLinking': pass

    @property
    def lineart(self) -> 'ObjectLineArt': pass

    @property
    def material_slots(self) -> bpy_prop_collection[MaterialSlot]: pass

    @property
    def mode(self) -> ObjectMode: pass

    @property
    def modifiers(self) -> 'ObjectModifiers': pass

    @property
    def motion_path(self) -> MotionPath: pass

    @property
    def particle_systems(self) -> ParticleSystems: pass

    @property
    def pose(self) -> Pose: pass

    @property
    def rigid_body(self) -> RigidBodyObject: pass

    @property
    def rigid_body_constraint(self) -> RigidBodyConstraint: pass

    @property
    def shader_effects(self) -> 'ObjectShaderFx': pass

    @property
    def soft_body(self) -> SoftBodySettings: pass

    @property
    def type(self) -> ObjectType: pass

    @property
    def use_dynamic_topology_sculpting(self) -> bool: pass

    @property
    def vertex_groups(self) -> VertexGroups: pass

    @property
    def children(self) -> tuple[()] | tuple['Object', ...]: pass

    @property
    def children_recursive(self) -> tuple[()] | tuple['Object', ...]: pass

    @property
    def users_collection(self) -> tuple[()] | tuple[Collection, ...]: pass

    @property
    def users_scene(self) -> tuple[()] | tuple[Scene, ...]: pass

    def select_get(self, view_layer: ViewLayer | None = None) -> bool: pass

    def select_set(self, state: bool, view_layer: ViewLayer | None = None) -> None: pass

    def hide_get(self, view_layer: ViewLayer | None = None) -> bool: pass

    def hide_set(self, state: bool, view_layer: ViewLayer | None = None) -> None: pass

    def visible_get(self, view_layer: ViewLayer | None = None, viewport: SpaceView3D | None = None) -> bool: pass

    def holdout_get(self, view_layer: ViewLayer | None = None) -> bool: pass

    def indirect_only_get(self, view_layer: ViewLayer | None = None) -> bool: pass

    def local_view_get(self, viewport: SpaceView3D) -> bool: pass

    def local_view_set(self, viewport: SpaceView3D, state: bool) -> None: pass

    def visible_in_viewport_get(self, viewport: SpaceView3D) -> bool: pass

    def convert_space(
        self,
        pose_bone: PoseBone | None = None,
        matrix: mathutils.Matrix = mathutils.Matrix((
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0),
        )),
        from_space: Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'] = 'WORLD',
        to_space: Literal['WORLD', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'] = 'WORLD',
    ) -> mathutils.Matrix: pass

    def calc_matrix_camera(
        self,
        depsgraph: Depsgraph,
        x: int = 1,
        y: int = 1,
        scale_x: float = 1.0,
        scale_y: float = 1.0,
    ) -> mathutils.Matrix: pass


class ObjectModifiers(bpy_prop_collection[Modifier]):  # NEW REGEX
    active: Modifier

    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: ObjectModifierType) -> Modifier: pass

    def remove(self, modifier: Modifier) -> None: pass

    def clear(self) -> None: pass

    def move(self, from_index: int, to_index: int): pass


# noinspection PyPropertyDefinition
class Operator(bpy_struct):  # NEW REGEX
    bl_cursor_pending: WindowCursor
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_options: set[OperatorTypeFlag]
    bl_property: str
    bl_translation_context: str
    bl_undo_group: str

    @property
    def has_reports(self) -> bool: pass

    @property
    def layout(self) -> UILayout: pass

    @property
    def macros(self) -> bpy_prop_collection[Macro]: pass

    @property
    def name(self) -> str: pass

    @property
    def options(self) -> 'OperatorOptions': pass

    @property
    def properties(self) -> 'OperatorProperties': pass

    # noinspection PyShadowingBuiltins
    def report(self, type: set[WmReportType], message: str) -> None: pass

    def is_repeat(self) -> bool: pass

    @classmethod
    def poll(cls, context: bpy.context) -> bool: pass

    def execute(self, context: bpy.context) -> set[OperatorReturn]: pass

    def check(self, context: bpy.context) -> bool: pass 

    # TODO: what type is 'event'?
    def invoke(self, context: bpy.context, event) -> set[OperatorReturn]: pass

    # TODO: what type is 'event'?
    def modal(self, context: bpy.context, event) -> set[OperatorReturn]: pass

    def draw(self, context: bpy.context) -> None: pass

    def cancel(self, context: bpy.context) -> None: pass

    # TODO: what type is 'properties'?
    @classmethod
    def description(cls, context: bpy.context, properties) -> str: pass

    # TODO: what is this?
    def as_keywords(self, *, ignore=()): pass

    @classmethod
    def poll_message_set(cls, message: str, *args): pass


# noinspection PyPropertyDefinition
class OperatorOptions(bpy_struct):  # NEW REGEX
    use_cursor_region: bool

    @property
    def is_grab_cursor(self) -> bool: pass

    @property
    def is_invoke(self) -> bool: pass

    @property
    def is_repeat(self) -> bool: pass

    @property
    def is_repeat_last(self) -> bool: pass


class OperatorProperties(bpy_struct):  # NEW REGEX
    pass
