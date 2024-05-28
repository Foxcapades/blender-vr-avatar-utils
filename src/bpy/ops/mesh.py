from typing import Literal

from bpy.types.a import AxisXyz
from bpy.types.m import (
    MESH_OT_duplicate,
    MESH_OT_extrude_context,
    MESH_OT_extrude_edges_indiv,
    MESH_OT_extrude_faces_indiv,
    MESH_OT_extrude_region,
    MESH_OT_loopcut,
    MESH_OT_offset_edge_loops,
    MESH_OT_polybuild_face_at_cursor,
    MESH_OT_polybuild_transform_at_cursor,
    MeshDelimitMode,
    MeshSelectMode
)
from bpy.types.o import OperatorReturn
from bpy.types.p import ProportionalFalloff, ProportionalFalloffCurveOnly
from bpy.types.t import TRANSFORM_OT_edge_slide, TRANSFORM_OT_shrink_fatten, TRANSFORM_OT_translate

import mathutils


# noinspection PyUnusedLocal
def attribute_set(
    value_float: float = 0.0,
    value_float_vector_2d: tuple[float, float] = (0.0, 0.0),
    value_float_vector_3d: tuple[float, float, float] = (0.0, 0.0, 0.0),
    value_int: int = 0,
    value_color: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool = False,
) -> set[OperatorReturn]:
    """
    Set values of the active attribute for selected elements

    Args:
        value_float: Value.
        value_float_vector_2d: Value.
        value_float_vector_3d: Value.
        value_int: Value.
        value_color: Value.
        value_bool: Value.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def average_normals(
    average_type: Literal['CUSTOM_NORMAL', 'FACE_AREA', 'CORNER_ANGLE'] = 'CUSTOM_NORMAL',
    weight: int = 50,
    threshold: float = 0.01,
) -> set[OperatorReturn]:
    """
    Average custom normals of selected vertices

    Args:
        average_type: Averaging method

            CUSTOM_NORMAL: Take average of vertex normals.

            FACE_AREA: Set all vertex normals by face area.

            CORNER_ANGLE: Set all vertex normals by corner angle.

        weight: Weight applied per face

            [1, 100]

        threshold: Threshold value for different weights to be considered equal.

            [0, 10]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def beautify_fill(angle_limit: float = 3.14159) -> set[OperatorReturn]:
    """
    Rearrange some faces to try to get less degenerated geometry

    Args:
        angle_limit: Max Angle, Angle limit

            [0, 3.14159]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def bevel(
    offset_type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE'] = 'OFFSET',
    offset: float = 0.0,
    profile_type: Literal['SUPERELLIPSE', 'CUSTOM'] = 'SUPERELLIPSE',
    offset_pct: float = 0.0,
    segments: int = 1,
    profile: float = 0.5,
    affect: Literal['VERTICES', 'EDGES'] = 'EDGES',
    clamp_overlap: bool = False,
    loop_slide: bool = True,
    mark_seam: bool = False,
    mark_sharp: bool = False,
    material: int = -1,
    harden_normals: bool = False,
    face_strength_mode: Literal['NONE', 'NEW', 'AFFECTED', 'ALL'] = 'NONE',
    miter_outer: Literal['SHARP', 'PATCH', 'ARC'] = 'SHARP',
    miter_inner: Literal['SHARP', 'ARC'] = 'SHARP',
    spread: float = 0.1,
    vmesh_method: Literal['ADJ', 'CUTOFF'] = 'ADJ',
    release_confirm: bool = False,
) -> set[OperatorReturn]:
    """
    Cut into selected items at an angle to create bevel or chamfer

    Args:
        offset_type: Width Type, The method for determining the size of the bevel

            OFFSET: Amount is offset of new edges from original.

            WIDTH: Amount is width of new face.

            DEPTH: Amount is perpendicular distance from original edge to bevel face.

            PERCENT: Amount is percent of adjacent edge length.

            ABSOLUTE: Amount is absolute distance along adjacent edge.

        offset: Width, Bevel amount

            [0, 1e+06]

        profile_type: The type of shape used to rebuild a beveled section

            SUPERELLIPSE: The profile can be a concave or convex curve.

            CUSTOM: The profile can be any arbitrary path between its endpoints.

        offset_pct: Width Percent, Bevel amount for percentage method.

            [0, 100]

        segments: Segments for curved edge

            [1, 1000]

        profile: Controls profile shape (0.5 = round)

            [0, 1]

        affect: Affect edges or vertices

            VERTICES: Affect only vertices.

            EDGES: Affect only edges.

        clamp_overlap: Do not allow beveled edges/vertices to overlap each other

        loop_slide: Prefer sliding along edges to even widths

        mark_seam: Mark Seams along beveled edges

        mark_sharp: Mark Sharp, Mark beveled edges as sharp

        material: Material Index, Material for bevel faces (-1 means use
            adjacent faces).

            [-1, inf]

        harden_normals: Harden Normals, Match normals of new faces to adjacent
            faces.

        face_strength_mode: Face Strength Mode, Whether to set face strength,
            and which faces to set face strength on.

            NONE: Do not set face strength.

            NEW: Set face strength on new faces only.

            AFFECTED: Set face strength on new and modified faces only.

            ALL: Set face strength on all faces.

        miter_outer: Pattern to use for outside of miters

            SHARP: Outside of miter is sharp.

            PATCH: Outside of miter is squared-off patch.

            ARC: Outside of miter is arc.

        miter_inner: Pattern to use for inside of miters

            SHARP: Inside of miter is sharp.

            ARC: Inside of miter is arc.

        spread: Amount to spread arcs for arc inner miters.

            [0, 1e+06]

        vmesh_method: Vertex Mesh Method, The method to use to create meshes at
            intersections.

            ADJ: Grid Fill – Default patterned fill.

            CUTOFF: A cutoff at each profile’s end before the intersection.

        release_confirm: Confirm on Release

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def bisect(
    plane_co: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    plane_no: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    use_fill: bool = False,
    clear_inner: bool = False,
    clear_outer: bool = False,
    threshold: float = 0.0001,
    xstart: int = 0,
    xend: int = 0,
    ystart: int = 0,
    yend: int = 0,
    flip: bool = False,
    cursor: int = 5,
) -> set[OperatorReturn]:
    """
    Cut geometry along a plane (click-drag to define plane)

    Args:
        plane_co: Plane Point, A point on the plane

            Vector of 3 items in [-inf, inf]

        plane_no: Plane Normal, The direction the plane points.

            Vector of 3 items in [-1, 1]

        use_fill: Fill, Fill in the cut

        clear_inner: Clear Inner, Remove geometry behind the plane

        clear_outer: Clear Outer, Remove geometry in front of the plane

        threshold: Axis Threshold, Preserves the existing geometry along the
            cut plane.

            [0, 10]

        xstart: X Start

        xend: X End

        ystart: Y Start

        yend: Y End

        flip: Flip

        cursor: Mouse cursor style to use during the modal operator.

            [0, inf]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def blend_from_shape(shape: str = '', blend: float = 1.0, add: bool = True) -> set[OperatorReturn]:
    """
    Blend in shape from a shape key

    Args:
        shape: Shape key to use for blending

        blend: Blending factor

            [-1000, 1000]

        add: Add, Add rather than blend between shapes

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def bridge_edge_loops(
    type: Literal['SINGLE', 'CLOSED', 'PAIRS'] = 'SINGLE',
    use_merge: bool = False,
    merge_factor: float = 0.5,
    twist_offset: int = 0,
    number_cuts: int = 0,
    interpolation: Literal['LINEAR', 'PATH', 'SURFACE'] = 'PATH',
    smoothness: float = 1.0,
    profile_shape_factor: float = 0.0,
    profile_shape: ProportionalFalloffCurveOnly = 'SMOOTH',
) -> set[OperatorReturn]:
    """
    Create a bridge of faces between two or more selected edge loops

    Args:
        type: Connect Loops, Method of bridging multiple loops

        use_merge: Merge, Merge rather than creating faces

        merge_factor: Merge Factor

            [0, 1]

        twist_offset: Twist offset for closed loops.

            [-1000, 1000]

        number_cuts: Number of Cuts.

            [0, 1000]

        interpolation: Interpolation method

        smoothness: Smoothness factor

            [0, 1000]

        profile_shape_factor: Profile Factor. How much intermediary new edges
            are shrunk/expanded.

            [-1000, 1000]

        profile_shape: Shape of the profile.

    Returns:
        Operation results.
    """
    pass


def colors_reverse() -> set[OperatorReturn]:
    """
    Flip direction of face corner color attribute inside faces

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def colors_rotate(use_ccw: bool = False) -> set[OperatorReturn]:
    """
    Rotate face corner color attribute inside faces

    Args:
        use_ccw: Counterclockwise

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def convex_hull(
    delete_unused: bool = True,
    use_existing_faces: bool = True,
    make_holes: bool = False,
    join_triangles: bool = True,
    face_threshold: float = 0.698132,
    shape_threshold: float = 0.698132,
    uvs: bool = False,
    vcols: bool = False,
    seam: bool = False,
    sharp: bool = False,
    materials: bool = False,
) -> set[OperatorReturn]:
    """
    Enclose selected vertices in a convex polyhedron

    Args:
        delete_unused: Delete Unused, Delete selected elements that are not used by the hull

        use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face

        make_holes: Make Holes, Delete selected faces that are used by the hull

        join_triangles: Join Triangles, Merge adjacent triangles into quads

        face_threshold: Max Face Angle, Face angle limit.

            [0, 3.14159]

        shape_threshold: Max Shape Angle, Shape angle limit

            [0, 3.14159]

        uvs: Compare UVs

        vcols: Compare VCols

        seam: Compare Seam

        sharp: Compare Sharp

        materials: Compare Materials

    Returns:
        Operation results.
    """
    pass


def customdata_custom_splitnormals_add() -> set[OperatorReturn]:
    """
    Add a custom split normals layer, if none exists yet

    Returns:
        Operation results.
    """
    pass


def customdata_custom_splitnormals_clear() -> set[OperatorReturn]:
    """
    Remove the custom split normals layer, if it exists

    Returns:
        Operation results.
    """
    pass


def customdata_mask_clear() -> set[OperatorReturn]:
    """
    Clear vertex sculpt masking data from the mesh

    Returns:
        Operation results.
    """
    pass


def customdata_skin_add() -> set[OperatorReturn]:
    """
    Add a vertex skin layer

    Returns:
        Operation results.
    """
    pass


def customdata_skin_clear() -> set[OperatorReturn]:
    """
    Clear vertex skin layer

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def decimate(
    ratio: float = 1.0,
    use_vertex_group: bool = False,
    vertex_group_factor: float = 1.0,
    invert_vertex_group: bool = False,
    use_symmetry: bool = False,
    symmetry_axis: AxisXyz = 'Y',
) -> set[OperatorReturn]:
    """
    Simplify geometry by collapsing edges

    Args:
        ratio: Ratio

            [0, 1]

        use_vertex_group: Vertex Group, Use active vertex group as an influence

        vertex_group_factor: Weight, Vertex group strength.

            [0, 1000]

        invert_vertex_group: Invert, Invert vertex group influence

        use_symmetry: Symmetry, Maintain symmetry on an axis

        symmetry_axis: Axis of symmetry.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def delete(type: Literal['VERT', 'EDGE', 'FACE', 'EDGE_FACE', 'ONLY_FACE'] = 'VERT') -> set[OperatorReturn]:
    """
    Delete selected vertices, edges or faces

    Args:
        type: Method used for deleting mesh data.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def delete_edgeloop(use_face_split: bool = True) -> set[OperatorReturn]:
    """
    Delete an edge loop by merging the faces on each side

    Args:
        use_face_split: Face Split, Split off face corners to maintain
            surrounding geometry.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def delete_loose(use_verts: bool = True, use_edges: bool = True, use_faces: bool = False) -> set[OperatorReturn]:
    """
    Delete loose vertices, edges or faces

    Args:
        use_verts: Vertices, Remove loose vertices

        use_edges: Edges, Remove loose edges

        use_faces: Faces, Remove loose faces

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dissolve_degenerate(threshold: float = 0.0001) -> set[OperatorReturn]:
    """
    Dissolve zero area faces and zero length edges

    Args:
        threshold: Merge Distance, Maximum distance between elements to merge.

            [1e-06, 50]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dissolve_edges(use_verts: bool = True, use_face_split: bool = False) -> set[OperatorReturn]:
    """
    Dissolve edges, merging faces

    Args:
        use_verts: Dissolve Vertices, Dissolve remaining vertices

        use_face_split: Face Split, Split off face corners to maintain
            surrounding geometry.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dissolve_faces(use_verts: bool = False) -> set[OperatorReturn]:
    """
    Dissolve faces

    Args:
        use_verts: Dissolve Vertices, Dissolve remaining vertices

    Returns:
        Operation results.
    """
    pass


# noinspection PyDefaultArgument,PyUnusedLocal
def dissolve_limited(
    angle_limit: float = 0.0872665,
    use_dissolve_boundaries: bool = False,
    delimit: set[MeshDelimitMode] = set('NORMAL'),
) -> set[OperatorReturn]:
    """
    Dissolve selected edges and vertices, limited by the angle of surrounding
    geometry.

    Args:
        angle_limit: Max Angle, Angle limit.

            [0, 3.14159]

        use_dissolve_boundaries: All Boundaries, Dissolve all vertices in
            between face boundaries.

        delimit: Delimit dissolve operation.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dissolve_mode(
    use_verts: bool = False,
    use_face_split: bool = False,
    use_boundary_tear: bool = False,
) -> set[OperatorReturn]:
    """
    Dissolve geometry based on the selection mode

    Args:
        use_verts: Dissolve Vertices, Dissolve remaining vertices

        use_face_split: Face Split, Split off face corners to maintain
            surrounding geometry.

        use_boundary_tear: Tear Boundary, Split off face corners instead of
            merging faces.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dissolve_verts(use_face_split: bool = False, use_boundary_tear: bool = False) -> set[OperatorReturn]:
    """
    Dissolve vertices, merge edges and faces

    Args:
        use_face_split: Face Split, Split off face corners to maintain
            surrounding geometry.

        use_boundary_tear: Tear Boundary, Split off face corners instead of
            merging faces.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def dupli_extrude_cursor(rotate_source: bool = True) -> set[OperatorReturn]:
    """
    Duplicate and extrude selected vertices, edges or faces towards the mouse
    cursor.

    Args:
        rotate_source: Rotate Source, Rotate initial selection giving better
            shape.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def duplicate(mode: int = 1) -> set[OperatorReturn]:
    """
    Duplicate selected vertices, edges or faces.

    Args:
        mode: Mode

            [0, inf]

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def duplicate_move(
    MESH_OT_duplicate: MESH_OT_duplicate | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Duplicate mesh and move

    Args:
        MESH_OT_duplicate: Duplicate selected vertices, edges or faces.

        TRANSFORM_OT_translate: Move selected items.

    Returns:
        Operation results.
    """
    pass


def edge_collapse() -> set[OperatorReturn]:
    """
    Collapse isolated edge and face regions, merging data such as UVs and color
    attributes. This can collapse edge-rings as well as regions of connected
    faces into vertices.

    Returns:
        Operation results.
    """
    pass


def edge_face_add() -> set[OperatorReturn]:
    """
    Add an edge or face to selected

    Returns:
        Operation results.
    """
    pass


def edge_rotate(use_ccw: bool = False) -> set[OperatorReturn]:
    """
    Rotate selected edge or adjoining faces

    Args:
        use_ccw: Counterclockwise

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def edge_split(type: Literal['EDGE', 'VERT'] = 'EDGE') -> set[OperatorReturn]:
    """
    Split selected edges so that each neighbor face gets its own copy

    Args:
        type: Method to use for splitting

            EDGE: Faces by Edges – Split faces along selected edges.

            VERT: Faces & Edges by Vertices – Split faces and edges connected to
            selected vertices.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def edgering_select(
    extend: bool = False,
    deselect: bool = False,
    toggle: bool = False,
    ring: bool = True,
) -> set[OperatorReturn]:
    """
    Select an edge ring

    Args:
        extend: Extend, Extend the selection

        deselect: Deselect, Remove from the selection

        toggle: Toggle Select, Toggle the selection

        ring: Select Ring, Select ring

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def edges_select_sharp(sharpness: float = 0.523599) -> set[OperatorReturn]:
    """
    Select all sharp enough edges

    Args:
        sharpness: Sharpness

            [0.000174533, 3.14159]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_context(
    use_normal_flip: bool = False,
    use_dissolve_ortho_edges: bool = False,
    mirror: bool = False,
) -> set[OperatorReturn]:
    """
    Extrude selection

    Args:
        use_normal_flip: Flip Normals

        use_dissolve_ortho_edges: Dissolve Orthogonal Edges

        mirror: Mirror Editing

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_context_move(
    MESH_OT_extrude_context: MESH_OT_extrude_context | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Extrude region together along the average normal

    Args:
        MESH_OT_extrude_context: Extrude Context, Extrude selection

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_edges_indiv(use_normal_flip: bool = False, mirror: bool = False) -> set[OperatorReturn]:
    """
    Extrude individual edges only

    Args:
        use_normal_flip: Flip Normals

        mirror: Mirror Editing

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_edges_move(
    MESH_OT_extrude_edges_indiv: MESH_OT_extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Extrude edges and move result

    Args:
        MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_faces_indiv(mirror: bool = False) -> set[OperatorReturn]:
    """
    Extrude individual faces only

    Args:
        mirror: Mirror Editing

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_faces_move(
    MESH_OT_extrude_faces_indiv: MESH_OT_extrude_faces_indiv | None = None,
    TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten | None = None,
) -> set[OperatorReturn]:
    """
    Extrude each individual face separately along local normals

    Args:
        MESH_OT_extrude_faces_indiv: Extrude individual faces only.

        TRANSFORM_OT_shrink_fatten: Shrink/fatten selected vertices along
            normals.

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_manifold(
    MESH_OT_extrude_region: MESH_OT_extrude_region | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Extrude, dissolves edges whose faces form a flat surface and intersect new
    edges.

    Args:
        MESH_OT_extrude_region: Extrude region of faces.

        TRANSFORM_OT_translate: Move selected items.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_region(
    use_normal_flip: bool = False,
    use_dissolve_ortho_edges: bool = False,
    mirror: bool = False,
) -> set[OperatorReturn]:
    """
    Extrude region of faces

    Args:
        use_normal_flip: Flip Normals

        use_dissolve_ortho_edges: Dissolve Orthogonal Edges

        mirror: Mirror Editing

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_region_move(
    MESH_OT_extrude_region: MESH_OT_extrude_region | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Extrude region and move result

    Args:
        MESH_OT_extrude_region: Extrude region of faces

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_region_shrink_fatten(
    MESH_OT_extrude_region: MESH_OT_extrude_region | None = None,
    TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten | None = None,
) -> set[OperatorReturn]:
    """
    Extrude region together along local normals

    Args:
        MESH_OT_extrude_region: Extrude region of faces.

        TRANSFORM_OT_shrink_fatten:: Shrink/fatten selected vertices along
            normals.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_repeat(
    steps: int = 10,
    offset: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    scale_offset: float = 1.0,
) -> set[OperatorReturn]:
    """
    Extrude selected vertices, edges or faces repeatedly

    Args:
        steps: Steps

            [0, 1000000]

        offset: Offset vector

            Vector of 3 items in [-100000, 100000]

        scale_offset: Scale Offset

            [0, inf]

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def extrude_vertices_move(MESH_OT_extrude_verts_indiv=None, TRANSFORM_OT_translate=None) -> set[OperatorReturn]:
    """
    Extrude vertices and move result

    Args:
        MESH_OT_extrude_verts_indiv (MESH_OT_extrude_verts_indiv, (optional)) – Extrude Only Vertices, Extrude individual vertices only

        TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def extrude_verts_indiv(mirror: bool = False) -> set[OperatorReturn]:
    """
    Extrude individual vertices only

    Args:
        mirror: Mirror Editing

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def face_make_planar(factor: float = 1.0, repeat: int = 1) -> set[OperatorReturn]:
    """
    Flatten selected faces

    Args:
        factor: Factor

            [-10, 10]

        repeat: Iterations

            [1, 10000]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def face_set_extract(
    add_boundary_loop: bool = True,
    smooth_iterations: int = 4,
    apply_shrinkwrap: bool = True,
    add_solidify: bool = True,
) -> set[OperatorReturn]:
    """
    Create a new mesh object from the selected Face Set

    Args:
        add_boundary_loop: Add Boundary Loop, Add an extra edge loop to better
            preserve the shape when applying a subdivision surface modifier.

        smooth_iterations: Smooth iterations applied to the extracted mesh.

            [0, inf]

        apply_shrinkwrap: Project the extracted mesh into the original sculpt.

        add_solidify: Extract the mask as a solid object with a solidify
            modifier.

    Returns:
        Operation results.
    """
    pass


def face_split_by_edges() -> set[OperatorReturn]:
    """
    Weld loose edges into faces (splitting them into new faces)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def faces_mirror_uv(direction: Literal['POSITIVE', 'NEGATIVE'] = 'POSITIVE', precision: int = 3) -> set[OperatorReturn]:
    """
    Copy mirror UV coordinates on the X axis based on a mirrored mesh

    Args:
        direction: Axis Direction

        precision: Tolerance for finding vertex duplicates

            [1, 16]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def faces_select_linked_flat(sharpness: float = 0.0174533) -> set[OperatorReturn]:
    """
    Select linked faces by angle

    Args:
        sharpness: Sharpness

            [0.000174533, 3.14159]

    Returns:
        Operation results.
    """
    pass


def faces_shade_flat() -> set[OperatorReturn]:
    """
    Display faces flat

    Returns:
        Operation results.
    """
    pass


def faces_shade_smooth() -> set[OperatorReturn]:
    """
    Display faces smooth (using vertex normals)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def fill(use_beauty: bool = True) -> set[OperatorReturn]:
    """
    Fill a selected edge loop with faces

    Args:
        use_beauty: Beauty, Use best triangulation division

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def fill_grid(span: int = 1, offset: int = 0, use_interp_simple: bool = False) -> set[OperatorReturn]:
    """
    Fill grid from two loops

    Args:
        span: Number of grid columns

            [1, 1000]

        offset: Vertex that is the corner of the grid

            [-1000, 1000]

        use_interp_simple: Use simple interpolation of grid vertices

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def fill_holes(sides: int = 4) -> set[OperatorReturn]:
    """
    Fill in holes (boundary edge loops)

    Args:
        sides: Number of sides in hole required to fill (zero fills all holes)

            [0, 1000]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def flip_normals(only_clnors: bool = False) -> set[OperatorReturn]:
    """
    Flip the direction of selected faces’ normals (and of their vertices)

    Args:
        only_clnors: Custom Normals Only - Only flip the custom loop normals of
            the selected elements

    Returns:
        Operation results.
    """
    pass


def flip_quad_tessellation() -> set[OperatorReturn]:
    """
    Flips the tessellation of selected quads

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def hide(unselected: bool = False) -> set[OperatorReturn]:
    """
    Hide (un)selected vertices, edges or faces

    Args:
        unselected: Hide unselected rather than selected

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def inset(
    use_boundary: bool = True,
    use_even_offset: bool = True,
    use_relative_offset: bool = False,
    use_edge_rail: bool = False,
    thickness: float = 0.0,
    depth: float = 0.0,
    use_outset: bool = False,
    use_select_inset: bool = False,
    use_individual: bool = False,
    use_interpolate: bool = True,
    release_confirm: bool = False,
) -> set[OperatorReturn]:
    """
    Inset new faces into selected faces

    Args:
        use_boundary: Boundary, Inset face boundaries

        use_even_offset: Offset Even, Scale the offset to give more even
            thickness.

        use_relative_offset: Offset Relative, Scale the offset by surrounding
            geometry.

        use_edge_rail: Edge Rail, Inset the region along existing edges

        thickness: Thickness

            [0, inf]

        depth: Depth

        use_outset: Outset, Outset rather than inset

        use_select_inset: Select Outer, Select the new inset faces

        use_individual: Individual, Individual face inset

        use_interpolate: Interpolate, Blend face data across the inset

        release_confirm: Confirm on Release

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def intersect(
    mode: Literal['SELECT', 'SELECT_UNSELECT'] = 'SELECT_UNSELECT',
    separate_mode: Literal['ALL', 'CUT', 'NONE'] = 'CUT',
    threshold: float = 1e-06,
    solver: Literal['FAST', 'EXACT'] = 'EXACT',
) -> set[OperatorReturn]:
    """
    Cut an intersection into faces

    Args:
        mode: Source

            SELECT: Self Intersect – Self intersect selected faces.

            SELECT_UNSELECT: Selected/Unselected – Intersect selected with
            unselected faces.

        separate_mode: Separate Mode

            ALL: Separate all geometry from intersections.

            CUT: Cut into geometry keeping each side separate
            (Selected/Unselected only).

            NONE: Merge all geometry from the intersection.

        threshold: Merge Threshold

            [0, 0.01]

        solver: Which Intersect solver to use

            FAST: Faster solver, some limitations.

            EXACT: Exact solver, slower, handles more cases.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def intersect_boolean(
    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
    use_swap: bool = False,
    use_self: bool = False,
    threshold: float = 1e-06,
    solver: Literal['FAST', 'EXACT'] = 'EXACT',
) -> set[OperatorReturn]:
    """
    Cut solid geometry from selected to unselected

    Args:
        operation: Which boolean operation to apply.

        use_swap: Use with difference intersection to swap which side is kept

        use_self: Self Intersection - Do self-union or self-intersection

        threshold: Merge Threshold

            [0, 0.01]

        solver: Which Boolean solver to use

            FAST: Faster solver, some limitations.

            EXACT: Exact solver, slower, handles more cases.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def knife_project(cut_through: bool = False) -> set[OperatorReturn]:
    """
    Use other objects outlines and boundaries to project knife cuts

    Args:
        cut_through: Cut through all faces, not just visible ones

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def knife_tool(
    use_occlude_geometry: bool = True,
    only_selected: bool = False,
    xray: bool = True,
    visible_measurements: Literal['NONE', 'BOTH', 'DISTANCE', 'ANGLE'] = 'NONE',
    angle_snapping: Literal['NONE', 'SCREEN', 'RELATIVE'] = 'NONE',
    angle_snapping_increment: float = 0.523599,
    wait_for_input: bool = True,
) -> set[OperatorReturn]:
    """
    Cut new topology

    Args:
        use_occlude_geometry: Only cut the front most geometry.

        only_selected: Only cut selected geometry.

        xray: Show cuts hidden by geometry.

        visible_measurements: Visible distance and angle measurements

            NONE: Show no measurements.

            BOTH: Show both distances and angles.

            DISTANCE: Show just distance measurements.

            ANGLE: Show just angle measurements.

        angle_snapping: Angle snapping mode

            NONE: No angle snapping.

            SCREEN: Screen space angle snapping.

            RELATIVE: Angle snapping relative to the previous cut edge.

        angle_snapping_increment: The angle snap increment used when in
            constrained angle mode.

            [0, 3.14159]

        wait_for_input: Wait for Input.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def loop_multi_select(ring: bool = False) -> set[OperatorReturn]:
    """
    Select a loop of connected edges by connection type

    Args:
        ring: Ring

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def loop_select(
    extend: bool = False,
    deselect: bool = False,
    toggle: bool = False,
    ring: bool = False,
) -> set[OperatorReturn]:
    """
    Select a loop of connected edges

    Args:
        extend: Extend the selection

        deselect: Remove from the selection

        toggle: Toggle the selection

        ring: Select ring

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def loop_to_region(select_bigger: bool = False) -> set[OperatorReturn]:
    """
    Select region of faces inside a selected loop of edges

    Args:
        select_bigger: Select bigger regions instead of smaller ones

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def loopcut(
    number_cuts: int = 1,
    smoothness: float = 0.0,
    falloff: ProportionalFalloffCurveOnly = 'INVERSE_SQUARE',
    object_index: int = -1,
    edge_index: int = -1,
    mesh_select_mode_init=(False, False, False),
) -> set[OperatorReturn]:
    """
    Add a new loop between existing loops

    Args:
        number_cuts: Number of Cuts

            [1, 1000000]

        smoothness: Smoothness factor

            [-1000, 1000]

        falloff: Falloff type of the feather

        object_index: Object Index

            [-1, inf]

        edge_index: Edge Index

            [-1, inf]

        mesh_select_mode_init: ???? TODO: What is this?

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def loopcut_slide(
    MESH_OT_loopcut: MESH_OT_loopcut | None = None,
    TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide | None = None,
) -> set[OperatorReturn]:
    """
    Cut mesh loop and slide it

    Args:
        MESH_OT_loopcut: Add a new loop between existing loops

        TRANSFORM_OT_edge_slide: Slide an edge loop along a mesh

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def mark_freestyle_edge(clear: bool = False) -> set[OperatorReturn]:
    """
    (Un)mark selected edges as Freestyle feature edges

    Args:
        clear: Clear

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def mark_freestyle_face(clear: bool = False) -> set[OperatorReturn]:
    """
    (Un)mark selected faces for exclusion from Freestyle feature edge detection

    Args:
        clear: Clear

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def mark_seam(clear: bool = False) -> set[OperatorReturn]:
    """
    (Un)mark selected edges as a seam

    Args:
        clear: Clear

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def mark_sharp(clear: bool = False, use_verts: bool = False) -> set[OperatorReturn]:
    """
    (Un)mark selected edges as sharp

    Args:
        clear: Clear

        use_verts: Consider vertices instead of edges to select which edges to
            (un)tag as sharp.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def merge(
    type: Literal['CENTER', 'CURSOR', 'COLLAPSE', 'FIRST', 'LAST'] = 'CENTER',
    uvs: bool = False,
) -> set[OperatorReturn]:
    """
    Merge selected vertices

    Args:
        type: Merge method to use

        uvs: Move UVs according to merge

    Returns:
        Operation results.
    """
    pass


def merge_normals() -> set[OperatorReturn]:
    """
    Merge custom normals of selected vertices

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def mod_weighted_strength(
    set: bool = False,
    face_strength: Literal['WEAK', 'MEDIUM', 'STRONG'] = 'MEDIUM',
) -> set[OperatorReturn]:
    """
    Set/Get strength of face (used in Weighted Normal modifier)

    Args:
        set: Set Value, Set value of faces

        face_strength: Strength to use for assigning or selecting face influence
            for weighted normal modifier

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def normals_make_consistent(inside: bool = False) -> set[OperatorReturn]:
    """
    Make face and vertex normals point either outside or inside the mesh

    Args:
        inside: Inside

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def normals_tools(
    mode: Literal['COPY', 'PASTE', 'ADD', 'MULTIPLY', 'RESET'] = 'COPY',
    absolute: bool = False,
) -> set[OperatorReturn]:
    """
    Custom normals tools using Normal Vector of UI

    Args:
        mode: Mode of tools taking input from interface

            COPY: Copy normal to the internal clipboard.

            PASTE: Paste normal from the internal clipboard.

            ADD: Add normal vector with selection.

            MULTIPLY: Multiply normal vector with selection.

            RESET: Reset the internal clipboard and/or normal of selected element.

        absolute: Copy Absolute coordinates or Normal vector

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def offset_edge_loops(use_cap_endpoint: bool = False) -> set[OperatorReturn]:
    """
    Create offset edge loop from the current selection

    Args:
        use_cap_endpoint: Extend loop around end-points

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def offset_edge_loops_slide(
    MESH_OT_offset_edge_loops: MESH_OT_offset_edge_loops | None = None,
    TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide | None = None,
) -> set[OperatorReturn]:
    """
    Offset edge loop slide

    Args:
        MESH_OT_offset_edge_loops: Create offset edge loop from the current
            selection

        TRANSFORM_OT_edge_slide: Slide an edge loop along a mesh

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def paint_mask_extract(
    mask_threshold: float = 0.5,
    add_boundary_loop: bool = True,
    smooth_iterations: int = 4,
    apply_shrinkwrap: bool = True,
    add_solidify: bool = True,
) -> set[OperatorReturn]:
    """
    Create a new mesh object from the current paint mask

    Args:
        mask_threshold: Minimum mask value to consider the vertex valid to
            extract a face from the original mesh.

            [0, 1]

        add_boundary_loop: Add an extra edge loop to better preserve the shape
            when applying a subdivision surface modifier

        smooth_iterations: Smooth iterations applied to the extracted mesh

            [0, inf]

        apply_shrinkwrap: Project the extracted mesh into the original sculpt

        add_solidify: Extract the mask as a solid object with a solidify
            modifier

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingNames
def paint_mask_slice(
    mask_threshold: float = 0.5,
    fill_holes: bool = True,
    new_object: bool = True,
) -> set[OperatorReturn]:
    """
    Slices the paint mask from the mesh

    Args:
        mask_threshold: Minimum mask value to consider the vertex valid to
            extract a face from the original mesh.

            [0, 1]

        fill_holes: Fill holes after slicing the mask

        new_object: Create a new object from the sliced mask

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def point_normals(
    mode: Literal['COORDINATES', 'MOUSE'] = 'COORDINATES',
    invert: bool = False,
    align: bool = False,
    target_location: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    spherize: bool = False,
    spherize_strength: float = 0.1,
) -> set[OperatorReturn]:
    """
    Point selected custom normals to specified Target

    Args:
        mode: How to define coordinates to point custom normals to

            COORDINATES: Use static coordinates (defined by various means).

            MOUSE: Follow mouse cursor.

        invert: Invert affected normals

        align: Make all affected normals parallel

        target_location: Target location to which normals will point

            Vector of 3 items in [-inf, inf]

        spherize: Interpolate between original and new normals

        spherize_strength: Ratio of spherized normal to original normal

            [0, 1]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def poke(
    offset: float = 0.0,
    use_relative_offset: bool = False,
    center_mode: Literal['MEDIAN_WEIGHTED', 'MEDIAN', 'BOUNDS'] = 'MEDIAN_WEIGHTED',
) -> set[OperatorReturn]:
    """
    Split a face into a fan

    Args:
        offset: Poke Offset

            `[-1000, 1000]`

        use_relative_offset: Scale the offset by surrounding geometry

        center_mode: Poke face center calculation

            MEDIAN_WEIGHTED: Weighted median face center.

            MEDIAN: Median face center.

            BOUNDS: Face bounds center.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def polybuild_delete_at_cursor(
    mirror: bool = False,
    use_proportional_edit: bool = False,
    proportional_edit_falloff: ProportionalFalloff = 'SMOOTH',
    proportional_size: float = 1.0,
    use_proportional_connected: bool = False,
    use_proportional_projected: bool = False,
    release_confirm: bool = False,
    use_accurate: bool = False,
) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff: Falloff type for proportional editing mode

        proportional_size: Proportional Size

            `[1e-06, inf]`

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Always confirm operation when releasing button

        use_accurate: Use accurate transformation

    Returns:
        Operation results.
    """
    pass


def polybuild_dissolve_at_cursor() -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def polybuild_extrude_at_cursor_move(
    MESH_OT_polybuild_transform_at_cursor: MESH_OT_polybuild_transform_at_cursor | None = None,
    MESH_OT_extrude_edges_indiv: MESH_OT_extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor

        MESH_OT_extrude_edges_indiv: Extrude individual edges only

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def polybuild_face_at_cursor(
    create_quads: bool = True,
    mirror: bool = False,
    use_proportional_edit: bool = False,
    proportional_edit_falloff: ProportionalFalloff = 'SMOOTH',
    proportional_size: float = 1.0,
    use_proportional_connected: bool = False,
    use_proportional_projected: bool = False,
    release_confirm: bool = False,
    use_accurate: bool = False,
) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        create_quads: Automatically split edges in triangles to maintain quad
            topology

        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff: Falloff type for proportional editing mode

        proportional_size: Proportional Size

            `[1e-06, inf]`

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Always confirm operation when releasing button

        use_accurate: Use accurate transformation

    Returns:
        Operation results.
    """
    pass


# noinspection PyPep8Naming,PyUnusedLocal
def polybuild_face_at_cursor_move(
    MESH_OT_polybuild_face_at_cursor: MESH_OT_polybuild_face_at_cursor | None = None,
    TRANSFORM_OT_translate: TRANSFORM_OT_translate | None = None,
) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor

        TRANSFORM_OT_translate: Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def polybuild_split_at_cursor(
    mirror: bool = False,
    use_proportional_edit: bool = False,
    proportional_edit_falloff: ProportionalFalloff = 'SMOOTH',
    proportional_size: float = 1.0,
    use_proportional_connected: bool = False,
    use_proportional_projected: bool = False,
    release_confirm: bool = False,
    use_accurate: bool = False,
) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff: Falloff type for proportional editing mode

        proportional_size: Proportional Size

            `[1e-06, inf]`

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Always confirm operation when releasing button

        use_accurate: Use accurate transformation

    Returns:
        Operation results.
    """
    pass


def polybuild_split_at_cursor_move(MESH_OT_polybuild_split_at_cursor=None, TRANSFORM_OT_translate=None) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        MESH_OT_polybuild_split_at_cursor (MESH_OT_polybuild_split_at_cursor, (optional)) – Poly Build Split at Cursor

        TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

    Returns:
        Operation results.
    """
    pass


def polybuild_transform_at_cursor(mirror: bool = False, use_proportional_edit: bool = False, proportional_edit_falloff='SMOOTH', proportional_size: float = 1.0, use_proportional_connected: bool = False, use_proportional_projected: bool = False, release_confirm: bool = False, use_accurate: bool = False) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff (enum in Proportional Falloff Items, (optional)) – Proportional Falloff, Falloff type for proportional editing mode

        proportional_size (float in [1e-06, inf], (optional)) – Proportional Size

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Confirm on Release, Always confirm operation when releasing button

        use_accurate: Accurate, Use accurate transformation

    Returns:
        Operation results.
    """
    pass


def polybuild_transform_at_cursor_move(MESH_OT_polybuild_transform_at_cursor=None, TRANSFORM_OT_translate=None) -> set[OperatorReturn]:
    """
    Undocumented, consider contributing.

    Args:
        MESH_OT_polybuild_transform_at_cursor (MESH_OT_polybuild_transform_at_cursor, (optional)) – Poly Build Transform at Cursor

        TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def primitive_circle_add(
    vertices: int = 32,
    radius: float = 1.0,
    fill_type: Literal['NOTHING', 'NGON', 'TRIFAN'] = 'NOTHING',
    calc_uvs: bool = True,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    rotation: mathutils.Euler = mathutils.Euler(mathutils.Vector((0.0, 0.0, 0.0))),
    scale: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Construct a circle mesh

    Args:
        vertices (int in [3, 10000000], (optional)) – Vertices

        radius (float in [0, inf], (optional)) – Radius

        fill_type: Fill Type

            NOTHING: Don’t fill at all.

            NGON N-Gon – Use n-gons.

            TRIFAN Triangle Fan – Use triangle fans.

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location: Location for the newly added object

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation results.
    """
    pass


def primitive_cone_add(vertices=32, radius1: float = 1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a conic mesh

    Args:
        vertices (int in [3, 10000000], (optional)) – Vertices

        radius1 (float in [0, inf], (optional)) – Radius 1

        radius2 (float in [0, inf], (optional)) – Radius 2

        depth (float in [0, inf], (optional)) – Depth

        end_fill_type (enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional)) –

        Base Fill Type

            NOTHING: Don’t fill at all.

            NGON N-Gon – Use n-gons.

            TRIFAN Triangle Fan – Use triangle fans.

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def primitive_cube_add(size=2.0, calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a cube mesh

    Args:
        size (float in [0, inf], (optional)) – Size

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def primitive_cube_add_gizmo(calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))) -> set[OperatorReturn]:
    """
    Construct a cube mesh

    Args:
        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

        matrix (mathutils.Matrix of 4 * 4 items in [-inf, inf], (optional)) – Matrix

    Returns:
        Operation results.
    """
    pass


def primitive_cylinder_add(vertices=32, radius: float = 1.0, depth=2.0, end_fill_type='NGON', calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a cylinder mesh

    Args:
        vertices (int in [3, 10000000], (optional)) – Vertices

        radius (float in [0, inf], (optional)) – Radius

        depth (float in [0, inf], (optional)) – Depth

        end_fill_type (enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional)) –

        Cap Fill Type

            NOTHING: Don’t fill at all.

            NGON N-Gon – Use n-gons.

            TRIFAN Triangle Fan – Use triangle fans.

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def primitive_grid_add(x_subdivisions: int = 10, y_subdivisions: int = 10, size=2.0, calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a grid mesh

    Args:
        x_subdivisions (int in [1, 10000000], (optional)) – X Subdivisions

        y_subdivisions (int in [1, 10000000], (optional)) – Y Subdivisions

        size (float in [0, inf], (optional)) – Size

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: – Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def primitive_ico_sphere_add(subdivisions=2, radius: float = 1.0, calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct an Icosphere mesh

    Args:
        subdivisions (int in [1, 10], (optional)) – Subdivisions

        radius (float in [0, inf], (optional)) – Radius

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def primitive_monkey_add(size=2.0, calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a Suzanne mesh

    Args:
        size (float in [0, inf], (optional)) – Size

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def primitive_plane_add(
    size: float = 2.0,
    calc_uvs: bool = True,
    enter_editmode: bool = False,
    align: Literal['WORLD', 'VIEW', 'CURSOR'] = 'WORLD',
    location: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    rotation: mathutils.Euler = mathutils.Euler(mathutils.Vector((0.0, 0.0, 0.0))),
    scale: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Construct a filled planar mesh with 4 vertices

    Args:
        size: Size

            [0, inf]

        calc_uvs: Generate a default UV map

        enter_editmode: Enter edit mode when adding this object.

        align: The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location: Location for the newly added object.

            Vector of 3 items in [-inf, inf]

        rotation: Rotation for the newly added object

            Euler rotation of 3 items in [-inf, inf]

        scale: Scale for the newly added object

            Vector of 3 items in [-inf, inf]

    Returns:
        Operation results.
    """
    pass


def primitive_torus_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius: float = 1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs: bool = True) -> set[OperatorReturn]:
    """
    Construct a torus mesh

    Args:
        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation

        major_segments (int in [3, 256], (optional)) – Major Segments, Number of segments for the main ring of the torus

        minor_segments (int in [3, 256], (optional)) – Minor Segments, Number of segments for the minor ring of the torus

        mode (enum in ['MAJOR_MINOR', 'EXT_INT'], (optional)) –

        Dimensions Mode

            MAJOR_MINOR Major/Minor – Use the major/minor radii for torus dimensions.

            EXT_INT Exterior/Interior – Use the exterior/interior radii for torus dimensions.

        major_radius (float in [0, 10000], (optional)) – Major Radius, Radius from the origin to the center of the cross sections

        minor_radius (float in [0, 10000], (optional)) – Minor Radius, Radius of the torus’ cross section

        abso_major_rad (float in [0, 10000], (optional)) – Exterior Radius, Total Exterior Radius of the torus

        abso_minor_rad (float in [0, 10000], (optional)) – Interior Radius, Total Interior Radius of the torus

        generate_uvs: Generate UVs, Generate a default UV map

    Returns:
        Operation results.
    """
    pass


def primitive_uv_sphere_add(segments=32, ring_count=16, radius: float = 1.0, calc_uvs: bool = True, enter_editmode: bool = False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Construct a UV sphere mesh

    Args:
        segments (int in [3, 100000], (optional)) – Segments

        ring_count (int in [3, 100000], (optional)) – Rings

        radius (float in [0, inf], (optional)) – Radius

        calc_uvs: Generate UVs, Generate a default UV map

        enter_editmode: Enter Edit Mode, Enter edit mode when adding this object

        align (enum in ['WORLD', 'VIEW', 'CURSOR'], (optional)) –

        Align, The alignment of the new object

            WORLD: Align the new object to the world.

            VIEW: Align the new object to the view.

            CURSOR: 3D Cursor – Use the 3D cursor orientation for the new object.

        location (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

        rotation (mathutils.Euler rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

        scale (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

    Returns:
        Operation results.
    """
    pass


def quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY') -> set[OperatorReturn]:
    """
    Triangulate selected faces

    Args:
        quad_method (enum in Modifier Triangulate Quad Method Items, (optional)) – Quad Method, Method for splitting the quads into triangles

        ngon_method (enum in Modifier Triangulate Ngon Method Items, (optional)) – N-gon Method, Method for splitting the n-gons into triangles

    Returns:
        Operation results.
    """
    pass


def region_to_loop() -> set[OperatorReturn]:
    """
    Select boundary edges around the selected faces

    Returns:
        Operation results.
    """
    pass


def remove_doubles(threshold=0.0001, use_unselected: bool = False, use_sharp_edge_from_normals: bool = False) -> set[OperatorReturn]:
    """
    Merge vertices based on their proximity

    Args:
        threshold (float in [1e-06, 50], (optional)) – Merge Distance, Maximum distance between elements to merge

        use_unselected: Unselected, Merge selected to other unselected vertices

        use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def reveal(select: bool = True) -> set[OperatorReturn]:
    """
    Reveal all hidden vertices, edges and faces

    Args:
        select: Select

    Returns:
        Operation results.
    """
    pass


def rip(mirror: bool = False, use_proportional_edit: bool = False, proportional_edit_falloff='SMOOTH', proportional_size: float = 1.0, use_proportional_connected: bool = False, use_proportional_projected: bool = False, release_confirm: bool = False, use_accurate: bool = False, use_fill: bool = False) -> set[OperatorReturn]:
    """
    Disconnect vertex or edges from connected geometry

    Args:
        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff (enum in Proportional Falloff Items, (optional)) – Proportional Falloff, Falloff type for proportional editing mode

        proportional_size (float in [1e-06, inf], (optional)) – Proportional Size

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Confirm on Release, Always confirm operation when releasing button

        use_accurate: Accurate, Use accurate transformation

        use_fill: Fill, Fill the ripped region

    Returns:
        Operation results.
    """
    pass


def rip_edge(mirror: bool = False, use_proportional_edit: bool = False, proportional_edit_falloff='SMOOTH', proportional_size: float = 1.0, use_proportional_connected: bool = False, use_proportional_projected: bool = False, release_confirm: bool = False, use_accurate: bool = False) -> set[OperatorReturn]:
    """
    Extend vertices along the edge closest to the cursor

    Args:
        mirror: Mirror Editing

        use_proportional_edit: Proportional Editing

        proportional_edit_falloff (enum in Proportional Falloff Items, (optional)) – Proportional Falloff, Falloff type for proportional editing mode

        proportional_size (float in [1e-06, inf], (optional)) – Proportional Size

        use_proportional_connected: Connected

        use_proportional_projected: Projected (2D)

        release_confirm: Confirm on Release, Always confirm operation when releasing button

        use_accurate: Accurate, Use accurate transformation

    Returns:
        Operation results.
    """
    pass


def rip_edge_move(MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None) -> set[OperatorReturn]:
    """
    Extend vertices and move the result

    Args:
        MESH_OT_rip_edge (MESH_OT_rip_edge, (optional)) – Extend Vertices, Extend vertices along the edge closest to the cursor

        TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

    Returns:
        Operation results.
    """
    pass


def rip_move(MESH_OT_rip=None, TRANSFORM_OT_translate=None) -> set[OperatorReturn]:
    """
    Rip polygons and move the result

    Args:
        MESH_OT_rip (MESH_OT_rip, (optional)) – Rip, Disconnect vertex or edges from connected geometry

        TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

    Returns:
        Operation results.
    """
    pass


def screw(steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)) -> set[OperatorReturn]:
    """
    Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    Args:
        steps (int in [1, 100000], (optional)) – Steps, Steps

        turns (int in [1, 100000], (optional)) – Turns, Turns

        center (mathutils.Vector of 3 items in [-inf, inf], (optional)) – Center, Center in global view space

        axis (mathutils.Vector of 3 items in [-1, 1], (optional)) – Axis, Axis in global view space

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_all(action: Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'] = 'TOGGLE') -> set[OperatorReturn]:
    """
    (De)select all vertices, edges or faces

    Args:
        action: Selection action to execute

            TOGGLE: Toggle selection for all elements.

            SELECT: Select all elements.

            DESELECT: Deselect all elements.

            INVERT: Invert selection of all elements.

    Returns:
        Operation results.
    """
    pass


def select_axis(orientation='LOCAL', sign='POS', axis='X', threshold=0.0001) -> set[OperatorReturn]:
    """
    Select all data in the mesh on a single axis

    Args:
        orientation (enum in Transform Orientation Items, (optional)) – Axis Mode, Axis orientation

        sign (enum in ['POS', 'NEG', 'ALIGN'], (optional)) – Axis Sign, Side to select

        axis (enum in Axis Xyz Items, (optional)) – Axis, Select the axis to compare each vertex on

        threshold (float in [1e-06, 50], (optional)) – Threshold

    Returns:
        Operation results.
    """
    pass


def select_by_attribute() -> set[OperatorReturn]:
    """
    Select elements based on the active boolean attribute

    Returns:
        Operation results.
    """
    pass


def select_face_by_sides(number=4, type='EQUAL', extend: bool = True) -> set[OperatorReturn]:
    """
    Select vertices or faces by the number of face sides

    Args:
        number (int in [3, inf], (optional)) – Number of Vertices

        type (enum in ['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL'], (optional)) – Type, Type of comparison to make

        extend: Extend, Extend the selection

    Returns:
        Operation results.
    """
    pass


def select_interior_faces() -> set[OperatorReturn]:
    """
    Select faces where all edges have more than 2 face users

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_less(use_face_step: bool = True) -> set[OperatorReturn]:
    """
    Deselect vertices, edges or faces at the boundary of each selection region

    Args:
        use_face_step: Connected faces (instead of edges)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyDefaultArgument
def select_linked(delimit: set[MeshDelimitMode] = set('SEAM')) -> set[OperatorReturn]:
    """
    Select all vertices connected to the current selection

    Args:
        delimit: Delimit selected region

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyDefaultArgument
def select_linked_pick(
    deselect: bool = False,
    delimit: set[MeshDelimitMode] = set('SEAM'),
    object_index: int = -1,
    index: int = -1,
) -> set[OperatorReturn]:
    """
    (De)select all vertices linked to the edge under the mouse cursor

    Args:
        deselect: Deselect

        delimit: Delimit selected region

        object_index: ????? TODO: what is this?

        index: ????? TODO: what is this?

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_loose(extend: bool = False) -> set[OperatorReturn]:
    """
    Select loose geometry based on the selection mode

    Args:
        extend: Extend the selection

    Returns:
        Operation results.
    """
    pass


def select_mirror(axis={'X'}, extend: bool = False) -> set[OperatorReturn]:
    """
    Select mesh items at mirrored locations

    Args:
        axis (enum set in Axis Flag Xyz Items, (optional)) – Axis

        extend: Extend, Extend the existing selection

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_mode(
    use_extend: bool = False,
    use_expand: bool = False,
    type: MeshSelectMode = 'VERT',
    action: Literal['DISABLE', 'ENABLE', 'TOGGLE'] = 'TOGGLE',
) -> set[OperatorReturn]:
    """
    Change selection mode

    Args:
        use_extend: Extend

        use_expand: Expand

        type: Type

        action: Selection action to execute

            DISABLE: Disable selected markers.

            ENABLE: Enable selected markers.

            TOGGLE: Toggle disabled flag for selected markers.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_more(use_face_step: bool = True) -> set[OperatorReturn]:
    """
    Select more vertices, edges or faces connected to initial selection

    Args:
        use_face_step: Face Step, Connected faces (instead of edges)

    Returns:
        Operation results.
    """
    pass


def select_next_item() -> set[OperatorReturn]:
    """
    Select the next element (using selection order)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_non_manifold(
    extend: bool = True,
    use_wire: bool = True,
    use_boundary: bool = True,
    use_multi_face: bool = True,
    use_non_contiguous: bool = True,
    use_verts: bool = True,
) -> set[OperatorReturn]:
    """
    Select all non-manifold vertices or edges

    Args:
        extend: Extend, Extend the selection

        use_wire: Wire, Wire edges

        use_boundary: Boundaries, Boundary edges

        use_multi_face: Multiple Faces, Edges shared by more than two faces

        use_non_contiguous: Non Contiguous, Edges between faces pointing in
            alternate directions

        use_verts: Vertices, Vertices connecting multiple face regions

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_nth(skip: int = 1, nth: int = 1, offset: int = 0) -> set[OperatorReturn]:
    """
    Deselect every Nth element starting from the active vertex, edge or face

    Args:
        skip: Number of deselected elements in the repetitive sequence

            [1, inf]

        nth: Number of selected elements in the repetitive sequence

            [1, inf]

        offset: Offset from the starting point

    Returns:
        Operation results.
    """
    pass


def select_prev_item() -> set[OperatorReturn]:
    """
    Select the previous element (using selection order)

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_random(
    ratio: float = 0.5,
    seed: int = 0,
    action: Literal['SELECT', 'DESELECT'] = 'SELECT',
) -> set[OperatorReturn]:
    """
    Randomly select vertices

    Args:
        ratio: Portion of items to select randomly

            [0, 1]

        seed: Seed for the random number generator

            [0, inf]

        action: Selection action to execute

            SELECT: Select all elements.

            DESELECT: Deselect all elements.

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal,PyShadowingBuiltins
def select_similar(
    type: Literal[
        'VERT_NORMAL',
        'VERT_FACES',
        'VERT_GROUPS',
        'VERT_EDGES',
        'VERT_CREASE',
        'EDGE_LENGTH',
        'EDGE_DIR',
        'EDGE_FACES',
        'EDGE_FACE_ANGLE',
        'EDGE_CREASE',
        'EDGE_BEVEL',
        'EDGE_SEAM',
        'EDGE_SHARP',
        'EDGE_FREESTYLE',
        'FACE_MATERIAL',
        'FACE_AREA',
        'FACE_SIDES',
        'FACE_PERIMETER',
        'FACE_NORMAL',
        'FACE_COPLANAR',
        'FACE_SMOOTH',
        'FACE_FREESTYLE'
    ] = 'VERT_NORMAL',
    compare: Literal['EQUAL', 'GREATER', 'LESS'] = 'EQUAL',
    threshold: float = 0.0,
) -> set[OperatorReturn]:
    """
    Select similar vertices, edges or faces by property types

    Args:
        type: Type

        compare: Compare

        threshold: Threshold

            [0, 1]

    Returns:
        Operation results.
    """
    pass


def select_similar_region() -> set[OperatorReturn]:
    """
    Select similar face regions to the current selection

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def select_ungrouped(extend: bool = False) -> set[OperatorReturn]:
    """
    Select vertices without a group

    Args:
        extend: Extend the selection

    Returns:
        Operation results.
    """
    pass


# noinspection PyShadowingBuiltins,PyUnusedLocal
def separate(type: Literal['SELECTED', 'MATERIAL', 'LOOSE'] = 'SELECTED') -> set[OperatorReturn]:
    """
    Separate selected geometry into a new mesh

    Args:
        type: Type

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def set_normals_from_faces(keep_sharp: bool = False) -> set[OperatorReturn]:
    """
    Set the custom normals from the selected faces ones
    Args:
        keep_sharp: Keep Sharp Edges, Do not set sharp edges to face

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def set_sharpness_by_angle(angle: float = 0.523599, extend: bool = False) -> set[OperatorReturn]:
    """
    Set edge sharpness based on the angle between neighboring faces

    Args:
        angle: Angle

            [0.000174533, 3.14159]

        extend: Add new sharp edges without clearing existing sharp edges

    Returns:
        Operation results.
    """
    pass


def shape_propagate_to_all() -> set[OperatorReturn]:
    """
    Apply selected vertex locations to all other shape keys

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def shortest_path_pick(
    edge_mode: Literal['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE'] = 'SELECT',
    use_face_step: bool = False,
    use_topology_distance: bool = False,
    use_fill: bool = False,
    skip: int = 0,
    nth: int = 1,
    offset: int = 0,
    index: int = -1,
) -> set[OperatorReturn]:
    """
    Select shortest path between two selections

    Args:
        edge_mode: The edge flag to tag when selecting the shortest path

        use_face_step: Face Stepping, Traverse connected faces (includes
            diagonals and edge-rings)

        use_topology_distance: Topology Distance, Find the minimum number of
            steps, ignoring spatial distance

        use_fill: Fill Region, Select all paths between the source/destination
            elements

        skip: Number of deselected elements in the repetitive sequence.

            [0, inf]

        nth: Number of selected elements in the repetitive sequence

            [1, inf]

        offset: Offset from the starting point.

        index: ????? TODO: document this

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def shortest_path_select(
    edge_mode: Literal['SELECT', 'SEAM', 'SHARP', 'CREASE', 'BEVEL', 'FREESTYLE'] = 'SELECT',
    use_face_step: bool = False,
    use_topology_distance: bool = False,
    use_fill: bool = False,
    skip: int = 0,
    nth: int = 1,
    offset: int = 0,
) -> set[OperatorReturn]:
    """
    Selected shortest path between two vertices/edges/faces

    Args:
        edge_mode: The edge flag to tag when selecting the shortest path

        use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)

        use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance

        use_fill: Fill Region, Select all paths between the source/destination elements

        skip: Number of deselected elements in the repetitive sequence.

            [0, inf]

        nth: Number of selected elements in the repetitive sequence

            [1, inf]

        offset: Offset from the starting point

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def smooth_normals(factor: float = 0.5) -> set[OperatorReturn]:
    """
    Smooth custom normals based on adjacent vertex normals
    Args:
        factor: Specifies weight of smooth vs original normal

            [0, 1]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def solidify(thickness: float = 0.01) -> set[OperatorReturn]:
    """
    Create a solid skin by extruding, compensating for sharp angles

    Args:
        thickness: Thickness

            [-10000, 10000]

    Returns:
        Operation results.
    """
    pass


# noinspection PyDefaultArgument,PyUnusedLocal,PyShadowingBuiltins
def sort_elements(
    type: Literal[
        'VIEW_ZAXIS',
        'VIEW_XAXIS',
        'CURSOR_DISTANCE',
        'MATERIAL',
        'SELECTED',
        'RANDOMIZE',
        'REVERSE'
    ] = 'VIEW_ZAXIS',
    elements: set[Literal['VERT', 'EDGE', 'FACE']] = set('VERT'),
    reverse: bool = False,
    seed: int = 0,
) -> set[OperatorReturn]:
    """
    The order of selected vertices/edges/faces is modified, based on a given
    method.

    Args:
        type: Type of reordering operation to apply

            VIEW_ZAXIS: View Z Axis – Sort selected elements from farthest to
            nearest one in current view.

            VIEW_XAXIS: View X Axis – Sort selected elements from left to right
            one in current view.

            CURSOR_DISTANCE: Sort selected elements from nearest to farthest
            from 3D cursor.

            MATERIAL: Sort selected faces from smallest to greatest material
            index.

            SELECTED: Move all selected elements in first places, preserving
            their relative order. Warning: This will affect unselected
            elements' indices as well.

            RANDOMIZE: Randomize order of selected elements.

            REVERSE: Reverse current order of selected elements.

        elements: Which elements to affect (vertices, edges and/or faces)

        reverse: Reverse, Reverse the sorting effect

        seed: Seed for random-based operations.

            [0, inf]

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def spin(
    steps: int = 12,
    dupli: bool = False,
    angle: float = 1.5708,
    use_auto_merge: bool = True,
    use_normal_flip: bool = False,
    center: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
    axis: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0)),
) -> set[OperatorReturn]:
    """
    Extrude selected vertices in a circle around the cursor in indicated viewport

    Args:
        steps: Steps

            [0, 1000000]

        dupli: Use Duplicates

        angle: Rotation for each step

        use_auto_merge: Merge first/last when the angle is a full revolution

        use_normal_flip: Flip Normals

        center: Center in global view space

            Vector of 3 items in [-inf, inf]

        axis: Axis in global view space

            Vector of 3 items in [-1, 1]

    Returns:
        Operation results.
    """
    pass


def split() -> set[OperatorReturn]:
    """
    Split off selected geometry from connected unselected geometry

    Returns:
        Operation results.
    """
    pass


def split_normals() -> set[OperatorReturn]:
    """
    Split custom normals of selected vertices

    Returns:
        Operation results.
    """
    pass


def subdivide(number_cuts=1, smoothness=0.0, ngon: bool = True, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0) -> set[OperatorReturn]:
    """
    Subdivide selected edges

    Args:
        number_cuts (int in [1, 100], (optional)) – Number of Cuts

        smoothness (float in [0, 1000], (optional)) – Smoothness, Smoothness factor

        ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces

        quadcorner (enum in ['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN'], (optional)) – Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)

        fractal (float in [0, 1e+06], (optional)) – Fractal, Fractal randomness factor

        fractal_along_normal (float in [0, 1], (optional)) – Along Normal, Apply fractal displacement along normal only

        seed (int in [0, inf], (optional)) – Random Seed, Seed for the random number generator

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def subdivide_edgering(
    number_cuts: int = 10,
    interpolation: Literal['LINEAR', 'PATH', 'SURFACE'] = 'PATH',
    smoothness: float = 1.0,
    profile_shape_factor: float = 0.0,
    profile_shape: ProportionalFalloffCurveOnly = 'SMOOTH',
) -> set[OperatorReturn]:
    """
    Subdivide perpendicular edges to the selected edge-ring

    Args:
        number_cuts: Number of Cuts

            `[0, 1000]`

        interpolation: Interpolation method

        smoothness: Smoothness factor

            `[0, 1000]`

        profile_shape_factor:: How much intermediary new edges are
            shrunk/expanded.

            `[-1000, 1000]`

        profile_shape: Shape of the profile

    Returns:
        Operation results.
    """
    pass


def symmetrize(direction='NEGATIVE_X', threshold=0.0001) -> set[OperatorReturn]:
    """
    Enforce symmetry (both form and topological) across an axis

    Args:
        direction (enum in Symmetrize Direction Items, (optional)) – Direction, Which sides to copy from and to

        threshold (float in [0, 10], (optional)) – Threshold, Limit for snap middle vertices to the axis center

    Returns:
        Operation results.
    """
    pass


def symmetry_snap(direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center: bool = True) -> set[OperatorReturn]:
    """
    Snap vertex pairs to their mirrored locations

    Args:
        direction (enum in Symmetrize Direction Items, (optional)) – Direction, Which sides to copy from and to

        threshold (float in [0, 10], (optional)) – Threshold, Distance within which matching vertices are searched

        factor (float in [0, 1], (optional)) – Factor, Mix factor of the locations of the vertices

        use_center: Center, Snap middle vertices to the axis center

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def tris_convert_to_quads(
    face_threshold: float = 0.698132,
    shape_threshold: float = 0.698132,
    uvs: bool = False,
    vcols: bool = False,
    seam: bool = False,
    sharp: bool = False,
    materials: bool = False,
) -> set[OperatorReturn]:
    """
    Join triangles into quads

    Args:
        face_threshold: Face angle limit

            `[0, 3.14159]`

        shape_threshold: Shape angle limit

            `[0, 3.14159]`

        uvs: Compare UVs

        vcols: Compare VCols

        seam: Compare Seam

        sharp: Compare Sharp

        materials: Compare Materials

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def unsubdivide(iterations: int = 2) -> set[OperatorReturn]:
    """
    Un-subdivide selected edges and faces

    Args:
        iterations: Number of times to un-subdivide.

            `[1, 1000]`

    Returns:
        Operation results.
    """
    pass


def uv_texture_add() -> set[OperatorReturn]:
    """
    Add UV map

    Returns:
        Operation results.
    """
    pass


def uv_texture_remove() -> set[OperatorReturn]:
    """
    Remove UV map

    Returns:
        Operation results.
    """
    pass


def uvs_reverse() -> set[OperatorReturn]:
    """
    Flip direction of UV coordinates inside faces

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def uvs_rotate(use_ccw: bool = False) -> set[OperatorReturn]:
    """
    Rotate UV coordinates inside faces

    Args:
        use_ccw: Counterclockwise

    Returns:
        Operation results.
    """
    pass


def vert_connect() -> set[OperatorReturn]:
    """
    Connect selected vertices of faces, splitting the face

    Returns:
        Operation results.
    """
    pass


def vert_connect_concave() -> set[OperatorReturn]:
    """
    Make all faces convex

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def vert_connect_nonplanar(angle_limit: float = 0.0872665) -> set[OperatorReturn]:
    """
    Split non-planar faces that exceed the angle threshold

    Args:
        angle_limit: Angle limit

            `[0, 3.14159]`

    Returns:
        Operation results.
    """
    pass


def vert_connect_path() -> set[OperatorReturn]:
    """
    Connect vertices by their selection order, creating edges, splitting faces

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def vertices_smooth(
    factor: float = 0.0,
    repeat: int = 1,
    xaxis: bool = True,
    yaxis: bool = True,
    zaxis: bool = True,
    wait_for_input: bool = True,
) -> set[OperatorReturn]:
    """
    Flatten angles of selected vertices

    Args:
        factor: Smoothing factor

            `[-10, 10]`

        repeat: Number of times to smooth the mesh

            `[1, 1000]`

        xaxis: X-Axis, Smooth along the X axis

        yaxis: Y-Axis, Smooth along the Y axis

        zaxis: Z-Axis, Smooth along the Z axis

        wait_for_input: Wait for Input

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def vertices_smooth_laplacian(
    repeat: int = 1,
    lambda_factor: float = 1.0,
    lambda_border: float = 5e-05,
    use_x: bool = True,
    use_y: bool = True,
    use_z: bool = True,
    preserve_volume: bool = True,
) -> set[OperatorReturn]:
    """
    Laplacian smooth of selected vertices

    Args:
        repeat: Number of iterations to smooth the mesh.

            [1, 1000]

        lambda_factor: Lambda factor

            [1e-07, 1000]

        lambda_border: Lambda factor in border

            [1e-07, 1000]

        use_x: Smooth object along X axis

        use_y: Smooth object along Y axis

        use_z: Smooth object along Z axis

        preserve_volume: Apply volume preservation after smooth

    Returns:
        Operation results.
    """
    pass


# noinspection PyUnusedLocal
def wireframe(
    use_boundary: bool = True,
    use_even_offset: bool = True,
    use_relative_offset: bool = False,
    use_replace: bool = True,
    thickness: float = 0.01,
    offset: float = 0.01,
    use_crease: bool = False,
    crease_weight: float = 0.01,
) -> set[OperatorReturn]:
    """
    Create a solid wireframe from faces

    Args:
        use_boundary: Boundary, Inset face boundaries

        use_even_offset: Offset Even, Scale the offset to give more even thickness

        use_relative_offset: Offset Relative, Scale the offset by surrounding geometry

        use_replace: Replace, Remove original faces

        thickness: Thickness

            [0, 10000]

        offset: Offset

            [0, 10000]

        use_crease: Crease hub edges for an improved subdivision surface.

        crease_weight: – Crease Weight

            [0, 1000]

    Returns:
        Operation results.
    """
    pass
