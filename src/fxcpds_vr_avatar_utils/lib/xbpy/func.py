import typing
import bpy.types

from . import aliases


class UIPropsParameters(typing.TypedDict):
    """
    Dictionary type for the UILayout.prop method arguments.
    """
    data: bpy.types.PropertyGroup | bpy.types.ID | bpy.types.Bone | bpy.types.PoseBone
    property: str
    text: typing.NotRequired[str]
    text_ctx: typing.NotRequired[str]
    translate: typing.NotRequired[bool]
    icon: typing.NotRequired[aliases.Icon]
    placeholder: typing.NotRequired[str]
    expand: typing.NotRequired[bool]
    slider: typing.NotRequired[bool]
    toggle: typing.NotRequired[int]
    icon_only: typing.NotRequired[bool]
    event: typing.NotRequired[bool]
    full_event: typing.NotRequired[bool]
    emboss: typing.NotRequired[bool]
    index: typing.NotRequired[int]
    icon_value: typing.NotRequired[int]
    invert_checkbox: typing.NotRequired[bool]


__all__ = ['UIPropsParameters']
