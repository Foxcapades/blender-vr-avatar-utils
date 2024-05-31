from typing import cast, Generator

from bpy.types import BlendData, Object


def all_mesh_objects(data: BlendData) -> Generator[Object, None, None]:
    for obj in data.objects:
        if obj.type == 'MESH':
            yield obj

    return None



