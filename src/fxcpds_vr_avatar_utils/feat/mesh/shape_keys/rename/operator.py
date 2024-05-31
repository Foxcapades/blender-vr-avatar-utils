from typing import Iterable

from bpy.types import Key, Object, UIPopupMenu

from .....utils.aliases import Context, Icon, OperatorReturn
from .....utils.bpy_wrappers import ObjectRef, ShapeKeyRef
from .....utils import context as C, Result, streams
from .....bases import FxOperator

from .props import RenameProps


class RenameOperator(FxOperator):
    bl_idname = 'fxcpds_vr_avatar_utils.rename_shape_keys'
    bl_label = 'Bulk Rename Shape Keys'
    bl_description = (
        'Renames matching shape keys found in this scene or blender file'
    )

    @staticmethod
    def is_runnable(target: Key) -> bool:
        f, t = _cleaned_names(target)

        return len(f) > 0 and len(t) > 0 and f != t and f in target.key_blocks and t not in target.key_blocks

    def execute(self, context: Context) -> set[OperatorReturn]:
        key = C.current_key(context)

        if not self.is_runnable(key):
            return {'CANCELLED'}

        dry_run = RenameProps.get_dry_run(context.scene)
        t_name = RenameProps.get_rename_to(key)

        if RenameProps.get_lock_to_scene(context.scene):
            stream = streams.scene_to_objects(context.scene)
        else:
            stream = streams.scenes_to_objects(context.blend_data.scenes, distinct=True)

        success: bool
        messages: list[str]
        if (result := _evaluate_context(key, stream)).is_result:
            success = True
            if dry_run:
                messages = [f"Would have updated object '{ref.object.name}'" for ref in result.value]
            else:
                messages = []
                for ref in result.value:
                    ref.shape_key.name = t_name
                    messages.append(f"Updated object '{ref.object.name}'")
        else:
            success = False
            prefix = f"A shape key with the name {t_name} already exists on object "
            messages = [prefix + f"'{obj.name}'" for obj in result.error]

        # noinspection PyShadowingNames
        def draw(self: UIPopupMenu, _: Context) -> None:
            col = self.layout.column()
            for msg in messages:
                col.label(text=msg)

        icon: Icon
        title: str
        op_result: OperatorReturn
        if dry_run:
            if success:
                icon = 'QUESTION'
                title = 'Operation Plan'
            else:
                icon = 'ERROR'
                title = 'Operation Would Be Aborted'

            op_result = 'CANCELLED'
        else:
            if success:
                icon = 'INFO'
                title = 'Operation Result'
                op_result = 'FINISHED'
            else:
                icon = 'ERROR'
                title = 'Operation Aborted'
                op_result = 'CANCELLED'

        context.window_manager.popup_menu(draw, title=title, icon=icon)

        return {op_result}


def register() -> None:
    import bpy
    bpy.utils.register_class(RenameOperator)


def unregister() -> None:
    from .....utils import silent_unregister_class
    silent_unregister_class(RenameOperator)


def _cleaned_names(target: Key) -> tuple[str, str]:
    return RenameProps.get_rename_from(target).strip(), RenameProps.get_rename_to(target).strip()


def _evaluate_context(source: Key, o_stream: Iterable[ObjectRef]) -> Result[list[ShapeKeyRef], list[Object]]:
    shape_keys: list[ShapeKeyRef] = []
    conflicts: list[Object] = []

    k_stream = streams.meshes_to_keys(streams.objects_to_meshes(o_stream))

    f_name = RenameProps.get_rename_from(source)
    t_name = RenameProps.get_rename_to(source)

    for ref in k_stream:
        if ref.key.name == source.name or f_name not in ref.key.key_blocks:
            continue

        if t_name in ref.key.key_blocks:
            conflicts.append(ref.object)
            continue

        if len(conflicts) == 0:
            shape_keys.append(ShapeKeyRef.from_key_ref(ref.key.key_blocks[f_name], ref))

    return Result.of_error(conflicts) if len(conflicts) > 0 else Result.of_value(shape_keys)
