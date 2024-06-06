import bpy.utils.previews


class Icons:
    __icons: dict[str, str] = {
        'globe': 'globe.svg',
        'invert': 'invert.svg',
        'bone_rotation': 'bone-rotation.svg',
    }

    __index: bpy.utils.previews.ImagePreviewCollection | None = None

    def _init(self, asset_dir: str) -> None:
        if self.__index is not None:
            return None

        import os
        from bpy.utils import previews

        icon_dir = os.path.join(asset_dir, "icons")

        self.__index = previews.new()

        for name in self.__icons:
            self.__index.load(name, os.path.join(icon_dir, self.__icons[name]), 'IMAGE')

    def _destroy(self) -> None:
        if self.__index is None:
            return None

        from bpy.utils import previews

        previews.remove(self.__index)
        self.__index = None

    def __getattr__(self, icon: str) -> int:
        if self.__index is None:
            raise Exception(f"attempted to lookup icon '{icon}' from icon index while icon index is unloaded")
        if icon not in self.__index:
            raise AttributeError(f"unregistered icon '{icon}'")

        return self.__index[icon].icon_id
