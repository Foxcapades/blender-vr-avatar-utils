from typing import Literal


RampBlend = Literal[
    'MIX',
    'DARKEN',
    'MULTIPLY',
    'BURN',
    'LIGHTEN',
    'SCREEN',
    'DODGE',
    'ADD',
    'OVERLAY',
    'SOFT_LIGHT',
    'LINEAR_LIGHT',
    'DIFFERENCE',
    'EXCLUSION',
    'SUBTRACT',
    'DIVIDE',
    'HUE',
    'SATURATION',
    'COLOR',
    'VALUE',
]

RegionType = Literal[
    'WINDOW',
    'HEADER',
    'CHANNELS',
    'TEMPORARY',
    'UI',
    'TOOLS',
    'TOOL_PROPS',
    'ASSET_SHELF',
    'ASSET_SHELF_HEADER',
    'PREVIEW',
    'HUD',
    'NAVIGATION_BAR',
    'EXECUTE',
    'FOOTER',
    'TOOL_HEADER',
    'XR',
]
