from base import bpy_prop_collection

from a import AnimData
from i import ID
from s import ShapeKey


# noinspection PyPropertyDefinition
class Key(ID):
    eval_time: float
    use_relative: bool

    @property
    def animation_data(self) -> AnimData: pass

    @property
    def key_blocks(self) -> bpy_prop_collection[ShapeKey]: pass
        
    @property
    def reference_key(self) -> ShapeKey: pass

    @property
    def user(self) -> ID: pass


