from typing import cast

import bpy
from bpy.props import BoolProperty, PointerProperty
from bpy.types import Key, PropertyGroup, Scene, UILayout

from .....properties import FxSceneProps
from .....utils import objects
from .....utils.aliases import Context


class SyncPropertyGroup(PropertyGroup):
    # noinspection PyTypeHints
    ignore_muted: BoolProperty(
        name='Ignore Muted',
        description=(
            'Whether muted shape keys on this object should be ignored when '
            'synchronizing shape key values to other objects in the scene.  If '
            'a shape key on this object is muted, it will not be considered '
            'when synchronizing values to other objects.  Shape keys that are '
            'muted on other objects in this scene may still be updated'
        ),
        default=True,
        options=set(),
    )

    # noinspection PyTypeHints
    ignore_locked: BoolProperty(
        name='Ignore Locked',
        description=(
            'Whether locked shape keys on other objects in this scene should '
            'be ignored when synchronizing shape key values from this object'
        ),
        default=True,
        options=set(),
    )

    # noinspection PyTypeHints
    skp_only_from_selected: BoolProperty(
        name='Only from Selected',
        description=(
            'Only synchronize values from those currently selected on this mesh'
        ),
        options=set(),
    )

    # noinspection PyTypeHints
    skp_only_to_selected: BoolProperty(
        name='Only to Selected',
        description=(
            'Only synchronize values to those currently selected on other '
            'meshes'
        ),
        options=set(),
    )


class SyncProps(FxSceneProps):
    def __init__(self, key: Key, scene: Scene):
        super().__init__(scene)
        self._key = key

    @classmethod
    def from_current_context(cls, ctx: Context) -> 'SyncProps':
        return cls(objects.require_key(ctx.object), ctx.scene)

    #

    @property
    def ignore_muted(self) -> bool:
        return self.get_ignore_muted(self._key)

    @staticmethod
    def draw_ignore_muted(target: Key, layout: UILayout) -> None:
        layout.prop(data=cast(ModdedKey, target).fxcpds_sk_sync_props, property='ignore_muted')

    @staticmethod
    def get_ignore_muted(target: Key) -> bool:
        return cast(ModdedKey, target).fxcpds_sk_sync_props.ignore_muted

    #

    @property
    def ignore_locked(self) -> bool:
        return self.get_ignore_locked(self._key)

    @staticmethod
    def draw_ignore_locked(target: Key, layout: UILayout) -> None:
        layout.prop(data=cast(ModdedKey, target).fxcpds_sk_sync_props, property='ignore_locked')

    @staticmethod
    def get_ignore_locked(target: Key) -> bool:
        return cast(ModdedKey, target).fxcpds_sk_sync_props.ignore_locked

    #

    @property
    def skp_only_from_selected(self) -> bool:
        return self.get_skp_only_from_selected(self._key)

    @staticmethod
    def draw_skp_only_from_selected(target: Key, layout: UILayout) -> None:
        layout.prop(data=cast(ModdedKey, target).fxcpds_sk_sync_props, property='skp_only_from_selected')

    @staticmethod
    def get_skp_only_from_selected(target: Key) -> bool:
        return cast(ModdedKey, target).fxcpds_sk_sync_props.skp_only_from_selected

    #

    @property
    def skp_only_to_selected(self) -> bool:
        return self.get_skp_only_to_selected(self._key)

    @staticmethod
    def draw_skp_only_to_selected(target: Key, layout: UILayout) -> None:
        layout.prop(data=cast(ModdedKey, target).fxcpds_sk_sync_props, property='skp_only_to_selected')

    @staticmethod
    def get_skp_only_to_selected(target: Key) -> bool:
        return cast(ModdedKey, target).fxcpds_sk_sync_props.skp_only_to_selected


class ModdedKey(Key):
    fxcpds_sk_sync_props: SyncPropertyGroup


def register():
    bpy.utils.register_class(SyncPropertyGroup)
    Key.fxcpds_sk_sync_props = PointerProperty(type=SyncPropertyGroup)


def unregister():
    from .....utils import silent_unregister_class

    try:
        # noinspection PyUnresolvedReferences
        del Key.fxcpds_sk_sync_props
    except Exception:
        pass

    silent_unregister_class(SyncPropertyGroup)
