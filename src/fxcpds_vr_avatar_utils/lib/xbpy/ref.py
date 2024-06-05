from dataclasses import dataclass

from bpy.types import Key, Mesh, Object, Scene, ShapeKey, ViewLayer

__all__ = ['ObjectRef', 'MeshRef', 'KeyRef', 'ShapeKeyRef']


@dataclass(frozen=True)
class ObjectRef:
    object: Object
    view_layer: ViewLayer | None = None
    scene: Scene | None = None

    @property
    def has_view_layer(self) -> bool:
        return self.view_layer is not None

    @property
    def has_scene(self) -> bool:
        return self.scene is not None

    def __str__(self) -> str:
        out = f"object '{self.object.name}'"

        if self.has_scene:
            out += f" in scene '{self.scene.name}'"

        return out


@dataclass(frozen=True)
class MeshRef:
    mesh: Mesh
    object: Object | None = None
    view_layer: ViewLayer | None = None
    scene: Scene | None = None

    @classmethod
    def from_object_ref(cls, mesh: Mesh, ref: ObjectRef) -> 'MeshRef':
        return cls(mesh, ref.object, ref.view_layer, ref.scene)

    @property
    def has_object(self) -> bool:
        return self.object is not None

    @property
    def has_view_layer(self) -> bool:
        return self.view_layer is not None

    @property
    def has_scene(self) -> bool:
        return self.scene is not None


@dataclass(frozen=True)
class KeyRef:
    key: Key
    mesh: Mesh | None = None
    object: Object | None = None
    view_layer: ViewLayer | None = None
    scene: Scene | None = None

    @classmethod
    def from_mesh_ref(cls, key: Key, ref: MeshRef) -> 'KeyRef':
        return cls(key, ref.mesh, ref.object, ref.view_layer, ref.scene)

    @property
    def has_mesh(self) -> bool:
        return self.mesh is not None

    @property
    def has_object(self) -> bool:
        return self.object is not None

    @property
    def has_view_layer(self) -> bool:
        return self.view_layer is not None

    @property
    def has_scene(self) -> bool:
        return self.scene is not None


@dataclass(frozen=True)
class ShapeKeyRef:
    shape_key: ShapeKey
    key: Key | None = None
    mesh: Mesh | None = None
    object: Object | None = None
    view_layer: ViewLayer | None = None
    scene: Scene | None = None

    @classmethod
    def from_key_ref(cls, shape_key: ShapeKey, key_ref: KeyRef) -> 'ShapeKeyRef':
        return cls(shape_key, key_ref.key, key_ref.mesh, key_ref.object, key_ref.view_layer, key_ref.scene)

    @property
    def has_key(self) -> bool:
        return self.key is not None

    @property
    def has_mesh(self) -> bool:
        return self.mesh is not None

    @property
    def has_object(self) -> bool:
        return self.object is not None

    @property
    def has_view_layer(self) -> bool:
        return self.view_layer is not None

    @property
    def has_scene(self) -> bool:
        return self.scene is not None
