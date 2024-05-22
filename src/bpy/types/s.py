from typing import Literal

from base import bpy_prop_collection, bpy_struct

from a import AnimData
from c import Collection, ColorManagedDisplaySettings, ColorManagedSequencerColorspaceSettings, ColorManagedViewSettings, CyclesCurveRenderSettings, CyclesRenderSettings
from d import DisplaySafeAreas
from g import GreasePencil
from i import ID
from k import KeyingSets, KeyingSetsAll
from m import MovieClip
from n import NodeTree
from o import Object
from r import RenderSettings, RigidBodyWorld
from t import TimelineMarkers, ToolSettings, TransformOrientationSlot
from u import UnitSettings, UnknownType
from v import View3DCursor, ViewLayers
from w import World

import mathutils as mathutils


SpaceType = Literal[
    'EMPTY',
    'VIEW_3D',
    'IMAGE_EDITOR',
    'NODE_EDITOR',
    'SEQUENCE_EDITOR',
    'CLIP_EDITOR',
    'DOPESHEET_EDITOR',
    'GRAPH_EDITOR',
    'NLA_EDITOR',
    'TEXT_EDITOR',
    'CONSOLE',
    'INFO',
    'TOPBAR',
    'STATUSBAR',
    'OUTLINER',
    'PROPERTIES',
    'FILE_BROWSER',
    'SPREADSHEET',
    'PREFERENCES',
]


# noinspection PyPropertyDefinition
class Scene(ID):
    active_clip: MovieClip 
    audio_distance_model: Literal[
        'NONE',
        'INVERSE',
        'INVERSE_CLAMPED',
        'LINEAR',
        'LINEAR_CLAMPED',
        'EXPONENT',
        'EXPONENT_CLAMPED'
    ]
    audio_doppler_factor: float 
    audio_doppler_speed: float 
    audio_volume: float 
    background_set: 'Scene' 
    camera: Object
    frame_current: int
    frame_end: int 
    frame_float: float 
    frame_preview_end: int 
    frame_preview_start: int 
    frame_start: int 
    frame_step: int 
    frame_subframe: float 
    gravity: mathutils.Vector 
    grease_pencil: GreasePencil 
    lock_frame_selection_to_range: bool
    show_keys_from_selected_only: bool 
    show_subframe: bool 
    simulation_frame_end: int 
    simulation_frame_start: int 
    sync_mode: Literal['NONE', 'FRAME_DROP', 'AUDIO_SYNC']
    use_audio: bool 
    use_audio_scrub: bool 
    use_custom_simulation_range: bool 
    use_gravity: bool 
    use_nodes: bool 
    use_preview_range: bool 
    use_stamp_note: str
    world: World 

    @property
    def animation_data(self) -> AnimData: pass

    @property
    def collection(self) -> Collection: pass

    @property
    def cursor(self) -> View3DCursor: pass

    @property
    def cycles(self) -> CyclesRenderSettings: pass

    @property
    def cycles_curves(self) -> CyclesCurveRenderSettings: pass

    @property
    def display(self) -> SceneDisplay: pass

    @property
    def display_settings(self) -> ColorManagedDisplaySettings: pass

    @property
    def eevee(self) -> SceneEEVEE: pass

    @property
    def frame_current_final(self) -> float: pass

    @property
    def grease_pencil_settings(self) -> SceneGpencil: pass

    @property
    def hydra(self) -> SceneHydra: pass

    @property
    def is_nla_tweakmode(self) -> bool: pass

    @property
    def keying_sets(self) -> KeyingSets: pass

    @property
    def keying_sets_all(self) -> KeyingSetsAll: pass

    @property
    def node_tree(self) -> NodeTree: pass

    @property
    def objects(self) -> 'SceneObjects': pass

    @property
    def render(self) -> RenderSettings: pass

    @property
    def rigidbody_world(self) -> RigidBodyWorld: pass

    @property
    def safe_areas(self) -> DisplaySafeAreas: pass

    @property
    def sequence_editor(self) -> 'SequenceEditor': pass

    @property
    def sequencer_colorspace_settings(self) -> ColorManagedSequencerColorspaceSettings: pass

    @property
    def timeline_markers(self) -> TimelineMarkers: pass
        
    @property
    def tool_settings(self) -> ToolSettings: pass
        
    @property
    def transform_orientation_slots(self) -> bpy_prop_collection[TransformOrientationSlot]: pass
        
    @property
    def unit_settings(self) -> UnitSettings: pass

    @property
    def view_layers(self) -> ViewLayers: pass

    @property
    def view_settings(self) -> ColorManagedViewSettings: pass


class SceneObjects(bpy_prop_collection[Object]):
    pass


class ShapeKey(bpy_struct):
    interpolation: Literal['KEY_LINEAR', 'KEY_CARDINAL', 'KEY_CATMULL_ROM', 'KEY_BSPLINE']
    lock_shape: bool 
    mute: bool 
    name: str
    relative_key: 'ShapeKey'
    slider_max: float 
    slider_min: float 
    value: float 
    vertex_group: str 

    @property
    def data(self) -> bpy_prop_collection[UnknownType]: pass

    @property
    def frame(self) -> float: pass

    @property
    def points(self) -> bpy_prop_collection['ShapeKeyPoint']: pass

    def normals_vertex_get(self) -> float: pass

    def normals_polygon_get(self) -> float: pass

    def normals_split_get(self) -> float: pass
