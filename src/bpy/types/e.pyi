from typing import Literal
from base import bpy_struct, bpy_prop_collection
from mathutils import Matrix, Vector

from b import BoneCollection, BoneColor
from c import Collection, CurveMapping
from g import GpencilModifier
from i import Icon
from m import Material, Modifier
from p import Property
from s import Sequence, SequenceCrop, SequenceProxy, SequenceTransform
from x import XrEventData

EventDirection = Literal[
    'ANY',
    'NORTH',
    'NORTH_EAST',
    'EAST',
    'SOUTH_EAST',
    'SOUTH',
    'SOUTH_WEST',
    'WEST',
    'NORTH_WEST',
]

EventType = Literal[
    'NONE',
    'LEFTMOUSE',
    'MIDDLEMOUSE',
    'RIGHTMOUSE',
    'BUTTON4MOUSE',
    'BUTTON5MOUSE',
    'BUTTON6MOUSE',
    'BUTTON7MOUSE',
    'PEN',
    'ERASER',
    'MOUSEMOVE',
    'INBETWEEN_MOUSEMOVE',
    'TRACKPADPAN',
    'TRACKPADZOOM',
    'MOUSEROTATE',
    'MOUSESMARTZOOM',
    'WHEELUPMOUSE',
    'WHEELDOWNMOUSE',
    'WHEELINMOUSE',
    'WHEELOUTMOUSE',
    'A'
    'B',
    'C'
    'D',
    'E'
    'F',
    'G'
    'H',
    'I'
    'J',
    'K'
    'L',
    'M'
    'N',
    'O'
    'P',
    'Q'
    'R',
    'S'
    'T',
    'U'
    'V',
    'W'
    'X',
    'Y'
    'Z',
    'ZERO'
    'ONE',
    'TWO'
    'THREE',
    'FOUR'
    'FIVE',
    'SIX'
    'SEVEN',
    'EIGHT'
    'NINE',
    'LEFT_CTRL',
    'LEFT_ALT',
    'LEFT_SHIFT',
    'RIGHT_ALT',
    'RIGHT_CTRL',
    'RIGHT_SHIFT',
    'OSKEY',
    'APP',
    'GRLESS',
    'ESC',
    'TAB',
    'RET',
    'SPACE',
    'LINE_FEED',
    'BACK_SPACE',
    'DEL',
    'SEMI_COLON',
    'PERIOD',
    'COMMA',
    'QUOTE',
    'ACCENT_GRAVE',
    'MINUS',
    'PLUS',
    'SLASH',
    'BACK_SLASH',
    'EQUAL',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_ARROW',
    'DOWN_ARROW',
    'RIGHT_ARROW',
    'UP_ARROW',
    'NUMPAD_2',
    'NUMPAD_4',
    'NUMPAD_6',
    'NUMPAD_8',
    'NUMPAD_1',
    'NUMPAD_3',
    'NUMPAD_5',
    'NUMPAD_7',
    'NUMPAD_9',
    'NUMPAD_PERIOD',
    'NUMPAD_SLASH',
    'NUMPAD_ASTERIX',
    'NUMPAD_0',
    'NUMPAD_MINUS',
    'NUMPAD_ENTER',
    'NUMPAD_PLUS',
    'F1',
    'F2',
    'F3',
    'F4',
    'F5',
    'F6',
    'F7',
    'F8',
    'F9',
    'F10',
    'F11',
    'F12',
    'F13',
    'F14',
    'F15',
    'F16',
    'F17',
    'F18',
    'F19',
    'F20',
    'F21',
    'F22',
    'F23',
    'F24',
    'PAUSE',
    'INSERT',
    'HOME',
    'PAGE_UP',
    'PAGE_DOWN',
    'END',
    'MEDIA_PLAY',
    'MEDIA_STOP',
    'MEDIA_FIRST',
    'MEDIA_LAST',
    'TEXTINPUT',
    'WINDOW_DEACTIVATE',
    'TIMER',
    'TIMER0',
    'TIMER1',
    'TIMER2',
    'TIMER_JOBS',
    'TIMER_AUTOSAVE',
    'TIMER_REPORT',
    'TIMERREGION',
    'NDOF_MOTION',
    'NDOF_BUTTON_MENU',
    'NDOF_BUTTON_FIT',
    'NDOF_BUTTON_TOP',
    'NDOF_BUTTON_BOTTOM',
    'NDOF_BUTTON_LEFT',
    'NDOF_BUTTON_RIGHT',
    'NDOF_BUTTON_FRONT',
    'NDOF_BUTTON_BACK',
    'NDOF_BUTTON_ISO1',
    'NDOF_BUTTON_ISO2',
    'NDOF_BUTTON_ROLL_CW',
    'NDOF_BUTTON_ROLL_CCW',
    'NDOF_BUTTON_SPIN_CW',
    'NDOF_BUTTON_SPIN_CCW',
    'NDOF_BUTTON_TILT_CW',
    'NDOF_BUTTON_TILT_CCW',
    'NDOF_BUTTON_ROTATE',
    'NDOF_BUTTON_PANZOOM',
    'NDOF_BUTTON_DOMINANT',
    'NDOF_BUTTON_PLUS',
    'NDOF_BUTTON_MINUS',
    'NDOF_BUTTON_V1',
    'NDOF_BUTTON_V2',
    'NDOF_BUTTON_V3',
    'NDOF_BUTTON_1',
    'NDOF_BUTTON_2',
    'NDOF_BUTTON_3',
    'NDOF_BUTTON_4',
    'NDOF_BUTTON_5',
    'NDOF_BUTTON_6',
    'NDOF_BUTTON_7',
    'NDOF_BUTTON_8',
    'NDOF_BUTTON_9',
    'NDOF_BUTTON_10',
    'NDOF_BUTTON_A',
    'NDOF_BUTTON_B',
    'NDOF_BUTTON_C',
    'ACTIONZONE_AREA',
    'ACTIONZONE_REGION',
    'ACTIONZONE_FULLSCREEN',
    'XR_ACTION',
]

EventValue = Literal['ANY', 'PRESS', 'RELEASE', 'CLICK', 'DOUBLE_CLICK', 'CLICK_DRAG', 'NOTHING']


# noinspection PyPropertyDefinition
class EQCurveMappingData(bpy_struct):
    @property
    def curve_mapping(self) -> CurveMapping: pass


class EdgeSplitModifier(Modifier):
    split_angle: float 
    use_edge_angle: bool
    use_edge_sharp: bool


# noinspection PyPropertyDefinition
class EditBone(bpy_struct):
    bbone_curveinx: float 
    bbone_curveinz: float 
    bbone_curveoutx: float 
    bbone_curveoutz: float 
    bbone_custom_handle_end: 'EditBone' 
    bbone_custom_handle_start: 'EditBone' 
    bbone_easein: float 
    bbone_easeout: float 
    bbone_handle_type_end: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'] 
    bbone_handle_type_start: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'] 
    bbone_handle_use_ease_end: bool 
    bbone_handle_use_ease_start: bool 
    bbone_handle_use_scale_end: tuple[bool, bool, bool] 
    bbone_handle_use_scale_start: tuple[bool, bool, bool] 
    bbone_mapping_mode: Literal['STRAIGHT', 'CURVED'] 
    bbone_rollin: float 
    bbone_rollout: float 
    bbone_scalein: Vector 
    bbone_scaleout: Vector 
    bbone_segments: int 
    bbone_x: float 
    bbone_z: float 
    envelope_distance: float 
    envelope_weight: float 
    head: Vector 
    head_radius: float 
    hide: bool 
    hide_select: bool 
    inherit_scale: Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY'] 
    length: float 
    lock: bool 
    matrix: str 
    parent: 'EditBone' 
    roll: float 
    select: bool 
    select_head: bool 
    select_tail: bool 
    show_wire: bool 
    tail: Vector 
    tail_radius: float 
    use_connect: bool 
    use_cyclic_offset: bool 
    use_deform: bool 
    use_endroll_as_inroll: bool 
    use_envelope_multiply: bool 
    use_inherit_rotation: bool 
    use_local_location: bool 
    use_relative_parent: bool 
    use_scale_easing: bool 
    
    @property
    def collections(self) -> bpy_prop_collection[BoneCollection]: pass
    
    @property
    def color(self) -> BoneColor: pass

    @property
    def basename(self) -> str: pass

    # TODO: what does this return?
    @property
    def center(self): pass

    # TODO: what does this return
    @property
    def children(self): pass

    # TODO: what does this return
    @property
    def children_recursive(self): pass

    # TODO: what does this return
    @property
    def children_recursive_basename(self): pass

    # TODO: what does this return
    @property
    def parent_recursive(self): pass

    # TODO: does this return a mathutils.Vector or a tuple or something?    
    @property
    def vector(self): pass

    # TODO: does this return a mathutils.Vector or a tuple or something?    
    @property
    def x_axis(self): pass

    # TODO: does this return a mathutils.Vector or a tuple or something?    
    @property
    def y_axis(self): pass

    # TODO: does this return a mathutils.Vector or a tuple or something?    
    @property
    def z_axis(self): pass

    def align_roll(self, vector: Vector) -> None: pass

    # TODO: is `other` another EditBone or something else?
    def align_orientation(self, other) -> None: pass

    # TODO: what is `parent_test`?  I assume some sort of predicate?
    # TODO: what does this return?
    def parent_index(self, parent_test): pass

    def transform(self, matrix: Matrix, *, scale: bool = True, roll: bool = True) -> None: pass

    # TODO: what type is `vec`?
    def translate(self, vec) -> None: pass


# noinspection PyPropertyDefinition
class EffectSequence(Sequence):
    alpha_mode: Literal['STRAIGHT', 'PREMUL'] 
    color_multiply: float 
    color_saturation: float 
    multiply_alpha: bool 
    strobe: float 
    use_deinterlace: bool 
    use_flip_x: bool 
    use_flip_y: bool 
    use_float: bool 
    use_proxy: bool 
    use_reverse_frames: bool 
    
    @property
    def crop(self) -> SequenceCrop: pass
    
    @property
    def proxy(self) -> SequenceProxy: pass
    
    @property
    def transform(self) -> SequenceTransform: pass


class EffectorWeights(bpy_struct):
    all: float 
    apply_to_hair_growing: bool
    boid: float 
    charge: float 
    collection: Collection 
    curve_guide: float 
    drag: float 
    force: float 
    gravity: float 
    harmonic: float 
    lennardjones: float 
    magnetic: float 
    smokeflow: float 
    texture: float 
    turbulence: float 
    vortex: float 
    wind: float


# noinspection PyPropertyDefinition
class EnumProperty(Property):
    @property
    def default(self) -> Literal['DUMMY']: pass
    
    @property
    def default_flag(self) -> set[Literal['DUMMY']]: pass
    
    @property
    def enum_items(self) -> bpy_prop_collection['EnumPropertyItem']: pass
    
    @property
    def enum_items_static(self) -> bpy_prop_collection['EnumPropertyItem']: pass
    
    @property
    def enum_items_static_ui(self) -> bpy_prop_collection['EnumPropertyItem']: pass


# noinspection PyPropertyDefinition
class EnumPropertyItem(bpy_struct):
    @property
    def description(self) -> str: pass
    
    @property
    def icon(self) -> Icon: pass
    
    @property
    def identifier(self) -> str: pass
    
    @property
    def name(self) -> str: pass
    
    @property
    def value(self) -> int: pass


class EnvelopeGpencilModifier(GpencilModifier):
    invert_layer_pass: bool
    invert_layers: bool
    invert_material_pass: bool
    invert_materials: bool
    invert_vertex: bool
    layer: str
    layer_pass: int 
    mat_nr: int 
    material: Material 
    mode: Literal['DEFORM', 'SEGMENTS', 'FILLS']
    pass_index: int 
    skip: int 
    spread: int 
    strength: float 
    thickness: float 
    vertex_group: str


# noinspection PyPropertyDefinition
class Event(bpy_struct):
    @property
    def alt(self) -> bool: pass
    
    @property
    def ascii(self) -> str: pass
    
    @property
    def ctrl(self) -> bool: pass
    
    @property
    def direction(self) -> EventDirection: pass
    
    @property
    def is_consecutive(self) -> bool: pass
    
    @property
    def is_mouse_absolute(self) -> bool: pass
    
    @property
    def is_repeat(self) -> bool: pass
    
    @property
    def is_tablet(self) -> bool: pass
    
    @property
    def mouse_prev_press_x(self) -> int: pass
    
    @property
    def mouse_prev_press_y(self) -> int: pass
    
    @property
    def mouse_prev_x(self) -> int: pass
    
    @property
    def mouse_prev_y(self) -> int: pass
    
    @property
    def mouse_region_x(self) -> int: pass
    
    @property
    def mouse_region_y(self) -> int: pass
    
    @property
    def mouse_x(self) -> int: pass
    
    @property
    def mouse_y(self) -> int: pass
    
    @property
    def oskey(self) -> bool: pass
    
    @property
    def pressure(self) -> float: pass
    
    @property
    def shift(self) -> bool: pass
    
    @property
    def tilt(self) -> Vector: pass
    
    @property
    def type(self) -> EventType: pass
    
    @property
    def type_prev(self) -> EventType: pass
    
    @property
    def unicode(self) -> str: pass
    
    @property
    def value(self) -> EventValue: pass
    
    @property
    def value_prev(self) -> EventValue: pass
    
    @property
    def xr(self) -> XrEventData: pass


class ExplodeModifier(Modifier):
    invert_vertex_group: bool
    particle_uv: str
    protect: float 
    show_alive: bool
    show_dead: bool
    show_unborn: bool
    use_edge_cut: bool
    use_size: bool
    vertex_group: str
