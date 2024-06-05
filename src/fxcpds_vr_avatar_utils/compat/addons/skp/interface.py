from typing import Iterable, Protocol

from bpy.types import Object, ShapeKey


class ShapeKeysPlus(Protocol):
    # noinspection PyShadowingBuiltins
    def selected_shape_keys(self, object: Object) -> Iterable[ShapeKey]:
        pass
