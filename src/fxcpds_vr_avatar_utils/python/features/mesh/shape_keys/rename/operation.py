from typing import Iterable

from bpy.types import Object, UIPopupMenu

from .....lib.operators import FxOperator
from .....lib.results import Result
from .....lib.xbpy import keys, Context, Icon, ObjectRef, OperatorReturn, ShapeKeyRef
from .....lib import streams
from .....var import op_return

from .state import State


class RenameOperator(FxOperator):
    bl_idname = 'fxcpds_vr_avatar_utils.rename_shape_keys'
    bl_label = 'Bulk Rename Shape Keys'
    bl_description = (
        'Renames matching shape keys found in this scene or blender file'
    )

    @classmethod
    def is_runnable(cls, c: Context) -> bool:
        f, t = _cleaned_names(c)
        k = keys.require_key(c.object)

        return len(f) > 0 and len(t) > 0 and f != t and f in k.key_blocks and t not in k.key_blocks

    def execute(self, context: Context) -> set[OperatorReturn]:
        if not self.is_runnable(context):
            return {op_return.CANCELLED}

        state = State.from_current_context(context)

        if state.lock_to_scene:
            stream = streams.scene_to_objects(context.scene)
        else:
            stream = streams.scenes_to_objects(context.blend_data.scenes, distinct=True)

        success: bool
        messages: list[str]
        if (result := _evaluate_context(state, stream)).is_result:
            success = True
            if state.dry_run:
                messages = [f"Would have updated object '{ref.object.name}'" for ref in result.value]
            else:
                messages = []
                for ref in result.value:
                    ref.shape_key.name = state.rename_to
                    messages.append(f"Updated object '{ref.object.name}'")
        else:
            success = False
            prefix = f"A shape key with the name {state.rename_to} already exists on object "
            messages = [prefix + f"'{obj.name}'" for obj in result.error]

        # noinspection PyShadowingNames
        def draw(self: UIPopupMenu, _: Context) -> None:
            col = self.layout.column()
            for msg in messages:
                col.label(text=msg)

        icon: Icon
        title: str
        op_result: OperatorReturn
        if state.dry_run:
            if success:
                icon = 'QUESTION'
                title = 'Operation Plan'
            else:
                icon = 'ERROR'
                title = 'Operation Would Be Aborted'

            op_result = op_return.CANCELLED
        else:
            if success:
                icon = 'INFO'
                title = 'Operation Result'
                op_result = op_return.FINISHED
            else:
                icon = 'ERROR'
                title = 'Operation Aborted'
                op_result = op_return.CANCELLED

        context.window_manager.popup_menu(draw, title=title, icon=icon)

        return {op_result}


def _cleaned_names(c: Context) -> tuple[str, str]:
    return State.get_rename_from(c).strip(), State.get_rename_to(c).strip()


def _evaluate_context(state: State, o_stream: Iterable[ObjectRef]) -> Result[list[ShapeKeyRef], list[Object]]:
    shape_keys: list[ShapeKeyRef] = []
    conflicts: list[Object] = []

    k_stream = streams.meshes_to_keys(streams.objects_to_meshes(o_stream))

    for ref in k_stream:
        if ref.key.name == state.current_key.name or state.rename_from not in ref.key.key_blocks:
            continue

        if state.rename_to in ref.key.key_blocks:
            conflicts.append(ref.object)
            continue

        if len(conflicts) == 0:
            shape_keys.append(ShapeKeyRef.from_key_ref(ref.key.key_blocks[state.rename_from], ref))

    return Result.of_error(conflicts) if len(conflicts) > 0 else Result.of_value(shape_keys)
