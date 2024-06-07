import abc, enum, typing
import bpy
from .. import lib


class UIComponentType(enum.Enum):
    BOX: typing.Any
    PANEL: typing.Any


class UIComponent(abc.ABC):
    type: UIComponentType
    title: str
    icon: lib.xbpy.Icon | int | None

    @classmethod
    def should_be_drawn(cls, context: lib.xbpy.Context) -> bool: pass

    @classmethod
    def should_be_enabled(cls, context: lib.xbpy.Context) -> bool: pass

    @classmethod
    @abc.abstractmethod
    def draw(cls, layout: bpy.types.UILayout, context: lib.xbpy.Context) -> None: pass


class UISubPanel(abc.ABC, UIComponent, bpy.types.Panel, lib.registry.Registrable):
    open_by_default: bool


class UIPanelBody(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def ui_components(cls, context: lib.xbpy.Context) -> typing.Iterable[UIComponent]:
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
    def should_be_drawn(cls, context: lib.xbpy.Context) -> bool: pass

    @classmethod
    def draw(cls, layout: bpy.types.UILayout, context: lib.xbpy.Context) -> None: pass
