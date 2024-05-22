from base import bpy_struct, bpy_prop_collection
from typing import Literal

import mathutils as mathutils

import b
import c
import e
import f
import g
import i
import l
import m
import o
import p
import r
import s
import t
import u


AttributeCurvesDomain = Literal['POINT', 'CURVE']

AttributeDomain = Literal[
    'POINT',
    'EDGE',
    'FACE',
    'CORNER',
    'CURVE',
    'INSTANCE',
    'LAYER',
]

AttributeType = Literal[
    'FLOAT',
    'INT',
    'FLOAT_VECTOR',
    'FLOAT_COLOR',
    'BYTE_COLOR',
    'STRING',
    'BOOLEAN',
    'FLOAT2',
    'INT8',
    'INT32_2D',
    'QUATERNION',
]

AxisXy = Literal['X', 'Y']

AxisXyz = Literal['X', 'Y', 'Z']


class AOV(bpy_struct):
    is_valid: bool
    name: str
    type: Literal['COLOR', 'VALUE']


class AOVs(bpy_prop_collection[AOV]):
    def add(self) -> AOV: pass
    def remove(self, aov: AOV) -> None: pass


class ASSETBROWSER_UL_metadata_tags(u.UIList):
    # TODO: what even is this.
    def draw_item(
        self,
        _context,
        layout,
        _data,
        item,
        icon,
        _active_data,
        _active_propname,
        _index,
    ): pass


# noinspection PyPropertyDefinition
class Action(i.ID):
    frame_end: float
    frame_range: mathutils.Vector
    frame_start: float
    id_root: i.IdType
    use_cyclic: bool
    use_frame_range: bool

    @property
    def curve_frame_range(self) -> mathutils.Vector: pass

    @property
    def fcurves(self) -> 'ActionFCurves': pass

    @property
    def groups(self) -> 'ActionGroups': pass

    @property
    def pose_markers(self) -> 'ActionPoseMarkers': pass

    # noinspection PyShadowingBuiltins
    def flip_with_pose(self, object: o.Object) -> None: pass


class ActionConstraint(c.Constraint):
    action: Action
    eval_time: float
    frame_end: int
    frame_start: int
    max: float
    min: float
    mix_mode: Literal['BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']
    subtarget: str
    target: o.Object
    transform_channel: Literal['LOCATION_X', 'LOCATION_Y', 'LOCATION_Z', 'ROTATION_X', 'ROTATION_Y', 'ROTATION_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z']
    use_bone_object_action: bool
    use_eval_time: bool


class ActionFCurves(bpy_prop_collection[f.FCurve]):
    def new(self, data_path: str, index: int = 0, action_group: str = '') -> f.FCurve: pass
    def find(self, data_path: str, index: int = 0) -> f.FCurve | None: pass
    def remove(self, fcurve: f.FCurve) -> None: pass
    def clear(self) -> None: pass


# noinspection PyPropertyDefinition
class ActionGroup(bpy_struct):
    color_set: c.ColorSets
    lock: bool
    mute: bool
    name: str
    select: bool
    show_expanded: bool
    show_expanded_graph: bool
    use_pin: bool

    @property
    def channels(self) -> bpy_prop_collection[f.FCurve]: pass

    @property
    def colors(self) -> t.ThemeBoneColorSet: pass

    @property
    def is_custom_color_set(self) -> bool: pass


class ActionPoseMarkers(bpy_struct):
    active: t.TimelineMarker
    active_index: int

    def name(self, name: str) -> t.TimelineMarker: pass
    def remove(self, marker: t.TimelineMarker) -> None: pass


# noinspection PyPropertyDefinition
class AddSequence(e.EffectSequnce):
    input_1: s.Sequence
    input_2: s.Sequence

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class Addon(bpy_struct):
    module: str

    @property
    def preferences(self) -> 'AddonPreferences': pass


class AddonPreferences(bpy_struct):
    bl_idname: str


class Addons(bpy_prop_collection[Addon]):
    @classmethod
    def new(cls) -> Addon: pass

    @classmethod
    def remove(cls, addon: Addon) -> None: pass


# noinspection PyPropertyDefinition
class AdjustmentSequence(e.EffectSequence):
    animation_offset_end: int
    animation_offset_start: int

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class AlphaOverSequence(e.EffectSequence):
    input_1: s.Sequence
    input_2: s.Sequence

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class AlphaUnderSequence(e.EffectSequence):
    input_1: s.Sequence
    input_2: s.Sequence

    @property
    def input_count(self) -> int: pass


# noinspection PyPropertyDefinition
class AnimData(bpy_struct):
    action: Action
    action_blend_type: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']
    action_extrapolation: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']
    action_influence: float
    action_tweak_storage: Action
    use_nla: bool
    use_pin: bool
    use_tweak_mode: bool

    @property
    def drivers(self) -> 'AnimDataDrivers': pass

    @property
    def nla_tracks(self) -> 'NlaTracks': pass

    def nla_tweak_strip_time_to_scene(self, frame: float, invert: bool = False) -> float: pass


class AnimDataDrivers(bpy_prop_collection[f.FCurve]):
    def new(self, data_path: str, index: int = 0) -> f.FCurve: pass
    def remove(self, driver: f.FCurve) -> None: pass
    def from_existing(self, src_driver: f.FCurve | None = None) -> f.FCurve: pass
    def find(self, data_path: str, index: int = 0) -> f.FCurve | None: pass


class AnimViz(bpy_struct):
    @property
    def motion_path(self) -> 'AnimVizMotionPaths': pass


# noinspection PyPropertyDefinition
class AnimVizMotionPaths(bpy_struct):
    bake_in_camera_space: bool
    bake_location: m.MotionpathBakeLocation
    frame_after: int
    frame_before: int
    frame_end: int
    frame_start: int
    frame_step: int
    range: m.MotionpathRange
    show_frame_numbers: bool
    show_keyframe_action_all: bool
    show_keyframe_highlight: bool
    show_keyframe_numbers: bool
    type: m.MotionpathDisplayType

    @property
    def has_motion_paths(self) -> bool: pass


AnyType = bpy_struct


# noinspection PyPropertyDefinition
class Area(bpy_struct):
    show_menus: bool
    type: s.SpaceType
    ui_type: Literal['']

    @property
    def height(self) -> int: pass

    @property
    def regions(self) -> bpy_prop_collection[r.Region]: pass

    @property
    def spaces(self) -> 'AreaSpaces': pass

    @property
    def width(self) -> int: pass

    @property
    def x(self) -> int: pass

    @property
    def y(self) -> int: pass


class AreaLight(l.Light):
    contact_shadow_bias: float
    contact_shadow_distance: float
    contact_shadow_thickness: float
    energy: float
    shadow_buffer_bias: float
    shadow_buffer_clip_start: float
    shadow_color: mathutils.Color
    shadow_soft_size: float
    shadow_softness_factor: float
    shape: Literal['SQUARE', 'RECTANGLE', 'DISK', 'ELLIPSE']
    size: float
    size_y: float
    spread: float
    use_contact_shadow: bool
    use_shadow: bool


# noinspection PyPropertyDefinition
class AreaSpaces(bpy_prop_collection[s.Space]):
    @property
    def active(self) -> s.Space: pass


# noinspection PyPropertyDefinition
class Armature(i.ID):
    axes_position: float
    collections: b.BoneCollections
    display_type: Literal['OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']
    is_editmode: bool
    pose_position: Literal['POSE', 'REST']
    relation_line_position: Literal['TAIL', 'HEAD']
    show_axes: bool
    show_bone_colors: bool
    show_bone_custom_shapes: bool
    show_names: bool
    use_mirror_x: bool

    @property
    def animation_data(self) -> AnimData: pass

    @property
    def bones(self) -> 'ArmatureBones': pass

    @property
    def collections_all(self) -> bpy_prop_collection[b.BoneCollection]: pass

    @property
    def edit_bones(self) -> 'ArmatureEditBones': pass

    def transform(self, matrix: mathutils.Matrix) -> None: pass


class ArmatureBones(bpy_prop_collection[b.Bone]):
    active: b.Bone


# noinspection PyPropertyDefinition
class ArmatureConstraint(c.Constraint):
    use_bone_envelopes: bool
    use_current_location: bool
    use_deform_preserve_volume: bool

    @property
    def targets(self) -> 'ArmatureConstraintTargets': pass


class ArmatureConstraintTargets(bpy_prop_collection[c.ConstraintTargetBone]):
    def new(self) -> c.ConstraintTargetBone: pass
    def remove(self, target: c.ConstraintTargetBone) -> None: pass
    def clear(self) -> None: pass


class ArmatureEditBones(bpy_prop_collection[e.EditBone]):
    active: e.EditBone

    def new(self, name: str) -> e.EditBone: pass
    def remove(self, bone: e.EditBone) -> None: pass


class ArmatureGpencilModifier(g.GpencilModifier):
    invert_vertex_group: bool
    object: o.Object
    use_bone_envelopes: bool
    use_deform_preserve_volume: bool
    use_vertex_groups: bool
    vertex_group: str


class ArmatureModifier(m.Modifier):
    invert_vertex_group: bool
    object: o.Object
    use_bone_envelopes: bool
    use_deform_preserve_volume: bool
    use_multi_modifier: bool
    use_vertex_groups: bool
    vertex_group: str


class ArrayGpencilModifier(g.GpencilModifier):
    constant_offset: mathutils.Vector 
    count: int 
    invert_layer_pass: bool
    invert_layers: bool
    invert_material_pass: bool
    invert_materials: bool
    layer: str
    layer_pass: int 
    material: m.Material
    offset_object: o.Object
    pass_index: int 
    random_offset: mathutils.Vector 
    random_rotation: mathutils.Euler
    random_scale: mathutils.Vector 
    relative_offset: mathutils.Vector 
    replace_material: int 
    seed: int 
    use_constant_offset: bool
    use_object_offset: bool
    use_relative_offset: bool
    use_uniform_random_scale: bool


class ArrayModifier(m.Modifier):
    constant_offset_displace: mathutils.Vector 
    count: int 
    curve: o.Object
    end_cap: o.Object
    fit_length: float 
    fit_type: Literal['FIXED_COUNT', 'FIT_LENGTH', 'FIT_CURVE']
    merge_threshold: float 
    offset_object: o.Object
    offset_u: float 
    offset_v: float 
    relative_offset_displace: mathutils.Vector 
    start_cap: o.Object
    use_constant_offset: bool
    use_merge_vertices: bool
    use_merge_vertices_cap: bool
    use_object_offset: bool
    use_relative_offset: bool


class AssetCatalogPath(bpy_struct):
    pass


class AssetHandle(p.PropertyGroup):
    file_data: f.FileSelectEntry


class AssetLibraryCollection(bpy_prop_collection[u.UserAssetLibrary]):
    @classmethod
    def new(cls, name: str = '', directory: str = '') -> u.UserAssetLibrary: pass

    @classmethod
    def remove(cls, library: u.UserAssetLibrary) -> None: pass


class AssetLibraryReference(bpy_struct):
    pass


# noinspection PyPropertyDefinition
class AssetMetaData(bpy_struct):
    active_tag: int
    author: str
    catalog_id: str
    copyright: str
    description: str
    license: str

    @property
    def catalog_simple_name(self) -> str: pass

    @property
    def tags(self) -> 'AssetTags': pass


# noinspection PyPropertyDefinition
class AssetRepresentation(bpy_struct):
    @property
    def full_library_path(self) -> str: pass
    
    @property
    def full_path(self) -> str: pass
    
    @property
    def id_type(self) -> i.IdType: pass
    
    @property
    def local_id(self) -> i.ID: pass
    
    @property
    def metadata(self) -> AssetMetaData: pass
    
    @property
    def name(self) -> str: pass


class AssetShelf(bpy_struct):
    asset_library_reference: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']
    bl_idname: s.SpaceType
    preview_size: int
    search_filter: bool

    @classmethod
    def poll(cls, context: s.ScreenContext) -> bool: pass

    @classmethod
    def asset_poll(cls, asset: AssetRepresentation) -> bool: pass

    @classmethod
    def draw_context_menu(cls, context: s.ScreenContext, asset: AssetRepresentation, layout: u.UILayout) -> None: pass


class AssetTag(bpy_struct):
    name: str


class AssetTags(bpy_prop_collection[AssetTag]):
    def new(self, name: str, skip_if_exists: bool = False) -> AssetTag: pass
    def remove(self, tag: AssetTag) -> None: pass


# noinspection PyPropertyDefinition
class AssetWeakReference(bpy_struct):
    @property
    def asset_library_identifier(self) -> str: pass
    
    @property
    def asset_library_type(self) -> Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']: pass
    
    @property
    def relative_asset_identifier(self) -> str: pass


# noinspection PyPropertyDefinition
class Attribute(bpy_struct):
    name: str
    
    @property
    def data_type(self) -> AttributeType: pass
    
    @property
    def domain(self) -> AttributeDomain: pass
    
    @property
    def is_internal(self) -> bool: pass
    
    @property
    def is_required(self) -> bool: pass


class AttributeGroup(bpy_prop_collection[Attribute]):
    active: Attribute 
    active_color: Attribute 
    active_color_index: int 
    active_color_name: str
    active_index: int 
    default_color_name: str
    render_color_index: int

    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: AttributeType, domain: AttributeDomain) -> Attribute: pass

    def remove(self, attribute: Attribute) -> None: pass
