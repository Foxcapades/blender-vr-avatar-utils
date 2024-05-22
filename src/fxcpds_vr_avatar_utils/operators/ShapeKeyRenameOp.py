from typing import cast, Iterable, Literal

from ..properties import get_property_group, PluginProperties
from ..utils import all_keys, scene_keys
from .aliases import Icon

from bpy.types import Key, Mesh, Object

import bpy


RenameResult = Literal['INVALID', 'NOTHING_CHANGED', 'SUCCESS']


# noinspection PyPep8Naming
class ShapeKeyRenamer:
    """
    Shape key renaming process encapsulation.
    """

    def __init__(self, context: bpy.context, props: PluginProperties):
        """
        Initializes a new _shapeKeyRenamerInstance instance.

        Args:
            context: Blender context.

            props: PluginProperties instance.
        """
        self._context = context
        self._props = props
        self._from = props.key_rename_from
        self._to = props.key_rename_to

    @property
    def _source_object(self) -> Object:
        return self._context.object

    @property
    def _source_mesh(self) -> Mesh:
        return cast(Mesh, self._source_object.data)

    @property
    def _source_key(self) -> bpy.types.Key:
        return self._source_mesh.shape_keys

    def run(self) -> tuple[RenameResult, list[str]]:
        """
        Attempts to execute the shape key renaming process.

        This method will validate the user input, check for any conflicts on
        relevant other meshes' shape keys, and then, if there are no issues
        found, rename all matching shape keys to the new value (self._to).

        Returns:
            A tuple containing an execution status and a list of notification
            messages for the user.
        """
        messages = self._perform_validation()

        if len(messages) > 0:
            return 'INVALID', messages

        stream = scene_keys(self._context.scene) if self._props.lock_to_scene else all_keys(self._context)

        messages = self._process_keys(stream)

        if len(messages) == 0:
            return 'NOTHING_CHANGED', ['Nothing would have changed.' if self._props.dry_run else 'Nothing changed.']

        return 'SUCCESS', messages

    def _process_keys(self, stream: Iterable[tuple[Object, Mesh, Key]]) -> list[str]:
        messages: list[str] = []

        # noinspection PyShadowingBuiltins
        for object, _, key in stream:
            for shape_key in key.key_blocks:
                if shape_key.name == self._from:
                    if self._props.dry_run:
                        messages.append(f'Would have updated object {object.name}')
                    else:
                        shape_key.name = self._to
                        messages.append(f'Updated object {object.name}')
                    break

        return messages

    def _perform_validation(self) -> list[str]:
        message = self._validate_inputs()

        if message is not None:
            return [message]

        return list(map(lambda m: f'Key conflict on object {m}', self._hunt_conflicts()))

    def _validate_inputs(self) -> str | None:
        if len(self._from) == 0:
            return '\'From\' value is blank'

        if len(self._to) == 0:
            return '\'To\' value is blank'

        if self._from == self._to:
            return '\'From\' and \'To\' values are the same'

        if self._from not in self._source_key.key_blocks:
            return '\'From\' value not present on selected object'

        return None

    def _hunt_conflicts(self) -> list[str]:
        """
        Hunts for conflicts in all relevant mesh objects.

        If the option is set to lock the operation to the current scene, this
        method will only test for conflicts in objects present in the current
        scene.

        If the option to lock the operation to the current scene is not set,
        this method will test for conflicts in objects present in all scenes
        in the blend file.

        Returns:
            A list of object keys that were found to have shape key name
            conflicts.
        """
        stream = scene_keys(self._context.scene) if self._props.lock_to_scene else all_keys(self._context)

        conflicts: list[str] = []

        # noinspection PyShadowingBuiltins
        for object, _, key in stream:
            keys = key.key_blocks.keys()
            if self._to in keys and self._from in keys:
                conflicts.append(object.name)

        return conflicts


class ShapeKeyRenameOp(bpy.types.Operator):
    bl_idname = 'fxcpds_vr_avatar_utils.rename_shape_keys'
    bl_label = 'Rename Shape Keys'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = 'Renames all matching shape keys'

    def execute(self, context: bpy.context):
        props = get_property_group()
        runner = ShapeKeyRenamer(context, props)

        (status, messages) = runner.run()

        # noinspection PyShadowingNames
        def draw(self, _):
            col = self.layout.column()
            for message in messages:
                col.label(text=message)

        if status == 'INVALID':
            icon: Icon = 'ERROR'
        else:
            icon: Icon = 'INFO'

        context.window_manager.popup_menu(draw, title="Rename Result", icon=icon)

        if props.dry_run or status != 'SUCCESS':
            return {'CANCELLED'}
        else:
            return {'FINISHED'}
