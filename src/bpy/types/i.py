from typing import Any, Literal, Protocol

from base import bpy_struct, bpy_prop_collection, bpy_raw_collection

from a import AnimData, AssetMetaData
from d import Depsgraph
from l import Library, LibraryWeakReference
from s import Scene
from v import ViewLayer

Icon = Literal[
    'NONE',
    'QUESTION',
    'ERROR',
    'CANCEL',
    'TRIA_RIGHT',
    'TRIA_DOWN',
    'TRIA_LEFT',
    'TRIA_UP',
    'ARROW_LEFTRIGHT',
    'PLUS',
    'DISCLOSURE_TRI_RIGHT',
    'DISCLOSURE_TRI_DOWN',
    'RADIOBUT_OFF',
    'RADIOBUT_ON',
    'MENU_PANEL',
    'BLENDER',
    'GRIP',
    'DOT',
    'COLLAPSEMENU',
    'X',
    'DUPLICATE',
    'TRASH',
    'COLLECTION_NEW',
    'OPTIONS',
    'NODE',
    'NODE_SEL',
    'WINDOW',
    'WORKSPACE',
    'RIGHTARROW_THIN',
    'BORDERMOVE',
    'VIEWZOOM',
    'ADD',
    'REMOVE',
    'PANEL_CLOSE',
    'COPY_ID',
    'EYEDROPPER',
    'CHECKMARK',
    'AUTO',
    'CHECKBOX_DEHLT',
    'CHECKBOX_HLT',
    'UNLOCKED',
    'LOCKED',
    'UNPINNED',
    'PINNED',
    'SCREEN_BACK',
    'RIGHTARROW',
    'DOWNARROW_HLT',
    'FCURVE_SNAPSHOT',
    'OBJECT_HIDDEN',
    'TOPBAR',
    'STATUSBAR',
    'PLUGIN',
    'HELP',
    'GHOST_ENABLED',
    'COLOR',
    'UNLINKED',
    'LINKED',
    'HAND',
    'ZOOM_ALL',
    'ZOOM_SELECTED',
    'ZOOM_PREVIOUS',
    'ZOOM_IN',
    'ZOOM_OUT',
    'DRIVER_DISTANCE',
    'DRIVER_ROTATIONAL_DIFFERENCE',
    'DRIVER_TRANSFORM',
    'FREEZE',
    'STYLUS_PRESSURE',
    'GHOST_DISABLED',
    'FILE_NEW',
    'FILE_TICK',
    'QUIT',
    'URL',
    'RECOVER_LAST',
    'THREE_DOTS',
    'FULLSCREEN_ENTER',
    'FULLSCREEN_EXIT',
    'BRUSHES_ALL',
    'LIGHT',
    'MATERIAL',
    'TEXTURE',
    'ANIM',
    'WORLD',
    'SCENE',
    'OUTPUT',
    'SCRIPT',
    'PARTICLES',
    'PHYSICS',
    'SPEAKER',
    'TOOL_SETTINGS',
    'SHADERFX',
    'MODIFIER',
    'RECORD_OFF',
    'RECORD_ON',
    'BLANK1',
    'FAKE_USER_OFF',
    'FAKE_USER_ON',
    'VIEW3D',
    'GRAPH',
    'OUTLINER',
    'PROPERTIES',
    'FILEBROWSER',
    'IMAGE',
    'INFO',
    'SEQUENCE',
    'TEXT',
    'SPREADSHEET',
    'SOUND',
    'ACTION',
    'NLA',
    'PREFERENCES',
    'TIME',
    'NODETREE',
    'GEOMETRY_NODES',
    'CONSOLE',
    'TRACKER',
    'ASSET_MANAGER',
    'NODE_COMPOSITING',
    'NODE_TEXTURE',
    'NODE_MATERIAL',
    'UV',
    'OBJECT_DATAMODE',
    'EDITMODE_HLT',
    'UV_DATA',
    'VPAINT_HLT',
    'TPAINT_HLT',
    'WPAINT_HLT',
    'SCULPTMODE_HLT',
    'POSE_HLT',
    'PARTICLEMODE',
    'TRACKING',
    'TRACKING_BACKWARDS',
    'TRACKING_FORWARDS',
    'TRACKING_BACKWARDS_SINGLE',
    'TRACKING_FORWARDS_SINGLE',
    'TRACKING_CLEAR_BACKWARDS',
    'TRACKING_CLEAR_FORWARDS',
    'TRACKING_REFINE_BACKWARDS',
    'TRACKING_REFINE_FORWARDS',
    'SCENE_DATA',
    'RENDERLAYERS',
    'WORLD_DATA',
    'OBJECT_DATA',
    'MESH_DATA',
    'CURVE_DATA',
    'META_DATA',
    'LATTICE_DATA',
    'LIGHT_DATA',
    'MATERIAL_DATA',
    'TEXTURE_DATA',
    'ANIM_DATA',
    'CAMERA_DATA',
    'PARTICLE_DATA',
    'LIBRARY_DATA_DIRECT',
    'GROUP',
    'ARMATURE_DATA',
    'COMMUNITY',
    'BONE_DATA',
    'CONSTRAINT',
    'SHAPEKEY_DATA',
    'CONSTRAINT_BONE',
    'CAMERA_STEREO',
    'PACKAGE',
    'UGLYPACKAGE',
    'EXPERIMENTAL',
    'BRUSH_DATA',
    'IMAGE_DATA',
    'FILE',
    'FCURVE',
    'FONT_DATA',
    'RENDER_RESULT',
    'SURFACE_DATA',
    'EMPTY_DATA',
    'PRESET',
    'RENDER_ANIMATION',
    'RENDER_STILL',
    'LIBRARY_DATA_BROKEN',
    'BOIDS',
    'STRANDS',
    'GREASEPENCIL',
    'LINE_DATA',
    'LIBRARY_DATA_OVERRIDE',
    'GROUP_BONE',
    'GROUP_VERTEX',
    'GROUP_VCOL',
    'GROUP_UVS',
    'FACE_MAPS',
    'RNA',
    'RNA_ADD',
    'MOUSE_LMB',
    'MOUSE_MMB',
    'MOUSE_RMB',
    'MOUSE_MOVE',
    'MOUSE_LMB_DRAG',
    'MOUSE_MMB_DRAG',
    'MOUSE_RMB_DRAG',
    'MEMORY',
    'PRESET_NEW',
    'DECORATE',
    'DECORATE_KEYFRAME',
    'DECORATE_ANIMATE',
    'DECORATE_DRIVER',
    'DECORATE_LINKED',
    'DECORATE_LIBRARY_OVERRIDE',
    'DECORATE_UNLOCKED',
    'DECORATE_LOCKED',
    'DECORATE_OVERRIDE',
    'FUND',
    'TRACKER_DATA',
    'HEART',
    'ORPHAN_DATA',
    'USER',
    'SYSTEM',
    'SETTINGS',
    'OUTLINER_OB_EMPTY',
    'OUTLINER_OB_MESH',
    'OUTLINER_OB_CURVE',
    'OUTLINER_OB_LATTICE',
    'OUTLINER_OB_META',
    'OUTLINER_OB_LIGHT',
    'OUTLINER_OB_CAMERA',
    'OUTLINER_OB_ARMATURE',
    'OUTLINER_OB_FONT',
    'OUTLINER_OB_SURFACE',
    'OUTLINER_OB_SPEAKER',
    'OUTLINER_OB_FORCE_FIELD',
    'OUTLINER_OB_GROUP_INSTANCE',
    'OUTLINER_OB_GREASEPENCIL',
    'OUTLINER_OB_LIGHTPROBE',
    'OUTLINER_OB_IMAGE',
    'OUTLINER_COLLECTION',
    'RESTRICT_COLOR_OFF',
    'RESTRICT_COLOR_ON',
    'HIDE_ON',
    'HIDE_OFF',
    'RESTRICT_SELECT_ON',
    'RESTRICT_SELECT_OFF',
    'RESTRICT_RENDER_ON',
    'RESTRICT_RENDER_OFF',
    'RESTRICT_INSTANCED_OFF',
    'OUTLINER_DATA_EMPTY',
    'OUTLINER_DATA_MESH',
    'OUTLINER_DATA_CURVE',
    'OUTLINER_DATA_LATTICE',
    'OUTLINER_DATA_META',
    'OUTLINER_DATA_LIGHT',
    'OUTLINER_DATA_CAMERA',
    'OUTLINER_DATA_ARMATURE',
    'OUTLINER_DATA_FONT',
    'OUTLINER_DATA_SURFACE',
    'OUTLINER_DATA_SPEAKER',
    'OUTLINER_DATA_LIGHTPROBE',
    'OUTLINER_DATA_GP_LAYER',
    'OUTLINER_DATA_GREASEPENCIL',
    'GP_SELECT_POINTS',
    'GP_SELECT_STROKES',
    'GP_MULTIFRAME_EDITING',
    'GP_ONLY_SELECTED',
    'GP_SELECT_BETWEEN_STROKES',
    'MODIFIER_OFF',
    'MODIFIER_ON',
    'ONIONSKIN_OFF',
    'ONIONSKIN_ON',
    'RESTRICT_VIEW_ON',
    'RESTRICT_VIEW_OFF',
    'RESTRICT_INSTANCED_ON',
    'MESH_PLANE',
    'MESH_CUBE',
    'MESH_CIRCLE',
    'MESH_UVSPHERE',
    'MESH_ICOSPHERE',
    'MESH_GRID',
    'MESH_MONKEY',
    'MESH_CYLINDER',
    'MESH_TORUS',
    'MESH_CONE',
    'MESH_CAPSULE',
    'EMPTY_SINGLE_ARROW',
    'LIGHT_POINT',
    'LIGHT_SUN',
    'LIGHT_SPOT',
    'LIGHT_HEMI',
    'LIGHT_AREA',
    'CUBE',
    'SPHERE',
    'CONE',
    'META_PLANE',
    'META_CUBE',
    'META_BALL',
    'META_ELLIPSOID',
    'META_CAPSULE',
    'SURFACE_NCURVE',
    'SURFACE_NCIRCLE',
    'SURFACE_NSURFACE',
    'SURFACE_NCYLINDER',
    'SURFACE_NSPHERE',
    'SURFACE_NTORUS',
    'EMPTY_AXIS',
    'STROKE',
    'EMPTY_ARROWS',
    'CURVE_BEZCURVE',
    'CURVE_BEZCIRCLE',
    'CURVE_NCURVE',
    'CURVE_NCIRCLE',
    'CURVE_PATH',
    'LIGHTPROBE_SPHERE',
    'LIGHTPROBE_PLANE',
    'LIGHTPROBE_VOLUME',
    'COLOR_RED',
    'COLOR_GREEN',
    'COLOR_BLUE',
    'TRIA_RIGHT_BAR',
    'TRIA_DOWN_BAR',
    'TRIA_LEFT_BAR',
    'TRIA_UP_BAR',
    'FORCE_FORCE',
    'FORCE_WIND',
    'FORCE_VORTEX',
    'FORCE_MAGNETIC',
    'FORCE_HARMONIC',
    'FORCE_CHARGE',
    'FORCE_LENNARDJONES',
    'FORCE_TEXTURE',
    'FORCE_CURVE',
    'FORCE_BOID',
    'FORCE_TURBULENCE',
    'FORCE_DRAG',
    'FORCE_FLUIDFLOW',
    'RIGID_BODY',
    'RIGID_BODY_CONSTRAINT',
    'AREA_JOIN',
    'AREA_SWAP',
    'SPLIT_HORIZONTAL',
    'SPLIT_VERTICAL',
    'IMAGE_PLANE',
    'IMAGE_BACKGROUND',
    'IMAGE_REFERENCE',
    'NODE_INSERT_ON',
    'NODE_INSERT_OFF',
    'NODE_TOP',
    'NODE_SIDE',
    'NODE_CORNER',
    'ANCHOR_TOP',
    'ANCHOR_BOTTOM',
    'ANCHOR_LEFT',
    'ANCHOR_RIGHT',
    'ANCHOR_CENTER',
    'SELECT_SET',
    'SELECT_EXTEND',
    'SELECT_SUBTRACT',
    'SELECT_INTERSECT',
    'SELECT_DIFFERENCE',
    'ALIGN_LEFT',
    'ALIGN_CENTER',
    'ALIGN_RIGHT',
    'ALIGN_JUSTIFY',
    'ALIGN_FLUSH',
    'ALIGN_TOP',
    'ALIGN_MIDDLE',
    'ALIGN_BOTTOM',
    'BOLD',
    'ITALIC',
    'UNDERLINE',
    'SMALL_CAPS',
    'CON_ACTION',
    'MOD_ENVELOPE',
    'MOD_OUTLINE',
    'MOD_LENGTH',
    'MOD_DASH',
    'MOD_LINEART',
    'HOLDOUT_OFF',
    'HOLDOUT_ON',
    'INDIRECT_ONLY_OFF',
    'INDIRECT_ONLY_ON',
    'CON_CAMERASOLVER',
    'CON_FOLLOWTRACK',
    'CON_OBJECTSOLVER',
    'CON_LOCLIKE',
    'CON_ROTLIKE',
    'CON_SIZELIKE',
    'CON_TRANSLIKE',
    'CON_DISTLIMIT',
    'CON_LOCLIMIT',
    'CON_ROTLIMIT',
    'CON_SIZELIMIT',
    'CON_SAMEVOL',
    'CON_TRANSFORM',
    'CON_TRANSFORM_CACHE',
    'CON_CLAMPTO',
    'CON_KINEMATIC',
    'CON_LOCKTRACK',
    'CON_SPLINEIK',
    'CON_STRETCHTO',
    'CON_TRACKTO',
    'CON_ARMATURE',
    'CON_CHILDOF',
    'CON_FLOOR',
    'CON_FOLLOWPATH',
    'CON_PIVOT',
    'CON_SHRINKWRAP',
    'MODIFIER_DATA',
    'MOD_WAVE',
    'MOD_BUILD',
    'MOD_DECIM',
    'MOD_MIRROR',
    'MOD_SOFT',
    'MOD_SUBSURF',
    'HOOK',
    'MOD_PHYSICS',
    'MOD_PARTICLES',
    'MOD_BOOLEAN',
    'MOD_EDGESPLIT',
    'MOD_ARRAY',
    'MOD_UVPROJECT',
    'MOD_DISPLACE',
    'MOD_CURVE',
    'MOD_LATTICE',
    'MOD_TINT',
    'MOD_ARMATURE',
    'MOD_SHRINKWRAP',
    'MOD_CAST',
    'MOD_MESHDEFORM',
    'MOD_BEVEL',
    'MOD_SMOOTH',
    'MOD_SIMPLEDEFORM',
    'MOD_MASK',
    'MOD_CLOTH',
    'MOD_EXPLODE',
    'MOD_FLUIDSIM',
    'MOD_MULTIRES',
    'MOD_FLUID',
    'MOD_SOLIDIFY',
    'MOD_SCREW',
    'MOD_VERTEX_WEIGHT',
    'MOD_DYNAMICPAINT',
    'MOD_REMESH',
    'MOD_OCEAN',
    'MOD_WARP',
    'MOD_SKIN',
    'MOD_TRIANGULATE',
    'MOD_WIREFRAME',
    'MOD_DATA_TRANSFER',
    'MOD_NORMALEDIT',
    'MOD_PARTICLE_INSTANCE',
    'MOD_HUE_SATURATION',
    'MOD_NOISE',
    'MOD_OFFSET',
    'MOD_SIMPLIFY',
    'MOD_THICKNESS',
    'MOD_INSTANCE',
    'MOD_TIME',
    'MOD_OPACITY',
    'REC',
    'PLAY',
    'FF',
    'REW',
    'PAUSE',
    'PREV_KEYFRAME',
    'NEXT_KEYFRAME',
    'PLAY_SOUND',
    'PLAY_REVERSE',
    'PREVIEW_RANGE',
    'ACTION_TWEAK',
    'PMARKER_ACT',
    'PMARKER_SEL',
    'PMARKER',
    'MARKER_HLT',
    'MARKER',
    'KEYFRAME_HLT',
    'KEYFRAME',
    'KEYINGSET',
    'KEY_DEHLT',
    'KEY_HLT',
    'MUTE_IPO_OFF',
    'MUTE_IPO_ON',
    'DRIVER',
    'SOLO_OFF',
    'SOLO_ON',
    'FRAME_PREV',
    'FRAME_NEXT',
    'NLA_PUSHDOWN',
    'IPO_CONSTANT',
    'IPO_LINEAR',
    'IPO_BEZIER',
    'IPO_SINE',
    'IPO_QUAD',
    'IPO_CUBIC',
    'IPO_QUART',
    'IPO_QUINT',
    'IPO_EXPO',
    'IPO_CIRC',
    'IPO_BOUNCE',
    'IPO_ELASTIC',
    'IPO_BACK',
    'IPO_EASE_IN',
    'IPO_EASE_OUT',
    'IPO_EASE_IN_OUT',
    'NORMALIZE_FCURVES',
    'ORIENTATION_PARENT',
    'FACE_CORNER',
    'VERTEXSEL',
    'EDGESEL',
    'FACESEL',
    'CURSOR',
    'PIVOT_BOUNDBOX',
    'PIVOT_CURSOR',
    'PIVOT_INDIVIDUAL',
    'PIVOT_MEDIAN',
    'PIVOT_ACTIVE',
    'CENTER_ONLY',
    'ROOTCURVE',
    'SMOOTHCURVE',
    'SPHERECURVE',
    'INVERSESQUARECURVE',
    'SHARPCURVE',
    'LINCURVE',
    'NOCURVE',
    'RNDCURVE',
    'PROP_OFF',
    'PROP_ON',
    'PROP_CON',
    'PROP_PROJECTED',
    'PARTICLE_POINT',
    'PARTICLE_TIP',
    'PARTICLE_PATH',
    'SNAP_FACE_NEAREST',
    'SNAP_FACE_CENTER',
    'SNAP_PERPENDICULAR',
    'SNAP_MIDPOINT',
    'SNAP_OFF',
    'SNAP_ON',
    'SNAP_NORMAL',
    'SNAP_GRID',
    'SNAP_VERTEX',
    'SNAP_EDGE',
    'SNAP_FACE',
    'SNAP_VOLUME',
    'SNAP_INCREMENT',
    'STICKY_UVS_LOC',
    'STICKY_UVS_DISABLE',
    'STICKY_UVS_VERT',
    'CLIPUV_DEHLT',
    'CLIPUV_HLT',
    'SNAP_PEEL_OBJECT',
    'GRID',
    'OBJECT_ORIGIN',
    'ORIENTATION_GLOBAL',
    'ORIENTATION_GIMBAL',
    'ORIENTATION_LOCAL',
    'ORIENTATION_NORMAL',
    'ORIENTATION_VIEW',
    'COPYDOWN',
    'PASTEDOWN',
    'PASTEFLIPUP',
    'PASTEFLIPDOWN',
    'VIS_SEL_11',
    'VIS_SEL_10',
    'VIS_SEL_01',
    'VIS_SEL_00',
    'AUTOMERGE_OFF',
    'AUTOMERGE_ON',
    'UV_VERTEXSEL',
    'UV_EDGESEL',
    'UV_FACESEL',
    'UV_ISLANDSEL',
    'UV_SYNC_SELECT',
    'GP_CAPS_FLAT',
    'GP_CAPS_ROUND',
    'FIXED_SIZE',
    'TRANSFORM_ORIGINS',
    'GIZMO',
    'ORIENTATION_CURSOR',
    'NORMALS_VERTEX',
    'NORMALS_FACE',
    'NORMALS_VERTEX_FACE',
    'SHADING_BBOX',
    'SHADING_WIRE',
    'SHADING_SOLID',
    'SHADING_RENDERED',
    'SHADING_TEXTURE',
    'OVERLAY',
    'XRAY',
    'LOCKVIEW_OFF',
    'LOCKVIEW_ON',
    'AXIS_SIDE',
    'AXIS_FRONT',
    'AXIS_TOP',
    'LAYER_USED',
    'LAYER_ACTIVE',
    'OUTLINER_OB_CURVES',
    'OUTLINER_DATA_CURVES',
    'CURVES_DATA',
    'OUTLINER_OB_POINTCLOUD',
    'OUTLINER_DATA_POINTCLOUD',
    'POINTCLOUD_DATA',
    'OUTLINER_OB_VOLUME',
    'OUTLINER_DATA_VOLUME',
    'VOLUME_DATA',
    'POINTCLOUD_POINT',
    'CURRENT_FILE',
    'HOME',
    'DOCUMENTS',
    'TEMP',
    'SORTALPHA',
    'SORTBYEXT',
    'SORTTIME',
    'SORTSIZE',
    'SHORTDISPLAY',
    'LONGDISPLAY',
    'IMGDISPLAY',
    'BOOKMARKS',
    'FONTPREVIEW',
    'FILTER',
    'NEWFOLDER',
    'FOLDER_REDIRECT',
    'FILE_PARENT',
    'FILE_REFRESH',
    'FILE_FOLDER',
    'FILE_BLANK',
    'FILE_BLEND',
    'FILE_IMAGE',
    'FILE_MOVIE',
    'FILE_SCRIPT',
    'FILE_SOUND',
    'FILE_FONT',
    'FILE_TEXT',
    'SORT_DESC',
    'SORT_ASC',
    'LINK_BLEND',
    'APPEND_BLEND',
    'IMPORT',
    'EXPORT',
    'LOOP_BACK',
    'LOOP_FORWARDS',
    'BACK',
    'FORWARD',
    'FILE_ARCHIVE',
    'FILE_CACHE',
    'FILE_VOLUME',
    'FILE_3D',
    'FILE_HIDDEN',
    'FILE_BACKUP',
    'DISK_DRIVE',
    'MATPLANE',
    'MATSPHERE',
    'MATCUBE',
    'MONKEY',
    'CURVES',
    'ALIASED',
    'ANTIALIASED',
    'MAT_SPHERE_SKY',
    'MATSHADERBALL',
    'MATCLOTH',
    'MATFLUID',
    'WORDWRAP_OFF',
    'WORDWRAP_ON',
    'SYNTAX_OFF',
    'SYNTAX_ON',
    'LINENUMBERS_OFF',
    'LINENUMBERS_ON',
    'SCRIPTPLUGINS',
    'DISC',
    'DESKTOP',
    'EXTERNAL_DRIVE',
    'NETWORK_DRIVE',
    'SEQ_SEQUENCER',
    'SEQ_PREVIEW',
    'SEQ_LUMA_WAVEFORM',
    'SEQ_CHROMA_SCOPE',
    'SEQ_HISTOGRAM',
    'SEQ_SPLITVIEW',
    'SEQ_STRIP_META',
    'SEQ_STRIP_DUPLICATE',
    'IMAGE_RGB',
    'IMAGE_RGB_ALPHA',
    'IMAGE_ALPHA',
    'IMAGE_ZDEPTH',
    'HANDLE_AUTOCLAMPED',
    'HANDLE_AUTO',
    'HANDLE_ALIGNED',
    'HANDLE_VECTOR',
    'HANDLE_FREE',
    'VIEW_CAMERA_UNSELECTED',
    'VIEW_UNLOCKED',
    'VIEW_LOCKED',
    'VIEW_PERSPECTIVE',
    'VIEW_ORTHO',
    'VIEW_CAMERA',
    'VIEW_PAN',
    'VIEW_ZOOM',
    'BRUSH_BLOB',
    'BRUSH_BLUR',
    'BRUSH_CLAY',
    'BRUSH_CLAY_STRIPS',
    'BRUSH_CLONE',
    'BRUSH_CREASE',
    'BRUSH_FILL',
    'BRUSH_FLATTEN',
    'BRUSH_GRAB',
    'BRUSH_INFLATE',
    'BRUSH_LAYER',
    'BRUSH_MASK',
    'BRUSH_MIX',
    'BRUSH_NUDGE',
    'BRUSH_PAINT_SELECT',
    'BRUSH_PINCH',
    'BRUSH_SCRAPE',
    'BRUSH_SCULPT_DRAW',
    'BRUSH_SMEAR',
    'BRUSH_SMOOTH',
    'BRUSH_SNAKE_HOOK',
    'BRUSH_SOFTEN',
    'BRUSH_TEXDRAW',
    'BRUSH_TEXFILL',
    'BRUSH_TEXMASK',
    'BRUSH_THUMB',
    'BRUSH_ROTATE',
    'GPBRUSH_SMOOTH',
    'GPBRUSH_THICKNESS',
    'GPBRUSH_STRENGTH',
    'GPBRUSH_GRAB',
    'GPBRUSH_PUSH',
    'GPBRUSH_TWIST',
    'GPBRUSH_PINCH',
    'GPBRUSH_RANDOMIZE',
    'GPBRUSH_CLONE',
    'GPBRUSH_WEIGHT',
    'GPBRUSH_PENCIL',
    'GPBRUSH_PEN',
    'GPBRUSH_INK',
    'GPBRUSH_INKNOISE',
    'GPBRUSH_BLOCK',
    'GPBRUSH_MARKER',
    'GPBRUSH_FILL',
    'GPBRUSH_AIRBRUSH',
    'GPBRUSH_CHISEL',
    'GPBRUSH_ERASE_SOFT',
    'GPBRUSH_ERASE_HARD',
    'GPBRUSH_ERASE_STROKE',
    'BRUSH_CURVES_ADD',
    'BRUSH_CURVES_COMB',
    'BRUSH_CURVES_CUT',
    'BRUSH_CURVES_DELETE',
    'BRUSH_CURVES_DENSITY',
    'BRUSH_CURVES_GROW_SHRINK',
    'BRUSH_CURVES_PINCH',
    'BRUSH_CURVES_PUFF',
    'BRUSH_CURVES_SLIDE',
    'BRUSH_CURVES_SMOOTH',
    'BRUSH_CURVES_SNAKE_HOOK',
    'KEYTYPE_KEYFRAME_VEC',
    'KEYTYPE_BREAKDOWN_VEC',
    'KEYTYPE_EXTREME_VEC',
    'KEYTYPE_JITTER_VEC',
    'KEYTYPE_MOVING_HOLD_VEC',
    'HANDLETYPE_FREE_VEC',
    'HANDLETYPE_ALIGNED_VEC',
    'HANDLETYPE_VECTOR_VEC',
    'HANDLETYPE_AUTO_VEC',
    'HANDLETYPE_AUTO_CLAMP_VEC',
    'COLORSET_01_VEC',
    'COLORSET_02_VEC',
    'COLORSET_03_VEC',
    'COLORSET_04_VEC',
    'COLORSET_05_VEC',
    'COLORSET_06_VEC',
    'COLORSET_07_VEC',
    'COLORSET_08_VEC',
    'COLORSET_09_VEC',
    'COLORSET_10_VEC',
    'COLORSET_11_VEC',
    'COLORSET_12_VEC',
    'COLORSET_13_VEC',
    'COLORSET_14_VEC',
    'COLORSET_15_VEC',
    'COLORSET_16_VEC',
    'COLORSET_17_VEC',
    'COLORSET_18_VEC',
    'COLORSET_19_VEC',
    'COLORSET_20_VEC',
    'COLLECTION_COLOR_01',
    'COLLECTION_COLOR_02',
    'COLLECTION_COLOR_03',
    'COLLECTION_COLOR_04',
    'COLLECTION_COLOR_05',
    'COLLECTION_COLOR_06',
    'COLLECTION_COLOR_07',
    'COLLECTION_COLOR_08',
    'SEQUENCE_COLOR_01',
    'SEQUENCE_COLOR_02',
    'SEQUENCE_COLOR_03',
    'SEQUENCE_COLOR_04',
    'SEQUENCE_COLOR_05',
    'SEQUENCE_COLOR_06',
    'SEQUENCE_COLOR_07',
    'SEQUENCE_COLOR_08',
    'SEQUENCE_COLOR_09',
    'LIBRARY_DATA_INDIRECT',
    'LIBRARY_DATA_OVERRIDE_NONEDITABLE',
    'EVENT_A',
    'EVENT_B',
    'EVENT_C',
    'EVENT_D',
    'EVENT_E',
    'EVENT_F',
    'EVENT_G',
    'EVENT_H',
    'EVENT_I',
    'EVENT_J',
    'EVENT_K',
    'EVENT_L',
    'EVENT_M',
    'EVENT_N',
    'EVENT_O',
    'EVENT_P',
    'EVENT_Q',
    'EVENT_R',
    'EVENT_S',
    'EVENT_T',
    'EVENT_U',
    'EVENT_V',
    'EVENT_W',
    'EVENT_X',
    'EVENT_Y',
    'EVENT_Z',
    'EVENT_SHIFT',
    'EVENT_CTRL',
    'EVENT_ALT',
    'EVENT_OS',
    'EVENT_F1',
    'EVENT_F2',
    'EVENT_F3',
    'EVENT_F4',
    'EVENT_F5',
    'EVENT_F6',
    'EVENT_F7',
    'EVENT_F8',
    'EVENT_F9',
    'EVENT_F10',
    'EVENT_F11',
    'EVENT_F12',
    'EVENT_ESC',
    'EVENT_TAB',
    'EVENT_PAGEUP',
    'EVENT_PAGEDOWN',
    'EVENT_RETURN',
    'EVENT_SPACEKEY',
]

IdType = Literal[
    'ACTION',
    'ARMATURE',
    'BRUSH',
    'CACHEFILE',
    'CAMERA',
    'COLLECTION',
    'CURVE',
    'CURVES',
    'FONT',
    'GREASEPENCIL',
    'GREASEPENCIL_V3',
    'IMAGE',
    'KEY',
    'LATTICE',
    'LIBRARY',
    'LIGHT',
    'LIGHT_PROBE',
    'LINESTYLE',
    'MASK',
    'MATERIAL',
    'MESH',
    'META',
    'MOVIECLIP',
    'NODETREE',
    'OBJECT',
    'PAINTCURVE',
    'PALETTE',
    'PARTICLE',
    'POINTCLOUD',
    'SCENE',
    'SCREEN',
    'SOUND',
    'SPEAKER',
    'TEXT',
    'TEXTURE',
    'VOLUME',
    'WINDOWMANAGER',
    'WORKSPACE',
    'WORLD',
]


# noinspection PyPropertyDefinition
class ID(bpy_struct):
    asset_data: AssetMetaData 
    is_runtime_data: bool
    name: str
    tag: bool
    use_extra_user: bool
    use_fake_user: bool

    @property
    def id_type(self) -> IdType: pass
        
    @property
    def is_embedded_data(self) -> bool: pass
        
    @property
    def is_evaluated(self) -> bool: pass
        
    @property
    def is_library_indirect(self) -> bool: pass
        
    @property
    def is_missing(self) -> bool: pass

    @property
    def library(self) -> Library: pass
        
    @property
    def library_weak_reference(self) -> LibraryWeakReference: pass

    @property
    def name_full(self) -> str: pass
        
    @property
    def original(self) -> 'ID': pass
        
    @property
    def override_library(self) -> 'IDOverrideLibrary': pass
        
    @property
    def preview(self) -> 'ImagePreview': pass
        
    @property
    def session_uid(self) -> int: pass

    @property
    def users(self) -> int: pass

    def evaluated_get(self, depsgraph: Depsgraph) -> 'ID': pass

    def copy(self) -> 'ID': pass

    def asset_mark(self): pass

    def asset_clear(self): pass

    def asset_generate_preview(self): pass

    def override_create(self, remap_local_usages: bool = False) -> 'ID': pass

    def override_hierarchy_create(
        self,
        scene: Scene,
        view_layer: ViewLayer,
        reference: 'ID | None' = None,
        do_fully_editable: bool = False,
    ) -> 'ID': pass

    def user_clear(self): pass

    def user_remap(self, new_id: 'ID'): pass

    def make_local(self, clear_proxy: bool = True, clear_liboverride: bool = False) -> 'ID': pass

    # noinspection PyShadowingBuiltins
    def user_of_id(self, id: 'ID') -> int: pass

    def animation_data_create(self) -> AnimData: pass

    def animation_data_clear(self): pass

    # noinspection PyDefaultArgument
    def update_tag(self, refresh: set[Literal['OBJECT', 'DATA', 'TIME']] = set()): pass

    def preview_ensure(self) -> 'ImagePreview': pass


class IDPropertyGroup(Protocol):
    def __getitem__(self, item: str) -> Any: pass
    def __setitem__(self, key: str, value: Any) -> None: pass
    def __delitem__(self, key: str) -> None: pass
    def clear(self) -> None: pass
    def get(self, key: str, default: Any | None = None) -> Any: pass
    def items(self) -> 'IDPropertyGroupViewItems': pass
    def keys(self) -> 'IDPropertyGroupViewKeys': pass
    def pop(self, key: str, default: Any | None = None) -> Any: pass
    def to_dict(self) -> dict[str, Any]: pass
    def update(self, other: 'IDPropertyGroup' | dict[str, Any]) -> None: pass
    def values(self) -> 'IDPropertyGroupViewValues': pass


class IDPropertyGroupViewItems(bpy_raw_collection[tuple[str, IDPropertyGroup]]):
    pass


class IDPropertyGroupViewKeys(bpy_raw_collection[str]):
    pass


class IDPropertyGroupViewValues(bpy_raw_collection[IDPropertyGroup]):
    pass


# noinspection PyPropertyDefinition
class ImagePreview(bpy_struct):  # NEW REGEX
    icon_pixels: int
    icon_pixels_float: float
    icon_size: tuple[int, int]
    image_pixels: int
    image_pixels_float: float
    image_size: tuple[int, int]
    is_icon_custom: bool
    is_image_custom: bool

    @property
    def icon_id(self) -> int: pass

    def reload(self) -> None: pass
