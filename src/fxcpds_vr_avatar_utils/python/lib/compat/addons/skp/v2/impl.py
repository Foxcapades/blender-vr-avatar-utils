from typing import cast, Generator

from bpy.types import Key, Mesh, Object, ShapeKey

import bpy


class ShapeKeysPlusV2:
    """
    Implements the `ShapeKeysPlus`_ protocol.

    .. _ShapeKeysPlus:
        :py:class:`fxcpds_vr_avatar_utils.compat.addons.skp.interface.ShapeKeysPlus`
    """

    def __init__(self, context: bpy.context):
        """
        Args:
            context: Blender context.
        """
        self._ctx = context

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

        # If the given object is not a mesh, then we are not interested in it.
        if object is None or object.type != 'MESH' or object.data is None:
            return None

        # Get a typed handle on the object's Key instance (if it exists)
        key = cast(Mesh, object.data).shape_keys

        # noinspection PyUnresolvedReferences
        if key is None or key.shape_keys_plus is None or key.shape_keys_plus.selections is None:
            return None

        # noinspection PyUnresolvedReferences
        from shape_keys_plus import core

        # A queue of folders to process.
        folders: list[ShapeKey] = []

        # Go through all the currently selected ShapeKeys...
        # noinspection PyUnresolvedReferences
        for index in key.shape_keys_plus.selections.keys():
            sk = self._get_shape_key(key, index)

            if sk is None:
                continue

            # If the ShapeKey is a folder, then all the contents should be
            # counted as selected as well.  Add the folder to the queue to be
            # processed after the initial scan.
            if core.key.is_folder(sk):
                folders.append(sk)
            else:
                yield sk

        # If there were any folders selected, yield the contents of those
        # folders and any sub-folders.
        while len(folders) > 0:
            for child in core.folder.get_children(folders.pop(0)):
                if core.key.is_folder(child):
                    folders.append(child)
                else:
                    yield child

        return None

    @staticmethod
    def _get_shape_key(key: Key, index: str) -> ShapeKey | None:
        """
        Attempts to get a shape key by index.

        Shape Keys+ stores the numerical index of selected keys as strings.
        This appears to be a holdover from some previous iteration of the addon?

        Args:
            key: Parent Key instance from which the target ShapeKey should be
                retrieved.

            index: Index of the ShapeKey to retrieve.

        Returns:
            The target ShapeKey instance, if present, otherwise None.
        """
        try:
            i = int(index)
            if i in key.key_blocks:
                return key.key_blocks[i]
        except ValueError:
            pass

        return None
