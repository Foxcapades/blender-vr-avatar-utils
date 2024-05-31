from typing import Callable, TypeVar


_icons: dict[str, str] = {
    'globe': 'globe.svg'
}


T = TypeVar('T')


def icon_dict(cls: type[T]) -> type[T]:
    global _icons

    functions: list[str] = []

    sub_init_lines: list[str] = [(
        'def _init(self, icon_dir: str) -> None:\n'
        '    import os\n'
        '    from bpy.utils.previews import new as new_index, ImagePreviewCollection\n'
        '    self.__index: ImagePreviewCollection | None = new_index()'
    )]

    properties: dict[str, str] = {}

    for name in _icons:
        getter_name = f"_get_{name}"

        sub_init_lines.append(f"    self.__index.load('{name}', os.path.join(icon_dir, '{_icons[name]}'), 'IMAGE')")

        functions.append(
            f"def {getter_name}(self) -> int:\n"
            f"    return self.__index['{name}'].icon_id\n"
        )

        properties[getter_name] = name

    functions.append('\n'.join(sub_init_lines))
    del sub_init_lines

    functions.append(
        'def _destroy(self) -> None:\n'
        '    if self.__index is None:\n'
        '        return\n'
        '    from bpy.utils.previews import remove as remove_index\n'
        '    remove_index(self.__index)\n'
        '    self.__index = None'
    )

    scope: dict[str, Callable] = {}

    exec('\n'.join(functions), globals(), scope)
    del functions

    docs: list[str] = [(
        "Icon Registry\n"
        "\n"
        "Attributes:"
    )]

    for name in scope:
        if name in properties:
            prop_name = properties[name]
            setattr(cls, prop_name, property(fget=scope[name]))
            docs.append(f"    {prop_name} (int): Icon ID for the '{prop_name}' icon.")

        setattr(cls, name, scope[name])

    docs.append('')

    cls.__doc__ = '\n'.join(docs)

    return cls


@icon_dict
class Icons:
    pass
