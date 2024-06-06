import abc, enum, typing
import bpy
import fxcpds_vr_avatar_utils


class UIComponentType(enum.Enum):
    BOX: typing.Any
    PANEL: typing.Any


class UIComponent(abc.ABC):
    type: UIComponentType
    title: str
    icon: fxcpds_vr_avatar_utils.lib.xbpy.Icon | int | None

    @classmethod
    def should_be_drawn(cls, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> bool: pass

    @classmethod
    def should_be_enabled(cls, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> bool: pass

    @classmethod
    @abc.abstractmethod
    def draw(cls, layout: bpy.types.UILayout, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> None: pass


class UISubPanel(abc.ABC, UIComponent, bpy.types.Panel, fxcpds_vr_avatar_utils.bases.Registrable):
    open_by_default: bool

    @classmethod
    def register(cls) -> None: pass

    @classmethod
    def unregister(cls) -> None: pass


class UIPanelBody(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def ui_components(cls, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> typing.Iterable[UIComponent]:
        """
        Returns an iterable over child components under this panel body.

        This method should perform minimal, if any context checking as it will
        be called on every draw cycle.

        Args:
            context: Blender context.

        Returns:
            An iterable over child UI components to render.
        """
        pass

    @classmethod
    def should_be_drawn(cls, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> bool: pass

    @classmethod
    def draw(cls, layout: bpy.types.UILayout, context: fxcpds_vr_avatar_utils.lib.xbpy.Context) -> None: pass
