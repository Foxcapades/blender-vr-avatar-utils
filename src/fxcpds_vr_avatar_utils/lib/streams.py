from typing import cast, Generator, Iterable

from bpy.types import Mesh, Object, Scene

from .xbpy import KeyRef, MeshRef, ObjectRef


def scene_to_objects(input: Scene) -> Generator[ObjectRef, None, None]:
    for obj in input.objects:
        yield ObjectRef(obj, scene=input)


def scenes_to_objects(input: Iterable[Scene], distinct: bool = False) -> Generator[ObjectRef, None, None]:
    if distinct:
        names: set[str] = set()

        for scene in input:
            for obj in scene.objects:
                if obj.name not in names:
                    names.add(obj.name)
                    yield ObjectRef(obj, scene=scene)
    else:
        for scene in input:
            for ref in scene_to_objects(scene):
                yield ref

    return None


def objects_to_meshes(input: Iterable[Object | ObjectRef], distinct: bool = False) -> Generator[MeshRef, None, None]:
    if distinct:
        names: set[str] = set()

        for it in input:
            if isinstance(it, ObjectRef):
                if it.object.type == 'MESH':
                    mesh = cast(Mesh, it.object.data)
                    if mesh.name not in names:
                        names.add(mesh.name)
                        yield MeshRef.from_object_ref(mesh, it)

            elif isinstance(it, Object):
                if it.type == 'MESH':
                    mesh = cast(Mesh, it.data)
                    if mesh.name not in names:
                        names.add(mesh.name)
                        yield MeshRef(mesh, it)
    else:
        for it in input:
            if isinstance(it, ObjectRef):
                if it.object.type == 'MESH':
                    yield MeshRef.from_object_ref(cast(Mesh, it.object.data), it)

            elif isinstance(it, Object):
                if it.type == 'MESH':
                    yield MeshRef(cast(Mesh, it.data), it)

    return None


def meshes_to_keys(input: Iterable[Mesh | MeshRef], distinct: bool = False) -> Generator[KeyRef, None, None]:
    if distinct:
        names: set[str] = set()

        for it in input:
            if isinstance(it, MeshRef):
                if it.mesh.shape_keys is not None and it.mesh.shape_keys.name not in names:
                    names.add(it.mesh.shape_keys.name)
                    yield KeyRef.from_mesh_ref(it.mesh.shape_keys, it)

            elif isinstance(it, Mesh):
                if it.shape_keys is not None and it.shape_keys.name not in names:
                    names.add(it.shape_keys.name)
                    yield KeyRef(it.shape_keys, it)
    else:
        for it in input:
            if isinstance(it, MeshRef):
                if it.mesh.shape_keys is not None:
                    yield KeyRef.from_mesh_ref(it.mesh.shape_keys, it)

            elif isinstance(it, Mesh):
                if it.shape_keys is not None:
                    yield KeyRef(it.shape_keys, it)

    return None
