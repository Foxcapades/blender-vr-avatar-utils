from base import bpy_struct
from typing import Literal

from a import AnyType
from c import Constraint
from i import Icon, ID
from k import KeyMapItem
from n import Node, NodeTreeInterface
from o import OperatorContext, OperatorProperties
from r import RegionType
from s import SpaceType
from t import TextureSlot


# noinspection PyPropertyDefinition,PyShadowingBuiltins,PyShadowingNames
class UILayout(bpy_struct):
    activate_init: bool 
    active: bool 
    active_default: bool 
    alert: bool 
    alignment: Literal['EXPAND', 'LEFT', 'CENTER', 'RIGHT'] 
    emboss: Literal['NORMAL', 'NONE', 'PULLDOWN_MENU', 'RADIAL_MENU', 'NONE_OR_STATUS']
    enabled: bool 
    operator_context: OperatorContext 
    scale_x: float 
    scale_y: float 
    ui_units_x: float 
    ui_units_y: float 
    use_property_decorate: bool 
    use_property_split: bool

    @property
    def direction(self) -> Literal['HORIZONTAL', 'VERTICAL']: pass

    def row(
        self,
        align: bool = False,
        heading: str = '',
        heading_ctxt: str = '',
        translate: bool = True,
    ) -> 'UILayout': pass

    def column(
        self,
        align: bool = False,
        heading: str = '',
        heading_ctxt: str = '',
        translate: bool = True,
    ) -> 'UILayout': pass

    def panel(self, idname: str, default_closed: bool = False) -> tuple['UILayout', 'UILayout']: pass

    def panel_prop(self, data: AnyType, property: str = '') -> tuple['UILayout', 'UILayout']: pass

    def column_flow(self, columns: int = 0, align: bool = False) -> 'UILayout': pass

    def grid_flow(
        self,
        row_major: bool = False,
        columns=0,
        even_columns: bool = False,
        even_rows: bool = False,
        align: bool = False,
    ) -> 'UILayout': pass

    def box(self) -> 'UILayout': pass

    def split(self, factor=0.0, align: bool = False) -> 'UILayout': pass

    def menu_pie(self) -> 'UILayout': pass

    @classmethod
    def icon(cls, data: AnyType) -> int: pass

    @classmethod
    def enum_item_name(cls, data: AnyType, property: str, identifier: str) -> str: pass

    @classmethod
    def enum_item_description(cls, data: AnyType, property: str, identifier: str) -> str: pass

    @classmethod
    def enum_item_icon(cls, data: AnyType, property: str, identifier: str) -> int: pass

    def prop(
        self,
        data: AnyType,
        property: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        placeholder: str = '',
        expand: bool = False,
        slider: bool = False,
        toggle: int = -1,
        icon_only: bool = False,
        event: bool = False,
        full_event: bool = False,
        emboss: bool = True,
        index: int = -1,
        icon_value: int = 0,
        invert_checkbox: bool = False,
    ): pass

    def props_enum(self, data: AnyType, property: str): pass

    def prop_menu_enum(
        self,
        data: AnyType,
        property: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
    ): pass

    def prop_with_popover(
        self,
        data: AnyType,
        property: str,
        text: str = "",
        text_ctxt: str = "",
        translate: bool = True,
        icon: Icon = 'NONE',
        icon_only: bool = False,
        panel: str = ''
    ): pass

    def prop_with_menu(
        self,
        data: AnyType,
        property: str,
        text: str = "",
        text_ctx: str = "",
        translate: bool = True,
        icon: Icon = 'NONE',
        icon_only: bool = False,
        menu: str = ''
    ): pass

    def prop_tabs_enum(
        self,
        data: AnyType,
        property: str,
        data_highlight: AnyType | None = None,
        property_highlight: str = '',
        icon_only: bool = False,
    ): pass

    def prop_enum(
        self,
        data: AnyType,
        property: str,
        value: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
    ): pass

    def prop_search(
        self,
        data: AnyType,
        property: str,
        search_data: AnyType,
        search_property: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        results_are_suggestions: bool = False,
    ): pass

    def prop_decorator(self, data: AnyType, property: str, index: int = -1): pass

    def operator(
        self,
        operator: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        emboss: bool = True,
        depress: bool = False,
        icon_value: int = 0,
    ) -> OperatorProperties: pass

    def operator_menu_hold(
        self,
        operator: str,
        text: str = "",
        text_ctx: str = "",
        translate: bool = True,
        icon: Icon = 'NONE',
        emboss: bool = True,
        depress: bool = False,
        icon_value: int = 0,
        menu: str = '',
    ) -> OperatorProperties: pass

    def operator_enum(self, operator: str, property: str, icon_only: bool = False) -> OperatorProperties: pass

    def operator_menu_enum(
        self,
        operator: str,
        property: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
    ) -> OperatorProperties: pass

    def label(
        self,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        icon_value: int = 0,
    ): pass

    def menu(
        self,
        menu: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        icon_value: int = 0,
    ): pass

    def menu_contents(self, menu: str): pass

    def popover(
        self,
        panel: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        icon: Icon = 'NONE',
        icon_value: int = 0,
    ): pass

    def popover_group(self, space_type: SpaceType, region_type: RegionType, context: str, category: str): pass

    def separator(self, factor: float = 1.0): pass

    def separator_spacer(self): pass

    def progress(
        self,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
        factor: float = 0.0,
        type: Literal['BAR', 'RING'] = 'BAR',
    ): pass

    def context_pointer_set(self, name: str, data: AnyType): pass

    def template_header(self): pass

    def template_ID(
        self,
        data: AnyType,
        property: str,
        new: str = '',
        open: str = '',
        unlink: str = '',
        filter: Literal['ALL', 'AVAILABLE'] = 'ALL',
        live_icon: bool = False,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
    ): pass

    def template_ID_preview(
        self,
        data: AnyType,
        property: str,
        new: str = '',
        open = '',
        unlink: str = '',
        rows: int = 0,
        cols: int = 0,
        filter: Literal['ALL', 'AVAILABLE'] = 'ALL',
        hide_buttons: bool = False,
    ): pass

    def template_any_ID(
        self,
        data: AnyType,
        property: str,
        type_property: str,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
    ): pass

    def template_ID_tabs(
        self,
        data: AnyType,
        property: str,
        new: str = '',
        menu: str = '',
        filter: Literal['ALL', 'AVAILABLE'] = 'ALL',
    ): pass

    def template_search(
        self,
        data: AnyType,
        property: str,
        search_data: AnyType,
        search_property: str,
        new: str = '',
        unlink: str = '',
    ): pass

    def template_search_preview(
        self,
        data: AnyType,
        property: str,
        search_data: AnyType,
        search_property: str,
        new: str = '',
        unlink: str = '',
        rows: int = 0,
        cols: int = 0,
    ): pass

    def template_path_builder(
        self,
        data: AnyType,
        property: str,
        root: ID,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
    ): pass

    def template_modifiers(self): pass

    def template_constraints(self, use_bone_constraints: bool = True): pass

    def template_grease_pencil_modifiers(self): pass

    def template_shaderfx(self): pass

    def template_greasepencil_color(
        self,
        data: AnyType,
        property: str,
        rows: int = 0,
        cols: int = 0,
        scale: float= 1.0,
        filter: Literal['ALL', 'AVAILABLE'] = 'ALL',
    ): pass

    def template_constraint_header(self, data: Constraint): pass

    def template_preview(
        self,
        id: ID,
        show_buttons: bool = True,
        parent: ID | None = None,
        slot: TextureSlot | None = None,
        preview_id: str = '',
    ): pass

    def template_curve_mapping(
        self,
        data: AnyType,
        property: str,
        type: Literal['NONE', 'VECTOR', 'COLOR', 'HUE'] = 'NONE',
        levels: bool = False,
        brush: bool = False,
        use_negative_slope: bool = False,
        show_tone: bool = False,
    ): pass

    def template_curveprofile(self, data: AnyType, property: str): pass

    def template_color_ramp(self, data: AnyType, property: str, expand: bool = False): pass

    def template_icon(self, icon_value: int, scale: float = 1.0): pass

    def template_icon_view(
        self,
        data: AnyType,
        property: str,
        show_labels: bool = False,
        scale: float = 6.0,
        scale_popup: float = 5.0,
    ): pass

    def template_histogram(self, data: AnyType, property: str): pass

    def template_waveform(self, data: AnyType, property: str): pass

    def template_vectorscope(self, data: AnyType, property: str): pass

    def template_layers(
        self,
        data: AnyType,
        property: str,
        used_layers_data: AnyType,
        used_layers_property: str,
        active_layer: int,
    ): pass

    def template_color_picker(
        self,
        data: AnyType,
        property: str,
        value_slider: bool = False,
        lock: bool = False,
        lock_luminosity: bool = False,
        cubic: bool = False,
    ): pass

    def template_palette(self, data: AnyType, property: str, color: bool = False): pass

    # TODO: param types
    def template_image_layers(self, image, image_user): pass

    def template_image(
        self,
        data: AnyType,
        property: str,
        image_user,  # TODO: param type
        compact: bool = False,
        multiview: bool = False,
    ): pass

    def template_image_settings(
        self,
        image_settings,  # TODO: param type
        color_management: bool = False,
    ): pass

    # TODO: param types
    def template_image_stereo_3d(self, stereo_3d_format): pass

    # TODO: param types
    def template_image_views(self, image_settings): pass

    def template_movieclip(self, data: AnyType, property: str, compact: bool = False): pass

    def template_track(self, data: AnyType, property: str): pass

    def template_marker(
        self,
        data: AnyType,
        property: str,
        clip_user,  # TODO: param type
        track,  # TODO: param type
        compact=False,
    ): pass

    # TODO: param types
    def template_movieclip_information(self, data: AnyType, property: str, clip_user): pass

    def template_list(
        self,
        listtype_name: str,
        list_id: str,
        dataptr: AnyType,
        propname: str,
        active_dataptr: AnyType,
        active_propname: str,
        item_dyntip_propname: str = '',
        rows: int = 5,
        maxrows: int = 5,
        type: UIListLayoutType = 'DEFAULT',
        columns: int = 9,
        sort_reverse: bool = False,
        sort_lock: bool = False,
    ): pass

    def template_running_jobs(self): pass

    def template_operator_search(self): pass

    def template_menu_search(self): pass

    def template_header_3D_mode(self): pass

    def template_edit_mode_selection(self): pass

    def template_reports_banner(self): pass

    def template_input_status(self): pass

    def template_status_info(self): pass

    # TODO: param types
    def template_node_link(self, ntree, node, socket): pass

    # TODO: param types
    def template_node_view(self, ntree, node, socket): pass

    def template_node_asset_menu_items(self, catalog_path: str = ''): pass

    def template_modifier_asset_menu_items(self, catalog_path: str = ''): pass

    def template_node_operator_asset_menu_items(self, catalog_path: str = ''): pass

    def template_node_operator_asset_root_items(self): pass

    def template_texture_user(self): pass

    # TODO: param types
    def template_keymap_item_properties(self, item): pass

    def template_component_menu(self, data: AnyType, property: str, name: str = ''): pass

    def template_colorspace_settings(self, data: AnyType, property: str): pass

    def template_colormanaged_view_settings(self, data: AnyType, property: str): pass

    def template_node_socket(self, color: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 1.0)): pass

    def template_cache_file(self, data: AnyType, property: str): pass

    def template_cache_file_velocity(self, data: AnyType, property: str): pass

    def template_cache_file_procedural(self, data: AnyType, property: str): pass

    def template_cache_file_time_settings(self, data: AnyType, property: str): pass

    def template_cache_file_layers(self, data: AnyType, property: str): pass

    def template_recent_files(self, rows: int = 5) -> int: pass

    # TODO: param types
    def template_file_select_path(self, params): pass

    def template_event_from_keymap_item(
        self,
        item: KeyMapItem,
        text: str = '',
        text_ctxt: str = '',
        translate: bool = True,
    ): pass

    # noinspection PyDefaultArgument
    def template_asset_view(
        self,
        list_id: str,
        asset_library_dataptr: AnyType,
        asset_library_propname: str,
        assets_dataptr: AnyType,
        assets_propname: str,
        active_dataptr: AnyType,
        active_propname: str,
        filter_id_types: set[Literal[()]] = set(),
        display_options: set[Literal['NO_NAMES', 'NO_FILTER', 'NO_LIBRARY']] = set(),
        activate_operator: str = '',
        drag_operator: str = '',
    ) -> tuple[OperatorProperties, OperatorProperties]: pass

    def template_light_linking_collection(self, context_layout: 'UILayout', data: AnyType, property: str): pass

    def template_bone_collection_tree(self): pass

    def template_node_tree_interface(self, interface: NodeTreeInterface): pass

    def template_node_inputs(self, node: Node): pass

    def introspect(self): pass


class UnknownType(bpy_struct):
    pass
