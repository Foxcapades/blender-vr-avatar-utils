from dataclasses import dataclass
from typing import cast, Generator, Iterable

from bpy.types import Key, Mesh, Object, Scene, ShapeKey, UIPopupMenu

from .....lib.operators import FxOperator
from .....lib.xbpy import meshes, Context, Icon, KeyRef, OperatorReturn
from .....lib.compat import addons
from .....lib import streams
from .....var import op_return
from .state import State


class SyncOperator(FxOperator):
    bl_idname = 'fxcpds_vr_avatar_utils.shape_key_value_sync'
    bl_label = 'Sync Shape Keys'
    bl_description = (
        'Synchronizes the values of shape keys with matching names on other'
        'meshes to the values set in this mesh\'s data'
    )

    @classmethod
    def is_runnable(cls, obj: Object):
        return meshes.is_mesh_with_shape_keys(obj)

    def execute(self, context: Context) -> set[OperatorReturn]:
        if not self.is_runnable(context.object):
            return {op_return.CANCELLED}

        sync_context = _SyncContext(context)
        changes = _execute(sync_context)

        # noinspection PyShadowingNames
        def draw(self: UIPopupMenu, _: Context) -> None:
            for change in changes:
                self.layout.label(text=change)

        icon: Icon
        title: str
        result: OperatorReturn
        if sync_context.dry_run:
            icon = 'QUESTION'
            title = 'Operation Plan'
            result = op_return.CANCELLED
        else:
            icon = 'INFO'
            title = 'Operation Result'
            result = op_return.FINISHED

        context.window_manager.popup_menu(draw, title=title, icon=icon)

        return {result}


class _SyncContext:
    def __init__(self, ctx: Context):
        self.context = ctx
        self.source_object = ctx.object
        self.use_skp_compatibility = addons.ShapeKeysPlus.is_available(ctx)
        self.dry_run = State.get_dry_run(ctx)

    @property
    def source_mesh(self) -> Mesh:
        return cast(Mesh, self.source_object.data)

    @property
    def source_key(self) -> Key:
        return self.source_mesh.shape_keys

    @property
    def source_scene(self) -> Scene:
        return self.context.scene


@dataclass(frozen=True)
class _Change:
    shape_key: ShapeKey
    key_ref: KeyRef
    old_value: float
    new_value: float

    def __lt__(self, other: '_Change') -> bool:
        return (self.key_ref.object.name < other.key_ref.object.name
            or (self.key_ref.object.name == other.key_ref.object.name and self.shape_key.name < other.shape_key.name))

    def __gt__(self, other: '_Change') -> bool:
        return (self.key_ref.object.name > other.key_ref.object.name
            or (self.key_ref.object.name == other.key_ref.object.name and self.shape_key.name > other.shape_key.name))

    def make_message(self, dry_run: bool) -> str:
        """
        Generates a message for the change represented by this reference.

        Output message will depend on whether the operation was run with the
        'Dry Run' option enabled.

        Possible output message styles:

        * Would have changed shape key 'foo' on object 'bar' from 0.0 to 1.0
        * Changed shape key 'foo' on object 'bar' from 0.0 to 1.0

        Args:
            dry_run: Whether the operation was run with the 'Dry Run' option
                enabled.

        Returns:
            A generated message string for the change made to the shape key
            represented by this reference instance.
        """
        o = round(self.old_value, 3)
        n = round(self.new_value, 3)
        return (
            ('Would have changed' if dry_run else 'Changed') +
            f" shape key '{self.shape_key.name}' on object '{self.key_ref.object.name}' " +
            f'from {o} to {n}'
        )


def _execute(ctx: _SyncContext) -> list[str]:
    source_shape_key_values = _build_shape_key_value_map(ctx)

    if State.get_lock_to_scene(ctx.context):
        stream = streams.scene_to_objects(ctx.source_scene)
    else:
        stream = streams.scenes_to_objects(ctx.context.blend_data.scenes)

    stream = streams.meshes_to_keys(streams.objects_to_meshes(stream))

    if ctx.use_skp_compatibility:
        stream = _run_with_skp(ctx, stream, source_shape_key_values)
    else:
        stream = _run_std(ctx, stream, source_shape_key_values)

    return [it.make_message(ctx.dry_run) for it in stream]


def _run_with_skp(
    ctx: _SyncContext,
    stream: Iterable[KeyRef],
    source_sk_values: dict[str, float],
) -> Generator[_Change, None, None]:
    skp = addons.ShapeKeysPlus.load(ctx.context)

    key_it: Iterable[ShapeKey]

    only_to_selected = State.get_skp_only_to_selected(ctx.context)

    for ref in stream:
        # Skip over the source object
        if ref.object.name == ctx.source_object.name:
            continue

        if only_to_selected:
            key_it = skp.selected_shape_keys(ref.object)
        else:
            key_it = ref.key.key_blocks

        for sk in key_it:
            if (res := _try_update_shape_key(ctx, sk, ref, source_sk_values)) is not None:
                yield res

    return None


def _run_std(
    ctx: _SyncContext,
    stream: Iterable[KeyRef],
    source_sk_values: dict[str, float],
) -> Generator[_Change, None, None]:
    i_lock = State.get_ignore_locked(ctx.context)

    for ref in stream:
        if ref.object.name == ctx.source_object.name:
            continue

        for sk in ref.key.key_blocks:
            if not i_lock or not sk.lock_shape:
                if (res := _try_update_shape_key(ctx, sk, ref, source_sk_values)) is not None:
                    yield res

    return None


def _try_update_shape_key(
    ctx: _SyncContext,
    shape_key: ShapeKey,
    parent_ref: KeyRef,
    source_values: dict[str, float],
) -> _Change | None:
    # If the current shape key does not align with anything in the source
    # object's shape keys, skip to the next one.
    if shape_key.name not in source_values:
        return None

    new_value = source_values[shape_key.name]

    # if the source object value is already the same as the current shape
    # key's value, skip to the next one.
    if new_value == shape_key.value:
        return None

    out = _Change(shape_key, parent_ref, shape_key.value, new_value)

    if not ctx.dry_run:
        shape_key.value = new_value

    return out


def _build_shape_key_value_map(ctx: _SyncContext) -> dict[str, float]:
    """
    Build source object key/value mapping.

    Returns:
        A dictionary mapping shape key names to values.
    """
    if ctx.use_skp_compatibility:
        return _build_shape_key_value_map_skp(ctx)
    else:
        return _build_shape_key_value_map_std(ctx)


def _build_shape_key_value_map_skp(ctx: _SyncContext) -> dict[str, float]:
    """
    Build source object key/value mapping using Shape Key+ specific options.

    SyncPropertyGroup options that apply in this method:

    * `skp_only_from_selected`: When enabled, only shape keys that have been
      selected in the SK+ shape keys panel will be used to build the source
      mapping.

    * `ignore_muted`: When enabled, shape keys on the source object that are
      marked as muted will be ignored when building the mapping.

    Args:
        ctx: Execution context.

    Returns:
        A dictionary mapping shape key names to values.
    """
    skp = addons.ShapeKeysPlus.load(ctx.context)
    key = ctx.source_key
    out: dict[str, float] = {}

    i_mute = State.get_ignore_muted(ctx.context)
    stream: Iterable[ShapeKey]

    if State.get_skp_only_from_selected(ctx.context):
        stream = skp.selected_shape_keys(ctx.source_object)
    else:
        stream = key.key_blocks

    for sk in stream:
        if not i_mute or not sk.mute:
            out[sk.name] = sk.value

    return out


def _build_shape_key_value_map_std(ctx: _SyncContext) -> dict[str, float]:
    """
    Build source object key/value mapping using the standard Blender shape keys
    options.

    SyncPropertyGroup options that apply in this method:

    * `ignore_muted`: When enabled, shape keys on the source object that are
      marked as muted will be ignored when building the mapping.

    Returns:
        A dictionary mapping shape key names to values.
    """
    key = ctx.source_key
    out: dict[str, float] = {}

    i_mute = State.get_ignore_muted(ctx.context)

    for sk in key.key_blocks:
        if not i_mute or not sk.mute:
            out[sk.name] = sk.value

    return out
