import dataclasses
import bpy.types

@dataclasses.dataclass(frozen=True)
class ObjectRef:
    object: bpy.types.Object
    view_layer: bpy.types.ViewLayer | None = None
    scene: bpy.types.Scene | None = None

    @property
    def has_view_layer(self) -> bool: pass

    @property
    def has_scene(self) -> bool: pass

@dataclasses.dataclass(frozen=True)
class MeshRef:
    mesh: bpy.types.Mesh
    object: bpy.types.Object | None = None
    view_layer: bpy.types.ViewLayer | None = None
    scene: bpy.types.Scene | None = None

    @classmethod
    def from_object_ref(cls, mesh: bpy.types.Mesh, ref: ObjectRef) -> 'MeshRef': pass

    @property
    def has_object(self) -> bool: pass

    @property
    def has_view_layer(self) -> bool: pass

    @property
    def has_scene(self) -> bool: pass

@dataclasses.dataclass(frozen=True)
class KeyRef:
    key: bpy.types.Key
    mesh: bpy.types.Mesh | None = None
    object: bpy.types.Object | None = None
    view_layer: bpy.types.ViewLayer | None = None
    scene: bpy.types.Scene | None = None

    @classmethod
    def from_mesh_ref(cls, key: bpy.types.Key, ref: MeshRef) -> 'KeyRef': pass

    @property
    def has_mesh(self) -> bool: pass

    @property
    def has_object(self) -> bool: pass

    @property
    def has_view_layer(self) -> bool: pass

    @property
    def has_scene(self) -> bool: pass

@dataclasses.dataclass(frozen=True)
class ShapeKeyRef:
    shape_key: bpy.types.ShapeKey
    key: bpy.types.Key | None = None
    mesh: bpy.types.Mesh | None = None
    object: bpy.types.Object | None = None
    view_layer: bpy.types.ViewLayer | None = None
    scene: bpy.types.Scene | None = None

    @classmethod
    def from_key_ref(cls, shape_key: bpy.types.ShapeKey, key_ref: KeyRef) -> 'ShapeKeyRef': pass

    @property
    def has_key(self) -> bool: pass

    @property
    def has_mesh(self) -> bool: pass

    @property
    def has_object(self) -> bool: pass

    @property
    def has_view_layer(self) -> bool: pass

    @property
    def has_scene(self) -> bool: pass
