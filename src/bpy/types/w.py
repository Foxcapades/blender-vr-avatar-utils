from typing import Callable, Literal

from bpy.types.base import bpy_prop_collection, bpy_struct

from a import Action, AssetHandle
from i import Icon, ID
from e import Event, EventType, EventValue
from g import GizmoGroup, GizmoGroupProperties
from h import Header
from k import KeyConfigurations, KeyMap
from o import Operator, OperatorProperties, OperatorReturn
from r import RegionType
from s import Scene, Screen, SpaceType, Stereo3dDisplay
from t import Timer
from u import UIPopover, UIPopupMenu
from v import ViewLayer
from x import XrSessionSettings, XrSessionState

import bpy


WindowCursor = Literal[
    'DEFAULT',
    'NONE',
    'WAIT',
    'CROSSHAIR',
    'MOVE_X',
    'MOVE_Y',
    'KNIFE',
    'TEXT',
    'PAINT_BRUSH',
    'PAINT_CROSS',
    'DOT',
    'ERASER',
    'HAND',
    'SCROLL_X',
    'SCROLL_Y',
    'SCROLL_XY',
    'EYEDROPPER',
    'PICK_AREA',
    'STOP',
    'COPY',
    'CROSS',
    'MUTE',
    'ZOOM_IN',
    'ZOOM_OUT',
]

WmReportType = Literal[
    'DEBUG',
    'INFO',
    'OPERATOR',
    'PROPERTY',
    'WARNING',
    'ERROR',
    'ERROR_INVALID_INPUT',
    'ERROR_INVALID_CONTEXT',
    'ERROR_OUT_OF_MEMORY',
]

WorkspaceObjectMode = Literal[
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
    'VERTEX_GPENCIL',
    'WEIGHT_GPENCIL',
]


# noinspection PyPropertyDefinition
class Window(bpy_struct):
    scene: Scene 
    screen: Screen 
    view_layer: ViewLayer 
    workspace: 'WorkSpace'

    @property
    def height(self) -> int: pass
    
    @property
    def parent(self) -> 'Window': pass
    
    @property
    def stereo_3d_display(self) -> Stereo3dDisplay: pass
    
    @property
    def width(self) -> int: pass
    
    @property
    def x(self) -> int: pass
    
    @property
    def y(self) -> int: pass

    def cursor_warp(self, x: int, y: int): pass

    def cursor_set(self, cursor: WindowCursor): pass

    def cursor_modal_set(self, cursor: WindowCursor): pass

    def cursor_modal_restore(self): pass

    def event_simulate(
        self,
        type: EventType,
        value: EventValue,
        unicode: str = '',
        x: int = 0,
        y: int = 0,
        shift: bool = False,
        ctrl: bool = False,
        alt: bool = False,
        oskey: bool = False
    ) -> Event: pass


# noinspection PyPropertyDefinition
class WindowManager(ID):
    addon_filter: str
    addon_search: str
    addon_support: set[Literal['OFFICIAL', 'COMMUNITY']]
    poselib_previous_action: Action
    preset_name: str
    clipboard: str

    @property
    def asset_path_dummy(self) -> str: pass
    
    @property
    def is_interface_locked(self) -> bool: pass
    
    @property
    def keyconfigs(self) -> KeyConfigurations: pass
    
    @property
    def operators(self) -> bpy_prop_collection[Operator]: pass
    
    @property
    def pose_assets(self) -> bpy_prop_collection[AssetHandle]: pass
    
    @property
    def windows(self) -> bpy_prop_collection[Window]: pass
    
    @property
    def xr_session_settings(self) -> XrSessionSettings: pass
    
    @property
    def xr_session_state(self) -> XrSessionState: pass

    @classmethod
    def fileselect_add(cls, operator: Operator): pass

    @classmethod
    def modal_handler_add(cls, operator: Operator): pass

    @classmethod
    def gizmo_group_type_ensure(cls, identifier: str): pass

    @classmethod
    def gizmo_group_type_unlink_delayed(cls, identifier: str): pass

    @classmethod
    def invoke_props_popup(cls, operator: Operator, event: Event) -> set[OperatorReturn]: pass

    @classmethod
    def invoke_props_dialog(
        cls,
        operator: Operator,
        width: int = 300,
        title: str = '',
        confirm_text: str = '',
        text_ctxt: str = '',
        translate: bool = True
    ) -> set[OperatorReturn]: pass

    @classmethod
    def invoke_search_popup(cls, operator: Operator): pass

    @classmethod
    def invoke_popup(cls, operator: Operator, width: int = 300) -> set[OperatorReturn]: pass

    @classmethod
    def invoke_confirm(
        cls,
        operator: Operator,
        event: Event,
        title: str = '',
        message: str = '',
        confirm_text: str = '',
        icon: Literal['NONE', 'WARNING', 'QUESTION', 'ERROR', 'INFO'] = 'WARNING',
        text_ctxt: str = '',
        translate: bool = True,
    ) -> set[OperatorReturn]: pass

    @classmethod
    def popmenu_begin__internal(cls, title: str, icon: Icon = 'NONE') -> UIPopupMenu: pass

    # TODO: what is this?
    @classmethod
    def popmenu_end__internal(cls, menu): pass

    @classmethod
    def popover_begin__internal(cls, ui_units_x: int = 0, from_active_button: bool = False) -> UIPopover: pass

    @classmethod
    def popover_end__internal(cls, menu, keymap: KeyMap = None): pass

    # TODO: what is this?
    @classmethod
    def piemenu_begin__internal(cls, title: str, icon: Icon = 'NONE', event = None): pass

    # TODO: what is this?
    @classmethod
    def piemenu_end__internal(cls, menu): pass

    @classmethod
    def operator_properties_last(cls, operator: Operator) -> OperatorProperties: pass

    # TODO: what is this?
    @classmethod
    def tag_script_reload(cls): pass

    @classmethod
    def draw_cursor_add(cls, callback, args, space_type: SpaceType, region_type: RegionType) -> object: pass

    @classmethod
    def draw_cursor_remove(cls, handler: object): pass

    def event_timer_add(self, time_step: float, window: Window = None) -> Timer: pass

    def event_timer_remove(self, timer: Timer): pass

    def popover(
        self,
        draw_func,  # TODO: what is this?
        *,  # TODO: what is this?
        ui_units_x: int = 0,
        keymap = None,  # TODO: what is this?
        from_active_button: bool = False,
    ): pass   # TODO: what is this?

    # TODO: what is this?
    def popup_menu(self, draw_func, *, title: str = '', icon: Icon = 'NONE'): pass

    def popup_menu_pie(self, event, draw_func, *, title: str = '', icon: Icon = 'NONE'): pass

    # TODO: what is this?
    def print_undo_steps(self): pass

    # noinspection PyShadowingBuiltins
    def progress_begin(self, min: float, max: float): pass

    def progress_update(self, value: float): pass

    def progress_end(self): pass


class wmOwnerID(bpy_struct):
    name: str


class wmOwnerIDs(bpy_prop_collection[wmOwnerID]):
    def new(self, name: str) -> wmOwnerID: pass

    def remove(self, owner_id: wmOwnerID): pass

    def clear(self): pass


class wmTools(bpy_prop_collection['WorkSpaceTool']):
    def from_space_view3d_mode(self, mode, create: bool = False) -> 'WorkSpaceTool': pass

    def from_space_image_mode(self, mode, create: bool = False) -> 'WorkSpaceTool': pass

    def from_space_node(self, create: bool = False) -> 'WorkSpaceTool': pass

    def from_space_sequencer(self, mode, create: bool = False) -> 'WorkSpaceTool': pass


# noinspection PyPropertyDefinition
class WorkSpace(ID):
    active_addon: int 
    active_pose_asset_index: int 
    asset_library_reference: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']
    object_mode: WorkspaceObjectMode
    use_filter_by_owner: bool
    use_pin_scene: bool

    @property
    def owner_ids(self) -> wmOwnerIDs: pass

    @property
    def screens(self) -> bpy_prop_collection[Screen]: pass

    @property
    def tools(self) -> wmTools: pass

    @classmethod
    def status_text_set_internal(cls, text: str): pass

    def status_text_set(self, text: str | None | Callable[[Header, bpy.context], str | None]): pass


# noinspection PyPropertyDefinition
class WorkSpaceTool(bpy_struct):
    idname: str
    idname_fallback: str

    @property
    def has_datablock(self) -> bool: pass

    @property
    def index(self) -> int: pass

    @property
    def mode(self) -> Literal['DEFAULT']: pass

    @property
    def space_type(self) -> SpaceType: pass

    @property
    def use_paint_canvas(self) -> bool: pass

    @property
    def widget(self) -> str: pass

    # noinspection PyDefaultArgument
    def setup(
        self,
        idname: str,
        cursor: WindowCursor = 'DEFAULT',
        keymap: str = '',
        gizmo_group: str = '',
        data_block: str = '',
        operator: str = '',
        index: int = 0,
        options: set[Literal['KEYMAP_FALLBACK']] = set(),
        idname_fallback: str = '',
        keymap_fallback: str = '',
    ): pass

    def operator_properties(self, operator: Operator) -> OperatorProperties: pass

    def gizmo_group_properties(self, group: GizmoGroup) -> GizmoGroupProperties: pass

    def refresh_from_context(self): pass
