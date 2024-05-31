import bpy
import typing

from ..utils.aliases import Context


class FxScenePropertyGroup(bpy.types.PropertyGroup):
    # noinspection PyTypeHints
    dry_run: bpy.props.BoolProperty(
        name='Dry Run',
        description=(
            'Decides whether changes should be performed or if the plugin '
            'should perform a \'dry run\' where it makes no changes and '
            'instead reports the changes it would have made if Dry Run was '
            'disabled'
        ),
        options=set(),
    )

    # noinspection PyTypeHints
    lock_to_scene: bpy.props.BoolProperty(
        name='This Scene Only',
        description=(
            'Whether bulk operations should be locked to objects in the '
            'current scene only.  If disabled, bulk operations will apply to '
            'relevant objects in all scenes'
        ),
        default=True,
        options=set(),
    )


class FxSceneProps:
    def __init__(self, scene: bpy.types.Scene):
        self._scene = scene

    @classmethod
    def from_current_context(cls, ctx: Context) -> 'FxSceneProps':
        return cls(ctx.scene)

    #

    @property
    def dry_run(self) -> bool:
        return self.get_dry_run(self._scene)

    @staticmethod
    def draw_dry_run(target: bpy.types.Scene, layout: bpy.types.UILayout) -> None:
        layout.prop(data=typing.cast(_ModdedScene, target).fxcpds_scene_props, property='dry_run')

    @staticmethod
    def get_dry_run(target: bpy.types.Scene) -> bool:
        return typing.cast(_ModdedScene, target).fxcpds_scene_props.dry_run

    #

    @property
    def lock_to_scene(self) -> bool:
        return self.get_lock_to_scene(self._scene)

    @staticmethod
    def draw_lock_to_scene(target: bpy.types.Scene, layout: bpy.types.UILayout) -> None:
        layout.prop(data=typing.cast(_ModdedScene, target).fxcpds_scene_props, property='lock_to_scene')

    @staticmethod
    def get_lock_to_scene(target: bpy.types.Scene) -> bool:
        return typing.cast(_ModdedScene, target).fxcpds_scene_props.lock_to_scene

    #

    @staticmethod
    def scene_props(target: bpy.types.Scene) -> FxScenePropertyGroup:
        return typing.cast(_ModdedScene, target).fxcpds_scene_props


class _ModdedScene(bpy.types.Scene):
    fxcpds_scene_props: FxScenePropertyGroup


def register() -> None:
    bpy.utils.register_class(FxScenePropertyGroup)
    bpy.types.Scene.fxcpds_scene_props = bpy.props.PointerProperty(type=FxScenePropertyGroup)


def unregister() -> None:
    from ..utils import silent_unregister_class

    try:
        # noinspection PyUnresolvedReferences
        del bpy.types.Scene.fxcpds_scene_props
    except Exception:
        pass

    silent_unregister_class(FxScenePropertyGroup)
