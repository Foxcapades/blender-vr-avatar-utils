from typing import cast, Generator

from bpy.types import Key, Mesh, Object, Scene


def meshes_in_scene(scene: Scene) -> Generator[tuple[Object, Mesh], None, None]:
    for obj in scene.objects:
        if obj.type == 'MESH':
            yield obj, cast(Mesh, obj.data)

    return None


def keys_in_scene(scene: Scene) -> Generator[tuple[Object, Mesh, Key], None, None]:
    for obj, mesh in meshes_in_scene(scene):
        if mesh.shape_keys is not None:
            yield obj, mesh, mesh.shape_keys

    return None
