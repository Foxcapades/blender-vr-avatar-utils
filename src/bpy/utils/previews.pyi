import bpy
import typing

class ImagePreviewCollection:
    def __getitem__(self, item: str) -> bpy.types.ImagePreview:
        pass

    def clear(self) -> None:
        pass

    def close(self) -> None:
        pass

    def load(
        self,
        name: str,
        filepath: str,
        filetype: typing.Literal['IMAGE', 'MOVIE', 'BLEND', 'FONT'],
        force_reload: bool = False,
    ) -> bpy.types.ImagePreview:
        pass


def new() -> ImagePreviewCollection:
    pass


def remove(pcoll: ImagePreviewCollection) -> None:
    pass

