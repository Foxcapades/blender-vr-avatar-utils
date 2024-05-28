import bpy

from .aliases import Context


class Compatibility:
    @staticmethod
    def have_shape_keys_plus(context: Context) -> bool:
        """
        Tests whether the current Blender instance has Shape Keys+ installed.
        """
        return 'shape_keys_plus' in context.preferences.addons
