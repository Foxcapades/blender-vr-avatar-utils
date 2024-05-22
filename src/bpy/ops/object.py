from typing import Literal

from bpy.types.base import bpy_prop_collection
from bpy.types.a import AssetLibraryType
from bpy.types.b import BakePassFilterType, BakeMarginType, BakePassType, BakeSaveMode, BakeTarget
from bpy.types.d import DtLayersSelectDst, DtLayersSelectSrc, DtMethodEdge, DtMethodLoop, DtMethodPoly, DtMethodVertex, DtMixMode
from bpy.types.i import IdType
from bpy.types.l import LightType
from bpy.types.m import MeshSelectMode, MetaelemType, MotionpathDisplayType, MotionpathRange
from bpy.types.n import NormalSpace, NormalSwizzle
from bpy.types.o import OBJECT_OT_duplicate, ObjectEmptyDrawtype, ObjectGpencilType, ObjectGreasepencilModifierType, ObjectMode, ObjectModifierType, ObjectShaderfxType, ObjectType, OperatorFileListElement, OperatorReturn
from bpy.types.t import TRANSFORM_OT_translate, TransformMode

from mathutils import Euler, Matrix, Vector


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyShadowingNames
def add(
    radius: float = 1.0,
    type: ObjectType = 'EMPTY',
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an object to the scene.

    Args:
        radius: Radius.

            [0, inf]

        type: Object Type

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align: The alignment of the new object.

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


def add_modifier_menu() -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def add_named(
    linked: bool = False,
    name: str = '',
    session_uid: int = 0,
    matrix: Matrix = Matrix((
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0)
    )),
    drop_x: int = 0,
    drop_y: int = 0,
) -> set[OperatorReturn]:
    """
    Add named object.

    Args:
        linked: Duplicate object but not object data, linking to the original
            data

        name: Name of the data-block to use by the operator.

        session_uid: Session UID of the data-block to use by the operator.

            [-inf, inf]

        matrix: Matrix of 4 * 4 items in [-inf, inf]

        drop_x: X-coordinate (screen space) to place the new object under.

            [-inf, inf]

        drop_y: Y-coordinate (screen space) to place the new object under.

            [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyDefaultArgument,PyUnusedLocal
def align(
    bb_quality: bool = True,
    align_mode: Literal['OPT_1', 'OPT_2', 'OPT_3'] = 'OPT_2',
    relative_to: Literal['OPT_1', 'OPT_2', 'OPT_3', 'OPT_4'] = 'OPT_4',
    align_axis: set[Literal['X', 'Y', 'Z']] = set(),
) -> set[OperatorReturn]:
    """
    Align objects.

    Args:
        bb_quality: High Quality. Enables high quality but slow calculation of
            the bounding box for perfect results on complex shape meshes with
            rotation/scale

        align_mode: Side of object to use for alignment.

        relative_to: Relative To, Reference location to align to.

            OPT_1: Use the scene origin as the position for the selected objects
                to align to.

            OPT_2: Use the 3D cursor as the position for the selected objects to
                align to.

            OPT_3: Use the selected objects as the position for the selected
                objects to align to.

            OPT_4: Use the active object as the position for the selected
                objects to align to.

        align_axis:

    Returns:
        Operation result.
    """
    pass


def anim_transforms_to_deltas() -> set[OperatorReturn]:
    """
    Convert object animation for normal transforms to delta transforms.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def armature_add(
    radius: float = 1.0,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an armature object to the scene.

    Args:
        radius: [0, inf]

        enter_editmode: Enter edit mode when adding this object.

        align: Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def assign_property_defaults(process_data: bool = True, process_bones: bool = True) -> set[OperatorReturn]:
    """
    Assign the current values of custom properties as their defaults, for use as
    part of the rest pose state in NLA track mixing.

    Args:
        process_data: Process data properties

        process_bones: Process bone properties

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyDefaultArgument
def bake(
    type: BakePassType = 'COMBINED',
    pass_filter: set[BakePassFilterType] = set(),
    filepath: str = '',
    width: int = 512,
    height: int = 512,
    margin: int = 16,
    margin_type: BakeMarginType = 'EXTEND',
    use_selected_to_active: bool = False,
    max_ray_distance: float = 0.0,
    cage_extrusion: float = 0.0,
    cage_object: str = '',
    normal_space: NormalSpace = 'TANGENT',
    normal_r: NormalSwizzle = 'POS_X',
    normal_g: NormalSwizzle = 'POS_Y',
    normal_b: NormalSwizzle = 'POS_Z',
    target: BakeTarget = 'IMAGE_TEXTURES',
    save_mode: BakeSaveMode = 'INTERNAL',
    use_clear: bool = False,
    use_cage: bool = False,
    use_split_materials: bool = False,
    use_automatic_name: bool = False,
    uv_layer: str = '',
) -> set[OperatorReturn]:
    """
    Bake image textures of selected objects

    Args:
        type: Type of pass to bake, some of them may not be supported by the
            current render engine

        pass_filter: Filter to combined, diffuse, glossy, transmission and
            subsurface passes

        filepath: Image filepath to use when saving externally

        width: Horizontal dimension of the baking map (external only).

            [1, inf]

        height: Vertical dimension of the baking map (external only).

            [1, inf]

        margin: Extends the baked result as a post process filter.

            [0, inf]

        margin_type: Which algorithm to use to generate the margin.

        use_selected_to_active: Bake shading on the surface of selected objects
            to the active object.

        max_ray_distance: The maximum ray distance for matching points between
            the active and selected objects. If zero, there is no limit.

            [0, inf]

        cage_extrusion: Inflate the active object by the specified distance for
            baking. This helps matching to points nearer to the outside of the
            selected object meshes.

            [0, inf]

        cage_object: Object to use as cage, instead of calculating the cage from
            the active object with cage extrusion.

        normal_space: Choose normal space for baking.

        normal_r: Axis to bake in red channel.

        normal_g: Axis to bake in green channel.

        normal_b: Axis to bake in blue channel.

        target: Where to output the baked map.

        save_mode: Where to save baked image textures.

        use_clear: Clear images before baking (only for internal saving)

        use_cage: Cast rays to active object from a cage.

        use_split_materials: Split baked maps per material, using material name
            in output file (external only).

        use_automatic_name: Automatically name the output file with the pass
            type.

        uv_layer: UV layer to override active.

    Returns:
        Operation result.
    """
    pass


def bake_image() -> set[OperatorReturn]:
    """
    Bake image textures of selected objects.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def camera_add(
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a camera object to the scene

    Args:
        enter_editmode: Enter edit mode when adding this object.

        align: Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf].

    Returns:
        Operation result.
    """
    pass


def clear_override_library() -> set[OperatorReturn]:
    """
    Delete the selected local overrides and relink their usages to the linked
    data-blocks if possible, else reset them and mark them as non editable.

    Returns:
        Operation result.
    """
    pass


def collection_add() -> set[OperatorReturn]:
    """
    Add an object to a new collection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def collection_external_asset_drop(
    session_uid: int = 0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
    use_instance: bool = True,
    drop_x: int = 0,
    drop_y: int = 0,
    collection: str = '',
) -> set[OperatorReturn]:
    """
    Add the dragged collection to the scene

    Args:
        session_uid: Session UID of the data-block to use by the operator

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

        use_instance: Add the dropped collection as collection instance

        drop_x: X-coordinate (screen space) to place the new object under

        drop_y: Y-coordinate (screen space) to place the new object under

        collection: Collection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def collection_instance_add(
    name: str = 'Collection',
    collection: str = '',
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
    session_uid: int = 0,
    drop_x: int = 0,
    drop_y: int = 0,
) -> set[OperatorReturn]:
    """
    Add a collection instance.

    Args:
        name: Collection name to add

        collection: Collection

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

        session_uid: Session UID of the data-block to use by the operator

        drop_x: X-coordinate (screen space) to place the new object under

        drop_y: Y-coordinate (screen space) to place the new object under

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def collection_link(collection: str = '') -> set[OperatorReturn]:
    """
    Add an object to an existing collection

    Args:
        collection: Collection

    Returns:
        Operation result.
    """
    pass


def collection_objects_select() -> set[OperatorReturn]:
    """
    Select all objects in collection

    Returns:
        Operation result.
    """
    pass


def collection_remove() -> set[OperatorReturn]:
    """
    Remove the active object from this collection

    Returns:
        Operation result.
    """
    pass


def collection_unlink() -> set[OperatorReturn]:
    """
    Unlink the collection from all objects

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def constraint_add(type: str = '') -> set[OperatorReturn]:
    """
    Add a constraint to the active object

    Args:
        type: Type

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def constraint_add_with_targets(type: str = '') -> set[OperatorReturn]:
    """
    Add a constraint to the active object, with target (where applicable) set to
    the selected objects/bones.

    Args:
        type: Type

    Returns:
        Operation result.
    """
    pass


def constraints_clear() -> set[OperatorReturn]:
    """
    Clear all constraints from the selected objects

    Returns:
        Operation result.
    """
    pass


def constraints_copy() -> set[OperatorReturn]:
    """
    Copy constraints to other selected objects

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def convert(
    target: Literal['CURVE', 'MESH', 'GPENCIL', 'CURVES'] = 'MESH',
    keep_original: bool = False,
    merge_customdata: bool = True,
    angle: float = 1.22173,
    thickness: int = 5,
    seams: bool = False,
    faces: bool = True,
    offset: float = 0.01,
) -> set[OperatorReturn]:
    """
    Convert selected objects to another type

    Args:
        target: Type of object to convert to

            CURVE: Curve from Mesh or Text objects.

            MESH: Mesh from Curve, Surface, Metaball, or Text objects.

            GPENCIL: Grease Pencil from Curve or Mesh objects.

            CURVES: Curves from evaluated curve data.

        keep_original: Keep Original, Keep original objects instead of replacing
            them

        merge_customdata: Merge UVs, Merge UV coordinates that share a vertex to
            account for imprecision in some modifiers.

        angle: Threshold Angle, Threshold to determine ends of the strokes.

            [0, 3.14159]

        thickness: Thickness

            [1, 100]

        seams: Convert only seam edges

        faces: Export faces as filled strokes

        offset: Offset strokes from fill

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def correctivesmooth_bind(modifier: str = '') -> set[OperatorReturn]:
    """
    Bind base pose in Corrective Smooth modifier

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def curves_empty_hair_add(
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an empty curve object to the scene with the selected mesh as surface

    Args:
        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def curves_random_add(
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a curves object with random curves to the scene

    Args:
        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyShadowingNames
def data_instance_add(
    name: str = '',
    session_uid: int = 0,
    type: IdType = 'ACTION',
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
    drop_x: int = 0,
    drop_y: int = 0,
) -> set[OperatorReturn]:
    """
    Add an object data instance

    Args:
        name: Name of the data-block to use by the operator

        session_uid: Session UID, Session UID of the data-block to use by the
            operator.

        type: Type

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

        drop_x: X-coordinate (screen space) to place the new object under

        drop_y: Y-coordinate (screen space) to place the new object under

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def data_transfer(
    use_reverse_transfer: bool = False,
    use_freeze: bool = False,
    data_type: Literal[
        'VGROUP_WEIGHTS',
        'BEVEL_WEIGHT_VERT',
        'COLOR_VERTEX',
        'SHARP_EDGE',
        'SEAM',
        'CREASE',
        'BEVEL_WEIGHT_EDGE',
        'FREESTYLE_EDGE',
        'CUSTOM_NORMAL',
        'COLOR_CORNER',
        'UV',
        'SMOOTH',
        'FREESTYLE_FACE'
    ] = '',
    use_create: bool = True,
    vert_mapping: DtMethodVertex = 'NEAREST',
    edge_mapping: DtMethodEdge = 'NEAREST',
    loop_mapping: DtMethodLoop = 'NEAREST_POLYNOR',
    poly_mapping: DtMethodPoly = 'NEAREST',
    use_auto_transform: bool = False,
    use_object_transform: bool = True,
    use_max_distance: bool = False,
    max_distance: float = 1.0,
    ray_radius: float = 0.0,
    islands_precision: float = 0.1,
    layers_select_src: DtLayersSelectSrc = 'ACTIVE',
    layers_select_dst: DtLayersSelectDst = 'ACTIVE',
    mix_mode: DtMixMode = 'REPLACE',
    mix_factor: float = 1.0,
) -> set[OperatorReturn]:
    """
    Transfer data layer(s) (weights, edge sharp, etc.) from active to selected
    meshes.

    Args:
        use_reverse_transfer: Transfer from selected objects to active one

        use_freeze: Prevent changes to settings to re-run the operator, handy to
            change several things at once with heavy geometry.

        data_type: Which data to transfer

            VGROUP_WEIGHTS: Transfer active or all vertex groups.

            BEVEL_WEIGHT_VERT: Transfer bevel weights.

            COLOR_VERTEX: Color Attributes.

            SHARP_EDGE: Transfer sharp mark.

            SEAM: Transfer UV seam mark.

            CREASE: Transfer crease values.

            BEVEL_WEIGHT_EDGE: Transfer bevel weights.

            FREESTYLE_EDGE: Transfer Freestyle edge mark.

            CUSTOM_NORMAL: Transfer custom normals.

            COLOR_CORNER: Color Attributes.

            UV: Transfer UV layers.

            SMOOTH: Transfer flat/smooth mark.

            FREESTYLE_FACE: Transfer Freestyle face mark.

        use_create: Add data layers on destination meshes if needed

        vert_mapping: Method used to map source vertices to destination ones

        edge_mapping: Method used to map source edges to destination ones

        loop_mapping: Method used to map source faces’ corners to destination
            ones.

        poly_mapping: Method used to map source faces to destination ones.

        use_auto_transform: Automatically compute transformation to get the best
            possible match between source and destination meshes.

            Warning: Results will never be as good as manual matching of
            objects.

        use_object_transform: Object Transform, Evaluate source and destination
            meshes in global space.

        use_max_distance: Source elements must be closer than given distance
            from destination one.

        max_distance: Max Distance, Maximum allowed distance between source and
            destination element, for non-topology mappings.

            [0, inf]

        ray_radius: ‘Width’ of rays (especially useful when raycasting against
            vertices or edges)

            [0, inf]

        islands_precision: Factor controlling precision of islands handling (the
            higher, the better the results).

            [0, 10]

        layers_select_src: Which layers to transfer, in case of multi-layers
            types.

        layers_select_dst: How to match source and destination layers.

        mix_mode: How to affect destination elements with source values.

        mix_factor: Factor to use when applying data to destination (exact
            behavior depends on mix mode).

            [0, 1]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def datalayout_transfer(
    modifier: str = '',
    data_type: Literal[
        'VGROUP_WEIGHTS',
        'BEVEL_WEIGHT_VERT',
        'COLOR_VERTEX',
        'SHARP_EDGE',
        'SEAM',
        'CREASE',
        'BEVEL_WEIGHT_EDGE',
        'FREESTYLE_EDGE',
        'CUSTOM_NORMAL',
        'COLOR_CORNER',
        'UV',
        'SMOOTH',
        'FREESTYLE_FACE',
    ] = '',
    use_delete: bool = False,
    layers_select_src: DtLayersSelectSrc = 'ACTIVE',
    layers_select_dst: DtLayersSelectDst = 'ACTIVE',
) -> set[OperatorReturn]:
    """
    Transfer layout of data layer(s) from active to selected meshes

    Args:

        modifier: Name of the modifier to edit

        data_type: Which data to transfer

            VGROUP_WEIGHTS: Transfer active or all vertex groups.

            BEVEL_WEIGHT_VERT: Transfer bevel weights.

            COLOR_VERTEX: Color Attributes.

            SHARP_EDGE: Transfer sharp mark.

            SEAM: Transfer UV seam mark.

            CREASE: Transfer crease values.

            BEVEL_WEIGHT_EDGE: Transfer bevel weights.

            FREESTYLE_EDGE: Transfer Freestyle edge mark.

            CUSTOM_NORMAL: Transfer custom normals.

            COLOR_CORNER: Color Attributes.

            UV: Transfer UV layers.

            SMOOTH: Transfer flat/smooth mark.

            FREESTYLE_FACE: Transfer Freestyle face mark.

        use_delete: Also delete some data layers from destination if necessary,
            so that it matches exactly source.

        layers_select_src: Which layers to transfer, in case of multi-layers
            types.

        layers_select_dst: How to match source and destination layers

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def delete(use_global: bool = False, confirm: bool = True) -> set[OperatorReturn]:
    """
    Delete selected objects

    Args:
        use_global: Remove object from all scenes

        confirm: Prompt for confirmation

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def drop_geometry_nodes(session_uid: int = 0, show_datablock_in_modifier: bool = True) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        session_uid: Session UID of the geometry node group being dropped

        show_datablock_in_modifier: Show the datablock selector in the modifier

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def drop_named_image(
    filepath: str = '',
    relative_path: bool = True,
    name: str = '',
    session_uid: int = 0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an empty image type to scene with data

    Args:
        filepath: Path to image file

        relative_path: Relative Path, Select the file relative to the blend file

        name: Name of the data-block to use by the operator

        session_uid: Session UID of the data-block to use by the operator

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location, Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale, Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def drop_named_material(name: str = '', session_uid: int = 0) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        name: Name of the data-block to use by the operator

        session_uid: Session UID of the data-block to use by the operator

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def duplicate(linked: bool = False, mode: TransformMode = 'TRANSLATION') -> set[OperatorReturn]:
    """
    Duplicate selected objects

    Args:
        linked: Duplicate object but not object data, linking to the original data

        mode: Mode

    Returns:
        Operation result.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def duplicate_move(
    OBJECT_OT_duplicate: OBJECT_OT_duplicate = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate = None,
) -> set[OperatorReturn]:
    """
    Duplicate the selected objects and move them

    Args:
        OBJECT_OT_duplicate: Duplicate selected objects

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation result.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def duplicate_move_linked(
    OBJECT_OT_duplicate: OBJECT_OT_duplicate = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate = None,
) -> set[OperatorReturn]:
    """
    Duplicate the selected objects, but not their object data, and move them

    Args:
        OBJECT_OT_duplicate: Duplicate selected objects

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def duplicates_make_real(use_base_parent: bool = False, use_hierarchy: bool = False) -> set[OperatorReturn]:
    """
    Make instanced objects attached to this object real

    Args:
        use_base_parent: Parent newly created objects to the original instancer

        use_hierarchy: Maintain parent child relationships

    Returns:
        Operation result.
    """
    pass


def editmode_toggle() -> set[OperatorReturn]:
    """
    Toggle object’s edit mode

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyShadowingNames
def effector_add(
    type: Literal[
        'FORCE',
        'WIND',
        'VORTEX',
        'MAGNET',
        'HARMONIC',
        'CHARGE',
        'LENNARDJ',
        'TEXTURE',
        'GUIDE',
        'BOID',
        'TURBULENCE',
        'DRAG',
        'FLUID',
    ] = 'FORCE',
    radius: float = 1.0,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an empty object with a physics effector to the scene

    Args:
        type: Type

        radius: Radius

            [0, inf]

        enter_editmode: Enter edit mode when adding this object

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: , (optional)) – Scale, Scale for the newly added object

            Vector of 3 items in [-inf, in

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyShadowingNames
def empty_add(
    type: ObjectEmptyDrawtype = 'PLAIN_AXES',
    radius: float = 1.0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an empty object to the scene

    Args:
        type: Type

        radius: Radius

            [0, inf]

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location:: Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: , (optional)) – Scale, Scale for the newly added object

            Vector of 3 items in [-inf, in

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def explode_refresh(modifier: str = '') -> set[OperatorReturn]:
    """
    Refresh data in the Explode modifier

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


def forcefield_toggle() -> set[OperatorReturn]:
    """
    Toggle object’s force field

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def geometry_node_bake_delete_single(
    session_uid: int = 0,
    modifier_name: str = '',
    bake_id: int = 0
) -> set[OperatorReturn]:
    """
    Delete baked data of a single bake node or simulation

    Args:

        session_uid: Session UID of the data-block to use by the operator

        modifier_name: Name of the modifier that contains the node

        bake_id: Nested node id of the node
            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def geometry_node_bake_single(
    session_uid: int = 0,
    modifier_name: str = '',
    bake_id: int = 0,
) -> set[OperatorReturn]:
    """
    Bake a single bake node or simulation

    Args:
        session_uid: Session UID of the data-block to use by the operator

        modifier_name: Name of the modifier that contains the node

        bake_id: Nested node id of the node

            [0, inf]

    Returns:
        Operation result.
    """
    pass


def geometry_node_tree_copy_assign() -> set[OperatorReturn]:
    """
    Copy the active geometry node group and assign it to the active modifier

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def geometry_nodes_input_attribute_toggle(input_name: str = '', modifier_name: str = '') -> set[OperatorReturn]:
    """
    Switch between an attribute and a single value to define the data for every element

    Args:
        input_name: Input Name

        modifier_name: Modifier Name

    Returns:
        Operation result.
    """
    pass


def geometry_nodes_move_to_nodes() -> set[OperatorReturn]:
    """
    Move inputs and outputs from in the modifier to a new node group

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames,PyShadowingBuiltins
def gpencil_add(
    radius: float = 1.0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
    type: ObjectGpencilType = 'EMPTY',
    use_in_front: bool = True,
    stroke_depth_offset: float = 0.05,
    use_lights: bool = False,
    stroke_depth_order: Literal['2D', '3D'] = '3D',
) -> set[OperatorReturn]:
    """
    Add a Grease Pencil object to the scene

    Args:
        radius: Radius

            [0, inf]

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location, Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, in

        type: Type

        use_in_front: Show line art grease pencil in front of everything

        stroke_depth_offset: Stroke offset for the line art modifier

            [0, inf]

        use_lights: Use Lights, Use lights for this grease pencil object

        stroke_depth_order: Defines how the strokes are ordered in 3D space (for
            objects not displayed ‘In Front’).

            2D: Display strokes using grease pencil layers to define order.

            3D: Display strokes using real 3D position in 3D space.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def gpencil_modifier_add(type: ObjectGreasepencilModifierType = 'GP_THICK') -> set[OperatorReturn]:
    """
    Add a procedural operation/effect to the active grease pencil object

    Args:
        type: Type

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_apply(
    apply_as: Literal['DATA', 'SHAPE'] = 'DATA',
    modifier: str = '',
    report: bool = False,
) -> set[OperatorReturn]:
    """
    Apply modifier and remove from the stack

    Args:
        apply_as: How to apply the modifier to the geometry

            DATA: Apply modifier to the object’s data.

            SHAPE: Apply deform-only modifier to a new shape on this object.

        modifier: Name of the modifier to edit

        report: Create a notification after the operation

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_copy(modifier: str = '') -> set[OperatorReturn]:
    """
    Duplicate modifier at the same position in the stack

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_copy_to_selected(modifier: str = '') -> set[OperatorReturn]:
    """
    Copy the modifier from the active object to all selected objects

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_move_down(modifier: str = '') -> set[OperatorReturn]:
    """
    Move modifier down in the stack

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_move_to_index(modifier: str = '', index: int = 0) -> set[OperatorReturn]:
    """
    Change the modifier’s position in the list so it evaluates after the set
    number of others.

    Args:
        modifier: Name of the modifier to edit

        index: The index to move the modifier to

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def gpencil_modifier_move_up(modifier: str = '') -> set[OperatorReturn]:
    """
    Move modifier up in the stack

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


def gpencil_modifier_remove(modifier: str = '', report: bool = False) -> set[OperatorReturn]:
    """
    Remove a modifier from the active grease pencil object

    Args:
        modifier: Name of the modifier to edit

        report: Create a notification after the operation

    Returns:
        Operation result.
    """
    pass


def grease_pencil_add(
    type: ObjectGpencilType = 'EMPTY',
    radius: float = 1.0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a Grease Pencil object to the scene

    Args:
        type: Type

        radius: Radius

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: , (optional)) – Scale, Scale for the newly added object

            Vector of 3 items in [-inf, in

    Returns:
        Operation result.
    """
    pass


def hide_collection(collection_index: int = -1, toggle: bool = False, extend: bool = False) -> set[OperatorReturn]:
    """
    Show only objects in collection (Shift to extend)

    Args:
        collection_index: Index of the collection to change visibility

            [-1, inf]

        toggle: Toggle visibility

        extend: Extend visibility

    Returns:
        Operation result.
    """
    pass


def hide_render_clear_all() -> set[OperatorReturn]:
    """
    Reveal all render objects by setting the hide render flag

    Returns:
        Operation result.
    """
    pass


def hide_view_clear(select: bool = True) -> set[OperatorReturn]:
    """
    Reveal temporarily hidden objects

    Args:
        select: Select

    Returns:
        Operation result.
    """
    pass


def hide_view_set(unselected: bool = False) -> set[OperatorReturn]:
    """
    Temporarily hide objects from the viewport

    Args:
        unselected: Hide unselected rather than selected objects

    Returns:
        Operation result.
    """
    pass


def hook_add_newob() -> set[OperatorReturn]:
    """
    Hook selected vertices to a newly created object

    Returns:
        Operation result.
    """
    pass


def hook_add_selob(use_bone: bool = False) -> set[OperatorReturn]:
    """
    Hook selected vertices to the first selected object

    Args:
        use_bone: Assign the hook to the hook object’s active bone

    Returns:
        Operation result.
    """
    pass


def hook_assign(modifier: str = '') -> set[OperatorReturn]:
    """
    Assign the selected vertices to a hook

    Args:
        modifier: Modifier number to assign to

    Returns:
        Operation result.
    """
    pass


def hook_recenter(modifier: str = '') -> set[OperatorReturn]:
    """
    Set hook center to cursor position

    Args:
        modifier: Modifier number to assign to

    Returns:
        Operation result.
    """
    pass


def hook_remove(modifier: str = '') -> set[OperatorReturn]:
    """
    Remove a hook from the active object

    Args:
        modifier: Modifier number to remove

    Returns:
        Operation result.
    """
    pass


def hook_reset(modifier: str = '') -> set[OperatorReturn]:
    """
    Recalculate and clear offset transformation

    Args:
        modifier: Modifier number to assign to

    Returns:
        Operation result.
    """
    pass


def hook_select(modifier: str = '') -> set[OperatorReturn]:
    """
    Select affected vertices on mesh

    Args:
        modifier: Modifier number to remove

    Returns:
        Operation result.
    """
    pass


def instance_offset_from_cursor() -> set[OperatorReturn]:
    """
    Set offset used for collection instances based on cursor position

    Returns:
        Operation result.
    """
    pass


def instance_offset_from_object() -> set[OperatorReturn]:
    """
    Set offset used for collection instances based on the active object position

    Returns:
        Operation result.
    """
    pass


def instance_offset_to_cursor() -> set[OperatorReturn]:
    """
    Set cursor position to the offset used for collection instances

    Returns:
        Operation result.
    """
    pass


def isolate_type_render() -> set[OperatorReturn]:
    """
    Hide unselected render objects of same type as active by setting the hide render flag

    Returns:
        Operation result.
    """
    pass


def join() -> set[OperatorReturn]:
    """
    Join selected objects into active object

    Returns:
        Operation result.
    """
    pass


def join_shapes() -> set[OperatorReturn]:
    """
    Copy the current resulting shape of another selected object to this one

    Returns:
        Operation result.
    """
    pass


def join_uvs() -> set[OperatorReturn]:
    """
    Transfer UV Maps from active to selected objects (needs matching geometry)

    Returns:
        Operation result.
    """
    pass


def laplaciandeform_bind(modifier: str = '') -> set[OperatorReturn]:
    """
    Bind mesh to system in laplacian deform modifier

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


def light_add(
    type: LightType = 'POINT',
    radius: float = 1.0,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a light object to the scene

    Args:
        type: Type

        radius: Radius

            [0, inf]

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: , (optional)) – Scale, Scale for the newly added object

            Vector of 3 items in [-inf, in

    Returns:
        Operation result.
    """
    pass


def light_linking_blocker_collection_new() -> set[OperatorReturn]:
    """
    Create new light linking collection used by the active emitter

    Returns:
        Operation result.
    """
    pass


def light_linking_blockers_link(link_state: Literal['INCLUDE', 'EXCLUDE'] = 'INCLUDE') -> set[OperatorReturn]:
    """
    Light link selected blockers to the active emitter object

    Args:
        link_state: State of the shadow linking

            INCLUDE: Include selected blockers to cast shadows from the active
                emitter.

            EXCLUDE: Exclude selected blockers from casting shadows from the
                active emitter.

    Returns:
        Operation result.
    """
    pass


def light_linking_blockers_select() -> set[OperatorReturn]:
    """
    Select all objects which block light from this emitter

    Returns:
        Operation result.
    """
    pass


def light_linking_receiver_collection_new() -> set[OperatorReturn]:
    """
    Create new light linking collection used by the active emitter

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def light_linking_receivers_link(link_state: Literal['INCLUDE', 'EXCLUDE'] = 'INCLUDE') -> set[OperatorReturn]:
    """
    Light link selected receivers to the active emitter object

    Args:
        link_state: State of the light linking

            INCLUDE: Include selected receivers to receive light from the active
                emitter.

            EXCLUDE: Exclude selected receivers from receiving light from the
                active emitter.

    Returns:
        Operation result.
    """
    pass


def light_linking_receivers_select() -> set[OperatorReturn]:
    """
    Select all objects which receive light from this emitter

    Returns:
        Operation result.
    """
    pass


def light_linking_unlink_from_collection() -> set[OperatorReturn]:
    """
    Remove this object or collection from the light linking collection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames,PyShadowingBuiltins
def lightprobe_add(
    type: Literal['SPHERE', 'PLANE', 'VOLUME'] = 'SPHERE',
    radius: float = 1.0,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a light probe object

    Args:
        type:

            SPHERE: Light probe that captures precise lighting from all
                directions at a single point in space.

            PLANE: Light probe that captures incoming light from a single
                direction on a plane.

            VOLUME: Light probe that captures low frequency lighting inside a
                volume.

        radius: Radius

            [0, inf]

        enter_editmode: Enter edit mode when adding this object

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, in

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def lightprobe_cache_bake(
    delay: int = 0,
    subset: Literal['ALL', 'SELECTED', 'ACTIVE'] = 'ALL',
) -> set[OperatorReturn]:
    """
    Bake irradiance volume light cache

    Args:
        delay: Delay in millisecond before baking starts.

            [0, 2000]

        subset:

        Subset, Subset of probes to update

            ALL: Bake all light probe volumes.

            SELECTED: Only bake selected light probe volumes.

            ACTIVE: Only bake the active light probe volume.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def lightprobe_cache_free(subset: Literal['ALL', 'SELECTED', 'ACTIVE'] = 'SELECTED') -> set[OperatorReturn]:
    """
    Delete cached indirect lighting

    Args:
        subset: Subset of probes to update

            ALL: Delete all light probes’ baked lighting data.

            SELECTED: Only delete selected light probes’ baked lighting data.

            ACTIVE: Only delete the active light probe’s baked lighting data.

    Returns:
        Operation result.
    """
    pass


def lineart_bake_strokes() -> set[OperatorReturn]:
    """
    Bake Line Art for current GPencil object

    Returns:
        Operation result.
    """
    pass


def lineart_bake_strokes_all() -> set[OperatorReturn]:
    """
    Bake all Grease Pencil objects that have a line art modifier

    Returns:
        Operation result.
    """
    pass


def lineart_clear() -> set[OperatorReturn]:
    """
    Clear all strokes in current GPencil object

    Returns:
        Operation result.
    """
    pass


def lineart_clear_all() -> set[OperatorReturn]:
    """
    Clear all strokes in all Grease Pencil objects that have a line art modifier

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def link_to_collection(
    collection_index: int = -1,
    is_new: bool = False,
    new_collection_name: str = '',
) -> set[OperatorReturn]:
    """
    Link objects to a collection

    Args:
        collection_index: Index of the collection to move to

            [-1, inf]

        is_new: Move objects to a new collection

        new_collection_name: Name of the newly added collection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def load_background_image(
    filepath: str = '',
    filter_image: bool = True,
    filter_movie: bool =True,
    filter_folder: bool = True,
    view_align: bool = True
) -> set[OperatorReturn]:
    """
    Add a reference image into the background behind objects

    Args:
        filepath:

        filter_image:

        filter_movie:

        filter_folder:

        view_align: Align to View

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def load_reference_image(
    filepath: str = '',
    filter_image: bool = True,
    filter_movie: bool = True,
    filter_folder: bool = True,
    view_align: bool = True,
) -> set[OperatorReturn]:
    """
    Add a reference image into the scene between objects

    Args:
        filepath:

        filter_image:

        filter_movie:

        filter_folder:

        view_align: Align to View

    Returns:
        Operation result.
    """
    pass


# noinspection PyIncorrectDocstring
def location_clear(clear_delta: bool = False) -> set[OperatorReturn]:
    """
    Clear the object’s location

    Args:
        clear_delta: Clear Delta, Clear delta location in addition to clearing
            the normal location transform

    Returns:
        Operation result.
    """
    pass


def make_dupli_face() -> set[OperatorReturn]:
    """
    Convert objects into instanced faces

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def make_links_data(
    type: Literal[
        'OBDATA',
        'MATERIAL',
        'ANIMATION',
        'GROUPS',
        'DUPLICOLLECTION',
        'FONTS',
        'MODIFIERS',
        'EFFECTS',
    ] = 'OBDATA',
) -> set[OperatorReturn]:
    """
    Transfer data from active object to selected objects

    Args:
        type:
            OBDATA: Replace assigned Object Data.

            MATERIAL: Replace assigned Materials.

            ANIMATION: Replace assigned Animation Data.

            GROUPS: Replace assigned Collections.

            DUPLICOLLECTION: Replace assigned Collection Instance.

            FONTS: Replace Text object Fonts.

            MODIFIERS: Replace Modifiers.

            EFFECTS: Replace Grease Pencil Effects.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def make_links_scene(scene: str = '') -> set[OperatorReturn]:
    """
    Link selection to another scene

    Args:
        scene: Scene

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def make_local(
    type: Literal['SELECT_OBJECT', 'SELECT_OBDATA', 'SELECT_OBDATA_MATERIAL', 'ALL'] = 'SELECT_OBJECT',
) -> set[OperatorReturn]:
    """
    Make library linked data-blocks local to this file

    Args:
        type: Type

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def make_override_library(collection: int = 0) -> set[OperatorReturn]:
    """
    Create a local override of the selected linked objects, and their hierarchy
    of dependencies.

    Args:
        collection: Session UID of the directly linked collection containing the
            selected object, to make an override from.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def make_single_user(
    type: Literal['SELECTED_OBJECTS', 'ALL'] = 'SELECTED_OBJECTS',
    object: bool = False,
    obdata: bool = False,
    material: bool = False,
    animation: bool = False,
    obdata_animation: bool = False,
) -> set[OperatorReturn]:
    """
    Make linked data local to each object

    Args:
        type:

        object: Make single user objects

        obdata: Make single user object data

        material: Make materials local to each data-block

        animation: Make object animation data local to each object

        obdata_animation: Make object data (mesh, curve etc.) animation data
            local to each object

    Returns:
        Operation result.
    """
    pass


def material_slot_add() -> set[OperatorReturn]:
    """
    Add a new material slot

    Returns:
        Operation result.
    """
    pass


def material_slot_assign() -> set[OperatorReturn]:
    """
    Assign active material slot to selection

    Returns:
        Operation result.
    """
    pass


def material_slot_copy() -> set[OperatorReturn]:
    """
    Copy material to selected objects

    Returns:
        Operation result.
    """
    pass


def material_slot_deselect() -> set[OperatorReturn]:
    """
    Deselect by active material slot

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def material_slot_move(direction: Literal['UP', 'DOWN'] = 'UP') -> set[OperatorReturn]:
    """
    Move the active material up/down in the list

    Args:
        direction: Direction to move the active material towards

    Returns:
        Operation result.
    """
    pass


def material_slot_remove() -> set[OperatorReturn]:
    """
    Remove the selected material slot

    Returns:
        Operation result.
    """
    pass


def material_slot_remove_unused() -> set[OperatorReturn]:
    """
    Remove unused material slots

    Returns:
        Operation result.
    """
    pass


def material_slot_select() -> set[OperatorReturn]:
    """
    Select by active material slot

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def meshdeform_bind(modifier: str = '') -> set[OperatorReturn]:
    """
    Bind mesh to cage in mesh deform modifier

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins,PyShadowingNames
def metaball_add(
    type: MetaelemType = 'BALL',
    radius: float = 2.0,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add an metaball object to the scene

    Args:
            type: Primitive

            radius: Radius

                [0, inf]

            enter_editmode: Enter edit mode when adding this object

            align: The alignment of the new object

                WORLD: Align the new object to the world.

                VIEW: Align the new object to the view.

                CURSOR: Use the 3D cursor orientation for the new object.

            location: Location for the newly added object

                Vector of 3 items in [-inf, in

            rotation: Rotation for the newly added object

                Euler rotation of 3 items in [-inf, inf]

            scale: Scale for the newly added object

                Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def mode_set(mode: ObjectMode = 'OBJECT', toggle: bool = False) -> set[OperatorReturn]:
    """
    Sets the object interaction mode

    Args:
        mode: Mode

        toggle: Toggle

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyDefaultArgument
def mode_set_with_submode(
    mode: ObjectMode = 'OBJECT',
    toggle: bool = False,
    mesh_select_mode: set[MeshSelectMode] = set(),
) -> set[OperatorReturn]:
    """
    Sets the object interaction mode

    Args:
        mode:

        toggle:

        mesh_select_mode: Mesh Mode

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def modifier_add(type: ObjectModifierType = 'SUBSURF') -> set[OperatorReturn]:
    """
    Add a procedural operation/effect to the active object

    Args:
        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_add_node_group(
    asset_library_type: AssetLibraryType = 'LOCAL',
    asset_library_identifier: str = '',
    relative_asset_identifier: str = '',
    session_uid: int = 0,
) -> set[OperatorReturn]:
    """
    Add a procedural operation/effect to the active object

    Args:
        asset_library_type: Asset Library Type

        asset_library_identifier: Asset Library Identifier

        relative_asset_identifier: Relative Asset Identifier

        session_uid: Session UID of the data-block to use by the operator

            [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_apply(
    modifier: str = '',
    report: bool = False,
    merge_customdata: bool = True,
    single_user: bool = False,
) -> set[OperatorReturn]:
    """
    Apply modifier and remove from the stack

    Args:
        modifier: Name of the modifier to edit

        report: Create a notification after the operation

        merge_customdata: Merge UVs, For mesh objects, merge UV coordinates that
            share a vertex to account for imprecision in some modifiers.

        single_user: Make the object’s data single user if needed

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_apply_as_shapekey(
    keep_modifier: bool = False,
    modifier: str = '',
    report: bool = False,
) -> set[OperatorReturn]:
    """
    Apply modifier as a new shape key and remove from the stack

    Args:
        keep_modifier: Do not remove the modifier from stack

        modifier: Name of the modifier to edit

        report: Create a notification after the operation

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_convert(modifier: str = '') -> set[OperatorReturn]:
    """
    Convert particles to a mesh object

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_copy(modifier: str = '') -> set[OperatorReturn]:
    """
    Duplicate modifier at the same position in the stack

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_copy_to_selected(modifier: str = '') -> set[OperatorReturn]:
    """
    Copy the modifier from the active object to all selected objects

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_move_down(modifier: str = '') -> set[OperatorReturn]:
    """
    Move modifier down in the stack

    Args:
        modifier: Modifier, Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_move_to_index(modifier: str = '', index: int = 0) -> set[OperatorReturn]:
    """
    Change the modifier’s index in the stack so it evaluates after the set
    number of others.

    Args:
        modifier: Name of the modifier to edit

        index: The index to move the modifier to

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_move_up(modifier: str = '') -> set[OperatorReturn]:
    """
    Move modifier up in the stack

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_remove(modifier: str = '', report: bool = False) -> set[OperatorReturn]:
    """
    Remove a modifier from the active object

    Args:
        modifier: Name of the modifier to edit

        report: Create a notification after the operation

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def modifier_set_active(modifier: str = '') -> set[OperatorReturn]:
    """
    Activate the modifier to use as the context

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def move_to_collection(
    collection_index: int = -1,
    is_new: bool = False,
    new_collection_name: str = '',
) -> set[OperatorReturn]:
    """
    Move objects to a collection

    Args:
        collection_index: Index of the collection to move to

            [-1, inf]

        is_new: Move objects to a new collection

        new_collection_name: Name of the newly added collection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_base_apply(modifier: str = '') -> set[OperatorReturn]:
    """
    Modify the base mesh to conform to the displaced mesh

    Args:
        modifier (string, (optional, never None)) – Modifier, Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


def multires_external_pack() -> set[OperatorReturn]:
    """
    Pack displacements from an external file

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_external_save(
    filepath: str = '',
    hide_props_region: bool = True,
    check_existing: bool = True,
    filter_blender: bool = False,
    filter_backup: bool = False,
    filter_image: bool = False,
    filter_movie: bool = False,
    filter_python: bool = False,
    filter_font: bool = False,
    filter_sound: bool = False,
    filter_text: bool = False,
    filter_archive: bool = False,
    filter_btx: bool = True,
    filter_collada: bool = False,
    filter_alembic: bool = False,
    filter_usd: bool = False,
    filter_obj: bool = False,
    filter_volume: bool = False,
    filter_folder: bool = True,
    filter_blenlib: bool = False,
    filemode: int = 9,
    relative_path: bool = True,
    display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL'] = 'DEFAULT',
    sort_method: str = '',
    modifier: str = ''
) -> set[OperatorReturn]:
    """
    Save displacements to an external file

    Args:
        filepath: Path to file

        hide_props_region: Collapse the region displaying the operator settings

        check_existing: Check and warn on overwriting existing files

        filter_blender: Filter .blend files

        filter_backup: Filter .blend files

        filter_image: Filter image files

        filter_movie: Filter movie files

        filter_python: Filter Python files

        filter_font: Filter font files

        filter_sound: Filter sound files

        filter_text: Filter text files

        filter_archive: Filter archive files

        filter_btx: Filter btx files

        filter_collada: Filter COLLADA files

        filter_alembic: Filter Alembic files

        filter_usd: Filter USD files

        filter_obj: Filter OBJ files

        filter_volume: Filter OpenVDB volume files

        filter_folder: Filter folders

        filter_blenlib: Filter Blender IDs

        filemode: The setting for the file browser mode to load a .blend file,
            a library or a special file

            [1, 9]

        relative_path: Select the file relative to the blend file

        display_type: Display Type

            DEFAULT: Automatically determine display type for files.

            LIST_VERTICAL: Display files as short list.

            LIST_HORIZONTAL: Display files as a detailed list.

            THUMBNAIL: Display files as thumbnails.

        sort_method: File sorting mode

        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_higher_levels_delete(modifier: str = '') -> set[OperatorReturn]:
    """
    Deletes the higher resolution mesh, potential loss of detail

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_rebuild_subdiv(modifier: str = '') -> set[OperatorReturn]:
    """
    Rebuilds all possible subdivisions levels to generate a lower resolution base mesh

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_reshape(modifier: str = '') -> set[OperatorReturn]:
    """
    Copy vertex coordinates from other object

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_subdivide(
    modifier: str = '',
    mode: Literal['CATMULL_CLARK', 'SIMPLE', 'LINEAR'] = 'CATMULL_CLARK',
) -> set[OperatorReturn]:
    """
    Add a new level of subdivision

    Args:
        modifier: Name of the modifier to edit

        mode: Subdivision Mode, How the mesh is going to be subdivided to create
            a new level

            CATMULL_CLARK: Create a new level using Catmull-Clark subdivisions.

            SIMPLE: Create a new level using simple subdivisions.

            LINEAR: Create a new level using linear interpolation of the
                sculpted displacement.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def multires_unsubdivide(modifier: str = '') -> set[OperatorReturn]:
    """
    Rebuild a lower subdivision level of the current base mesh

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def ocean_bake(modifier: str = '', free: bool = False) -> set[OperatorReturn]:
    """
    Bake an image sequence of ocean data

    Args:
        modifier: Name of the modifier to edit

        free: Free the bake, rather than generating it

    Returns:
        Operation result.
    """
    pass


def origin_clear() -> set[OperatorReturn]:
    """
    Clear the object’s origin

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def origin_set(
    type: Literal[
        'GEOMETRY_ORIGIN',
        'ORIGIN_GEOMETRY',
        'ORIGIN_CURSOR',
        'ORIGIN_CENTER_OF_MASS',
        'ORIGIN_CENTER_OF_VOLUME',
    ] = 'GEOMETRY_ORIGIN',
    center: Literal['MEDIAN', 'BOUNDS'] = 'MEDIAN',
) -> set[OperatorReturn]:
    """
    Set the object’s origin, by either moving the data, or set to center of
    data, or use 3D cursor

    Args:
        type: Type

            GEOMETRY_ORIGIN: Move object geometry to object origin.

            ORIGIN_GEOMETRY: Calculate the center of geometry based on the
                current pivot point (median, otherwise bounding box).

            ORIGIN_CURSOR: Move object origin to position of the 3D cursor.

            ORIGIN_CENTER_OF_MASS Origin to Center of Mass (Surface) –
                Calculate the center of mass from the surface area.

            ORIGIN_CENTER_OF_VOLUME Origin to Center of Mass (Volume) –
                Calculate the center of mass from the volume (must be
                manifold geometry with consistent normals).

        center: Center

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def parent_clear(type: Literal['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'] = 'CLEAR') -> set[OperatorReturn]:
    """
    Clear the object’s parenting

    Args:
        type: Type

            CLEAR: Completely clear the parenting relationship, including
                involved modifiers if any.

            CLEAR_KEEP_TRANSFORM: As ‘Clear Parent’, but keep the current visual
                transformations of the object.

            CLEAR_INVERSE: Reset the transform corrections applied to the
                parenting relationship, does not remove parenting itself.

    Returns:
        Operation result.
    """
    pass


def parent_inverse_apply() -> set[OperatorReturn]:
    """
    Apply the object’s parent inverse to its data

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def parent_no_inverse_set(confirm: bool = True, keep_transform: bool = False) -> set[OperatorReturn]:
    """
    Set the object’s parenting without setting the inverse parent correction

    Args:
        confirm: Prompt for confirmation

        keep_transform: Preserve the world transform throughout parenting

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def parent_set(
    type: Literal[
        'OBJECT',
        'ARMATURE',
        'ARMATURE_NAME',
        'ARMATURE_AUTO',
        'ARMATURE_ENVELOPE',
        'BONE',
        'BONE_RELATIVE',
        'CURVE',
        'FOLLOW',
        'PATH_CONST',
        'LATTICE',
        'VERTEX',
        'VERTEX_TRI',
    ] = 'OBJECT',
    xmirror: bool = False,
    keep_transform: bool = False,
) -> set[OperatorReturn]:
    """
    Set the object’s parenting

    Args:
        type: Type

        xmirror: Apply weights symmetrically along X axis, for
            Envelope/Automatic vertex groups creation

        keep_transform: Apply transformation before parenting

    Returns:
        Operation result.
    """
    pass


def particle_system_add() -> set[OperatorReturn]:
    """
    Add a particle system

    Returns:
        Operation result.
    """
    pass


def particle_system_remove() -> set[OperatorReturn]:
    """
    Remove the selected particle system

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def paths_calculate(
    display_type: MotionpathDisplayType = 'RANGE',
    range: MotionpathRange = 'SCENE',
) -> set[OperatorReturn]:
    """
    Generate motion paths for the selected objects

    Args:
        display_type: Display type

        range: Computation Range

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def paths_clear(only_selected: bool = False) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        only_selected: Only Selected, Only clear motion paths of selected
            objects

    Returns:
        Operation result.
    """
    pass


def paths_update() -> set[OperatorReturn]:
    """
    Recalculate motion paths for selected objects

    Returns:
        Operation result.
    """
    pass


def paths_update_visible() -> set[OperatorReturn]:
    """
    Recalculate all visible motion paths for objects and poses

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def pointcloud_add(
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a point cloud object to the scene

    Args:
        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


def posemode_toggle() -> set[OperatorReturn]:
    """
    Enable or disable posing/selecting bones

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def quadriflow_remesh(
    use_mesh_symmetry: bool = True,
    use_preserve_sharp: bool = False,
    use_preserve_boundary: bool = False,
    preserve_attributes: bool = False,
    smooth_normals: bool = False,
    mode: Literal['RATIO', 'EDGE', 'FACES'] = 'FACES',
    target_ratio: float = 1.0,
    target_edge_length: float = 0.1,
    target_faces: int = 4000,
    mesh_area: float = -1.0,
    seed: int = 0,
) -> set[OperatorReturn]:
    """
    Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

    Args:
        use_mesh_symmetry: Generates a symmetrical mesh using the mesh symmetry configuration

        use_preserve_sharp: Try to preserve sharp features on the mesh

        use_preserve_boundary: Try to preserve mesh boundary on the mesh

        preserve_attributes: Reproject attributes onto the new mesh

        smooth_normals: Set the output mesh normals to smooth

        mode: How to specify the amount of detail for the new mesh

            RATIO: Specify target number of faces relative to the current mesh.

            EDGE: Input target edge length in the new mesh.

            FACES: Input target number of faces in the new mesh.

        target_ratio: Relative number of faces compared to the current mesh

            [0, inf]

        target_edge_length: Target edge length in the new mesh

            [1e-07, inf]

        target_faces: Approximate number of faces (quads) in the new mesh

            [1, inf]

        mesh_area: Old Object Face Area, This property is only used to cache the
            object area for later calculations

            [-inf, inf]

        seed: Random seed to use with the solver. Different seeds will cause the
            remesher to come up with different quad layouts on the mesh

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def quick_explode(
    style: Literal['EXPLODE', 'BLEND'] = 'EXPLODE',
    amount: int = 100,
    frame_duration: int = 50,
    frame_start: int = 1,
    frame_end: int = 10,
    velocity: float = 1.0,
    fade: bool = True,
) -> set[OperatorReturn]:
    """
    Make selected objects explode

    Args:
        style: Explode Style

        amount: Number of Pieces

            [2, 10000]

        frame_duration: Duration

            [1, 300000]

        frame_start: Start Frame

            [1, 300000]

        frame_end: End Frame

            [1, 300000]

        velocity: Outwards Velocity

            [0, 300000]

        fade: Fade the pieces over time

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def quick_fur(
    density: Literal['LOW', 'MEDIUM', 'HIGH'] = 'MEDIUM',
    length: float = 0.1,
    radius: float = 0.001,
    view_percentage: float = 1.0,
    apply_hair_guides: bool = True,
    use_noise: bool = True,
    use_frizz: bool = True,
) -> set[OperatorReturn]:
    """
    Add a fur setup to the selected objects

    Args:
        density: Density

        length: Length

            [0.001, 100]

        radius: Hair Radius

            [0, 10]

        view_percentage: View Percentage

            [0, 1]

        apply_hair_guides: Apply Hair Guides

        use_noise: Noise

        use_frizz: Frizz

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def quick_liquid(show_flows: bool = False) -> set[OperatorReturn]:
    """
    Make selected objects liquid

    Args:
        show_flows: – Render Liquid Objects, Keep the liquid objects visible
            during rendering

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def quick_smoke(style: Literal['SMOKE', 'FIRE', 'BOTH'] = 'SMOKE', show_flows: bool = False) -> set[OperatorReturn]:
    """
    Use selected objects as smoke emitters

    Args:
        style: Smoke Style

        show_flows: Keep the smoke objects visible during rendering

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def randomize_transform(
    random_seed: int = 0,
    use_delta: bool = False,
    use_loc: bool = True,
    loc: Vector = Vector((0.0, 0.0, 0.0)),
    use_rot: bool = True,
    rot: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    use_scale: bool = True,
    scale_even: bool = False,
    scale: tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> set[OperatorReturn]:
    """
    Randomize objects location, rotation, and scale

    Args:
        random_seed: Seed value for the random generator.

            [0, 10000]

        use_delta: Transform Delta, randomize delta transform values instead of
            regular transform

        use_loc: Randomize the location values.

        loc: Maximum distance the objects can spread over each axis.

            Vector of 3 items in [-100, 100]

        use_rot: Randomize the rotation values

        rot: Maximum rotation over each axis

            Euler rotation of 3 items in [-3.14159, 3.14159]

        use_scale: Randomize the scale values

        scale_even: Use the same scale value for all axis

        scale: Maximum scale randomization over each axis

            3 items in [-100, 100]

    Returns:
        Operation result.
    """
    pass


def reset_override_library() -> set[OperatorReturn]:
    """
    Reset the selected local overrides to their linked references values

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def rotation_clear(clear_delta: bool = False) -> set[OperatorReturn]:
    """
    Clear the object’s rotation

    Args:
        clear_delta: Clear delta rotation in addition to clearing the normal
            rotation transform.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def scale_clear(clear_delta: bool = False) -> set[OperatorReturn]:
    """
    Clear the object’s scale

    Args:
        clear_delta: Clear delta scale in addition to clearing the normal scale
            transform.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_all(action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'] = 'TOGGLE') -> set[OperatorReturn]:
    """
    Change selection of all visible objects in scene

    Args:
        action: Selection action to execute

            TOGGLE: Toggle selection for all elements.

            SELECT: Select all elements.

            DESELECT: Deselect all elements.

            INVERT: Invert selection of all elements.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_by_type(extend: bool = False, type: ObjectType = 'MESH') -> set[OperatorReturn]:
    """
    Select all visible objects that are of a type

    Args:
        extend: Extend selection instead of deselecting everything first

        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_camera(extend: bool = False) -> set[OperatorReturn]:
    """
    Select the active camera

    Args:
        extend: Extend the selection

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_grouped(
    extend: bool = False,
    type: Literal[
        'CHILDREN_RECURSIVE',
        'CHILDREN',
        'PARENT',
        'SIBLINGS',
        'TYPE',
        'COLLECTION',
        'HOOK',
        'PASS',
        'COLOR',
        'KEYINGSET',
        'LIGHT_TYPE',
    ] = 'CHILDREN_RECURSIVE'
) -> set[OperatorReturn]:
    """
    Select all visible objects grouped by various properties

    Args:
        extend: Extend selection instead of deselecting everything first

        type: Type

            CHILDREN_RECURSIVE: Children.

            CHILDREN: Immediate Children.

            PARENT: Parent.

            SIBLINGS: Shared parent.

            TYPE: Shared object type.

            COLLECTION: Shared collection.

            HOOK: Hook.

            PASS: Render pass index.

            COLOR: Object color.

            KEYINGSET: Objects included in active Keying Set.

            LIGHT_TYPE: Matching light types.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_hierarchy(direction: Literal['PARENT', 'CHILD'] = 'PARENT', extend: bool = False) -> set[OperatorReturn]:
    """
    Select object relative to the active object’s position in the hierarchy

    Args:
        direction: Direction to select in the hierarchy

        extend: Extend the existing selection

    Returns:
        Operation result.
    """
    pass


def select_less() -> set[OperatorReturn]:
    """
    Deselect objects at the boundaries of parent/child relationships

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_linked(
    extend: bool = False,
    type: Literal['OBDATA', 'MATERIAL', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA'] = 'OBDATA',
) -> set[OperatorReturn]:
    """
    Select all visible objects that are linked

    Args:
        extend: Extend selection instead of deselecting everything first

        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_mirror(extend: bool = False) -> set[OperatorReturn]:
    """
    Select the mirror objects of the selected object e.g. “L.sword” and
    “R.sword”.

    Args:
        extend: Extend selection instead of deselecting everything first

    Returns:
        Operation result.
    """
    pass


def select_more() -> set[OperatorReturn]:
    """
    Select connected parent/child objects

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_pattern(pattern: str = '*', case_sensitive: bool = False, extend: bool = True) -> set[OperatorReturn]:
    """
    Select objects matching a naming pattern

    Args:
        pattern: Pattern, name filter using ‘*’, ‘?’ and ‘[abc]’ unix style
            wildcards

        case_sensitive: Do a case sensitive compare

        extend: Extend the existing selection


    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_random(
    ratio: float = 0.5,
    seed: int = 0,
    action: Literal['SELECT', 'DESELECT'] = 'SELECT',
) -> set[OperatorReturn]:
    """
    Select or deselect random visible objects

    Args:
        ratio: Portion of items to select randomly

            [0, 1]

        seed: Seed for the random number generator
            [0, inf]

        action: Selection action to execute

            SELECT: Select all elements.

            DESELECT: Deselect all elements.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def select_same_collection(collection: str = '') -> set[OperatorReturn]:
    """
    Select object in the same collection

    Args:
        collection: Name of the collection to select

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shade_flat(keep_sharp_edges: bool = True) -> set[OperatorReturn]:
    """
    Render and display faces uniform, using face normals

    Args:
        keep_sharp_edges: Keep Sharp Edges, Don’t remove sharp edges, which are
            redundant with faces shaded smooth

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shade_smooth(keep_sharp_edges: bool = True) -> set[OperatorReturn]:
    """
    Render and display faces smooth, using interpolated vertex normals

    Args:
        keep_sharp_edges: Keep Sharp Edges, Don’t remove sharp edges. Tagged
            edges will remain sharp

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shade_smooth_by_angle(angle: float = 0.523599, keep_sharp_edges: bool = True) -> set[OperatorReturn]:
    """
    Set the sharpness of mesh edges based on the angle between the neighboring
    faces.

    Args:
        angle: Maximum angle between face normals that will be considered as
            smooth.

            [0, 3.14159]

        keep_sharp_edges: Keep Sharp Edges, Only add sharp edges instead of
            clearing existing tags first

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def shaderfx_add(type: ObjectShaderfxType = 'FX_BLUR') -> set[OperatorReturn]:
    """
    Add a visual effect to the active object

    Args:
        type: Type

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shaderfx_copy(shaderfx: str = '') -> set[OperatorReturn]:
    """
    Duplicate effect at the same position in the stack

    Args:
        shaderfx: Name of the shaderfx to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shaderfx_move_down(shaderfx: str = '') -> set[OperatorReturn]:
    """
    Move effect down in the stack.

    Args:
        shaderfx: Name of the shaderfx to edit.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shaderfx_move_to_index(shaderfx: str = '', index: int = 0) -> set[OperatorReturn]:
    """
    Change the effect’s position in the list, so it evaluates after the set
    number of others.

    Args:
        shaderfx: Name of the shaderfx to edit

        index: The index to move the effect to

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shaderfx_move_up(shaderfx: str = '') -> set[OperatorReturn]:
    """
    Move effect up in the stack

    Args:
        shaderfx: Name of the shaderfx to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shaderfx_remove(shaderfx: str = '', report: bool = False) -> set[OperatorReturn]:
    """
    Remove an effect from the active grease pencil object.

    Args:
        shaderfx: Name of the shaderfx to edit

        report: Create a notification after the operation

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shape_key_add(from_mix: bool = True) -> set[OperatorReturn]:
    """
    Add shape key to the object

    Args:
        from_mix: Create the new shape key from the existing mix of keys

    Returns:
        Operation result.
    """
    pass


def shape_key_clear() -> set[OperatorReturn]:
    """
    Clear weights for all shape keys

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shape_key_lock(action: Literal['LOCK', 'UNLOCK'] = 'LOCK') -> set[OperatorReturn]:
    """
    Change the lock state of all shape keys of active object

    Args:
        action: Lock action to execute on vertex groups

            LOCK: Lock all shape keys.

            UNLOCK: Unlock all shape keys.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shape_key_mirror(use_topology: bool = False) -> set[OperatorReturn]:
    """
    Mirror the current shape key along the local X axis

    Args:
        use_topology: Topology Mirror, Use topology based mirroring (for when
            both sides of mesh have matching, unique topology).

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def shape_key_move(type: Literal['TOP', 'UP', 'DOWN', 'BOTTOM'] = 'TOP') -> set[OperatorReturn]:
    """
    Move the active shape key up/down in the list

    Args:
        type: Type

            TOP: Top of the list.

            UP: Up.

            DOWN: Down.

            BOTTOM: Bottom of the list.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def shape_key_remove(all: bool = False, apply_mix: bool = False) -> set[OperatorReturn]:
    """
    Remove shape key from the object

    Args:
        all: Remove all shape keys

        apply_mix: Apply current mix of shape keys to the geometry before
            removing them

    Returns:
        Operation result.
    """
    pass


def shape_key_retime() -> set[OperatorReturn]:
    """
    Resets the timing for absolute shape keys

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def shape_key_transfer(
    mode: Literal['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE'] = 'OFFSET',
    use_clamp: bool = False,
) -> set[OperatorReturn]:
    """
    Copy the active shape key of another selected object to this one

    Args:
        mode: Transformation Mode, Relative shape positions to the new shape
            method.

            OFFSET: Apply the relative positional offset.

            RELATIVE_FACE: Calculate relative position (using faces).

            RELATIVE_EDGE: Calculate relative position (using edges).

        use_clamp: Clamp the transformation to the distance each vertex moves in
            the original shape

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def simulation_nodes_cache_bake(selected: bool = False) -> set[OperatorReturn]:
    """
    Bake simulations in geometry nodes modifiers

    Args:
        selected: Bake cache on all selected objects

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def simulation_nodes_cache_calculate_to_frame(selected: bool = False) -> set[OperatorReturn]:
    """
    Calculate simulations in geometry nodes modifiers from the start to current
    frame.

    Args:
        selected: Calculate all selected objects instead of just the active
            object.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def simulation_nodes_cache_delete(selected: bool = False) -> set[OperatorReturn]:
    """
    Delete cached/baked simulations in geometry nodes modifiers

    Args:
        selected: Delete cache on all selected objects

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def skin_armature_create(modifier: str = '') -> set[OperatorReturn]:
    """
    Create an armature that parallels the skin layout

    Args:
        modifier: Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def skin_loose_mark_clear(action: Literal['MARK', 'CLEAR'] = 'MARK') -> set[OperatorReturn]:
    """
    Mark/clear selected vertices as loose

    Args:
        action: Action

            MARK: Mark selected vertices as loose.

            CLEAR: Set selected vertices as not loose.

    Returns:
        Operation result.
    """
    pass


def skin_radii_equalize() -> set[OperatorReturn]:
    """
    Make skin radii of selected vertices equal on each axis

    Returns:
        Operation result.
    """
    pass


def skin_root_mark() -> set[OperatorReturn]:
    """
    Mark selected vertices as roots

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def speaker_add(
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a speaker object to the scene

    Args:
        enter_editmode: Enter edit mode when adding this object.

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def subdivision_set(level: int = 1, relative: bool = False) -> set[OperatorReturn]:
    """
    Sets a Subdivision Surface level (1 to 5)

    Args:
        level: Level

            [-100, 100]

        relative: Apply the subdivision surface level as an offset relative to
            the current level

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def surfacedeform_bind(modifier: str = '') -> set[OperatorReturn]:
    """
    Bind mesh to target in surface deform modifier

    Args:
        modifier (string, (optional, never None)) – Modifier, Name of the modifier to edit

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def text_add(
    radius: float = 1.0,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a text object to the scene

    Args:
        radius: Radius

            [0, inf]

        enter_editmode: Enter edit mode when adding this object

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def track_clear(type: Literal['CLEAR', 'CLEAR_KEEP_TRANSFORM'] = 'CLEAR') -> set[OperatorReturn]:
    """
    Clear tracking constraint or flag from object

    Args:
        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def track_set(type: Literal['DAMPTRACK', 'TRACKTO', 'LOCKTRACK'] = 'DAMPTRACK') -> set[OperatorReturn]:
    """
    Make the object track another object, using various methods/constraints

    Args:
        type:

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def transfer_mode(use_flash_on_transfer: bool = True) -> set[OperatorReturn]:
    """
    Switches the active object and assigns the same mode to a new one under the
    mouse cursor, leaving the active mode in the current one

    Args:
        use_flash_on_transfer: Flash the target object when transferring the
            mode.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def transform_apply(
    location: bool = True,
    rotation: bool = True,
    scale: bool = True,
    properties: bool = True,
    isolate_users: bool = False
) -> set[OperatorReturn]:
    """
    Apply the object’s transformation to its data

    Args:
        location:

        rotation:

        scale:

        properties: Modify properties such as curve vertex radius, font size and
            bone envelope

        isolate_users: Isolate Multi User Data, Create new object-data users if
            needed

    Returns:
        Operation result.
    """
    pass


def transform_axis_target() -> set[OperatorReturn]:
    """
    Interactively point cameras and lights to a location (Ctrl translates)

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def transform_to_mouse(
    name: str = '',
    session_uid: int = 0,
    matrix: Matrix = Matrix((
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0)
    )),
    drop_x: int = 0,
    drop_y: int = 0,
) -> set[OperatorReturn]:
    """
    Snap selected item(s) to the mouse location

    Args:
        name: Object name to place (uses the active object when this and
            ‘session_uid’ are unset)

        session_uid: Session UUID of the object to place (uses the active object
            when this and ‘name’ are unset)

        matrix:

            Matrix of 4 * 4 items in [-inf, inf]

        drop_x: X-coordinate (screen space) to place the new object under

        drop_y: Y-coordinate (screen space) to place the new object under

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def transforms_to_deltas(
    mode: Literal['ALL', 'LOC', 'ROT', 'SCALE'] = 'ALL',
    reset_values: bool = True,
) -> set[OperatorReturn]:
    """
    Convert normal object transforms to delta transforms, any existing delta
    transforms will be included as well.

    Args:
        mode: Which transforms to transfer

            ALL: Transfer location, rotation, and scale transforms.

            LOC: Transfer location transforms only.

            ROT: Transfer rotation transforms only.

            SCALE: Transfer scale transforms only.

        reset_values: Clear transform values after transferring to deltas

    Returns:
        Operation result.
    """
    pass


def unlink_data() -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Returns:
        Operation result.
    """
    pass


def vertex_group_add() -> set[OperatorReturn]:
    """
    Add a new vertex group to the active object

    Returns:
        Operation result.
    """
    pass


def vertex_group_assign() -> set[OperatorReturn]:
    """
    Assign the selected vertices to the active vertex group

    Returns:
        Operation result.
    """
    pass


def vertex_group_assign_new() -> set[OperatorReturn]:
    """
    Assign the selected vertices to a new vertex group

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_clean(
    group_select_mode: str = '',
    limit: float = 0.0,
    keep_single: bool = False,
) -> set[OperatorReturn]:
    """
    Remove vertex group assignments which are not required

    Args:
        group_select_mode: Define which subset of groups shall be used

        limit: Remove vertices which weight is below or equal to this limit

            [0, 1]

        keep_single: Keep verts assigned to at least one group when cleaning

    Returns:
        Operation result.
    """
    pass


def vertex_group_copy() -> set[OperatorReturn]:
    """
    Make a copy of the active vertex group

    Returns:
        Operation result.
    """
    pass


def vertex_group_copy_to_selected() -> set[OperatorReturn]:
    """
    Replace vertex groups of selected objects by vertex groups of active object

    Returns:
        Operation result.
    """
    pass


def vertex_group_deselect() -> set[OperatorReturn]:
    """
    Deselect all selected vertices assigned to the active vertex group

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_invert(
    group_select_mode: str = '',
    auto_assign: bool = True,
    auto_remove: bool = True,
) -> set[OperatorReturn]:
    """
    Invert active vertex group’s weights

    Args:
        group_select_mode: Define which subset of groups shall be used

        auto_assign: Add vertices from groups that have zero weight before
            inverting

        auto_remove: Remove vertices from groups that have zero weight after
            inverting

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_levels(group_select_mode: str = '', offset: float = 0.0, gain: float = 1.0) -> set[OperatorReturn]:
    """
    Add some offset and multiply with some gain the weights of the active vertex
    group.

    Args:
        group_select_mode: Define which subset of groups shall be used

        offset: Value to add to weights

            [-1, 1]

        gain: Value to multiply weights by

            [0, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_limit_total(group_select_mode: str = '', limit: int = 4) -> set[OperatorReturn]:
    """
    Limit deform weights associated with a vertex to a specified number by
    removing lowest weights

    Args:
        group_select_mode: Define which subset of groups shall be used

        limit: Maximum number of deform weights

            [1, 32]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_lock(
    action: Literal['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT'] = 'TOGGLE',
    mask: Literal['ALL', 'SELECTED', 'UNSELECTED', 'INVERT_UNSELECTED'] = 'ALL',
) -> set[OperatorReturn]:
    """
    Change the lock state of all or some vertex groups of active object

    Args:
        action: Lock action to execute on vertex groups

            TOGGLE: Unlock all vertex groups if there is at least one locked
                group, lock all in other case.

            LOCK: Lock all vertex groups.

            UNLOCK: Unlock all vertex groups.

            INVERT: Invert the lock state of all vertex groups.

        mask: Apply the action based on vertex group selection

            ALL: Apply action to all vertex groups.

            SELECTED: Apply to selected vertex groups.

            UNSELECTED: Apply to unselected vertex groups.

            INVERT_UNSELECTED: Apply the opposite of Lock/Unlock to unselected
                vertex groups.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_mirror(
    mirror_weights: bool = True,
    flip_group_names: bool = True,
    all_groups: bool = False,
    use_topology: bool = False,
) -> set[OperatorReturn]:
    """
    Mirror vertex group, flip weights and/or names, editing only selected
    vertices, flipping when both sides are selected otherwise copy from
    unselected.

    Args:
        mirror_weights: Mirror weights

        flip_group_names: Flip vertex group names

        all_groups: Mirror all vertex groups weights

        use_topology: Use topology based mirroring (for when both sides of mesh
            have matching, unique topology)

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_move(direction: Literal['UP', 'DOWN'] = 'UP') -> set[OperatorReturn]:
    """
    Move the active vertex group up/down in the list

    Args:
        direction: Direction to move the active vertex group towards

    Returns:
        Operation result.
    """
    pass


def vertex_group_normalize() -> set[OperatorReturn]:
    """
    Normalize weights of the active vertex group, so that the highest ones are now 1.0

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_normalize_all(group_select_mode: str = '', lock_active: bool = True) -> set[OperatorReturn]:
    """
    Normalize all weights of all vertex groups, so that for each vertex, the sum
    of all weights is 1.0.

    Args:
        group_select_mode: Define which subset of groups shall be used

        lock_active: Keep the values of the active group while normalizing
            others.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_quantize(group_select_mode: str = '', steps: int = 4) -> set[OperatorReturn]:
    """
    Set weights to a fixed number of steps

    Args:
        group_select_mode: Subset, Define which subset of groups shall be used

        steps: Number of steps between 0 and 1

            [1, 1000]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def vertex_group_remove(all: bool = False, all_unlocked: bool = False) -> set[OperatorReturn]:
    """
    Delete the active or all vertex groups from the active object

    Args:
        all: Remove all vertex groups

        all_unlocked: Remove all unlocked vertex groups

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_remove_from(use_all_groups: bool = False, use_all_verts: bool = False) -> set[OperatorReturn]:
    """
    Remove the selected vertices from active or all vertex group(s)

    Args:
        use_all_groups: Remove from all groups

        use_all_verts: Clear the active group

    Returns:
        Operation result.
    """
    pass


def vertex_group_select() -> set[OperatorReturn]:
    """
    Select all the vertices assigned to the active vertex group

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_set_active(group: str = '') -> set[OperatorReturn]:
    """
    Set the active vertex group

    Args:
        group: Vertex group to set as active

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_smooth(
    group_select_mode: str = '',
    factor: float = 0.5,
    repeat: int = 1,
    expand: float = 0.0,
) -> set[OperatorReturn]:
    """
    Smooth weights for selected vertices

    Args:
        group_select_mode: Define which subset of groups shall be used

        factor: Factor

            [0, 1]

        repeat: Iterations

            [1, 10000]

        expand: Expand/contract weights

            [-1, 1]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_group_sort(sort_type: Literal['NAME', 'BONE_HIERARCHY'] = 'NAME') -> set[OperatorReturn]:
    """
    Sort vertex groups

    Args:
        sort_type: Sort type

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_parent_set(confirm: bool = True) -> set[OperatorReturn]:
    """
    Parent selected objects to the selected vertices

    Args:
        confirm: Prompt for confirmation

    Returns:
        Operation result.
    """
    pass


def vertex_weight_copy() -> set[OperatorReturn]:
    """
    Copy weights from active to selected

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_weight_delete(weight_group: int = -1) -> set[OperatorReturn]:
    """
    Delete this weight from the vertex (disabled if vertex group is locked).

    Args:
        weight_group: Index of source weight in active vertex group.

            [-1, inf]

    Returns:
        Operation result.
    """
    pass


def vertex_weight_normalize_active_vertex() -> set[OperatorReturn]:
    """
    Normalize active vertex’s weights.

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_weight_paste(weight_group: int = -1) -> set[OperatorReturn]:
    """
    Copy this group’s weight to other selected vertices (disabled if vertex
    group is locked).

    Args:
        weight_group: Index of source weight in active vertex group.

            [-1, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal
def vertex_weight_set_active(weight_group: int = -1) -> set[OperatorReturn]:
    """
    Set as active vertex group

    Args:
        weight_group: Index of source weight in active vertex group

            [-1, inf]

    Returns:
        Operation result.
    """
    pass


def visual_transform_apply() -> set[OperatorReturn]:
    """
    Apply the object’s visual transformation to its data

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def volume_add(
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Add a volume object to the scene

    Args:

        align: Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def volume_import(
    filepath: str = '',
    directory: str = '',
    files: bpy_prop_collection[OperatorFileListElement] | None = None,
    hide_props_region: bool = True,
    check_existing: bool = False,
    filter_blender: bool = False,
    filter_backup: bool = False,
    filter_image: bool = False,
    filter_movie: bool = False,
    filter_python: bool = False,
    filter_font: bool = False,
    filter_sound: bool = False,
    filter_text: bool = False,
    filter_archive: bool = False,
    filter_btx: bool = False,
    filter_collada: bool = False,
    filter_alembic: bool = False,
    filter_usd: bool = False,
    filter_obj: bool = False,
    filter_volume: bool = True,
    filter_folder: bool = True,
    filter_blenlib: bool = False,
    filemode: int = 9,
    relative_path: bool = True,
    display_type: Literal['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL'] = 'DEFAULT',
    sort_method: Literal['DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'] = '',
    use_sequence_detection: bool = True,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: Vector = Vector((0.0, 0.0, 0.0)),
    rotation: Euler = Euler(Vector((0.0, 0.0, 0.0))),
    scale: Vector = Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Import OpenVDB volume file

    Args:
        filepath: Path to file

        directory: Directory of the file

        files: Files

        hide_props_region: Collapse the region displaying the operator settings

        check_existing: Check and warn on overwriting existing files

        filter_blender: Filter .blend files

        filter_backup: Filter .blend files

        filter_image: Filter image files

        filter_movie: Filter movie files

        filter_python: Filter Python files

        filter_font: Filter font files

        filter_sound: Filter sound files

        filter_text: Filter text files

        filter_archive: Filter archive files

        filter_btx: Filter btx files

        filter_collada: Filter COLLADA files

        filter_alembic: Filter Alembic files

        filter_usd: Filter USD files

        filter_obj: Filter OBJ files

        filter_volume: Filter OpenVDB volume files

        filter_folder: Filter folders

        filter_blenlib: Filter Blender IDs

        filemode: The setting for the file browser mode to load a .blend file, a
            library or a special file.

            [1, 9]

        relative_path: Select the file relative to the blend file.

        display_type: Display Type

            DEFAULT: Automatically determine display type for files.

            LIST_VERTICAL: Display files as short list.

            LIST_HORIZONTAL: Display files as a detailed list.

            THUMBNAIL: Display files as thumbnails.

        sort_method: File sorting mode

            DEFAULT: Automatically determine sort method for files.

            FILE_SORT_ALPHA: Sort the file list alphabetically.

            FILE_SORT_EXTENSION: Sort the file list by extension/type.

            FILE_SORT_TIME: Sort files by modification time.

            FILE_SORT_SIZE: Sort files by size.

        use_sequence_detection: Automatically detect animated sequences in
            selected volume files (based on file names).

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object.

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object.

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation result.
    """
    pass


def voxel_remesh() -> set[OperatorReturn]:
    """
    Calculates a new manifold mesh based on the volume of the current mesh. All
    data layers will be lost.

    Returns:
        Operation result.
    """


def voxel_size_edit() -> set[OperatorReturn]:
    """
    Modify the mesh voxel size interactively used in the voxel remesher.

    Returns:
        Operation result.
    """
