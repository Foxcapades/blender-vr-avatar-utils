from typing import Literal
from base import bpy_struct, bpy_prop_collection
from mathutils import Color, Vector

from a import ActionGroup, AnyType
from b import BeztripleKeyframeType
from d import Driver
from k import Keyframe
from u import UIList

FcurveAutoSmoothing = Literal['NONE', 'CONT_ACCEL']

FmodifierType = Literal[
    'NULL',
    'GENERATOR',
    'FNGENERATOR',
    'ENVELOPE',
    'CYCLES',
    'NOISE',
    'LIMITS',
    'STEPPED',
]


# noinspection PyPropertyDefinition
class FCurve(bpy_struct):
    array_index: int 
    auto_smoothing: FcurveAutoSmoothing
    color: Color
    color_mode: Literal['AUTO_RAINBOW', 'AUTO_RGB', 'AUTO_YRGB', 'CUSTOM']
    data_path: str
    extrapolation: Literal['CONSTANT', 'LINEAR']
    group: ActionGroup 
    hide: bool
    is_valid: bool
    lock: bool
    mute: bool
    select: bool
    
    @property
    def driver(self) -> Driver: pass
    
    @property
    def is_empty(self) -> bool: pass
    
    @property
    def keyframe_points(self) -> 'FCurveKeyframePoints': pass
    
    @property
    def modifiers(self) -> 'FCurveModifiers': pass
    
    @property
    def sampled_points(self) -> bpy_prop_collection['FCurveSample']: pass

    def evaluate(self, frame: float) -> float: pass

    def update(self) -> None: pass

    def range(self) -> Vector: pass

    def update_autoflags(self, data: AnyType) -> None: pass

    def convert_to_samples(self, start: int, end: int) -> None: pass

    def convert_to_keyframes(self, start: int, end: int) -> None: pass


class FCurveKeyframePoints(bpy_prop_collection[Keyframe]):
    # noinspection PyDefaultArgument
    def insert(
        self,
        frame: float,
        value: float,
        options: set[Literal['REPLACE', 'NEEDED', 'FAST']] = set(),
        keyframe_type: BeztripleKeyframeType = 'KEYFRAME',
    ) -> Keyframe: pass

    # TODO: does this return a keyframe?
    def add(self, count: int): pass

    def remove(self, keyframe: Keyframe, fast: bool = False) -> None: pass

    def clear(self) -> None: pass

    def sort(self) -> None: pass

    def deduplicate(self) -> None: pass

    def handles_recalc(self) -> None: pass


class FCurveModifiers(bpy_prop_collection['FModifier']):
    active: 'FModifier'

    def new(self, type: FmodifierType) -> 'FModifier': pass

    def remove(self, modifier: FModifier) -> None: pass


class FCurveSample(bpy_struct):
    co: Vector
    select: bool


class FFmpegSettings(bpy_struct):
    audio_bitrate: int 
    audio_channels: Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']
    audio_codec: Literal['NONE', 'AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PCM', 'VORBIS']
    audio_mixrate: int 
    audio_volume: float 
    buffersize: int 
    codec: Literal[
        'NONE',
        'DNXHD',
        'DV',
        'FFV1',
        'FLASH',
        'H264',
        'HUFFYUV',
        'MPEG1',
        'MPEG2',
        'MPEG4',
        'PNG',
        'QTRLE',
        'THEORA',
        'WEBM',
        'AV1'
    ]
    constant_rate_factor: Literal['NONE', 'LOSSLESS', 'PERC_LOSSLESS', 'HIGH', 'MEDIUM', 'LOW', 'VERYLOW', 'LOWEST']
    ffmpeg_preset: Literal['BEST', 'GOOD', 'REALTIME']
    format: Literal['MPEG1', 'MPEG2', 'MPEG4', 'AVI', 'QUICKTIME', 'DV', 'OGG', 'MKV', 'FLASH', 'WEBM']
    gopsize: int 
    max_b_frames: int 
    maxrate: int 
    minrate: int 
    muxrate: int 
    packetsize: int 
    use_autosplit: bool
    use_lossless_output: bool
    use_max_b_frames: bool
    video_bitrate: int 


# TODO: what is this?
class FILEBROWSER_UL_dir(UIList):
    def draw_item(self, _context, layout, _data, item, icon, _active_data, _active_propname, _index): pass


class FModifier(bpy_struct):
    active: bool
    blend_in: float 
    blend_out: float 
    frame_end: float 
    frame_start: float 
    influence: float 
    mute: bool
    name: str
    show_expanded: bool
    use_influence: bool
    use_restricted_range: bool

    @property
    def is_valid(self) -> bool: pass

    @property
    def type(self) -> FmodifierType: pass



