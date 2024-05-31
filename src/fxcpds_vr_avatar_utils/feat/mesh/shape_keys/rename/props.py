from typing import cast

from bpy.props import PointerProperty, StringProperty
from bpy.types import Key, PropertyGroup, Scene, UILayout

from .....properties import FxSceneProps
from .....utils import context, shape_keys
from .....utils.aliases import Context


class RenamePropertyGroup(PropertyGroup):
    # noinspection PyTypeHints
    rename_from: StringProperty(
        name='From',
        description=(
            'Original shape key name that will be changed to the value of the '
            '\'To\' field'
        ),
        options=set(),
        search=shape_keys.shape_key_search_cb,
        search_options=set(),
    )

    # noinspection PyTypeHints
    rename_to: StringProperty(
        name='To',
        description=(
            'New shape key name that will be used as the replacement for the '
            '\'From\' field value'
        ),
        options=set()
    )


class RenameProps(FxSceneProps):
    def __init__(self, target: Key, scene: Scene):
        super().__init__(scene)
        self.__target = target

    @classmethod
    def from_current_context(cls, ctx: Context) -> 'RenameProps':
        return cls(context.current_key(ctx), ctx.scene)

    #

    @property
    def rename_from(self) -> str:
        return self.get_rename_from(self.__target)

    @staticmethod
    def draw_rename_from(target: Key, layout: UILayout) -> None:
        layout.prop(data=RenameProps.get_property_group(target), property='rename_from')

    @staticmethod
    def get_rename_from(target: Key) -> str:
        return RenameProps.get_property_group(target).rename_from

    #

    @property
    def rename_to(self) -> str:
        return self.get_rename_to(self.__target)

    @staticmethod
    def draw_rename_to(target: Key, layout: UILayout) -> None:
        layout.prop(data=RenameProps.get_property_group(target), property='rename_to')

    @staticmethod
    def get_rename_to(target: Key) -> str:
        return RenameProps.get_property_group(target).rename_to

    #

    @property
    def property_group(self) -> RenamePropertyGroup:
        return self.get_property_group(self.__target)

    @staticmethod
    def get_property_group(target: Key) -> RenamePropertyGroup:
        return _ModdedKey.cast(target).fxcpds_sk_rename_props


class _ModdedKey(Key):
    fxcpds_sk_rename_props: RenamePropertyGroup

    @staticmethod
    def cast(value: Key) -> '_ModdedKey':
        return cast(_ModdedKey, value)


def register() -> None:
    import bpy
    bpy.utils.register_class(RenamePropertyGroup)
    Key.fxcpds_sk_rename_props = PointerProperty(type=RenamePropertyGroup)


def unregister() -> None:
    from .....utils import silent_unregister_class

    try:
        # noinspection PyUnresolvedReferences
        del Key.fxcpds_sk_rename_props
    except Exception:
        pass

    silent_unregister_class(RenamePropertyGroup)
