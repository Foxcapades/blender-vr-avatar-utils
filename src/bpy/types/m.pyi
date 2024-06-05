import bpy
import mathutils

from base import bpy_prop_collection, bpy_struct
from typing import Callable, Literal, Sequence

from a import AnimData, AttributeGroup
from c import CyclesMeshSettings
from i import ID, IDMaterials
from k import Key
from l import LoopColors
from r import ReadOnlyInteger
from u import UILayout, UVLoopLayers


MeshDelimitMode = Literal['NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV']

MeshSelectMode = Literal['VERT', 'EDGE', 'FACE']

MotionpathDisplayType = Literal['CURRENT_FRAME', 'RANGE']

MotionpathRange = Literal['KEYS_ALL', 'KEYS_SELECTED', 'SCENE', 'MANUAL']

MotionpathBakeLocation = Literal['HEADS', 'TAILS']


# noinspection PyPropertyDefinition
class Menu(bpy_struct):
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_options: set[Literal['SEARCH_ON_KEY_PRESS']]
    bl_owner_id: str
    bl_translation_context: str

    @property
    def layout(self) -> UILayout: pass

    @classmethod
    def poll(cls, context: bpy.context) -> bool: pass

    def draw(self, context: bpy.context): pass

    # TODO: what is this?
    def draw_preset(self, _context): pass

    def path_menu(
        self,
        searchpaths: Sequence[str],
        operator: str,
        *,  # TODO: what is this?
        props_default: dict = None,
        prop_filepath: str = 'filepath',
        filter_ext: Callable[[str], bool] = None,
        filter_path: Callable[[str], bool] = None,
        display_name: Callable[[str], str] = None,
        add_operator=None  # TODO: what is this?
    ): pass


# TODO: incomplete, messing methods
# noinspection PyPropertyDefinition
class Mesh(ID):
    auto_texspace: bool
    remesh_mode: Literal['VOXEL', 'QUAD']
    remesh_voxel_adaptivity: float
    remesh_voxel_size: float
    texco_mesh: 'Mesh'
    texspace_location: mathutils.Vector
    texspace_size: mathutils.Vector
    texture_mesh: 'Mesh'
    use_auto_texspace: bool
    use_mirror_topology: bool
    use_mirror_vertex_groups: bool
    use_mirror_x: bool
    use_mirror_y: bool
    use_mirror_z: bool
    use_paint_bone_selection: bool
    use_paint_mask: bool
    use_paint_mask_vertex: bool
    use_remesh_fix_poles: bool
    use_remesh_preserve_attributes: bool
    use_remesh_preserve_volume: bool
    uv_layer_clone: 'MeshUVLoopLayer'
    uv_layer_clone_index: int
    uv_layer_stencil: 'MeshUVLoopLayer'
    uv_layer_stencil_index: int

    @property
    def animation_data(self) -> AnimData: pass
        
    @property
    def attributes(self) -> AttributeGroup: pass

    @property
    def color_attributes(self) -> AttributeGroup: pass
        
    @property
    def corner_normals(self) -> bpy_prop_collection['MeshNormalValue']: pass
        
    @property
    def cycles(self) -> CyclesMeshSettings: pass
        
    @property
    def edges(self) -> 'MeshEdges': pass
        
    @property
    def has_custom_normals(self) -> bool: pass
        
    @property
    def is_editmode(self) -> bool: pass
        
    @property
    def loop_triangle_polygons(self) -> bpy_prop_collection[ReadOnlyInteger]: pass
        
    @property
    def loop_triangles(self) -> 'MeshLoopTriangles': pass
        
    @property
    def loops(self) -> 'MeshLoops': pass
        
    @property
    def materials(self) -> IDMaterials: pass
        
    @property
    def normals_domain(self) -> Literal['POINT', 'FACE', 'CORNER']: pass
        
    @property
    def polygon_normals(self) -> bpy_prop_collection['MeshNormalValue']: pass
        
    @property
    def polygons(self) -> 'MeshPolygons': pass

    @property
    def shape_keys(self) -> Key: pass
        
    @property
    def skin_vertices(self) -> bpy_prop_collection['MeshSkinVertexLayer']: pass

    @property
    def total_edge_sel(self) -> int: pass
        
    @property
    def total_face_sel(self) -> int: pass
        
    @property
    def total_vert_sel(self) -> int: pass

    @property
    def uv_layers(self) -> UVLoopLayers: pass
        
    @property
    def vertex_colors(self) -> LoopColors: pass
        
    @property
    def vertex_normals(self) -> bpy_prop_collection['MeshNormalValue']: pass
        
    @property
    def vertices(self) -> 'MeshVertices': pass

    @property
    def edge_creases(self): pass

    @property
    def edge_keys(self): pass

    @property
    def vertex_creases(self): pass

    @property
    def vertex_paint_mask(self): pass
