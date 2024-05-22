from typing import cast, Generator, Iterable

from bpy.types import Key, Mesh, Object, Scene

from .aliases import Context, ObjectType

import bpy


def scene_mesh_objects(scene: Scene) -> Generator[Object, None, None]:
    if scene.objects is None:
        return None

    for o in _filter_objects_by_type(scene.objects, 'MESH'):
        yield o

    return None


def all_mesh_objects(context: Context) -> Generator[Object, None, None]:
    if context.blend_data.objects is None:
        return None

    for o in _filter_objects_by_type(context.blend_data.objects, 'MESH'):
        yield o

    return None


def scene_meshes(scene: Scene) -> Generator[tuple[Object, Mesh], None, None]:
    for o in scene_mesh_objects(scene):
        yield o, cast(Mesh, o.data)

    return None


def all_meshes(context: Context) -> Generator[tuple[Object, Mesh], None, None]:
    for o in all_mesh_objects(context):
        yield o, cast(Mesh, o.data)

    return None


def scene_keys(scene: Scene) -> Generator[tuple[Object, Mesh, Key], None, None]:
    for o, m in scene_meshes(scene):
        if m.shape_keys is not None:
            yield o, m, m.shape_keys

    return None


def all_keys(context: Context) -> Generator[tuple[Object, Mesh, Key], None, None]:
    for o, m in all_meshes(context):
        if m.shape_keys is not None:
            yield o, m, m.shape_keys

    return None


def _filter_objects_by_type(stream: Iterable[Object], kind: ObjectType) -> Generator[Object, None, None]:
    for o in stream:
        if o.type == kind:
            yield o

    return None
