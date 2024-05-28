from typing import Any, Callable, Generator, Literal, Sequence
import bpy as bpy

PropertyFlag = Literal[
    'HIDDEN',
    'SKIP_SAVE',
    'SKIP_PRESET',
    'ANIMATABLE',
    'LIBRARY_EDITABLE',
    'PROPORTIONAL',
    'TEXTEDIT_UPDATE',
    'OUTPUT_PATH',
]

PropertyOverrideFlag = Literal['LIBRARY_OVERRIDABLE']

PropertySubtypeNumber = Literal[
    'PIXEL',
    'UNSIGNED',
    'PERCENTAGE',
    'FACTOR',
    'ANGLE',
    'TIME',
    'TIME_ABSOLUTE',
    'DISTANCE',
    'DISTANCE_CAMERA',
    'POWER',
    'TEMPERATURE',
    'NONE',
]

PropertySubtypeString = Literal[
    'FILE_PATH',
    'DIR_PATH',
    'FILE_NAME',
    'BYTE_STRING',
    'PASSWORD',
    'NONE',
]


# noinspection PyPep8Naming,PyDefaultArgument,PyUnusedLocal,PyShadowingBuiltins
def BoolProperty(
    name: str = '',
    description: str = '',
    translation_context: str = '*',
    default: bool = False,
    options: set[PropertyFlag] = set('ANIMATABLE'),
    override: set[PropertyOverrideFlag] = set(),
    tags: set[str] = set(),
    subtype: PropertySubtypeNumber = 'NONE',
    update: Callable[[Any, bpy.context], None] | None = None,
    get: Callable[[Any], bool] | None = None,
    set: Callable[[Any, bool], None] | None = None,
) -> type[bool]:
    pass


# noinspection PyUnusedLocal,PyDefaultArgument,PyShadowingBuiltins
def EnumProperty(
    items: Sequence[tuple[str, str, str, str, str]] | Sequence[tuple[str, str, str, str]] | Sequence[tuple[str, str, str]] | Callable[[Any, bpy.context | None], Sequence[tuple[str, str, str, str, str]] | Sequence[tuple[str, str, str, str]] | Sequence[tuple[str, str, str]]],
    name: str = '',
    description: str = '',
    translation_context: str = '*',
    default: str | int | set[str | int] = None,
    options: set[PropertyFlag] = set('ANIMATABLE'),
    override: set[PropertyOverrideFlag] = set(),
    tags: set[str] = set(),
    update: Callable[[Any, bpy.context], None] | None = None,
    get: Callable[[Any], str] | None = None,
    set: Callable[[Any, str], None] | None = None,
) -> type[str]:
    pass


# noinspection PyDefaultArgument,PyPep8Naming,PyUnusedLocal,PyShadowingBuiltins
def StringProperty(
    name: str = '',
    description: str = '',
    translation_context: str = '*',
    default: str = '',
    maxlen: int = 0,
    options: set[PropertyFlag] = set('ANIMATABLE'),
    override: set[PropertyOverrideFlag] = set(),
    tags: set[str] = set(),
    subtype: PropertySubtypeString = 'NONE',
    update: Callable[[Any, bpy.context], None] | None = None,
    get: Callable[[Any], str] | None = None,
    set: Callable[[Any, str], None] | None = None,
    search: Callable[
        [Any, bpy.context, str],
        Sequence[str | tuple[str, str]] | Generator[str | tuple[str, str], Any, Any]
    ] | None = None,
    search_options: set[Literal['SORT', 'SUGGESTION']] = set('SUGGESTION'),
) -> type[str]: pass
