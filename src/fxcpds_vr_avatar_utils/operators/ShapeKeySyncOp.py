from typing import cast, Iterable
from dataclasses import dataclass

from ..compat import addons
from ..properties import get_property_group, PluginProperties
from ..utils import all_keys, scene_keys

from .aliases import Context, OperatorReturn

from bpy.types import Key, Mesh, Object, Operator, Scene, ShapeKey


@dataclass(frozen=True)
class ShapeKeyRef:
    """
    Shape Key Reference

    Contains fields describing a shape key that was updated by the shape key
    synchronization process.

    Additionally, this class defines `__lt__` and `__gt__` methods so the
    results can be sorted for reporting to the user.

    Attributes:
          object_name: Name of the parent object to which the shape key belongs.

          shape_key_name: Name of the shape key that was updated.

          old_value: Previous shape key value.

          new_value: New shape key value.
    """
    object_name: str
    shape_key_name: str
    old_value: float
    new_value: float

    def __lt__(self, other: 'ShapeKeyRef') -> bool:
        return (self.object_name < other.object_name
            or (self.object_name == other.object_name and self.shape_key_name < other.shape_key_name))

    def __gt__(self, other: 'ShapeKeyRef') -> bool:
        return (self.object_name > other.object_name
            or (self.object_name == other.object_name and self.shape_key_name > other.shape_key_name))

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
            f" shape key '{self.shape_key_name}' on object '{self.object_name}' " +
            f'from {o} to {n}'
        )


class ShapeKeySynchronizer:
    """
    ShapeKey synchronization process definition.

    Defines the process and context necessary to perform the shape key sync
    operation.
    """

    def __init__(self, context: Context, props: PluginProperties):
        self._context = context
        self._props = props
        self._skp_compat = addons.ShapeKeysPlus.is_available(context)

    @property
    def _source_object(self) -> Object:
        return self._context.object

    @property
    def _source_mesh(self) -> Mesh:
        return cast(Mesh, self._source_object.data)

    @property
    def _source_key(self) -> Key:
        return self._source_mesh.shape_keys

    @property
    def _scene(self) -> Scene:
        return self._context.scene

    def run(self) -> list[ShapeKeyRef]:
        """
        Runs the shape key synchronization process.

        First builds a mapping of the relevant shape keys on the source object,
        then iterates through all the shape keys on every other object in the
        scene attempting to match shape keys on each object to the source object
        map by key name.  When a key name is found on a target object that is
        present in the source map, the value from the source map will be set on
        the located key.

        If the dry run option is set this method will not make any changes, but
        will return references to the shape keys that it would have changed had
        dry run been disabled.

        Returns:
            A list of references to the shape keys that were changed by this
            operation.
        """
        source_values = self._build_source_mapping()

        if self._props.lock_to_scene:
            stream = scene_keys(self._context.scene)
        else:
            stream = all_keys(self._context)

        if self._skp_compat:
            changed = self._run_skp(stream, source_values)
        else:
            changed = self._run_std(stream, source_values)

        changed.sort()

        return changed

    def _run_skp(self, stream: Iterable[tuple[Object, Mesh, Key]], source_keys: dict[str, float]) -> list[ShapeKeyRef]:
        """
        Executes the shape key synchronization against the objects yielded by
        the given stream using Shape Keys+ specific options.

        Options that impact this method:

        * Dry Run: See :func:`_try_update_shape_key`.

        * Only To Selected: When enabled, this method will only attempt to
            update the values of shape keys that are marked as selected for each
            target object.

        Args:
            stream: Iterable stream of target objects whose shape keys should be
                synchronized.

            source_keys: Shape key values from the source object.  These are the
                values that will be set on relevant target keys.

        Returns:
            A list of references to shape keys that were or would have been
            updated by this method.
        """
        skp = addons.ShapeKeysPlus.load(self._context)

        changed: list[ShapeKeyRef] = []

        # noinspection PyShadowingBuiltins
        for object, _, key in stream:
            if object.name == self._source_object.name:
                continue

            if self._props.key_sync_skp_only_to_selected:
                key_it = skp.selected_shape_keys(object)
            else:
                key_it = key.key_blocks

            for shape_key in key_it:
                self._try_update_shape_key(object, shape_key, source_keys, changed)

        return changed

    def _run_std(self, stream: Iterable[tuple[Object, Mesh, Key]], source_keys: dict[str, float]) -> list[ShapeKeyRef]:
        """
        Executes the shape key synchronization against the objects yielded by
        the given stream using the standard option set.

        Options that impact this method:

        * Dry Run: See :func:`_try_update_shape_key`.

        * Ignored Locked: When enabled, this method will only attempt to
            update the values of shape keys that are not marked as locked.

        Args:
            stream: Iterable stream of target objects whose shape keys should be
                synchronized.

            source_keys: Shape key values from the source object.  These are the
                values that will be set on relevant target keys.

        Returns:
            A list of references to shape keys that were or would have been
            updated by this method.
        """
        changed: list[ShapeKeyRef] = []

        i_lock = self._props.key_sync_ignore_locked

        # noinspection PyShadowingBuiltins
        for object, _, key in stream:
            if object.name == self._source_object.name:
                continue

            for shape_key in key.key_blocks:
                # If we care about shape key locking and the current shape key
                # is locked, skip to the next one.
                if i_lock and shape_key.lock_shape:
                    continue

                self._try_update_shape_key(object, shape_key, source_keys, changed)

        return changed

    # noinspection PyShadowingBuiltins
    def _try_update_shape_key(
        self,
        object: Object,
        target_shape_key: ShapeKey,
        source_values: dict[str, float],
        changes: list[ShapeKeyRef],
    ) -> None:
        """
        Updates the target shape key if necessary.

        Options that impact this method:

        * Dry Run: When enabled, this method will not update the target shape
            key's value and will instead simply update the `changes` list as if
            it had.

        Args:
            object: Parent object containing the target shape key.

            target_shape_key: Shape key that may be updated.

            source_values: Mapping of shape key values from the source object.

            changes: List of changes that this the shape key sync operation has
                made.  This method will mutate this list by appending a new
                shape key reference if a change was or would have been made.
        """
        # If the current shape key does not align with anything in the source
        # object's shape keys, skip to the next one.
        if target_shape_key.name not in source_values:
            return

        new_value = source_values[target_shape_key.name]

        # if the source object value is already the same as the current shape
        # key's value, skip to the next one.
        if new_value == target_shape_key.value:
            return

        changes.append(ShapeKeyRef(object.name, target_shape_key.name, target_shape_key.value, new_value))

        if not self._props.dry_run:
            target_shape_key.value = new_value

    def _build_source_mapping(self) -> dict[str, float]:
        """
        Build source object key/value mapping.

        Returns:
            A dictionary mapping shape key names to values.
        """

        # If Shape Keys+ is present, then build the source mapping using options
        # specific to that plugin.
        if self._skp_compat:
            return self._build_source_mapping_skp()

        # Otherwise use the default options.
        else:
            return self._build_source_mapping_standard()

    def _build_source_mapping_skp(self) -> dict[str, float]:
        """
        Build source object key/value mapping using Shape Key+ specific options.

        Options that apply in this method:

        * Only Selected: When enabled, only shape keys that have been selected
          in the SK+ shape keys panel will be used to build the source mapping.

        * Ignore Muted: When enabled, shape keys on the source object that are
          marked as muted will be ignored when building the mapping.

        Returns:
            A dictionary mapping shape key names to values.
        """
        skp = addons.ShapeKeysPlus.load(self._context)

        out: dict[str, float] = {}

        i_mute = self._props.key_sync_ignore_muted

        if self._props.key_sync_skp_only_from_selected:
            stream = skp.selected_shape_keys(self._source_object)
        else:
            stream = self._source_key.key_blocks

        for sk in stream:
            if not i_mute or not sk.mute:
                out[sk.name] = sk.value

        return out

    def _build_source_mapping_standard(self) -> dict[str, float]:
        """
        Build source object key/value mapping using the standard Blender shape
        keys options.

        Options that apply in this method:

        * Ignore Muted: When enabled, shape keys on the source object that are
          marked as muted will be ignored when building the mapping.

        Returns:
            A dictionary mapping shape key names to values.
        """
        out: dict[str, float] = {}

        i_mute = self._props.key_sync_ignore_muted

        for sk in self._source_key.key_blocks:
            if not i_mute or not sk.mute:
                out[sk.name] = sk.value

        return out


class ShapeKeySyncOp(Operator):
    bl_idname = 'fxcpds_vr_avatar_utils.shape_key_value_sync'
    bl_label = 'Sync Shape Keys'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = 'Synchronizes shape keys with matching names to the values set in this mesh\'s data'

    def execute(self, context: Context) -> set[OperatorReturn]:
        if not self._is_applicable(context.object):
            return {'CANCELLED'}

        props = get_property_group()

        changes = ShapeKeySynchronizer(context, props).run()

        # noinspection PyShadowingNames
        def draw(self, _):
            col = self.layout.column()

            if len(changes) == 0:
                if props.dry_run:
                    col.label(text='Nothing would have changed.')
                else:
                    col.label(text='Nothing was changed.')
            else:
                for change in changes:
                    col.label(text=change.make_message(props.dry_run))

        context.window_manager.popup_menu(draw, title="Sync Result", icon='INFO')

        return {'CANCELLED' if props.dry_run else 'FINISHED'}

    @staticmethod
    def _is_applicable(obj: Object) -> bool:
        return obj is not None and obj.type == 'MESH' and cast(Mesh, obj.data).shape_keys is not None
