from typing import Literal

from .base import bpy_prop_collection
from .o import Object


LightprobesType = Literal['SPHERE', 'PLANE', 'VOLUME']

LightType = Literal['POINT', 'SUN', 'SPOT', 'AREA']


# noinspection PyPropertyDefinition
class LayerObjects(bpy_prop_collection[Object]):  # NEW REGEX
    active: Object

    @property
    def selected(self) -> bpy_prop_collection[Object]:
        pass
