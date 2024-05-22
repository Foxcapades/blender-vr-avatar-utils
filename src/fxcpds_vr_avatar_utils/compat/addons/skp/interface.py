from typing import Generator, Protocol

from bpy.types import Object, ShapeKey


class ShapeKeysPlus(Protocol):
    """
    Shape Keys+ Abstraction Layer

    Defines an interface through which the VR Avatar Utils plugin will interact
    with the internals of the Shape Keys+ plugin.

    Implemented by:

    * .v2.ShapeKeysPlusV2
    """

    # noinspection PyShadowingBuiltins
    def selected_shape_keys(self, object: Object) -> Generator[ShapeKey, None, None]:
        """
        Iterates over the ShapeKey instances attached to the given mesh object
        that are marked as selected according to the Shape Keys+ addon.

        This method will not yield any folder keys.

        Args:
            object:  Object from which attached ShapeKey instances will be
                yielded.

        Yields:
             ShapeKey instances from the given object that are marked as
             selected in Shape Keys+.

        Returns:
            None.
        """
        pass
