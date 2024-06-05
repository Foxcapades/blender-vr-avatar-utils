from typing import ContextManager, Iterable, Literal, Sequence

from base import bpy_struct, bpy_prop_collection

import mathutils as mathutils

import a
import c
import d
import f
import g
import i
import k
import l
import m
import n
import o
import p
import s
import t
import v
import w

BakeMarginType = Literal['ADJACENT_FACES', 'EXTEND']

BakePassFilterType = Literal[
    'NONE',
    'EMIT',
    'DIRECT',
    'INDIRECT',
    'COLOR',
    'DIFFUSE',
    'GLOSSY',
    'TRANSMISSION',
]

BakeSaveMode = Literal['INTERNAL', 'EXTERNAL']

BakeTarget = Literal['IMAGE_TEXTURES', 'VERTEX_COLORS']

BeztripleKeyframeType = Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER']

BoidruleType = Literal[
    'GOAL',
    'AVOID',
    'AVOID_COLLISION',
    'SEPARATE',
    'FLOCK',
    'FOLLOW_LEADER',
    'AVERAGE_SPEED',
    'FIGHT',
]

BrushCurvesSculptTool = Literal[
    'SELECTION_PAINT',
    'ADD',
    'DELETE',
    'DENSITY',
    'COMB',
    'SNAKE_HOOK',
    'GROW_SHRINK',
    'PINCH',
    'PUFF',
    'SMOOTH',
    'SLIDE',
]

BrushGpencilSculptTypes = Literal[
    'SMOOTH',
    'THICKNESS',
    'STRENGTH',
    'RANDOMIZE',
    'GRAB',
    'PUSH',
    'TWIST',
    'PINCH',
    'CLONE',
]

BrushGpencilTypes = Literal['DRAW', 'FILL', 'ERASE', 'TINT']

BrushGpencilVertexTypes = Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR', 'REPLACE']

BrushGpencilWeightTypes = Literal['WEIGHT', 'BLUR', 'AVERAGE', 'SMEAR']

BrushImageTool = Literal['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK']

BrushSculptTool = Literal[
    'DRAW',
    'DRAW_SHARP',
    'CLAY',
    'CLAY_STRIPS',
    'CLAY_THUMB',
    'LAYER',
    'INFLATE',
    'BLOB',
    'CREASE',
    'SMOOTH',
    'FLATTEN',
    'FILL',
    'SCRAPE',
    'MULTIPLANE_SCRAPE',
    'PINCH',
    'GRAB',
    'ELASTIC_DEFORM',
    'SNAKE_HOOK',
    'THUMB',
    'POSE',
    'NUDGE',
    'ROTATE',
    'TOPOLOGY',
    'BOUNDARY',
    'CLOTH',
    'SIMPLIFY',
    'MASK',
    'DRAW_FACE_SETS',
    'DISPLACEMENT_ERASER',
    'DISPLACEMENT_SMEAR',
    'PAINT',
    'SMEAR',
]

BrushUvSculptTool = Literal['GRAB', 'RELAX', 'PINCH']

BrushVertexTool = Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']

BrushWeightTool = Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']


class BakeSettings(bpy_struct):
    cage_extrusion: float
    cage_object: o.Object
    filepath: str
    height: int
    margin: int
    margin_type: BakeMarginType
    max_ray_distance: float
    normal_b: n.NormalSwizzle
    normal_g: n.NormalSwizzle
    normal_r: n.NormalSwizzle
    normal_space: n.NormalSpace
    pass_filter: BakeSaveMode
    target: BakeTarget
    use_automatic_name: bool
    use_cage: bool
    use_clear: bool
    use_pass_color: bool
    use_pass_diffuse: bool
    use_pass_direct: bool
    use_pass_emit: bool
    use_pass_glossy: bool
    use_pass_indirect: bool
    use_pass_transmission: bool
    use_selected_to_active: bool
    use_split_materials: bool
    view_from: Literal['ABOVE_SURFACE', 'ACTIVE_CAMERA']
    width: int

    # noinspection PyPropertyDefinition
    @property
    def image_settings(self) -> i.ImageFormatSettings: pass


class BevelModifier(m.Modifier):
    affect: Literal['VERTICES', 'EDGES']
    angle_limit: float
    face_strength_mode: Literal['FSTR_NONE', 'FSTR_NEW', 'FSTR_AFFECTED', 'FSTR_ALL']
    harden_normals: bool
    invert_vertex_group: bool
    limit_method: Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']
    loop_slide: bool
    mark_seam: bool
    mark_sharp: bool
    material: int
    miter_inner: Literal['MITER_SHARP', 'MITER_ARC']
    miter_outer: Literal['MITER_SHARP', 'MITER_PATCH', 'MITER_ARC']
    offset_type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']
    profile: float
    profile_type: Literal['SUPERELLIPSE', 'CUSTOM']
    segments: int
    spread: float
    use_clamp_overlap: bool
    vertex_group: str
    vmesh_method: Literal['ADJ', 'CUTOFF']
    width: float
    width_pct: float

    # noinspection PyPropertyDefinition
    @property
    def custom_profile(self) -> c.CurveProfile: pass


class BezierSplinePoint(bpy_struct):
    co: mathutils.Vector
    handle_left: mathutils.Vector
    handle_left_type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
    handle_right: mathutils.Vector
    handle_right_type: Literal['FREE', 'VECTOR', 'ALIGNED', 'AUTO']
    hide: bool
    radius: float
    select_control_point: bool
    select_left_handle: bool
    select_right_handle: bool
    tilt: float
    weight_softbody: float


# noinspection PyPropertyDefinition
class BlendData(bpy_struct):
    use_autopack: bool

    @property
    def actions(self) -> 'BlendDataActions': pass
    @property
    def armatures(self) -> 'BlendDataArmatures': pass
    @property
    def brushes(self) -> 'BlendDataBrushes': pass
    @property
    def cache_files(self) -> 'BlendDataCacheFiles': pass
    @property
    def cameras(self) -> 'BlendDataCameras': pass
    @property
    def collections(self) -> 'BlendDataCollections': pass
    @property
    def curves(self) -> 'BlendDataCurves': pass
    @property
    def filepath(self) -> str: pass
    @property
    def fonts(self) -> 'BlendDataFonts': pass
    @property
    def grease_pencils(self) -> 'BlendDataGreasePencils': pass
    @property
    def hair_curves(self) -> 'BlendDataHairCurves': pass
    @property
    def images(self) -> 'BlendDataImages': pass
    @property
    def is_dirty(self) -> bool: pass
    @property
    def is_saved(self) -> bool: pass
    @property
    def lattices(self) -> 'BlendDataLattices': pass
    @property
    def libraries(self) -> 'BlendDataLibraries': pass
    @property
    def lightprobes(self) -> 'BlendDataProbes': pass
    @property
    def lights(self) -> 'BlendDataLights': pass
    @property
    def linestyles(self) -> 'BlendDataLineStyles': pass
    @property
    def masks(self) -> 'BlendDataMasks': pass
    @property
    def materials(self) -> 'BlendDataMaterials': pass
    @property
    def meshes(self) -> 'BlendDataMeshes': pass
    @property
    def metaballs(self) -> 'BlendDataMetaBalls': pass
    @property
    def movieclips(self) -> 'BlendDataMovieClips': pass
    @property
    def node_groups(self) -> 'BlendDataNodeTrees': pass
    @property
    def objects(self) -> 'BlendDataObjects': pass
    @property
    def paint_curves(self) -> 'BlendDataPaintCurves': pass
    @property
    def palettes(self) -> 'BlendDataPalettes': pass
    @property
    def particles(self) -> 'BlendDataParticles': pass
    @property
    def pointclouds(self) -> 'BlendDataPointClouds': pass
    @property
    def scenes(self) -> 'BlendDataScenes': pass
    @property
    def screens(self) -> 'BlendDataScreens': pass
    @property
    def shape_keys(self) -> bpy_prop_collection[k.Key]: pass
    @property
    def sounds(self) -> 'BlendDataSounds': pass
    @property
    def speakers(self) -> 'BlendDataSpeakers': pass
    @property
    def texts(self) -> 'BlendDataTexts': pass
    @property
    def textures(self) -> 'BlendDataTextures': pass
    @property
    def version(self) -> tuple[int, int, int]: pass
    @property
    def volumes(self) -> 'BlendDataVolumes': pass
    @property
    def window_managers(self) -> 'BlendDataWindowManagers': pass
    @property
    def workspaces(self) -> 'BlendDataWorkSpaces': pass
    @property
    def worlds(self) -> 'BlendDataWorlds': pass
    def batch_remove(self, ids: Iterable[i.ID]) -> None: pass
    def orphans_purge(
        self,
        do_local_ids: bool = True,
        do_linked_ids: bool = True,
        do_recursive: bool = False,
    ) -> int: pass
    def temp_data(self, filepath: str | bytes | None = None) -> 'BlendData': pass
    def user_map(self, subset: Sequence, key_types: set[i.ID], value_types: set[i.ID]) -> dict[i.ID, set[i.ID]]: pass


class BlendDataActions(bpy_prop_collection[a.Action]):
    def new(self, name: str) -> a.Action: pass

    def remove(
        self,
        action: a.Action,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataArmatures(bpy_prop_collection[a.Armature]):
    def new(self, name: str) -> a.Armature: pass

    def remove(
        self,
        armature: a.Armature,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataBrushes(bpy_prop_collection['Brush']):
    def new(self, name: str) -> 'Brush': pass

    def remove(
        self,
        armature: 'Brush',
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass

    def create_gpencil_data(self, brush: 'Brush') -> None: pass


class BlendDataCacheFiles(bpy_prop_collection[c.CacheFile]):
    def tag(self, value: bool) -> None: pass


class BlendDataCameras(bpy_prop_collection[c.Camera]):
    def new(self, name: str) -> c.Camera: pass

    def remove(
        self,
        camera: c.Camera,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataCollections(bpy_prop_collection[c.Collection]):
    def new(self, name: str) -> c.Collection: pass

    def remove(
        self,
        collection: c.Collection,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataCurves(bpy_prop_collection[c.Curve]):
    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: o.ObjectTypeCurve) -> c.Curve: pass

    def remove(
        self,
        curve: c.Curve,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataFonts(bpy_prop_collection[v.VectorFont]):
    def load(self, filepath: str, check_existing: bool = False) -> v.VectorFont: pass

    def remove(
        self,
        vfont: v.VectorFont,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataGreasePencils(bpy_prop_collection[g.GreasePencil]):
    def new(self, name: str) -> g.GreasePencil: pass

    def remove(
        self,
        grease_pencil: g.GreasePencil,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataHairCurves(bpy_prop_collection[c.Curves]):
    def new(self, name: str) -> c.Curves: pass

    def remove(
        self,
        curves: c.Curves,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataImages(bpy_prop_collection[i.Image]):
    def new(
        self,
        name: str,
        width: int,
        height: int,
        alpha: bool = False,
        float_buffer: bool = False,
        stereo3d: bool = False,
        is_data: bool = False,
        tiled: bool = False,
    ) -> i.Image: pass

    def load(self, filepath: str, check_existing: bool = False) -> i.Image: pass

    def remove(
        self,
        image: i.Image,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataLattices(bpy_prop_collection[l.Lattice]):
    def new(self, name: str) -> l.Lattice: pass

    def remove(
        self,
        lattice: l.Lattice,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataLibraries(bpy_prop_collection[l.Library]):
    def load(
        self,
        filepath: str,
        link: bool = False,
        relative: bool = False,
        assets_only: bool = False,
        create_liboverrides: bool = False,
        reuse_liboverrides: bool = False,
        create_liboverrides_runtime: bool = False,
    ) -> ContextManager[tuple[l.Library, l.Library]]: pass

    def remove(
        self,
        library: l.Library,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass

    def write(
        self,
        filepath: str,
        datablocks: set[i.ID],
        path_remap: bool = False,
        fake_user: bool = False,
        compress: bool = False,
    ) -> None: pass


class BlendDataLights(bpy_prop_collection[l.Light]):
    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: l.LightType) -> l.Light: pass

    def remove(
        self,
        light: l.Light,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataLineStyles(bpy_prop_collection[f.FreestyleLineStyle]):
    def new(self, name: str) -> f.FreestyleLineStyle: pass

    def remove(
        self,
        linestyle: f.FreestyleLineStyle,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataMasks(bpy_prop_collection[m.Mask]):
    def new(self, name: str) -> m.Mask: pass

    def remove(
        self,
        mask: m.Mask,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataMaterials(bpy_prop_collection[m.Material]):
    def create_gpencil_data(self, material: m.Material): pass

    def new(self, name: str) -> m.Material: pass

    def remove(
        self,
        material: m.Material,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def remove_gpencil_data(self, material: m.Material) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataMeshes(bpy_prop_collection[m.Mesh]):
    def new(self, name: str) -> m.Mesh: pass

    def new_from_object(
        self,
        object: o.Object,
        preserve_all_data_layers: bool = False,
        depsgraph: d.Depsgraph | None = None,
    ) -> m.Mesh: pass

    def remove(
        self,
        mesh: m.Mesh,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataMetaBalls(bpy_prop_collection[m.MetaBall]):
    def new(self, name: str) -> m.MetaBall: pass

    def remove(
        self,
        metaball: m.MetaBall,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataMovieClips(bpy_prop_collection[m.MovieClip]):
    def load(self, filepath: str, check_existing: bool = False) -> m.MovieClip: pass

    def remove(
        self,
        clip: m.MovieClip,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataNodeTrees(bpy_prop_collection[n.NodeTree]):
    def new(self, name: str) -> n.NodeTree: pass

    def remove(
        self,
        tree: n.NodeTree,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataObjects(bpy_prop_collection[o.Object]):
    def new(self, name: str, object_data: i.ID) -> o.Object: pass

    # noinspection PyShadowingBuiltins
    def remove(
        self,
        object: o.Object,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataPaintCurves(bpy_prop_collection[p.PaintCurve]):
    def tag(self, value: bool) -> None: pass


class BlendDataPalettes(bpy_prop_collection[p.Palette]):
    def new(self, name: str) -> p.Palette: pass

    def remove(
        self,
        palette: p.Palette,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataParticles(bpy_prop_collection[p.ParticleSettings]):
    def new(self, name: str) -> p.ParticleSettings: pass

    def remove(
        self,
        particle: p.ParticleSettings,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataPointClouds(bpy_prop_collection[p.PointCloud]):
    def new(self, name: str) -> p.PointCloud: pass

    def remove(
        self,
        pointcloud: p.PointCloud,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataProbes(bpy_prop_collection[l.LightProbe]):
    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: l.LightprobesType) -> l.LightProbe: pass

    def remove(
        self,
        lightprobe: l.LightProbe,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataScenes(bpy_prop_collection[s.Scene]):
    def new(self, name: str) -> s.Scene: pass

    def remove(self, scene: s.Scene, do_unlink: bool = True) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataScreens(bpy_prop_collection[s.Screen]):
    def tag(self, value: bool) -> None: pass


class BlendDataSounds(bpy_prop_collection[s.Sound]):
    def load(self, filepath: str, check_existing: bool = False) -> s.Sound: pass

    def remove(
        self,
        sound: s.Sound,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataSpeakers(bpy_prop_collection[s.Speaker]):
    def new(self, name: str) -> s.Speaker: pass

    def remove(
        self,
        speaker: s.Speaker,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataTexts(bpy_prop_collection[t.Text]):
    def new(self, name: str) -> t.Text: pass

    def remove(
        self,
        text: t.Text,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def load(self, filepath: str, internal: bool = False) -> t.Text: pass

    def tag(self, value: bool) -> None: pass


class BlendDataTextures(bpy_prop_collection[t.Texture]):
    # noinspection PyShadowingBuiltins
    def new(self, name: str, type: t.TextureType) -> s.Speaker: pass

    def remove(
        self,
        speaker: s.Speaker,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataVolumes(bpy_prop_collection[v.Volume]):
    def new(self, name: str) -> v.Volume: pass

    def remove(
        self,
        volume: v.Volume,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


class BlendDataWindowManagers(bpy_prop_collection[w.WindowManager]):
    def tag(self, value: bool) -> None: pass


class BlendDataWorkSpaces(bpy_prop_collection[w.WorkSpace]):
    def tag(self, value: bool) -> None: pass


class BlendDataWorlds(bpy_prop_collection[w.World]):
    def new(self, name: str) -> w.World: pass

    def remove(
        self,
        world: w.World,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: pass

    def tag(self, value: bool) -> None: pass


# noinspection PyPropertyDefinition
class BlendTexture(bpy_struct):
    progression: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL']
    use_flip_axis: Literal['HORIZONTAL', 'VERTICAL']

    # TODO: what does this return?  a bpy_prop_collection?  a Sequence?
    @property
    def users_material(self): pass

    # TODO: what does this return?  a bpy_prop_collection?  a Sequence?
    @property
    def users_object_modifier(self): pass


# noinspection PyPropertyDefinition
class BlenderRNA(bpy_struct):
    @property
    def structs(self) -> bpy_prop_collection[s.Struct]: pass


class BoidRule(bpy_struct):
    name: str
    use_in_air: bool
    use_on_land: bool

    # noinspection PyPropertyDefinition
    @property
    def type(self) -> BoidruleType: pass


class BoidRuleAverageSpeed(BoidRule):
    level: float
    speed: float
    wander: float


class BoidRuleAvoid(BoidRule):
    fear_factor: float
    object: o.Object
    use_predict: bool


class BoidRuleAvoidCollision(BoidRule):
    look_ahead: float
    use_avoid: bool
    use_avoid_collision: bool


class BoidRuleFight(BoidRule):
    distance: float
    flee_distance: float


class BoidRuleFollowLeader(BoidRule):
    distance: float
    object: o.Object
    queue_count: int
    use_line: bool


class BoidRuleGoal(BoidRule):
    object: o.Object
    use_predict: bool


# noinspection PyPropertyDefinition
class BoidSettings(BoidRule):
    accuracy: float
    active_boid_state_index: int
    aggression: float
    air_acc_max: float
    air_ave_max: float
    air_personal_space: float
    air_speed_max: float
    air_speed_min: float
    bank: float
    health: float
    height: float
    land_acc_max: float
    land_ave_max: float
    land_jump_speed: float
    land_personal_space: float
    land_smooth: float
    land_speed_max: float
    land_stick_force: float
    pitch: float
    range: float
    strength: float
    use_climb: bool
    use_flight: bool
    use_land: bool

    @property
    def states(self) -> bpy_prop_collection['BoidState']: pass

    @property
    def active_boid_state(self) -> BoidRule: pass


# noinspection PyPropertyDefinition
class BoidState(bpy_struct):
    active_boid_rule_index: int
    falloff: float
    name: str
    rule_fuzzy: float
    ruleset_type: Literal['FUZZY', 'RANDOM', 'AVERAGE']
    volume: float

    @property
    def active_boid_rule(self) -> BoidRule: pass

    @property
    def rules(self) -> bpy_prop_collection[BoidRule]: pass


# noinspection PyPropertyDefinition,PyPep8Naming
class Bone(bpy_struct):
    bbone_curveinx: float
    bbone_curveinz: float
    bbone_curveoutx: float
    bbone_curveoutz: float
    bbone_custom_handle_end: 'Bone'
    bbone_custom_handle_start: 'Bone'
    bbone_easein: float
    bbone_easeout: float
    bbone_handle_type_end: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT']
    bbone_handle_type_start: Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT']
    bbone_handle_use_ease_end: bool
    bbone_handle_use_ease_start: bool
    bbone_handle_use_scale_end: Literal['STRAIGHT', 'CURVED']
    bbone_rollin: float
    bbone_rollout: float
    bbone_scalein: int
    bbone_x: float
    bbone_z: float
    envelope_distance: float
    envelope_weight: float
    head: float
    hide: bool
    hide_select: bool
    inherit_scale: Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY']
    matrix: str
    select: bool
    select_head: bool
    select_tail: bool
    show_wire: bool
    tail: float
    use_cyclic_offset: bool
    use_deform: bool
    use_endroll_as_inroll: bool
    use_envelope_multiply: bool
    use_inherit_rotation: bool
    use_local_location: bool
    use_relative_parent: bool
    use_scale_easing: bool

    @property
    def children(self) -> bpy_prop_collection['Bone']: pass

    @property
    def collections(self) -> 'BoneCollectionMemberships': pass

    @property
    def color(self) -> 'BoneColor': pass

    @property
    def length(self) -> float: pass

    @property
    def parent(self) -> 'Bone': pass

    @property
    def use_connect(self) -> bool: pass

    @property
    def basename(self) -> str: pass

    # TODO: what is this?
    @property
    def center(self): pass

    # TODO: this returns some type of collection of bones?
    @property
    def children_recursive(self): pass

    # TODO: this returns some type of collection of bones?
    @property
    def children_recursive_basename(self): pass

    # TODO: this returns some type of collection of bones?
    @property
    def parent_recursive(self): pass

    # TODO: does this return a vector, a tuple, something else?
    @property
    def vector(self): pass

    # TODO: does this return a vector, a tuple, something else?
    @property
    def x_axis(self): pass

    # TODO: does this return a vector, a tuple, something else?
    @property
    def y_axis(self): pass

    # TODO: does this return a vector, a tuple, something else?
    @property
    def z_axis(self): pass

    def evaluate_envelope(self, point: mathutils.Vector) -> float: pass

    def convert_local_to_pose(
        self,
        matrix: mathutils.Matrix,
        matrix_local: mathutils.Matrix,
        parent_matrix: mathutils.Matrix = mathutils.Matrix(
            (
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0)
            )
        ),
        parent_matrix_local: mathutils.Matrix = mathutils.Matrix(
            (
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0),
                (0.0, 0.0, 0.0, 0.0))
        ),
        invert: bool = False
    ) -> mathutils.Matrix: pass

    @classmethod
    def MatrixFromAxisRoll(cls, axis: mathutils.Vector, roll: float) -> mathutils.Matrix: pass

    @classmethod
    def AxisRollFromMatrix(cls, matrix: mathutils.Matrix, axis: tuple[float, float, float]) -> tuple[
        mathutils.Vector, float]: pass

    # TODO: what the heck is this?
    def parent_index(self, parent_test): pass

    # TODO: what is the type of vec?  is it mathutils.Vector?
    def translate(self, vec) -> None: pass


# noinspection PyPropertyDefinition
class BoneCollection(bpy_struct):
    child_number: int
    is_expanded: bool
    is_solo: bool
    is_visible: bool
    name: str
    parent: 'BoneCollection | None'

    @property
    def bones(self) -> bpy_prop_collection[Bone]: pass

    @property
    def children(self) -> bpy_prop_collection['BoneCollection']: pass

    @property
    def index(self) -> int: pass

    @property
    def is_editable(self) -> bool: pass

    @property
    def is_local_override(self) -> bool: pass

    @property
    def is_visible_ancestors(self) -> bool: pass

    @property
    def is_visible_effectively(self) -> bool: pass

    # TODO: A set of all bones assigned to this bone collection and its child collections.
    @property
    def bones_recursive(self): pass


class BoneCollectionMemberships(bpy_prop_collection[BoneCollection]):
    def clear(self) -> None: pass


class BoneCollections(bpy_prop_collection[BoneCollection]):
    active: BoneCollection
    active_index: int
    active_name: str

    # noinspection PyPropertyDefinition
    @property
    def is_solo_active(self) -> False: pass

    def new(self, name: str, parent: BoneCollection | None = None) -> BoneCollection: pass

    def remove(self, bone_collection: BoneCollection) -> None: pass

    def move(self, from_index: int, to_index: int) -> None: pass


# noinspection PyPropertyDefinition
class BoneColor(bpy_struct):
    palette: Literal[
        'DEFAULT',
        'THEME01',
        'THEME02',
        'THEME03',
        'THEME04',
        'THEME05',
        'THEME06',
        'THEME07',
        'THEME08',
        'THEME09',
        'THEME10',
        'THEME11',
        'THEME12',
        'THEME13',
        'THEME14',
        'THEME15',
        'THEME16',
        'THEME17',
        'THEME18',
        'THEME19',
        'THEME20',
        'CUSTOM'
    ]

    @property
    def custom(self) -> t.ThemeBoneColorSet: pass

    @property
    def is_custom(self) -> bool: pass


class BoolAttribute(a.Attribute):
    data: bpy_prop_collection['BoolAttributeValue']


class BoolAttributeValue(bpy_struct):
    value: bool


# noinspection PyPropertyDefinition
class BoolProperty(p.Property):
    @property
    def array_dimensions(self) -> tuple[int, int, int]: pass

    @property
    def array_length(self) -> int: pass

    @property
    def default(self) -> bool: pass

    @property
    def default_array(self) -> tuple[bool, bool, bool]: pass

    @property
    def is_array(self) -> bool: pass


class BooleanModifier(m.Modifier):
    collection: c.Collection
    debug_options: set[Literal['SEPARATE', 'NO_DISSOLVE', 'NO_CONNECT_REGIONS']]
    double_threshold: float
    material_mode: Literal['INDEX', 'TRANSFER']
    object: o.Object
    operand_type: Literal['OBJECT', 'COLLECTION']
    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE']
    solver: Literal['FAST', 'EXACT']
    use_hole_tolerant: bool
    use_self: bool


class BrightContrastModifier(s.SequenceModifier):
    bright: float
    contrast: float


# noinspection PyPropertyDefinition
class Brush(i.ID):
    area_radius_factor: float
    auto_smooth_factor: float
    automasking_boundary_edges_propagation_steps: int
    automasking_cavity_blur_steps: int
    automasking_cavity_factor: float
    automasking_start_normal_falloff: float
    automasking_start_normal_limit: float
    automasking_view_normal_falloff: float
    automasking_view_normal_limit: float
    blend: Literal[
        'MIX',
        'DARKEN',
        'MUL',
        'COLORBURN',
        'LINEARBURN',
        'LIGHTEN',
        'SCREEN',
        'COLORDODGE',
        'ADD',
        'OVERLAY',
        'SOFTLIGHT',
        'HARDLIGHT',
        'VIVIDLIGHT',
        'LINEARLIGHT',
        'PINLIGHT',
        'DIFFERENCE',
        'EXCLUSION',
        'SUB',
        'HUE',
        'SATURATION',
        'COLOR',
        'LUMINOSITY',
        'ERASE_ALPHA',
        'ADD_ALPHA'
    ]
    blur_kernel_radius: int
    blur_mode: Literal['BOX', 'GAUSSIAN']
    boundary_deform_type: Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']
    boundary_falloff_type: Literal['CONSTANT', 'RADIUS', 'LOOP', 'LOOP_INVERT']
    boundary_offset: float
    clone_alpha: float
    clone_image: i.Image
    clone_offset: mathutils.Vector
    cloth_constraint_softbody_strength: float
    cloth_damping: float
    cloth_deform_type: Literal[
        'DRAG',
        'PUSH',
        'PINCH_POINT',
        'PINCH_PERPENDICULAR',
        'INFLATE',
        'GRAB',
        'EXPAND',
        'SNAKE_HOOK'
    ]
    cloth_force_falloff_type: Literal['RADIAL', 'PLANE']
    cloth_mass: float
    cloth_sim_falloff: float
    cloth_sim_limit: float
    cloth_simulation_area_type: Literal['LOCAL', 'GLOBAL', 'DYNAMIC']
    color: mathutils.Color
    color_type: Literal['COLOR', 'GRADIENT']
    crease_pinch_factor: float
    cursor_color_add: tuple[float, float, float, float]
    cursor_color_subtract: tuple[float, float, float, float]
    cursor_overlay_alpha: int
    curve_preset: Literal[
        'CUSTOM', 'SMOOTH', 'SMOOTHER', 'SPHERE', 'ROOT', 'SHARP', 'LIN', 'POW4', 'INVSQUARE', 'CONSTANT']
    curves_sculpt_tool: BrushCurvesSculptTool
    dash_ratio: float
    dash_samples: int
    deform_target: Literal['GEOMETRY', 'CLOTH_SIM']
    density: float
    direction: Literal['ADD', 'SUBTRACT']
    disconnected_distance_max: float
    elastic_deform_type: Literal['GRAB', 'GRAB_BISCALE', 'GRAB_TRISCALE', 'SCALE', 'TWIST']
    elastic_deform_volume_preservation: float
    falloff_angle: float
    falloff_shape: Literal['SPHERE', 'PROJECTED']
    fill_threshold: float
    flow: float
    gpencil_sculpt_tool: BrushGpencilSculptTypes
    gpencil_tool: BrushGpencilTypes
    gpencil_vertex_tool: BrushGpencilVertexTypes
    gpencil_weight_tool: BrushGpencilWeightTypes
    grad_spacing: int
    gradient_fill_mode: Literal['LINEAR', 'RADIAL']
    gradient_stroke_mode: Literal['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP']
    hardness: float
    height: float
    icon_filepath: str
    image_tool: BrushImageTool
    input_samples: int
    invert_density_pressure: bool
    invert_flow_pressure: bool
    invert_hardness_pressure: bool
    invert_to_scrape_fill: bool
    invert_wet_mix_pressure: bool
    invert_wet_persistence_pressure: bool
    jitter: float
    jitter_absolute: int
    jitter_unit: Literal['VIEW', 'BRUSH']
    mask_overlay_alpha: int
    mask_stencil_dimension: mathutils.Vector
    mask_stencil_pos: mathutils.Vector
    mask_texture: t.Texture
    mask_tool: Literal['DRAW', 'SMOOTH']
    multiplane_scrape_angle: float
    normal_radius_factor: float
    normal_weight: float
    paint_curve: p.PaintCurve
    plane_offset: float
    plane_trim: float
    pose_deform_type: Literal['ROTATE_TWIST', 'SCALE_TRANSLATE', 'SQUASH_STRETCH']
    pose_ik_segments: int
    pose_offset: float
    pose_origin_type: Literal['TOPOLOGY', 'FACE_SETS', 'FACE_SETS_FK']
    pose_smooth_iterations: int
    rake_factor: float
    rate: float
    sculpt_plane: Literal['AREA', 'VIEW', 'X', 'Y', 'Z']
    sculpt_tool: BrushSculptTool
    secondary_color: mathutils.Color
    sharp_threshold: float
    show_multiplane_scrape_planes_preview: bool
    size: int
    slide_deform_type: Literal['DRAG', 'PINCH', 'EXPAND']
    smear_deform_type: Literal['DRAG', 'PINCH', 'EXPAND']
    smooth_deform_type: Literal['LAPLACIAN', 'SURFACE']
    smooth_stroke_factor: float
    smooth_stroke_radius: int
    snake_hook_deform_type: Literal['FALLOFF', 'ELASTIC']
    spacing: int
    stencil_dimension: mathutils.Vector
    stencil_pos: mathutils.Vector
    strength: float
    stroke_method: Literal['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']
    surface_smooth_current_vertex: float
    surface_smooth_iterations: int
    surface_smooth_shape_preservation: float
    texture: t.Texture
    texture_overlay_alpha: int
    texture_sample_bias: float
    tilt_strength_factor: float
    tip_roundness: float
    tip_scale_x: float
    topology_rake_factor: float
    unprojected_radius: float
    use_accumulate: bool
    use_adaptive_space: bool
    use_airbrush: bool
    use_alpha: bool
    use_anchor: bool
    use_automasking_boundary_edges: bool
    use_automasking_boundary_face_sets: bool
    use_automasking_cavity: bool
    use_automasking_cavity_inverted: bool
    use_automasking_custom_cavity_curve: bool
    use_automasking_face_sets: bool
    use_automasking_start_normal: bool
    use_automasking_topology: bool
    use_automasking_view_normal: bool
    use_automasking_view_occlusion: bool
    use_cloth_collision: bool
    use_cloth_pin_simulation_boundary: bool
    use_color_as_displacement: bool
    use_connected_only: bool
    use_cursor_overlay: bool
    use_cursor_overlay_override: bool
    use_curve: bool
    use_custom_icon: bool
    use_density_pressure: bool
    use_edge_to_edge: bool
    use_flow_pressure: bool
    use_frontface: bool
    use_frontface_falloff: bool
    use_grab_active_vertex: bool
    use_grab_silhouette: bool
    use_hardness_pressure: bool
    use_inverse_smooth_pressure: bool
    use_line: bool
    use_locked_size: Literal['VIEW', 'SCENE']
    use_multiplane_scrape_dynamic: bool
    use_offset_pressure: bool
    use_original_normal: bool
    use_original_plane: bool
    use_paint_antialiasing: bool
    use_paint_grease_pencil: bool
    use_paint_image: bool
    use_paint_sculpt: bool
    use_paint_sculpt_curves: bool
    use_paint_uv_sculpt: bool
    use_paint_vertex: bool
    use_paint_weight: bool
    use_persistent: bool
    use_plane_trim: bool
    use_pose_ik_anchored: bool
    use_pose_lock_rotation: bool
    use_pressure_area_radius: bool
    use_pressure_jitter: bool
    use_pressure_masking: Literal['NONE', 'RAMP', 'CUTOFF']
    use_pressure_size: bool
    use_pressure_spacing: bool
    use_pressure_strength: bool
    use_primary_overlay: bool
    use_primary_overlay_override: bool
    use_restore_mesh: bool
    use_scene_spacing: Literal['VIEW', 'SCENE']
    use_secondary_overlay: bool
    use_secondary_overlay_override: bool
    use_smooth_stroke: bool
    use_space: bool
    use_space_attenuation: bool
    use_vertex_grease_pencil: bool
    use_wet_mix_pressure: bool
    use_wet_persistence_pressure: bool
    uv_sculpt_tool: BrushUvSculptTool
    vertex_tool: BrushVertexTool
    weight: float
    weight_tool: BrushWeightTool
    wet_mix: float
    wet_paint_radius_factor: float
    wet_persistence: float

    @property
    def automasking_cavity_curve(self) -> c.CurveMapping: pass

    @property
    def brush_capabilities(self) -> 'BrushCapabilities': pass

    @property
    def image_paint_capabilities(self) -> 'BrushCapabilitiesImagePaint': pass

    @property
    def curve(self) -> c.CurveMapping: pass

    @property
    def curves_sculpt_settings(self) -> 'BrushCurvesSculptSettings': pass

    @property
    def gpencil_settings(self) -> 'BrushGpencilSettings': pass

    @property
    def gradient(self) -> c.ColorRamp: pass

    @property
    def mask_texture_slot(self) -> 'BrushTextureSlot': pass

    @property
    def sculpt_capabilities(self) -> 'BrushCapabilitiesSculpt': pass

    @property
    def texture_slot(self) -> 'BrushTextureSlot': pass

    @property
    def vertex_paint_capabilities(self) -> 'BrushCapabilitiesVertexPaint': pass

    @property
    def weight_paint_capabilities(self) -> 'BrushCapabilitiesWeightPaint': pass


# noinspection PyPropertyDefinition
class BrushCapabilities(bpy_struct):
    @property
    def has_overlay(self) -> bool: pass

    @property
    def has_random_texture_angle(self) -> bool: pass

    @property
    def has_smooth_stroke(self) -> bool: pass

    @property
    def has_spacing(self) -> bool: pass


# noinspection PyPropertyDefinition
class BrushCapabilitiesImagePaint(bpy_struct):
    @property
    def has_accumulate(self) -> bool: pass

    @property
    def has_color(self) -> bool: pass

    @property
    def has_radius(self) -> bool: pass

    @property
    def has_space_attenuation(self) -> bool: pass


# noinspection PyPropertyDefinition
class BrushCapabilitiesSculpt(bpy_struct):
    @property
    def has_accumulate(self) -> bool: pass

    @property
    def has_auto_smooth(self) -> bool: pass

    @property
    def has_color(self) -> bool: pass

    @property
    def has_direction(self) -> bool: pass

    @property
    def has_gravity(self) -> bool: pass

    @property
    def has_height(self) -> bool: pass

    @property
    def has_jitter(self) -> bool: pass

    @property
    def has_normal_weight(self) -> bool: pass

    @property
    def has_persistence(self) -> bool: pass

    @property
    def has_pinch_factor(self) -> bool: pass

    @property
    def has_plane_offset(self) -> bool: pass

    @property
    def has_rake_factor(self) -> bool: pass

    @property
    def has_random_texture_angle(self) -> bool: pass

    @property
    def has_sculpt_plane(self) -> bool: pass

    @property
    def has_secondary_color(self) -> bool: pass

    @property
    def has_smooth_stroke(self) -> bool: pass

    @property
    def has_space_attenuation(self) -> bool: pass

    @property
    def has_strength_pressure(self) -> bool: pass

    @property
    def has_tilt(self) -> bool: pass

    @property
    def has_topology_rake(self) -> bool: pass


# noinspection PyPropertyDefinition
class BrushCapabilitiesVertexPaint(bpy_struct):
    @property
    def has_color(self) -> bool: pass


# noinspection PyPropertyDefinition
class BrushCapabilitiesWeightPaint(bpy_struct):
    @property
    def has_weight(self) -> bool: pass


# noinspection PyPropertyDefinition
class BrushCurvesSculptSettings(bpy_struct):
    add_amount: int
    curve_length: float
    density_add_attempts: int
    density_mode: Literal['AUTO', 'ADD', 'REMOVE']
    interpolate_length: bool
    interpolate_point_count: bool
    interpolate_shape: bool
    minimum_distance: float
    minimum_length: float
    points_per_curve: int
    scale_uniform: bool

    @property
    def curve_parameter_falloff(self) -> c.CurveMapping: pass


# noinspection PyPropertyDefinition
class BrushGpencilSettings(bpy_struct):
    active_smooth_factor: float
    angle: float
    angle_factor: float
    aspect: mathutils.Vector
    brush_draw_mode: Literal['ACTIVE', 'MATERIAL', 'VERTEXCOLOR']
    caps_type: Literal['ROUND', 'FLAT']
    dilate: int
    eraser_mode: Literal['SOFT', 'HARD', 'STROKE']
    eraser_strength_factor: float
    eraser_thickness_factor: float
    extend_stroke_factor: float
    fill_direction: Literal['NORMAL', 'INVERT']
    fill_draw_mode: Literal['BOTH', 'STROKE', 'CONTROL']
    fill_extend_mode: Literal['EXTEND', 'RADIUS']
    fill_factor: float
    fill_layer_mode: Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', 'ALL_ABOVE', 'ALL_BELOW']
    fill_simplify_level: int
    fill_threshold: float
    gpencil_paint_icon: Literal[
        'PENCIL',
        'PEN',
        'INK',
        'INKNOISE',
        'BLOCK',
        'MARKER',
        'AIRBRUSH',
        'CHISEL',
        'FILL',
        'SOFT',
        'HARD',
        'STROKE'
    ]
    gpencil_sculpt_icon: Literal[
        'SMOOTH',
        'THICKNESS',
        'STRENGTH',
        'RANDOMIZE',
        'GRAB',
        'PUSH',
        'TWIST',
        'PINCH',
        'CLONE'
    ]
    gpencil_vertex_icon: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR', 'REPLACE']
    gpencil_weight_icon: Literal['DRAW', 'BLUR', 'AVERAGE', 'SMEAR']
    hardness: float
    input_samples: int
    material: m.Material
    material_alt: m.Material
    outline_thickness_factor: float
    pen_jitter: float
    pen_smooth_factor: float
    pen_smooth_steps: int
    pen_strength: float
    pen_subdivision_steps: int
    pin_draw_mode: bool
    random_hue_factor: float
    random_pressure: float
    random_saturation_factor: float
    random_strength: float
    random_value_factor: float
    show_fill: bool
    show_fill_boundary: bool
    show_fill_extend: bool
    show_lasso: bool
    simplify_factor: float
    use_active_layer_only: bool
    use_collide_strokes: bool
    use_default_eraser: bool
    use_edit_position: bool
    use_edit_strength: bool
    use_edit_thickness: bool
    use_edit_uv: bool
    use_fill_limit: bool
    use_jitter_pressure: bool
    use_keep_caps_eraser: bool
    use_material_pin: bool
    use_occlude_eraser: bool
    use_pressure: bool
    use_random_press_hue: bool
    use_random_press_radius: bool
    use_random_press_sat: bool
    use_random_press_strength: bool
    use_random_press_uv: bool
    use_random_press_val: bool
    use_settings_outline: bool
    use_settings_postprocess: bool
    use_settings_random: bool
    use_settings_stabilizer: bool
    use_strength_pressure: bool
    use_stroke_random_hue: bool
    use_stroke_random_radius: bool
    use_stroke_random_sat: bool
    use_stroke_random_strength: bool
    use_stroke_random_uv: bool
    use_stroke_random_val: bool
    use_trim: bool
    uv_random: float
    vertex_color_factor: float
    vertex_mode: Literal['STROKE', 'FILL', 'BOTH']

    @property
    def curve_jitter(self) -> c.CurveMapping: pass

    @property
    def curve_random_hue(self) -> c.CurveMapping: pass

    @property
    def curve_random_pressure(self) -> c.CurveMapping: pass

    @property
    def curve_random_saturation(self) -> c.CurveMapping: pass

    @property
    def curve_random_strength(self) -> c.CurveMapping: pass

    @property
    def curve_random_uv(self) -> c.CurveMapping: pass

    @property
    def curve_random_value(self) -> c.CurveMapping: pass

    @property
    def curve_sensitivity(self) -> c.CurveMapping: pass

    @property
    def curve_strength(self) -> c.CurveMapping: pass


# noinspection PyPropertyDefinition
class BrushTextureSlot(t.TextureSlot):
    angle: float
    map_mode: Literal['VIEW_PLANE', 'AREA_PLANE', 'TILED', '3D', 'RANDOM', 'STENCIL']
    mask_map_mode: Literal['VIEW_PLANE', 'TILED', 'RANDOM', 'STENCIL']
    random_angle: float
    use_rake: bool
    use_random: bool

    @property
    def has_random_texture_angle(self) -> bool: pass

    @property
    def has_texture_angle(self) -> bool: pass

    @property
    def has_texture_angle_source(self) -> bool: pass


class BuildGpencilModifier(g.GpencilModifier):
    concurrent_time_alignment: Literal['START', 'END']
    fade_factor: float
    fade_opacity_strength: float
    fade_thickness_strength: float
    frame_end: float
    frame_start: float
    invert_layer_pass: bool
    invert_layers: bool
    layer: str
    layer_pass: int
    length: float
    mode: Literal['SEQUENTIAL', 'CONCURRENT', 'ADDITIVE']
    object: o.Object
    percentage_factor: float
    speed_factor: float
    speed_maxgap: float
    start_delay: float
    target_vertex_group: str
    time_mode: Literal['DRAWSPEED', 'FRAMES', 'PERCENTAGE']
    transition: Literal['GROW', 'SHRINK', 'FADE']
    use_fading: bool
    use_percentage: bool
    use_restrict_frame_range: bool


class BuildModifier(m.Modifier):
    frame_duration: float
    frame_start: float
    seed: int
    use_random_order: bool
    use_reverse: bool


class ByteColorAttribute(a.Attribute):
    data: bpy_prop_collection['ByteColorAttributeValue']


class ByteColorAttributeValue(bpy_struct):
    color: tuple[float, float, float, float]
    color_srgb: tuple[float, float, float, float]


class ByteIntAttribute(a.Attribute):
    data: bpy_prop_collection['ByteIntAttributeValue']


class ByteIntAttributeValue(bpy_struct):
    value: int
