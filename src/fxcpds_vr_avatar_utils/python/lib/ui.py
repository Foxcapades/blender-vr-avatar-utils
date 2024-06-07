from abc import abstractmethod, ABC
from enum import auto, Enum
from typing import cast, Iterable

from bpy.types import UILayout

from .xbpy import Icon, Context, Panel


class UIComponentType(Enum):
    BOX = auto()
    PANEL = auto()


class UIComponent(ABC):
    type: UIComponentType = UIComponentType.BOX

    icon: Icon | int | None = None

    title: str

    # noinspection PyUnusedLocal
    @classmethod
    def should_be_drawn(cls, context: Context) -> bool:
        return True

    # noinspection PyUnusedLocal
    @classmethod
    def should_be_enabled(cls, context: Context) -> bool:
        return True

    @classmethod
    @abstractmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        pass


class _UISubPanel(type(UIComponent), type(Panel)): pass


class UISubPanel(UIComponent, Panel, ABC, metaclass=_UISubPanel):
    open_by_default = False

    @classmethod
    def register(cls) -> None:
        """
        This is here just to override the ABC.register classmethod to avoid
        errors from Blender's register_class method calling it.
        """
        pass


class UIPanelBody(ABC):
    @classmethod
    @abstractmethod
    def ui_components(cls, context: Context) -> Iterable[UIComponent]:
        pass

    @classmethod
    def should_be_drawn(cls, context: Context) -> bool:
        for _ in _drawable_components(cls.ui_components(context), context):
            return True
        return False

    @classmethod
    def draw(cls, layout: UILayout, context: Context) -> None:
        for component in cls.ui_components(context):
            if component.type == UIComponentType.BOX:
                _draw_box(layout, component, context)
            elif component.type == UIComponentType.PANEL:
                _draw_panel(layout, cast(UISubPanel, component), context)


def _drawable_components(source: Iterable[UIComponent], context: Context) -> Iterable[UIComponent]:
    for c in source:
        if c.should_be_drawn(context):
            yield c


def _draw_box(layout: UILayout, component: UIComponent, context: Context) -> None:
    sub = layout.box()

    if len(component.title) > 0 or component.icon is not None:
        header = sub.column()
        _draw_header(header, component)
        header.separator()

    sub = sub.column()
    component.draw(sub, context)
    if not component.should_be_enabled(context):
        sub.enabled = False


def _draw_panel(layout: UILayout, component: UISubPanel, context: Context) -> None:
    ref = cast(UISubPanel, component)
    header, sub = layout.panel(idname=ref.bl_idname, default_closed=not ref.open_by_default)

    if len(component.title) > 0 or component.icon is not None:
        _draw_header(header, component)

    if not component.should_be_enabled(context):
        sub.enabled = False


def _draw_header(layout: UILayout, component: UIComponent) -> None:
    if isinstance(component.icon, int):
        layout.label(text=component.title, icon_value=component.icon)
    elif isinstance(component.icon, str):
        # noinspection PyTypeChecker
        layout.label(text=component.title, icon=component.icon)
    else:
        layout.label(text=component.title)
