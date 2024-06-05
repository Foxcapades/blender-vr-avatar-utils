import typing
import bpy.types
from . import xbpy

def scene_to_objects(input: bpy.types.Scene) -> typing.Iterable[xbpy.ObjectRef]: pass

def scenes_to_objects(input: typing.Iterable[bpy.types.Scene], distinct: bool = False) -> typing.Iterable[xbpy.ObjectRef]: pass

def objects_to_meshes(input: typing.Iterable[bpy.types.Object | xbpy.ObjectRef], distinct: bool = False) -> typing.Iterable[xbpy.MeshRef]: pass

def meshes_to_keys(input: typing.Iterable[bpy.types.Mesh | xbpy.MeshRef], distinct: bool = False) -> typing.Iterable[xbpy.KeyRef]: pass
