from typing import Literal

from bpy.types.base import bpy_struct


TextureType = Literal[
    'NONE',
    'BLEND',
    'CLOUDS',
    'DISTORTED_NOISE',
    'IMAGE',
    'MAGIC',
    'MARBLE',
    'MUSGRAVE',
    'NOISE',
    'STUCCI',
    'VORONOI',
    'WOOD',
]


# noinspection PyPropertyDefinition
class Timer(bpy_struct):
    @property
    def time_delta(self) -> float: pass
    
    @property
    def time_duration(self) -> float: pass
    
    @property
    def time_step(self) -> float: pass
