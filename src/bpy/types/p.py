from typing import Literal

from base import bpy_prop_collection, bpy_struct

from a import Action, Addons, AnimViz, AssetLibraryCollection
from b import BeztripleInterpolationMode, Bone, BoneColor
from c import ColorRamp, Constraint, ConstraintType
from f import FcurveAutoSmoothing
from h import Header
from i import IKParam
from k import KeyframeHandleType
from m import MotionPath
from n import NavigationMode
from o import Object, ObjectRotationMode
from r import RegionType
from s import ScriptDirectoryCollection, SpaceType, StudioLights
from t import Theme, ThemeStyle
from u import UILayout, UserExtensionRepoCollection, UserSolidLight
from w import WalkNavigation

import bpy
import mathutils


PreferenceSection = Literal[
    'INTERFACE',
    'THEMES',
    'VIEWPORT',
    'LIGHTS',
    'EDITING',
    'ANIMATION',
    'ADDONS',
    'INPUT',
    'NAVIGATION',
    'KEYMAP',
    'SYSTEM',
    'SAVE_LOAD',
    'FILE_PATHS',
    'EXPERIMENTAL',
]

PropDynamicpaintType = Literal['CANVAS', 'BRUSH']

ProportionalFalloff = Literal[
    'SMOOTH',
    'SPHERE',
    'ROOT',
    'INVERSE_SQUARE',
    'SHARP',
    'LINEAR',
    'CONSTANT',
    'RANDOM',
]

ProportionalFalloffCurveOnly = Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR']


# noinspection PyPropertyDefinition
class Panel(bpy_struct):
    bl_category: str
    bl_context: str
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_options: set[Literal['DEFAULT_CLOSED', 'HIDE_HEADER', 'INSTANCED', 'HEADER_LAYOUT_EXPAND']]
    bl_order: int 
    bl_owner_id: str
    bl_parent_id: str
    bl_region_type: RegionType
    bl_space_type: SpaceType
    bl_translation_context: str 
    bl_ui_units_x: int 
    text: str
    use_pin: bool

    @property
    def custom_data(self) -> Constraint: pass

    @property
    def is_popover(self) -> bool: pass

    @property
    def layout(self) -> UILayout: pass

    @classmethod
    def poll(cls, context: bpy.context) -> bool: pass

    def draw(self, context: bpy.context) -> None: pass

    def draw_header(self, context: bpy.context) -> None: pass

    def draw_header_preset(self, context: bpy.context) -> None: pass


class PathCompare(bpy_struct):  # NEW REGEX
    path: str
    use_glob: bool


class PathCompareCollection(bpy_prop_collection[PathCompare]):  # NEW REGEX
    @classmethod
    def new(cls) -> PathCompare: pass

    @classmethod
    def remove(cls, pathcmp: PathCompare) -> None: pass


# noinspection PyPropertyDefinition
class Pose(bpy_struct):
    ik_solver: Literal['LEGACY', 'ITASC'] 
    use_auto_ik: bool 
    use_mirror_relative: bool 
    use_mirror_x: bool 

    @property
    def animation_visualization(self) -> AnimViz: pass
    
    @property
    def bones(self) -> bpy_prop_collection['PoseBone']: pass
    
    @property
    def ik_param(self) -> IKParam: pass

    @classmethod
    def apply_pose_from_action(cls, action: Action, evaluation_time: float = 0.0): pass

    @classmethod
    def blend_pose_from_action(cls, action: Action, blend_factor: float = 1.0, evaluation_time: float = 0.0): pass

    @classmethod
    def backup_create(cls, action: Action): pass

    @classmethod
    def backup_restore(cls) -> bool: pass

    @classmethod
    def backup_clear(cls): pass


# noinspection PyPropertyDefinition
class PoseBone(bpy_struct):
    bbone_curveinx: float
    bbone_curveinz: float
    bbone_curveoutx: float
    bbone_curveoutz: float
    bbone_easein: float
    bbone_easeout: float
    bbone_rollin: float
    bbone_rollout: float
    bbone_scalein: mathutils.Vector
    bbone_scaleout: mathutils.Vector
    custom_shape: Object
    custom_shape_rotation_euler: mathutils.Euler
    custom_shape_scale_xyz: mathutils.Vector
    custom_shape_transform: 'PoseBone'
    custom_shape_translation: mathutils.Vector
    ik_linear_weight: float
    ik_max_x: float
    ik_max_y: float
    ik_max_z: float
    ik_min_x: float
    ik_min_y: float
    ik_min_z: float
    ik_rotation_weight: float
    ik_stiffness_x: float
    ik_stiffness_y: float
    ik_stiffness_z: float
    ik_stretch: float
    location: mathutils.Vector
    lock_ik_x: bool
    lock_ik_y: bool
    lock_ik_z: bool
    lock_location: tuple[bool, bool, bool]
    lock_rotation: tuple[bool, bool, bool]
    lock_rotation_w: bool
    lock_rotations_4d: bool
    lock_scale: tuple[bool, bool, bool]
    matrix: mathutils.Matrix
    matrix_basis: mathutils.Matrix
    name: str
    rotation_axis_angle: tuple[float, float, float, float]
    rotation_euler: mathutils.Euler
    rotation_mode: ObjectRotationMode
    rotation_quaternion: mathutils.Quaternion
    scale: mathutils.Vector
    use_custom_shape_bone_size: bool
    use_ik_limit_x: bool
    use_ik_limit_y: bool
    use_ik_limit_z: bool
    use_ik_linear_control: bool
    use_ik_rotation_control: bool
    
    @property
    def basename(self) -> bool: pass
    
    @property
    def bbone_custom_handle_end(self) -> 'PoseBone': pass
    
    @property
    def bbone_custom_handle_start(self) -> 'PoseBone': pass
    
    @property
    def bone(self) -> Bone: pass
    
    @property
    def center(self): pass
    
    @property
    def child(self) -> 'PoseBone': pass
    
    @property
    def children(self): pass
    
    @property
    def children_recursive(self): pass
    
    @property
    def children_recursive_basename(self): pass
    
    @property
    def color(self) -> BoneColor: pass
    
    @property
    def constraints(self) -> 'PoseBoneConstraints': pass
    
    @property
    def head(self) -> mathutils.Vector: pass
    
    @property
    def is_in_ik_chain(self) -> bool: pass
    
    @property
    def length(self) -> float: pass
    
    @property
    def matrix_channel(self) -> mathutils.Matrix: pass
    
    @property
    def motion_path(self) -> MotionPath: pass
    
    @property
    def parent(self) -> 'PoseBone': pass
    
    @property
    def parent_recursive(self): pass
    
    @property
    def tail(self) -> mathutils.Vector: pass
    
    @property
    def vector(self): pass
    
    @property
    def x_axis(self): pass
    
    @property
    def y_axis(self): pass
    
    @property
    def z_axis(self): pass

    def evaluate_envelope(self, point: mathutils.Vector) -> float: pass

    def bbone_segment_index(self, point: mathutils.Vector) -> tuple[int, float]: pass

    def bbone_segment_matrix(self, index: int, rest: bool = False) -> mathutils.Matrix: pass

    def compute_bbone_handles(
        self,
        rest: bool = False,
        ease: bool = False,
        offsets: bool = False,
    ) -> tuple[mathutils.Vector, float, mathutils.Vector, float]: pass

    # TODO: what is this?
    def parent_index(self, parent_test): pass

    # TODO: what is this?
    def translate(self, vec): pass


class PoseBoneConstraints(bpy_prop_collection[Constraint]):  # NEW REGEX
    active: Constraint

    # noinspection PyShadowingBuiltins
    def new(self, type: ConstraintType) -> Constraint: pass

    def remove(self, constraint: Constraint) -> None: pass

    def move(self, from_index: int, to_index: int) -> None: pass

    def copy(self, constraint: Constraint) -> Constraint: pass


# noinspection PyPropertyDefinition
class Preferences(bpy_struct):  # NEW REGEX
    active_section: PreferenceSection
    app_template: str
    is_dirty: bool
    use_preferences_save: bool
    use_recent_searches: bool

    @property
    def addons(self) -> Addons: pass
    
    @property
    def apps(self) -> 'PreferencesApps': pass
    
    @property
    def autoexec_paths(self) -> PathCompareCollection: pass
    
    @property
    def edit(self) -> 'PreferencesEdit': pass
    
    @property
    def experimental(self) -> 'PreferencesExperimental': pass
    
    @property
    def filepaths(self) -> 'PreferencesFilePaths': pass
    
    @property
    def inputs(self) -> 'PreferencesInput': pass
    
    @property
    def keymap(self) -> 'PreferencesKeymap': pass
    
    @property
    def studio_lights(self) -> StudioLights: pass
    
    @property
    def system(self) -> 'PreferencesSystem': pass
    
    @property
    def themes(self) -> bpy_prop_collection[Theme]: pass
    
    @property
    def ui_styles(self) -> bpy_prop_collection[ThemeStyle]: pass
    
    @property
    def version(self) -> tuple[int, int, int]: pass
    
    @property
    def view(self) -> 'PreferencesView': pass


class PreferencesApps(bpy_struct):  # NEW REGEX
    show_corner_split: bool
    show_edge_resize: bool
    show_regions_visibility_toggle: bool


class PreferencesEdit(bpy_struct):  # NEW REGEX
    auto_keying_mode: Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']
    collection_instance_empty_size: float 
    fcurve_new_auto_smoothing: FcurveAutoSmoothing
    fcurve_unselected_alpha: float 
    grease_pencil_default_color: tuple[float, float, float, float]
    grease_pencil_eraser_radius: int 
    grease_pencil_euclidean_distance: int 
    grease_pencil_manhattan_distance: int 
    key_insert_channels: set[Literal['LOCATION', 'ROTATION', 'SCALE', 'ROTATE_MODE', 'CUSTOM_PROPS']]
    keyframe_new_handle_type: KeyframeHandleType
    keyframe_new_interpolation_type: BeztripleInterpolationMode
    material_link: Literal['OBDATA', 'OBJECT']
    node_margin: int 
    node_preview_resolution: int 
    node_use_insert_offset: bool
    object_align: Literal['WORLD', 'VIEW', 'CURSOR']
    sculpt_paint_overlay_color: mathutils.Color 
    show_only_selected_curve_keyframes: bool
    undo_memory_limit: int 
    undo_steps: int 
    use_anim_channel_group_colors: bool
    use_auto_keyframe_insert_needed: bool
    use_auto_keying: bool
    use_auto_keying_warning: bool
    use_cursor_lock_adjust: bool
    use_duplicate_action: bool
    use_duplicate_armature: bool
    use_duplicate_camera: bool
    use_duplicate_curve: bool
    use_duplicate_curves: bool
    use_duplicate_grease_pencil: bool
    use_duplicate_lattice: bool
    use_duplicate_light: bool
    use_duplicate_lightprobe: bool
    use_duplicate_material: bool
    use_duplicate_mesh: bool
    use_duplicate_metaball: bool
    use_duplicate_node_tree: bool
    use_duplicate_particle: bool
    use_duplicate_pointcloud: bool
    use_duplicate_speaker: bool
    use_duplicate_surface: bool
    use_duplicate_text: bool
    use_duplicate_volume: bool
    use_enter_edit_mode: bool
    use_fcurve_high_quality_drawing: bool
    use_global_undo: bool
    use_insertkey_xyz_to_rgb: bool
    use_keyframe_insert_available: bool
    use_keyframe_insert_needed: bool
    use_mouse_depth_cursor: bool
    use_negative_frames: bool
    use_text_edit_auto_close: bool
    use_visual_keying: bool


class PreferencesExperimental(bpy_struct):  # NEW REGEX
    enable_overlay_next: bool
    override_auto_resync: bool
    show_asset_debug_info: bool
    use_all_linked_data_direct: bool
    use_asset_indexing: bool
    use_cycles_debug: bool
    use_eevee_debug: bool
    use_experimental_compositors: bool
    use_extended_asset_browser: bool
    use_extension_repos: bool
    use_grease_pencil_version3: bool
    use_new_curves_tools: bool
    use_new_point_cloud_type: bool
    use_new_volume_nodes: bool
    use_sculpt_texture_paint: bool
    use_sculpt_tools_tilt: bool
    use_shader_node_previews: bool
    use_undo_legacy: bool
    use_viewport_debug: bool


# noinspection PyPropertyDefinition
class PreferencesFilePaths(bpy_struct):  # NEW REGEX
    active_asset_library: int 
    active_extension_repo: int 
    animation_player: str
    animation_player_preset: Literal['INTERNAL', 'DJV', 'FRAMECYCLER', 'RV', 'MPLAYER', 'CUSTOM']
    auto_save_time: int
    file_preview_type: Literal['NONE', 'AUTO', 'SCREENSHOT', 'CAMERA']
    font_directory: str
    i18n_branches_directory: str
    image_editor: str
    recent_files: int 
    render_cache_directory: str
    render_output_directory: str
    save_version: int 
    show_hidden_files_datablocks: bool
    show_recent_locations: bool
    show_system_bookmarks: bool
    sound_directory: str
    temporary_directory: str
    text_editor: str
    text_editor_args: str
    texture_directory: str
    use_auto_save_temporary_files: bool
    use_file_compression: bool
    use_filter_files: bool
    use_load_ui: bool
    use_relative_paths: bool
    use_scripts_auto_execute: bool
    use_tabs_as_spaces: bool

    @property
    def asset_libraries(self) -> AssetLibraryCollection: pass

    @property
    def extension_repos(self) -> UserExtensionRepoCollection: pass

    @property
    def script_directories(self) -> ScriptDirectoryCollection: pass


# noinspection PyPropertyDefinition
class PreferencesInput(bpy_struct):  # NEW REGEX
    drag_threshold: int 
    drag_threshold_mouse: int 
    drag_threshold_tablet: int 
    invert_mouse_zoom: bool 
    invert_zoom_wheel: bool 
    mouse_double_click_time: int 
    mouse_emulate_3_button_modifier: Literal['ALT', 'OSKEY'] 
    move_threshold: int 
    navigation_mode: NavigationMode 
    ndof_deadzone: float 
    ndof_fly_helicopter: bool 
    ndof_lock_camera_pan_zoom: bool 
    ndof_lock_horizon: bool 
    ndof_orbit_sensitivity: float 
    ndof_pan_yz_swap_axis: bool 
    ndof_panx_invert_axis: bool 
    ndof_pany_invert_axis: bool 
    ndof_panz_invert_axis: bool 
    ndof_rotx_invert_axis: bool 
    ndof_roty_invert_axis: bool 
    ndof_rotz_invert_axis: bool 
    ndof_sensitivity: float 
    ndof_show_guide: bool 
    ndof_view_navigate_method: Literal['FREE', 'ORBIT']
    ndof_view_rotate_method: Literal['TURNTABLE', 'TRACKBALL']
    ndof_zoom_invert: bool 
    pressure_softness: float 
    pressure_threshold_max: float 
    tablet_api: Literal['AUTOMATIC', 'WINDOWS_INK', 'WINTAB']
    use_auto_perspective: bool 
    use_drag_immediately: bool 
    use_emulate_numpad: bool 
    use_mouse_continuous: bool 
    use_mouse_depth_navigate: bool 
    use_mouse_emulate_3_button: bool 
    use_multitouch_gestures: bool 
    use_numeric_input_advanced: bool
    use_rotate_around_active: bool 
    use_zoom_to_mouse: bool 
    view_rotate_method: Literal['TURNTABLE', 'TRACKBALL']
    view_rotate_sensitivity_trackball: float 
    view_rotate_sensitivity_turntable: float 
    view_zoom_axis: Literal['VERTICAL', 'HORIZONTAL']
    view_zoom_method: Literal['CONTINUE', 'DOLLY', 'SCALE']

    @property
    def use_ndof(self) -> bool: pass

    @property
    def walk_navigation(self) -> WalkNavigation: pass


class PreferencesKeymap(bpy_struct):  # NEW REGEX
    active_keyconfig: str
    show_ui_keyconfig: bool


# noinspection PyPropertyDefinition
class PreferencesSystem(bpy_struct):  # NEW REGEX
    anisotropic_filter: Literal['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16']
    audio_channels: Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']
    audio_device: Literal['None']
    audio_mixing_buffer: Literal[
        'SAMPLES_256',
        'SAMPLES_512',
        'SAMPLES_1024',
        'SAMPLES_2048',
        'SAMPLES_4096',
        'SAMPLES_8192',
        'SAMPLES_16384',
        'SAMPLES_32768',
    ]
    audio_sample_format: Literal['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE']
    audio_sample_rate: Literal['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000']
    gl_clip_alpha: float
    gl_texture_limit: Literal[
        'CLAMP_OFF',
        'CLAMP_8192',
        'CLAMP_4096',
        'CLAMP_2048',
        'CLAMP_1024',
        'CLAMP_512',
        'CLAMP_256',
        'CLAMP_128',
    ]
    gpu_backend: Literal['OPENGL', 'METAL', 'VULKAN']
    image_draw_method: Literal['AUTO', '2DTEXTURE', 'GLSL']
    light_ambient: mathutils.Color
    memory_cache_limit: int 
    register_all_users: bool
    scrollback: int 
    sequencer_disk_cache_compression: Literal['NONE', 'LOW', 'HIGH']
    sequencer_disk_cache_dir: str
    sequencer_disk_cache_size_limit: int 
    sequencer_proxy_setup: Literal['MANUAL', 'AUTOMATIC']
    texture_collection_rate: int
    texture_time_out: int
    use_edit_mode_smooth_wire: bool
    use_gpu_subdivision: bool
    use_overlay_smooth_wire: bool
    use_region_overlap: bool
    use_select_pick_depth: bool
    use_sequencer_disk_cache: bool
    use_studio_light_edit: bool
    vbo_collection_rate: int
    vbo_time_out: int
    viewport_aa: Literal['OFF', 'FXAA', '5', '8', '11', '16', '32']

    @property
    def dpi(self) -> int: pass

    @property
    def is_microsoft_store_install(self) -> bool: pass

    @property
    def legacy_compute_device_type(self) -> int: pass

    @property
    def pixel_size(self) -> float: pass

    @property
    def solid_lights(self) -> bpy_prop_collection[UserSolidLight]: pass

    @property
    def ui_line_width(self) -> float: pass

    @property
    def ui_scale(self) -> float: pass


class PreferencesView(bpy_struct):  # NEW REGEX
    color_picker_type: Literal['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV']
    factor_display_type: Literal['FACTOR', 'PERCENTAGE']
    filebrowser_display_type: Literal['SCREEN', 'WINDOW']
    font_path_ui: str
    font_path_ui_mono: str
    gizmo_size: int
    gizmo_size_navigate_v3d: int
    header_align: Literal['NONE', 'TOP', 'BOTTOM']
    language: Literal['DEFAULT']
    lookdev_sphere_size: int
    mini_axis_brightness: int
    mini_axis_size: int
    mini_axis_type: Literal['NONE', 'MINIMAL', 'GIZMO']
    open_sublevel_delay: int
    open_toplevel_delay: int
    pie_animation_timeout: int
    pie_initial_timeout: int
    pie_menu_confirm: int
    pie_menu_radius: int
    pie_menu_threshold: int
    pie_tap_timeout: int
    playback_fps_samples: int
    render_display_type: Literal['NONE', 'SCREEN', 'AREA', 'WINDOW']
    rotation_angle: float
    show_addons_enabled_only: bool
    show_column_layout: bool
    show_developer_ui: bool
    show_gizmo: bool
    show_navigate_ui: bool
    show_object_info: bool
    show_playback_fps: bool
    show_splash: bool
    show_statusbar_memory: bool
    show_statusbar_scene_duration: bool
    show_statusbar_stats: bool
    show_statusbar_version: bool
    show_statusbar_vram: bool
    show_tooltips: bool
    show_tooltips_python: bool
    show_view_name: bool
    smooth_view: int
    text_hinting: Literal['AUTO', 'NONE', 'SLIGHT', 'FULL']
    timecode_style: Literal['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY']
    ui_line_width: Literal['THIN', 'AUTO', 'THICK']
    ui_scale: float
    use_fresnel_edit: bool
    use_mouse_over_open: bool
    use_save_prompt: bool
    use_text_antialiasing: bool
    use_text_render_subpixelaa: bool
    use_translate_interface: bool
    use_translate_new_dataname: bool
    use_translate_reports: bool
    use_translate_tooltips: bool
    use_weight_color_range: bool
    view2d_grid_spacing_min: int
    view_frame_keyframes: int
    view_frame_seconds: float
    view_frame_type: Literal['KEEP_RANGE', 'SECONDS', 'KEYFRAMES']

    # noinspection PyPropertyDefinition
    @property
    def weight_color_range(self) -> ColorRamp: pass


class PropertyGroup(bpy_struct):  # NEW REGEX
    name: str
