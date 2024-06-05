from typing import Literal
from base import bpy_struct, bpy_prop_collection
from mathutils import Color, Vector

from a import AxisXyz
from c import ChannelDriverVariables, Collection, ColorRamp, Constraint
from e import EffectorWeights 
from g import GpencilModifier
from i import ID, IdType
from m import Material, Modifier
from o import Object
from p import ParticleSystem, PointCache, PropDynamicpaintType
from s import Scene
from t import Texture
from u import UIList
from v import ViewLayer

DriverTargetRotationMode = Literal[
    'AUTO',
    'XYZ',
    'XZY',
    'YXZ',
    'YZX',
    'ZXY',
    'ZYX',
    'QUATERNION',
    'SWING_TWIST_X',
    'SWING_TWIST_Y',
    'SWING_TWIST_Z',
]

DtLayersSelectDst = Literal['ACTIVE', 'NAME', 'INDEX']

DtLayersSelectSrc = Literal['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM']

DtMethodEdge = Literal['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ']

DtMethodLoop = Literal[
    'TOPOLOGY',
    'NEAREST_NORMAL',
    'NEAREST_POLYNOR',
    'NEAREST_POLY',
    'POLYINTERP_NEAREST',
    'POLYINTERP_LNORPROJ',
]

DtMethodPoly = Literal['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ']

DtMethodVertex = Literal[
    'TOPOLOGY',
    'NEAREST',
    'EDGE_NEAREST',
    'EDGEINTERP_NEAREST',
    'POLY_NEAREST',
    'POLYINTERP_NEAREST',
    'POLYINTERP_VNORPROJ',
]

DtMixMode = Literal['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL']


# TODO: what is this?
class DATA_UL_bone_collections(UIList):
    def draw_item(self, _context, layout, armature, bcoll, _icon, _active_data, _active_propname, _index): pass


class DampedTrackConstraint(Constraint):
    head_tail: float
    subtarget: str
    target: Object
    track_axis: Literal['TRACK_X', 'TRACK_Y', 'TRACK_Z', 'TRACK_NEGATIVE_X', 'TRACK_NEGATIVE_Y', 'TRACK_NEGATIVE_Z']
    use_bbone_shape: bool


# noinspection PyPropertyDefinition
class DashGpencilModifierData(GpencilModifier):
    dash_offset: int
    invert_layer_pass: bool
    invert_layers: bool
    invert_material_pass: bool
    invert_materials: bool
    layer: str
    layer_pass: int
    material: Material
    pass_index: int
    segment_active_index: int

    @property
    def segments(self) -> bpy_prop_collection['DashGpencilModifierSegment']: pass


class DashGpencilModifierSegment(bpy_struct):
    dash: int
    gap: int
    material_index: int
    name: str
    opacity: float
    radius: float
    use_cyclic: bool


class DataTransferModifier(Modifier):
    ata_types_edges: set[Literal['SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE']]
    data_types_loops: set[Literal['CUSTOM_NORMAL', 'COLOR_CORNER', 'UV']]
    data_types_polys: set[Literal['SMOOTH', 'FREESTYLE_FACE']]
    data_types_verts: set[Literal['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'COLOR_VERTEX']]
    edge_mapping: DtMethodEdge
    invert_vertex_group: bool
    islands_precision: float
    layers_uv_select_dst: DtLayersSelectDst
    layers_uv_select_src: DtLayersSelectSrc
    layers_vcol_loop_select_dst: DtLayersSelectDst
    layers_vcol_loop_select_src: DtLayersSelectSrc
    layers_vcol_vert_select_dst: DtLayersSelectDst
    layers_vcol_vert_select_src: DtLayersSelectSrc
    layers_vgroup_select_dst: DtLayersSelectDst
    layers_vgroup_select_src: DtLayersSelectSrc
    loop_mapping: DtMethodLoop
    max_distance: float
    mix_factor: float
    mix_mode: DtMixMode
    object: Object
    poly_mapping: DtMethodPoly
    ray_radius: float
    use_edge_data: bool
    use_loop_data: bool
    use_max_distance: bool
    use_object_transform: bool
    use_poly_data: bool
    use_vert_data: bool
    vert_mapping: DtMethodVertex
    vertex_group: str


# noinspection PyPropertyDefinition
class DecimateModifier(Modifier):
    angle_limit: float 
    decimate_type: Literal['COLLAPSE', 'UNSUBDIV', 'DISSOLVE']
    invert_vertex_group: bool
    iterations: int 
    ratio: float 
    symmetry_axis: AxisXyz
    use_collapse_triangulate: bool
    use_dissolve_boundaries: bool
    use_symmetry: bool
    vertex_group: str
    vertex_group_factor: float

    @property
    def delimit(self) -> int: pass


# noinspection PyPropertyDefinition
class Depsgraph(bpy_struct):
    @property
    def ids(self) -> bpy_prop_collection[ID]: pass
    
    @property
    def mode(self) -> Literal['VIEWPORT', 'RENDER']: pass
    
    @property
    def object_instances(self) -> bpy_prop_collection['DepsgraphObjectInstance']: pass
    
    @property
    def objects(self) -> bpy_prop_collection[Object]: pass
    
    @property
    def scene(self) -> Scene: pass
    
    @property
    def scene_eval(self) -> Scene: pass
    
    @property
    def updates(self) -> bpy_prop_collection ['DepsgraphUpdate']: pass
    
    @property
    def view_layer(self) -> ViewLayer: pass
    
    @property
    def view_layer_eval(self) -> ViewLayer: pass

    # TODO: does this return something?
    def debug_relations_graphviz(self, filepath: str): pass

    # TODO: does this return something?
    def debug_stats_gnuplot(self, filepath: str, output_filepath: str): pass

    # TODO: does this return something?
    def debug_tag_update(self): pass

    def debug_stats(self) -> str: pass

    def update(self) -> None: pass

    # noinspection PyShadowingBuiltins
    def id_eval_get(self, id: ID) -> ID: pass

    def id_type_updated(self, id_type: IdType): pass


# noinspection PyPropertyDefinition
class DepsgraphObjectInstance(bpy_struct):
    @property
    def instance_object(self) -> Object: pass
    
    @property
    def is_instance(self) -> bool: pass
    
    @property
    def matrix_world(self) -> Object: pass
    
    @property
    def orco(self) -> Vector: pass
    
    @property
    def parent(self) -> Object: pass
    
    @property
    def particle_system(self) -> ParticleSystem: pass
    
    @property
    def persistent_id(self) -> tuple[int, int, int, int, int, int, int, int]: pass
    
    @property
    def random_id(self) -> int: pass
    
    @property
    def show_particles(self) -> bool: pass
    
    @property
    def show_self(self) -> bool: pass
    
    @property
    def uv(self) -> tuple[float, float]: pass


# noinspection PyPropertyDefinition
class DepsgraphUpdate(bpy_struct):
    @property
    def id(self) -> ID: pass
    
    @property
    def is_updated_geometry(self) -> bool: pass
    
    @property
    def is_updated_shading(self) -> bool: pass
    
    @property
    def is_updated_transform(self) -> bool: pass


class DisplaceModifier(Modifier):
    direction: Literal['X', 'Y', 'Z', 'NORMAL', 'CUSTOM_NORMAL', 'RGB_TO_XYZ']
    invert_vertex_group: bool
    mid_level: float 
    space: Literal['LOCAL', 'GLOBAL']
    strength: float 
    texture: Texture 
    texture_coords: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']
    texture_coords_bone: str
    texture_coords_object: Object 
    uv_layer: str
    vertex_group: str


class DisplaySafeAreas(bpy_struct):
    action: Vector
    action_center: Vector
    title: Vector
    title_center: Vector


# noinspection PyPropertyDefinition
class DistortedNoiseTexture(Texture):
    distortion: float 
    nabla: float 
    noise_basis: Literal[
        'BLENDER_ORIGINAL',
        'ORIGINAL_PERLIN',
        'IMPROVED_PERLIN',
        'VORONOI_F1',
        'VORONOI_F2',
        'VORONOI_F3',
        'VORONOI_F4',
        'VORONOI_F2_F1',
        'VORONOI_CRACKLE',
        'CELL_NOISE'
    ]
    noise_distortion: Literal[
        'BLENDER_ORIGINAL',
        'ORIGINAL_PERLIN',
        'IMPROVED_PERLIN',
        'VORONOI_F1',
        'VORONOI_F2',
        'VORONOI_F3',
        'VORONOI_F4',
        'VORONOI_F2_F1',
        'VORONOI_CRACKLE',
        'CELL_NOISE'
    ]
    noise_scale: float 

    # TODO: what does this return?
    @property
    def users_material(self): pass

    @property
    def users_object_modifier(self): pass


# noinspection PyPropertyDefinition
class DopeSheet(bpy_struct):
    filter_collection: Collection 
    filter_fcurve_name: str 
    filter_text: str 
    show_armatures: bool 
    show_cache_files: bool 
    show_cameras: bool 
    show_curves: bool 
    show_datablock_filters: bool 
    show_driver_fallback_as_error: bool 
    show_expanded_summary: bool 
    show_gpencil: bool 
    show_hair_curves: bool 
    show_hidden: bool 
    show_lattices: bool 
    show_lights: bool 
    show_linestyles: bool 
    show_materials: bool 
    show_meshes: bool 
    show_metaballs: bool 
    show_missing_nla: bool 
    show_modifiers: bool 
    show_movieclips: bool 
    show_nodes: bool 
    show_only_errors: bool 
    show_only_selected: bool 
    show_particles: bool 
    show_pointclouds: bool 
    show_scenes: bool 
    show_shapekeys: bool 
    show_speakers: bool 
    show_summary: bool 
    show_textures: bool 
    show_transforms: bool 
    show_volumes: bool 
    show_worlds: bool 
    use_datablock_sort: bool
    use_filter_invert: bool 
    use_multi_word_filter: bool

    @property
    def source(self) -> ID: pass


# noinspection PyPropertyDefinition
class Driver(bpy_struct):
    expression: str 
    is_valid: bool 
    type: Literal['AVERAGE', 'SUM', 'SCRIPTED', 'MIN', 'MAX'] 
    use_self: bool 
    
    @property
    def is_simple_expression(self) -> bool: pass
    
    @property
    def variables(self) -> ChannelDriverVariables: pass


# noinspection PyPropertyDefinition
class DriverTarget(bpy_struct):
    bone_target: str 
    context_property: Literal['ACTIVE_SCENE', 'ACTIVE_VIEW_LAYER'] 
    data_path: str 
    fallback_value: float 
    id: ID 
    id_type: IdType 
    rotation_mode: DriverTargetRotationMode
    transform_space: Literal['WORLD_SPACE', 'TRANSFORM_SPACE', 'LOCAL_SPACE'] 
    transform_type: Literal[
        'LOC_X',
        'LOC_Y',
        'LOC_Z',
        'ROT_X',
        'ROT_Y',
        'ROT_Z',
        'ROT_W',
        'SCALE_X',
        'SCALE_Y',
        'SCALE_Z',
        'SCALE_AVG'
    ] 
    use_fallback_value: bool

    @property
    def is_fallback_used(self) -> bool: pass


# noinspection PyPropertyDefinition
class DriverVariable(bpy_struct):
    name: str
    type: Literal['SINGLE_PROP', 'TRANSFORMS', 'ROTATION_DIFF', 'LOC_DIFF', 'CONTEXT_PROP'] 
    
    @property
    def is_name_valid(self) -> bool: pass
    
    @property
    def targets(self) -> bpy_prop_collection[DriverTarget]: pass


# noinspection PyPropertyDefinition
class DynamicPaintBrushSettings(bpy_struct):
    invert_proximity: bool 
    paint_alpha: float 
    paint_color: Color 
    paint_distance: float 
    paint_source: Literal['PARTICLE_SYSTEM', 'POINT', 'DISTANCE', 'VOLUME_DISTANCE', 'VOLUME'] 
    paint_wetness: float 
    particle_system: ParticleSystem 
    proximity_falloff: Literal['SMOOTH', 'CONSTANT', 'RAMP'] 
    ray_direction: Literal['CANVAS', 'BRUSH', 'Z_AXIS'] 
    smooth_radius: float 
    smudge_strength: float 
    solid_radius: float 
    use_absolute_alpha: bool 
    use_negative_volume: bool 
    use_paint_erase: bool 
    use_particle_radius: bool 
    use_proximity_project: bool 
    use_proximity_ramp_alpha: bool 
    use_smudge: bool 
    use_velocity_alpha: bool 
    use_velocity_color: bool 
    use_velocity_depth: bool 
    velocity_max: float 
    wave_clamp: float 
    wave_factor: float 
    wave_type: Literal['CHANGE', 'DEPTH', 'FORCE', 'REFLECT'] 
    
    @property
    def paint_ramp(self) -> ColorRamp: pass
    
    @property
    def velocity_ramp(self) -> ColorRamp: pass


# noinspection PyPropertyDefinition
class DynamicPaintCanvasSettings(bpy_struct):
    @property
    def canvas_surfaces(self) -> 'DynamicPaintSurfaces': pass


# noinspection PyPropertyDefinition
class DynamicPaintModifier(Modifier):
    ui_type: PropDynamicpaintType
    
    @property
    def brush_settings(self) -> DynamicPaintBrushSettings: pass
    
    @property
    def canvas_settings(self) -> DynamicPaintCanvasSettings: pass


# noinspection PyPropertyDefinition
class DynamicPaintSurface(bpy_struct):
    brush_collection: Collection 
    brush_influence_scale: float 
    brush_radius_scale: float 
    color_dry_threshold: float 
    color_spread_speed: float 
    depth_clamp: float 
    displace_factor: float 
    displace_type: Literal['DISPLACE', 'DEPTH'] 
    dissolve_speed: int 
    drip_acceleration: float 
    drip_velocity: float 
    dry_speed: int 
    effect_ui: Literal['SPREAD', 'DRIP', 'SHRINK'] 
    frame_end: int 
    frame_start: int 
    frame_substeps: int 
    image_fileformat: Literal['PNG', 'OPENEXR'] 
    image_output_path: str 
    image_resolution: int 
    init_color: tuple[float, float, float, float] 
    init_color_type: Literal['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR'] 
    init_layername: str 
    init_texture: Texture 
    is_active: bool 
    name: str 
    output_name_a: str 
    output_name_b: str 
    shrink_speed: float 
    spread_speed: float 
    surface_format: Literal['VERTEX', 'IMAGE'] 
    surface_type: Literal['PAINT'] 
    use_antialiasing: bool 
    use_dissolve: bool 
    use_dissolve_log: bool 
    use_drip: bool 
    use_dry_log: bool 
    use_drying: bool 
    use_incremental_displace: bool 
    use_output_a: bool 
    use_output_b: bool 
    use_premultiply: bool 
    use_shrink: bool 
    use_spread: bool 
    use_wave_open_border: bool 
    uv_layer: str 
    wave_damping: float 
    wave_smoothness: float 
    wave_speed: float 
    wave_spring: float 
    wave_timescale: float 
    
    @property
    def effector_weights(self) -> EffectorWeights: pass
    
    @property
    def is_cache_user(self) -> bool: pass
    
    @property
    def point_cache(self) -> PointCache: pass

    # TODO: what type is "object"?
    # noinspection PyShadowingBuiltins
    def output_exists(self, object, index: int) -> bool: pass


# noinspection PyPropertyDefinition
class DynamicPaintSurfaces(bpy_prop_collection[DynamicPaintSurface]):
    active_index: int

    @property
    def active(self) -> DynamicPaintSurface: pass


