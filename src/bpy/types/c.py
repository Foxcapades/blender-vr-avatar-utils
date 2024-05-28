from typing import ContextManager, Literal, Protocol

from base import bpy_struct, bpy_prop_collection

from mathutils import Color, Matrix, Vector

import a
import b
import d
import e
import f
import g
import i
import k
import l
import m
import n
import o
import p
import r
import s
import t
import u
import v
import w


ColorSpaceConvertDefault = Literal['NONE']

ConstraintType = Literal[
    'CAMERA_SOLVER',
    'FOLLOW_TRACK',
    'OBJECT_SOLVER',
    'COPY_LOCATION',
    'COPY_ROTATION',
    'COPY_SCALE',
    'COPY_TRANSFORMS',
    'LIMIT_DISTANCE',
    'LIMIT_LOCATION',
    'LIMIT_ROTATION',
    'LIMIT_SCALE',
    'MAINTAIN_VOLUME',
    'TRANSFORM',
    'TRANSFORM_CACHE',
    'CLAMP_TO',
    'DAMPED_TRACK',
    'IK',
    'LOCKED_TRACK',
    'SPLINE_IK',
    'STRETCH_TO',
    'TRACK_TO',
    'ACTION',
    'ARMATURE',
    'CHILD_OF',
    'FLOOR',
    'FOLLOW_PATH',
    'PIVOT',
    'SHRINKWRAP',
]

CurveFitMethod = Literal['REFIT', 'SPLIT']


# noinspection PyPep8Naming
class CLIP_UL_tracking_objects(u.UIList):
    # TODO: what is this?
    def draw_item(self, _context, layout, _data, item, _icon, _active_data, _active_propname, _index): pass


# noinspection PyShadowingBuiltins,PyPep8Naming
class CURVES_UL_attributes(u.UIList):
    # TODO: what is this?
    def draw_item(self, _context, layout, _data, attribute, _icon, _active_data, _active_propname, _index): pass

    # TODO: what is this?
    def filter_items(self, _context, data, property): pass


# noinspection PyPropertyDefinition
class CacheFile(i.ID):
    active_index: int 
    filepath: str
    forward_axis: o.ObjectAxis 
    frame: float 
    frame_offset: float 
    is_sequence: bool 
    override_frame: bool 
    prefetch_cache_size: int 
    scale: float 
    up_axis: o.ObjectAxis 
    use_prefetch: bool 
    use_render_procedural: bool 
    velocity_name: str
    velocity_unit: v.VelocityUnit 
    
    @property
    def animation_data(self) -> a.AnimData: pass
    
    @property
    def layers(self) -> 'CacheFileLayers': pass
    
    @property
    def object_paths(self) -> 'CacheObjectPaths': pass


class CacheFileLayer(bpy_struct):
    filepath: str
    hide_layer: bool


class CacheFileLayers(bpy_prop_collection[CacheFileLayer]):
    active: CacheFileLayer

    def new(self, filepath: str) -> CacheFileLayer: pass

    def remove(self, layer: CacheFileLayer) -> None: pass


class CacheObjectPath(bpy_struct):
    path: str


class CacheObjectPaths(bpy_prop_collection[CacheObjectPath]):
    pass


# noinspection PyPropertyDefinition
class Camera(i.ID):
    angle: float 
    angle_x: float 
    angle_y: float 
    clip_end: float
    clip_start: float 
    display_size: float
    fisheye_fov: float
    fisheye_lens: float 
    fisheye_polynomial_k0: float 
    fisheye_polynomial_k1: float 
    fisheye_polynomial_k2: float 
    fisheye_polynomial_k3: float 
    fisheye_polynomial_k4: float 
    latitude_max: float 
    latitude_min: float 
    lens: float 
    lens_unit: Literal['MILLIMETERS', 'FOV']
    longitude_max: float 
    longitude_min: float 
    ortho_scale: float 
    panorama_type: Literal[
        'EQUIRECTANGULAR',
        'EQUIANGULAR_CUBEMAP_FACE',
        'MIRRORBALL',
        'FISHEYE_EQUIDISTANT',
        'FISHEYE_EQUISOLID',
        'FISHEYE_LENS_POLYNOMIAL'
    ]
    passepartout_alpha: float 
    sensor_fit: Literal['AUTO', 'HORIZONTAL', 'VERTICAL']
    sensor_height: float 
    sensor_width: float 
    shift_x: float 
    shift_y: float 
    show_background_images: bool
    show_composition_center: bool
    show_composition_center_diagonal: bool
    show_composition_golden: bool
    show_composition_golden_tria_a: bool
    show_composition_golden_tria_b: bool
    show_composition_harmony_tri_a: bool
    show_composition_harmony_tri_b: bool
    show_composition_thirds: bool
    show_limits: bool
    show_mist: bool
    show_name: bool
    show_passepartout: bool
    show_safe_areas: bool
    show_safe_center: bool
    show_sensor: bool
    type: Literal['PERSP', 'ORTHO', 'PANO']

    @property
    def animation_data(self) -> a.AnimData: pass

    @property
    def background_images(self) -> 'CameraBackgroundImages': pass

    @property
    def dof(self) -> 'CameraDOFSettings': pass

    @property
    def stereo(self) -> 'CameraStereoData': pass

    def view_frame(self, scene: s.Scene | None = None) -> tuple[Vector, Vector, Vector, Vector]: pass


# noinspection PyPropertyDefinition
class CameraBackgroundImage(bpy_struct):
    alpha: float 
    clip: m.MovieClip
    display_depth: Literal['BACK', 'FRONT']
    frame_method: Literal['STRETCH', 'FIT', 'CROP']
    image: i.Image
    offset: float
    scale: float 
    show_background_image: bool
    show_expanded: bool
    show_on_foreground: bool
    source: Literal['IMAGE', 'MOVIE_CLIP']
    use_camera_clip: bool
    use_flip_x: bool
    use_flip_y: bool

    @property
    def clip_user(self) -> m.MovieClipUser: pass

    @property
    def image_user(self) -> i.ImageUser: pass

    @property
    def is_override_data(self) -> bool: pass


class CameraBackgroundImages(bpy_prop_collection[CameraBackgroundImage]):
    def new(self) -> CameraBackgroundImage: pass
    def remove(self, image: CameraBackgroundImage) -> None: pass
    def clear(self) -> None: pass


class CameraDOFSettings(bpy_struct):
    aperture_blades: int 
    aperture_fstop: float 
    aperture_ratio: float 
    aperture_rotation: float 
    focus_distance: float 
    focus_object: o.Object
    focus_subtarget: str
    use_dof: bool


class CameraSolverConstraint('Constraint'):
    clip: m.MovieClip
    use_active_clip: bool


class CameraStereoData(bpy_struct):
    convergence_distance: float 
    convergence_mode: Literal['OFFAXIS', 'PARALLEL', 'TOE']
    interocular_distance: float 
    pivot: Literal['LEFT', 'RIGHT', 'CENTER']
    pole_merge_angle_from: float 
    pole_merge_angle_to: float 
    use_pole_merge: bool
    use_spherical_stereo: bool


class CastModifier(m.Modifier):
    cast_type: Literal['SPHERE', 'CYLINDER', 'CUBOID']
    factor: float 
    invert_vertex_group: bool
    object: o.Object
    radius: float 
    size: float 
    use_radius_as_size: bool
    use_transform: bool
    use_x: bool
    use_y: bool
    use_z: bool
    vertex_group: str


class ChannelDriverVariables(bpy_prop_collection[d.DriverVariable]):
    def new(self) -> d.DriverVariable: pass
    def remove(self, variable: d.DriverVariable) -> None: pass


class ChildOfConstraint('Constraint'):
    inverse_matrix: bool
    subtarget: str
    target: o.Object
    use_location_x: bool
    use_location_y: bool
    use_location_z: bool
    use_rotation_x: bool
    use_rotation_y: bool
    use_rotation_z: bool
    use_scale_x: bool
    use_scale_y: bool
    use_scale_z: bool


class ChildParticle(bpy_struct):
    pass


class ClampToConstraint('Constraint'):
    main_axis: Literal['CLAMPTO_AUTO', 'CLAMPTO_X', 'CLAMPTO_Y', 'CLAMPTO_Z']
    target: o.Object
    use_cyclic: bool


class ClothCollisionSettings(bpy_struct):
    collection: 'Collection'
    collision_quality: int 
    damping: float 
    distance_min: float 
    friction: float 
    impulse_clamp: float 
    self_distance_min: float 
    self_friction: float 
    self_impulse_clamp: float 
    use_collision: bool
    use_self_collision: bool
    vertex_group_object_collisions: str
    vertex_group_self_collisions: str


# noinspection PyPropertyDefinition
class ClothModifier(m.Modifier):
    @property
    def collision_settings(self) -> ClothCollisionSettings: pass
    
    @property
    def hair_grid_max(self) -> tuple[float, float, float]: pass
    
    @property
    def hair_grid_min(self) -> tuple[float, float, float]: pass
    
    @property
    def hair_grid_resolution(self) -> tuple[int, int, int]: pass
    
    @property
    def point_cache(self) -> p.PointCache: pass
    
    @property
    def settings(self) -> 'ClothSettings': pass
    
    @property
    def solver_result(self) -> 'ClothSolverResult': pass


# noinspection PyPropertyDefinition
class ClothSettings(bpy_struct):
    air_damping: float 
    bending_damping: float 
    bending_model: Literal['ANGULAR', 'LINEAR'] 
    bending_stiffness: float 
    bending_stiffness_max: float 
    collider_friction: float 
    compression_damping: float 
    compression_stiffness: float 
    compression_stiffness_max: float 
    density_strength: float 
    density_target: float 
    fluid_density: float
    goal_default: float 
    goal_friction: float 
    goal_max: float 
    goal_min: float 
    goal_spring: float 
    gravity: Vector 
    internal_compression_stiffness: float 
    internal_compression_stiffness_max: float 
    internal_friction: float 
    internal_spring_max_diversion: float 
    internal_spring_max_length: float 
    internal_spring_normal_check: bool 
    internal_tension_stiffness: float 
    internal_tension_stiffness_max: float 
    mass: float 
    pin_stiffness: float 
    pressure_factor: float 
    quality: int 
    rest_shape_key: s.ShapeKey 
    sewing_force_max: float 
    shear_damping: float 
    shear_stiffness: float 
    shear_stiffness_max: float 
    shrink_max: float 
    shrink_min: float 
    target_volume: float 
    tension_damping: float 
    tension_stiffness: float 
    tension_stiffness_max: float 
    time_scale: float 
    uniform_pressure_force: float 
    use_dynamic_mesh: bool 
    use_internal_springs: bool 
    use_pressure: bool 
    use_pressure_volume: bool 
    use_sewing_springs: bool 
    vertex_group_bending: str 
    vertex_group_intern: str 
    vertex_group_mass: str 
    vertex_group_pressure: str 
    vertex_group_shear_stiffness: str 
    vertex_group_shrink: str 
    vertex_group_structural_stiffness: str 
    voxel_cell_size: float

    @property
    def effector_weights(self) -> e.EffectorWeights: pass


# noinspection PyPropertyDefinition
class ClothSolverResult(bpy_struct):
    @property
    def avg_error(self) -> float: pass
    
    @property
    def avg_iterations(self) -> float: pass
    
    @property
    def max_error(self) -> float: pass
    
    @property
    def max_iterations(self) -> int: pass
    
    @property
    def min_error(self) -> float: pass
    
    @property
    def min_iterations(self) -> int: pass
    
    @property
    def status(self) -> set[Literal['SUCCESS', 'NUMERICAL_ISSUE', 'NO_CONVERGENCE', 'INVALID_INPUT']]: pass


# noinspection PyPropertyDefinition
class CloudsTexture(t.Texture):
    cloud_type: Literal['GRAYSCALE', 'COLOR'] 
    nabla: float 
    noise_basis: Literal['BLENDER_ORIGINAL', 'ORIGINAL_PERLIN', 'IMPROVED_PERLIN', 'VORONOI_F1', 'VORONOI_F2', 'VORONOI_F3', 'VORONOI_F4', 'VORONOI_F2_F1', 'VORONOI_CRACKLE', 'CELL_NOISE'] 
    noise_depth: int 
    noise_scale: float 
    noise_type: Literal['SOFT_NOISE', 'HARD_NOISE']

    # TODO: i assume this is some form of collection of material instances?
    @property
    def users_material(self): pass

    # TODO: i assume this is some form of collection of object modifier instances?
    @property
    def users_object_modifier(self): pass


# noinspection PyPropertyDefinition
class Collection(i.ID):
    color_tag: 'CollectionColor'
    hide_render: bool
    hide_select: bool 
    hide_viewport: bool 
    instance_offset: Vector 
    lineart_intersection_mask: tuple[bool, bool, bool, bool, bool, bool, bool, bool] 
    lineart_intersection_priority: int 
    lineart_usage: Literal[
        'INCLUDE',
        'OCCLUSION_ONLY',
        'EXCLUDE',
        'INTERSECTION_ONLY',
        'NO_INTERSECTION',
        'FORCE_INTERSECTION'
    ]
    lineart_use_intersection_mask: bool
    use_lineart_intersection_priority: bool

    @property
    def all_objects(self) -> bpy_prop_collection[o.Object]: pass

    @property
    def children(self) -> 'CollectionChildren': pass

    @property
    def collection_children(self) -> bpy_prop_collection['CollectionChild']: pass

    @property
    def collection_objects(self) -> bpy_prop_collection['CollectionObject']: pass

    @property
    def objects(self) -> 'CollectionObjects': pass

    # TODO: what is the actual type of the return value
    @property
    def children_recursive(self): pass

    # TODO: What does this return?
    @property
    def users_dupli_group(self): pass


class CollectionChild(bpy_struct):
    light_linking: 'CollectionLightLinking'


class CollectionChildren(bpy_prop_collection[CollectionChild]):
    def link(self, child: Collection) -> None: pass
    def unlink(self, child: Collection) -> None: pass


class CollectionLightLinking(bpy_struct):
    link_state: Literal['INCLUDE', 'EXCLUDE']


class CollectionObject(bpy_struct):
    light_linking: CollectionLightLinking


# noinspection PyShadowingBuiltins
class CollectionObjects(bpy_prop_collection[o.Object]):
    def link(self, object: o.Object) -> None: pass
    def unlink(self, object: o.Object) -> None: pass


# noinspection PyPropertyDefinition
class CollectionProperty(p.Property):
    @property
    def fixed_type(self) -> s.Struct: pass


class CollisionModifier(m.Modifier):
    @property
    def settings(self) -> 'CollisionSettings': pass


class CollisionSettings(bpy_struct):
    absorption: float 
    cloth_friction: float 
    damping: float 
    damping_factor: float 
    damping_random: float 
    friction_factor: float 
    friction_random: float 
    permeability: float 
    stickiness: float 
    thickness_inner: float 
    thickness_outer: float 
    use: bool
    use_culling: bool
    use_normal: bool
    use_particle_kill: bool


# noinspection PyPropertyDefinition
class ColorBalanceModifier(s.SequenceModifier):
    color_multiply: float

    @property
    def color_balance(self) -> s.SequenceColorBalanceData: pass


# noinspection PyPropertyDefinition
class ColorGpencilModifier(g.GpencilModifier):
    hue: float
    invert_layer_pass: bool 
    invert_layers: bool 
    invert_material_pass: bool 
    invert_materials: bool 
    layer: str
    layer_pass: int 
    material: m.Material 
    modify_color: Literal['BOTH', 'STROKE', 'FILL'] 
    pass_index: int 
    saturation: float 
    use_custom_curve: bool 
    value: float

    @property
    def curve(self) -> 'CurveMapping': pass


class ColorManagedDisplaySettings(bpy_struct):
    display_device: Literal['NONE']


class ColorManagedInputColorspaceSettings(bpy_struct):
    is_data: bool
    name: ColorSpaceConvertDefault


class ColorManagedSequencerColorspaceSettings(bpy_struct):
    name: ColorSpaceConvertDefault


# noinspection PyPropertyDefinition
class ColorManagedViewSettings(bpy_struct):
    exposure: float
    gamma: float 
    look: Literal['NONE'] 
    use_curve_mapping: bool 
    use_hdr_view: bool 
    view_transform: Literal['NONE'] 

    @property
    def curve_mapping(self) -> 'CurveMapping': pass


# noinspection PyPropertyDefinition
class ColorMapping(bpy_struct):

    @property
    def blend_color(self) -> Color: pass

    @property
    def blend_factor(self) -> float: pass

    @property
    def blend_type(self) -> Literal[
        'MIX',
        'DARKEN',
        'MULTIPLY',
        'LIGHTEN',
        'SCREEN',
        'ADD',
        'OVERLAY',
        'SOFT_LIGHT',
        'LINEAR_LIGHT',
        'DIFFERENCE',
        'SUBTRACT',
        'DIVIDE',
        'HUE',
        'SATURATION',
        'COLOR',
        'VALUE'
    ]: pass

    @property
    def brightness(self) -> float: pass

    @property
    def color_ramp(self) -> 'ColorRamp': pass

    @property
    def contrast(self) -> float: pass

    @property
    def saturation(self) -> float: pass

    @property
    def use_color_ramp(self) -> bool: pass


# noinspection PyPropertyDefinition
class ColorMixSequence(e.EffectSequence):
    blend_effect: Literal[
        'DARKEN',
        'MULTIPLY',
        'BURN',
        'LINEAR_BURN',
        'LIGHTEN',
        'SCREEN',
        'DODGE',
        'ADD',
        'OVERLAY',
        'SOFT_LIGHT',
        'HARD_LIGHT',
        'VIVID_LIGHT',
        'LINEAR_LIGHT',
        'PIN_LIGHT',
        'DIFFERENCE',
        'EXCLUSION',
        'SUBTRACT',
        'HUE',
        'SATURATION',
        'COLOR',
        'VALUE'
    ]
    factor: float 
    input_1: s.Sequence
    input_2: s.Sequence

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class ColorRamp(bpy_struct):
    color_mode: Literal['RGB', 'HSV', 'HSL']
    hue_interpolation: Literal['NEAR', 'FAR', 'CW', 'CCW']
    interpolation: Literal['EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT']

    @property
    def elements(self) -> 'ColorRampElements': pass


class ColorRampElement(bpy_struct):
    alpha: float 
    color: tuple[float, float, float, float]
    position: float


class ColorRampElements(bpy_prop_collection[ColorRampElement]):
    def new(self, position: float) -> ColorRampElement: pass
    def remove(self, element: ColorRampElement) -> None: pass


class ColorSequence(e.EffectSequence):
    color: Color
    input_count: int


class CompositorNode(n.NodeInternal):
    def tag_need_exec(self) -> None: pass
    def update(self) -> None: pass


class CompositorNodeAlphaOver(CompositorNode):
    premul: float
    use_premultiply: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeAntiAliasing(CompositorNode):
    contrast_limit: float 
    corner_rounding: float 
    threshold: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBilateralblur(CompositorNode):
    iterations: int
    sigma_color: float
    sigma_space: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBlur(CompositorNode):
    aspect_correction: Literal['NONE', 'Y', 'X']
    factor: float 
    factor_x: float 
    factor_y: float 
    filter_type: Literal['FLAT', 'TENT', 'QUAD', 'CUBIC', 'GAUSS', 'FAST_GAUSS', 'CATROM', 'MITCH']
    size_x: int 
    size_y: int 
    use_bokeh: bool
    use_extended_bounds: bool
    use_gamma_correction: bool
    use_relative: bool
    use_variable_size: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBokehBlur(CompositorNode):
    blur_max: float 
    use_extended_bounds: bool
    use_variable_size: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBokehImage(CompositorNode):
    angle: float 
    catadioptric: float 
    flaps: int 
    rounding: float 
    shift: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBoxMask(CompositorNode):
    height: float 
    mask_type: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'NOT']
    rotation: float 
    width: float 
    x: float 
    y: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeBrightContrast(CompositorNode):
    use_premultiply: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeChannelMatte(CompositorNode):
    color_space: Literal['RGB', 'HSV', 'YUV', 'YCC']
    limit_channel: Literal['R', 'G', 'B']
    limit_max: float 
    limit_method: Literal['SINGLE', 'MAX']
    limit_min: float 
    matte_channel: Literal['R', 'G', 'B']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeChromaMatte(CompositorNode):
    gain: float 
    lift: float 
    shadow_adjust: float 
    threshold: float 
    tolerance: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeColorBalance(CompositorNode):
    correction_method: Literal['LIFT_GAMMA_GAIN', 'OFFSET_POWER_SLOPE']
    gain: Color
    gamma: Color
    lift: Color
    offset: Color
    offset_basis: float 
    power: Color
    slope: Color

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeColorCorrection(CompositorNode):
    blue: bool
    green: bool
    highlights_contrast: float 
    highlights_gain: float 
    highlights_gamma: float 
    highlights_lift: float 
    highlights_saturation: float 
    master_contrast: float 
    master_gain: float 
    master_gamma: float 
    master_lift: float 
    master_saturation: float 
    midtones_contrast: float 
    midtones_end: float 
    midtones_gain: float 
    midtones_gamma: float 
    midtones_lift: float 
    midtones_saturation: float 
    midtones_start: float 
    red: bool
    shadows_contrast: float 
    shadows_gain: float 
    shadows_gamma: float 
    shadows_lift: float 
    shadows_saturation: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeColorMatte(CompositorNode):
    color_hue: float 
    color_saturation: float 
    color_value: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeColorSpill(CompositorNode):
    channel: Literal['R', 'G', 'B']
    limit_channel: Literal['R', 'G', 'B']
    limit_method: Literal['SIMPLE', 'AVERAGE']
    ratio: float 
    unspill_blue: float 
    unspill_green: float 
    unspill_red: float 
    use_unspill: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombHSVA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombRGBA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombYCCA(CompositorNode):
    mode: Literal['ITUBT601', 'ITUBT709', 'JFIF']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombYUVA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombineColor(CompositorNode):
    mode: Literal['RGB', 'HSV', 'HSL', 'YCC', 'YUV']
    ycc_mode: Literal['ITUBT601', 'ITUBT709', 'JFIF']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCombineXYZ(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeComposite(CompositorNode):
    use_alpha: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeConvertColorSpace(CompositorNode):
    from_color_space: ColorSpaceConvertDefault
    to_color_space: ColorSpaceConvertDefault

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCornerPin(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCrop(CompositorNode):
    max_x: int 
    max_y: int 
    min_x: int 
    min_y: int 
    rel_max_x: float 
    rel_max_y: float 
    rel_min_x: float 
    rel_min_y: float 
    relative: bool
    use_crop_size: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCryptomatte(CompositorNode):
    add: Color
    matte_id: str
    remove: Color

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


# noinspection PyPropertyDefinition
class CompositorNodeCryptomatteV2(CompositorNode):
    add: Color 
    frame_duration: int
    frame_offset: int 
    frame_start: int
    image: i.Image
    layer: Literal['PLACEHOLDER'] 
    layer_name: Literal['CryptoObject', 'CryptoMaterial', 'CryptoAsset'] 
    matte_id: str 
    remove: Color 
    scene: s.Scene 
    source: Literal['RENDER', 'IMAGE'] 
    use_auto_refresh: bool 
    use_cyclic: bool
    view: Literal['ALL'] 

    @property
    def entries(self) -> bpy_prop_collection['CryptomatteEntry']: pass

    @property
    def has_layers(self) -> bool: pass

    @property
    def has_views(self) -> bool: pass

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCurveRGB(CompositorNode):
    mapping: 'CurveMapping'

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCurveVec(CompositorNode):
    mapping: 'CurveMapping'

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeCustomGroup(CompositorNode):
    node_tree: n.NodeTree


class CompositorNodeDBlur(CompositorNode):
    angle: float 
    center_x: float 
    center_y: float 
    distance: float 
    iterations: int 
    spin: float 
    zoom: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDefocus(CompositorNode):
    angle: float 
    blur_max: float 
    bokeh: Literal['OCTAGON', 'HEPTAGON', 'HEXAGON', 'PENTAGON', 'SQUARE', 'TRIANGLE', 'CIRCLE']
    f_stop: float 
    scene: s.Scene
    threshold: float 
    use_gamma_correction: bool
    use_preview: bool
    use_zbuffer: bool
    z_scale: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDenoise(CompositorNode):
    prefilter: Literal['NONE', 'FAST', 'ACCURATE']
    use_hdr: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDespeckle(CompositorNode):
    threshold: float 
    threshold_neighbor: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDiffMatte(CompositorNode):
    falloff: float 
    tolerance: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDilateErode(CompositorNode):
    distance: int 
    edge: float 
    falloff: p.ProportionalFalloffCurveOnly
    mode: Literal['STEP', 'THRESHOLD', 'DISTANCE', 'FEATHER']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDisplace(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDistanceMatte(CompositorNode):
    channel: Literal['RGB', 'YCC']
    falloff: float 
    tolerance: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeDoubleEdgeMask(CompositorNode):
    edge_mode: Literal['BLEED_OUT', 'KEEP_IN']
    inner_mode: Literal['ALL', 'ADJACENT_ONLY']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeEllipseMask(CompositorNode):
    height: float 
    mask_type: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'NOT']
    rotation: float 
    width: float 
    x: float 
    y: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeExposure(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeFilter(CompositorNode):
    filter_type: n.NodeFilter

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeFlip(CompositorNode):
    axis: Literal['X', 'Y', 'XY']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeGamma(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeGlare(CompositorNode):
    angle_offset: float 
    color_modulation: float 
    fade: float 
    glare_type: Literal['GHOSTS', 'STREAKS', 'FOG_GLOW', 'SIMPLE_STAR']
    iterations: int 
    mix: float 
    quality: Literal['HIGH', 'MEDIUM', 'LOW']
    size: int 
    streaks: int 
    threshold: float 
    use_rotate_45: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeGroup(CompositorNode):
    node_tree: n.NodeTree

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeHueCorrect(CompositorNode):
    @property
    def mapping(self) -> 'CurveMapping': pass

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeHueSat(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeIDMask(CompositorNode):
    index: int
    use_antialiasing: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


# noinspection PyPropertyDefinition
class CompositorNodeImage(CompositorNode):
    frame_duration: int 
    frame_offset: int 
    frame_start: int 
    image: i.Image
    layer: Literal['PLACEHOLDER'] 
    use_auto_refresh: bool 
    use_cyclic: bool 
    use_straight_alpha_output: bool 
    view: Literal['ALL']

    @property
    def has_layers(self) -> bool: pass

    @property
    def has_views(self) -> bool: pass

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeInpaint(CompositorNode):
    distance: int

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeInvert(CompositorNode):
    invert_alpha: bool
    invert_rgb: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeKeying(CompositorNode):
    blur_post: int 
    blur_pre: int 
    clip_black: float 
    clip_white: float 
    despill_balance: float 
    despill_factor: float 
    dilate_distance: int 
    edge_kernel_radius: int 
    edge_kernel_tolerance: float 
    feather_distance: int 
    feather_falloff: p.ProportionalFalloffCurveOnly
    screen_balance: float 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeKeyingScreen(CompositorNode):
    clip: m.MovieClip
    smoothness: float
    tracking_object: str

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeKuwahara(CompositorNode):
    eccentricity: float 
    sharpness: float 
    uniformity: int 
    use_high_precision: bool
    variation: Literal['CLASSIC', 'ANISOTROPIC']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeLensdist(CompositorNode):
    use_fit: bool
    use_jitter: bool
    use_projector: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeLevels(CompositorNode):
    channel: Literal['COMBINED_RGB', 'RED', 'GREEN', 'BLUE', 'LUMINANCE'] 

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeLumaMatte(CompositorNode):
    limit_max: float
    limit_min: float

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMapRange(CompositorNode):
    use_clamp: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMapUV(CompositorNode):
    alpha: int
    filter_type: Literal['NEAREST', 'ANISOTROPIC']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMapValue(CompositorNode):
    max: tuple[float]
    min: tuple[float]
    offset: tuple[float]
    size: tuple[float]
    use_max: bool
    use_min: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMask(CompositorNode):
    mask: m.Mask
    motion_blur_samples: int 
    motion_blur_shutter: float 
    size_source: Literal['SCENE', 'FIXED', 'FIXED_SCENE']
    size_x: int 
    size_y: int 
    use_feather: bool
    use_motion_blur: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMath(CompositorNode):
    operation: n.NodeMath
    use_clamp: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMixRGB(CompositorNode):
    blend_type: r.RampBlend
    use_alpha: bool
    use_clamp: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMovieClip(CompositorNode):
    clip: m.MovieClip

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeMovieDistortion(CompositorNode):
    clip: m.MovieClip
    distortion_type: Literal['UNDISTORT', 'DISTORT']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeNormal(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeNormalize(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


# noinspection PyPropertyDefinition
class CompositorNodeOutputFile(CompositorNode):
    active_input_index: int 
    base_path: str 
    
    @property
    def file_slots(self) -> 'CompositorNodeOutputFileFileSlots': pass
    
    @property
    def format(self) -> i.ImageFormatSettings: pass
    
    @property
    def layer_slots(self) -> 'CompositorNodeOutputFileLayerSlots': pass

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeOutputFileFileSlots(bpy_prop_collection[n.NodeSocket]):
    def new(self, name: str) -> n.NodeSocket: pass
    def remove(self, socket: n.NodeSocket) -> None: pass
    def clear(self) -> None: pass
    def move(self, from_index: int, to_index: int) -> None: pass


class CompositorNodeOutputFileLayerSlots(bpy_prop_collection[n.NodeSocket]):
    def new(self, name: str) -> n.NodeSocket: pass
    def remove(self, socket: n.NodeSocket) -> None: pass
    def clear(self) -> None: pass
    def move(self, from_index: int, to_index: int) -> None: pass


class CompositorNodePixelate(CompositorNode):
    pixel_size: int

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodePlaneTrackDeform(CompositorNode):
    clip: m.MovieClip
    motion_blur_samples: int 
    motion_blur_shutter: float 
    plane_track_name: str
    tracking_object: str
    use_motion_blur: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodePosterize(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodePremulKey(CompositorNode):
    mapping: Literal['STRAIGHT_TO_PREMUL', 'PREMUL_TO_STRAIGHT']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeRGB(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeRGBToBW(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeRLayers(CompositorNode):
    layer: Literal['PLACEHOLDER']
    scene: s.Scene

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeRotate(CompositorNode):
    filter_Type: Literal['NEAREST', 'BILINEAR', 'BICUBIC']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeScale(CompositorNode):
    frame_method: Literal['STRETCH', 'FIT', 'CROP']
    offset_x: float 
    offset_y: float 
    space: Literal['RELATIVE', 'ABSOLUTE', 'SCENE_SIZE', 'RENDER_SIZE']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSceneTime(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSepHSVA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSepRGBA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSepYCCA(CompositorNode):
    mode: Literal['ITUBT601', 'ITUBT709', 'JFIF']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSepYUVA(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSeparateColor(CompositorNode):
    mode: Literal['RGB', 'HSV', 'HSL', 'YCC', 'YUV']
    ycc_mode: Literal['ITUBT601', 'ITUBT709', 'JFIF']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSeparateXYZ(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSetAlpha(CompositorNode):
    mode: Literal['APPLY', 'REPLACE_ALPHA']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSplit(CompositorNode):
    axis: a.AxisXy
    factor: int

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeStabilize(CompositorNode):
    clip: m.MovieClip
    filter_type: Literal['NEAREST', 'BILINEAR', 'BICUBIC']
    invert: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSunBeams(CompositorNode):
    ray_length: float
    source: tuple[float, float]

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSwitch(CompositorNode):
    check: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeSwitchView(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTexture(CompositorNode):
    node_output: int
    texture: t.Texture

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTime(CompositorNode):
    curve: 'CurveMapping'
    frame_end: int
    frame_start: int

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTonemap(CompositorNode):
    adaptation: float 
    contrast: float 
    correction: float 
    gamma: float 
    intensity: float 
    key: float 
    offset: float 
    tonemap_type: Literal['RD_PHOTORECEPTOR', 'RH_SIMPLE']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTrackPos(CompositorNode):
    clip: m.MovieClip
    frame_relative: int 
    position: Literal['ABSOLUTE', 'RELATIVE_START', 'RELATIVE_FRAME', 'ABSOLUTE_FRAME']
    track_name: str
    tracking_object: str

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTransform(CompositorNode):
    filter_type: Literal['NEAREST', 'BILINEAR', 'BICUBIC']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTranslate(CompositorNode):
    use_relative: bool
    wrap_axis: Literal['NONE', 'XAXIS', 'YAXIS', 'BOTH']

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeTree(n.NodeTree):
    chunk_size: Literal['32', '64', '128', '256', '512', '1024']
    edit_quality: Literal['HIGH', 'MEDIUM', 'LOW']
    execution_mode: Literal['TILED', 'FULL_FRAME', 'REALTIME']
    precision: Literal['AUTO', 'FULL']
    render_quality: Literal['HIGH', 'MEDIUM', 'LOW']
    use_groupnode_buffer: bool
    use_opencl: bool
    use_two_pass: bool
    use_viewer_border: bool


class CompositorNodeValToRGB(CompositorNode):
    color: ColorRamp

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeValue(CompositorNode):
    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeVecBlur(CompositorNode):
    factor: float 
    samples: int 
    speed_max: int 
    speed_min: int 
    use_curved: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeViewer(CompositorNode):
    center_x: float 
    center_y: float 
    tile_order: Literal['CENTEROUT', 'RANDOM', 'BOTTOMUP', 'RULE_OF_THIRDS']
    use_alpha: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class CompositorNodeZcombine(CompositorNode):
    use_alpha: bool
    use_antialias_z: bool

    @classmethod
    def is_registered_node_type(cls) -> bool: pass

    @classmethod
    def input_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass

    @classmethod
    def output_template(cls, index: int) -> n.NodeInternalSocketTemplate: pass


class ConsoleLine(bpy_struct):
    body: str
    current_character: int
    type: Literal['OUTPUT', 'INPUT', 'INFO', 'ERROR']


# noinspection PyPropertyDefinition
class Constraint(bpy_struct):
    active: bool
    enabled: bool
    influence: float
    mute: bool
    name: str 
    owner_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL'] 
    show_expanded: bool
    space_object: o.Object
    space_subtarget: str
    target_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']

    @property
    def error_location(self) -> float: pass

    @property
    def error_rotation(self) -> float: pass

    @property
    def is_override_data(self) -> bool: pass

    @property
    def is_valid(self) -> bool: pass

    @property
    def type(self) -> ConstraintType: pass


class ConstraintTarget(bpy_struct):
    subtarget: str
    target: o.Object


class ConstraintTargetBone(bpy_struct):
    subtarget: str
    target: o.Object
    weight: float


# noinspection PyPropertyDefinition
class Context(Protocol, bpy_struct):
    @property
    def area(self) -> a.Area: pass
    
    @property
    def asset(self) -> a.AssetRepresentation: pass
    
    @property
    def blend_data(self) -> b.BlendData: pass
    
    @property
    def collection(self) -> Collection: pass
    
    @property
    def engine(self) -> str: pass
    
    @property
    def gizmo_group(self) -> g.GizmoGroup: pass
    
    @property
    def layer_collection(self) -> l.LayerCollection: pass
    
    @property
    def mode(self) -> 'ContextMode': pass
    
    @property
    def preferences(self) -> p.Preferences: pass
    
    @property
    def region(self) -> r.Region: pass
    
    @property
    def region_data(self) -> r.RegionView3D: pass
    
    @property
    def scene(self) -> s.Scene: pass
    
    @property
    def screen(self) -> s.Screen: pass
    
    @property
    def space_data(self) -> s.Space: pass
    
    @property
    def tool_settings(self) -> t.ToolSettings: pass
    
    @property
    def view_layer(self) -> v.ViewLayer: pass
    
    @property
    def window(self) -> w.Window: pass
    
    @property
    def window_manager(self) -> w.WindowManager: pass
    
    @property
    def workspace(self) -> w.WorkSpace: pass

    def evaluated_depsgraph_get(self) -> d.Depsgraph: pass

    def copy(self) -> 'Context': pass

    def temp_override(self, **kwargs) -> ContextManager:
        """
        Context manager to temporarily override members in the context.

        Keyword Args:
            window (w.Window | None): Window override or None.
            screen (s.Screen | None): Screen override or None.
            area (a.Area | None): Area override or None.
            region (r.Region | None): Region override or None.

        Args:
            **kwargs: Additional keywords override context members.

        Returns:
            (ContextTempOverride): Temporarily overridden context manager.
        """


class CopyLocationConstraint(Constraint):
    head_tail: float 
    invert_x: bool
    invert_y: bool
    invert_z: bool
    subtarget: str
    target: o.Object
    use_bbone_shape: bool
    use_offset: bool
    use_x: bool
    use_y: bool
    use_z: bool


class CopyRotationConstraint(Constraint):
    euler_order: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
    invert_x: bool
    invert_y: bool
    invert_z: bool
    mix_mode: Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER', 'OFFSET']
    subtarget: str
    target: o.Object
    use_offset: bool
    use_x: bool
    use_y: bool
    use_z: bool


class CopyScaleConstraint(Constraint):
    power: float 
    subtarget: str
    target: o.Object
    use_add: bool
    use_make_uniform: bool
    use_offset: bool
    use_x: bool
    use_y: bool
    use_z: bool


class CopyTransformsConstraint(Constraint):
    head_tail: float 
    mix_mode: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']
    remove_target_shear: bool
    subtarget: str
    target: o.Object
    use_bbone_shape: bool


# noinspection PyPropertyDefinition
class CorrectiveSmoothModifier(m.Modifier):
    factor: float 
    invert_vertex_group: bool
    iterations: int
    rest_source: Literal['ORCO', 'BIND']
    scale: float 
    smooth_type: Literal['SIMPLE', 'LENGTH_WEIGHTED']
    use_only_smooth: bool
    use_pin_boundary: bool
    vertex_group: str

    @property
    def is_bind(self) -> bool: pass


# noinspection PyPropertyDefinition
class CrossSequence(e.EffectSequence):
    input_1: s.Sequence
    input_2: s.Sequence

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class CryptomatteEntry(bpy_struct):
    @property
    def encoded_hash(self) -> float: pass
    
    @property
    def name(self) -> str: pass


# noinspection PyPropertyDefinition
class Curve(i.ID):
    bevel_depth: float
    bevel_factor_end: float 
    bevel_factor_mapping_end: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE'] 
    bevel_factor_mapping_start: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE'] 
    bevel_factor_start: float 
    bevel_mode: Literal['ROUND', 'OBJECT', 'PROFILE'] 
    bevel_object: o.Object
    bevel_resolution: int
    dimensions: Literal['2D', '3D']
    eval_time: float 
    extrude: float 
    fill_mode: Literal['FULL', 'BACK', 'FRONT', 'HALF'] 
    offset: float
    path_duration: int 
    render_resolution_u: int 
    render_resolution_v: int 
    resolution_u: int 
    resolution_v: int
    taper_object: o.Object
    taper_radius_mode: Literal['OVERRIDE', 'MULTIPLY', 'ADD'] 
    texspace_location: Vector 
    texspace_size: Vector 
    twist_mode: Literal['Z_UP', 'MINIMUM', 'TANGENT'] 
    twist_smooth: float 
    use_auto_texspace: bool 
    use_deform_bounds: bool 
    use_fill_caps: bool 
    use_map_taper: bool 
    use_path: bool 
    use_path_clamp: bool 
    use_path_follow: bool 
    use_radius: bool 
    use_stretch: bool

    @property
    def animation_data(self) -> a.AnimData: pass

    @property
    def bevel_profile(self) -> 'CurveProfile': pass

    @property
    def cycles(self) -> 'CyclesMeshSettings': pass

    @property
    def is_editmode(self) -> bool: pass

    @property
    def materials(self) -> i.IDMaterials: pass

    @property
    def shape_keys(self) -> k.Key: pass

    @property
    def splines(self) -> 'CurveSplines': pass

    def transform(self, matrix: Matrix, shape_keys: bool = False): pass

    def validate_material_indices(self) -> bool: pass

    # TODO: what is this?
    def update_gpu_tag(self): pass


class CurveMap(bpy_struct):
    points: 'CurveMapPoints'


class CurveMapPoint(bpy_struct):
    handle_type: Literal['AUTO', 'AUTO_CLAMPED', 'VECTOR']
    location: Vector
    select: bool


class CurveMapPoints(bpy_prop_collection[CurveMapPoint]):
    def new(self, position: float, value: float) -> CurveMapPoint: pass
    def remove(self, point: CurveMapPoint) -> None: pass


# noinspection PyPropertyDefinition
class CurveMapping(bpy_struct):
    black_level: Color 
    clip_max_x: float 
    clip_max_y: float 
    clip_min_x: float 
    clip_min_y: float 
    extend: Literal['HORIZONTAL', 'EXTRAPOLATED']
    tone: Literal['STANDARD', 'FILMLIKE'] 
    use_clip: bool
    white_level: Color

    @property
    def curves(self) -> bpy_prop_collection[CurveMap]: pass

    def update(self) -> None: pass

    def reset_view(self) -> None: pass

    def initialize(self) -> None: pass

    def evaluate(self, curve: CurveMap, position: float) -> float: pass


class CurveModifier(m.Modifier):
    deform_axis: Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']
    invert_vertex_group: bool
    object: o.Object
    vertex_group: str


class CurvePaintSettings(bpy_struct):
    corner_angle: float 
    curve_type: Literal['POLY', 'BEZIER']
    depth_mode: Literal['CURSOR', 'SURFACE']
    error_threshold: int 
    fit_method: CurveFitMethod
    radius_max: float 
    radius_min: float 
    radius_taper_end: float 
    radius_taper_start: float 
    surface_offset: float 
    surface_plane: Literal['NORMAL_VIEW', 'NORMAL_SURFACE', 'VIEW']
    use_corners_detect: bool
    use_offset_absolute: bool
    use_pressure_radius: bool
    use_stroke_endpoints: bool


# noinspection PyPropertyDefinition
class CurvePoint(bpy_struct):
    position: Vector
    radius: float 

    @property
    def index(self) -> int: pass


class CurveProfile(bpy_struct):
    preset: Literal['LINE', 'SUPPORTS', 'CORNICE', 'CROWN', 'STEPS'] 
    use_clip: bool
    use_sample_even_lengths: bool
    use_sample_straight_edges: bool

    @property
    def points(self) -> 'CurveProfilePoints': pass

    @property
    def segments(self) -> bpy_prop_collection['CurveProfilePoint']: pass

    def update(self) -> None: pass

    def reset_view(self) -> None: pass

    def initialize(self, totsegments: int) -> None: pass

    def evaluate(self, length_portion: float) -> Vector: pass


class CurveProfilePoint(bpy_struct):
    handle_type_1: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
    handle_type_2: Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
    location: Vector
    select: bool


class CurveProfilePoints(bpy_prop_collection[CurveProfilePoint]):
    def add(self, x: float, y: float) -> CurveProfilePoint: pass
    def remove(self, point: CurveProfilePoint) -> None: pass


# noinspection PyPropertyDefinition
class CurveSlice(bpy_struct):
    @property
    def first_point_index(self) -> int: pass
    
    @property
    def index(self) -> int: pass
    
    @property
    def points(self) -> bpy_prop_collection[CurvePoint]: pass
    
    @property
    def points_length(self) -> int: pass


class CurveSplines(bpy_prop_collection[s.Spline]):
    active: s.Spline

    # noinspection PyShadowingBuiltins
    def new(self, type: Literal['POLY', 'BEZIER', 'NURBS']) -> s.Spline: pass

    def remove(self, spline: s.Spline) -> None: pass

    def clear(self) -> None: pass


# noinspection PyPropertyDefinition
class Curves(i.ID):
    selection_domain: a.AttributeCurvesDomain
    surface: o.Object
    surface_uv_map: str
    use_mirror_x: bool
    use_mirror_y: bool
    use_mirror_z: bool

    @property
    def animation_data(self) -> a.AnimData: pass

    @property
    def attributes(self) -> a.AttributeGroup: pass

    @property
    def color_attributes(self) -> a.AttributeGroup: pass

    @property
    def curve_offset_data(self) -> bpy_prop_collection[i.IntAttributeValue]: pass

    @property
    def curves(self) -> bpy_prop_collection[CurveSlice]: pass

    @property
    def materials(self) -> i.IDMaterials: pass

    @property
    def normals(self) -> bpy_prop_collection[f.FloatVectorValueReadOnly]: pass

    @property
    def points(self) -> bpy_prop_collection[CurvePoint]: pass

    @property
    def position_data(self) -> bpy_prop_collection[f.FloatVectorAttributeValue]: pass


# noinspection PyPropertyDefinition
class CurvesModifier(s.SequenceModifier):
    @property
    def curve_mapping(self) -> CurveMapping: pass


class CurvesSculpt(p.Paint):
    pass


class CyclesRenderLayerSettings(p.PropertyGroup):  # Undocumented type.
    pass
