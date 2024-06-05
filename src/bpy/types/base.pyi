import typing

import c
import f
import i
import p


IT = typing.TypeVar('IT')


class bpy_raw_collection(typing.Generic[IT]):
    def __len__(self) -> int: pass
    def __contains__(self, item: typing.Any) -> bool: pass
    def __iter__(self) -> 'bpy_iterator'[IT]: pass


class bpy_iterator(typing.Generic[IT]):
    def __iter__(self) -> 'bpy_iterator'[IT]: pass
    def __next__(self) -> IT: pass


# noinspection PyPep8Naming,PyShadowingBuiltins,PyDefaultArgument
class bpy_struct():
    id_data: i.ID

    def __contains__(self, item) -> bool: pass
    def __getitem__(self, item) -> typing.Any: pass
    def as_pointer(self) -> int: pass
    def driver_add(self, path: str, index: int = -1) -> f.FCurve | list[f.FCurve]: pass
    def driver_remove(self, path: str, index: int = -1) -> bool: pass
    def get(self, key: str, default: typing.Any = None) -> typing.Any: pass
    def id_properties_clear(self) -> None: pass
    def id_properties_ensure(self) -> i.IDPropertyGroup: pass
    def id_properties_ui(self, key: str) -> i.IDPropertyUIManager: pass
    def is_property_hidden(self, property: str) -> bool: pass
    def is_property_overridable_library(self, property: str) -> bool: pass
    def is_property_readonly(self, property: str) -> bool: pass
    def is_property_set(self, property: str, ghost: bool = True) -> bool: pass
    def items(self) -> i.IDPropertyGroupViewItems: pass
    def keyframe_delete(self, data_path: str, index: int = -1, frame: c.Context = None, group: str = '') -> bool: pass
    def keyframe_insert(
        self,
        data_path: str,
        frame: c.Context,
        group: str = '',
        options: set[str] = set()
    ) -> bool: pass
    def keys(self) -> i.IDPropertyGroupViewKeys: pass
    def path_from_id(self, property: str = '') -> str: pass
    def path_resolve(self, path: str, coerce: bool = True) -> p.Property: pass
    def pop(self, key: str, default: p.Property | None = None) -> p.Property | None: pass
    def property_overridable_library_set(self, property: p.Property, overridable: bool) -> bool: pass
    def property_unset(self, property: p.Property): pass
    def type_recast(self) -> 'bpy_struct': pass
    def values(self) -> i.IDPropertyGroupViewValues: pass


CT = typing.TypeVar('CT')


# noinspection PyPep8Naming
class bpy_prop_collection(bpy_struct, typing.Generic[CT]):
    def __contains__(self, item: typing.Any) -> bool: pass
    def __delitem__(self, key: str | int) -> None: pass
    def __getitem__(self, key: str | int) -> CT | None: pass
    def __iter__(self) -> typing.Iterator[CT]: pass
    def __len__(self) -> int: pass
    def __setitem__(self, key: str | int, item: CT) -> None: pass
    def find(self, key: str) -> int: pass
    def foreach_get(self, attr: str, seq) -> None: pass
    def foreach_set(self, attr: str, seq) -> None: pass
    def get(self, key: str, default: CT | None = None) -> CT | None: pass
    def items(self) -> list[tuple[str, CT]]: pass
    def keys(self) -> list[str]: pass
    def values(self) -> list[CT]: pass

__all__ = ['bpy_prop_collection', 'bpy_struct']
