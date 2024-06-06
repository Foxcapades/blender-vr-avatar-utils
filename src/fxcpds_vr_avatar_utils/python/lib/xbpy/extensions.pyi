import bpy
from .. import registry

class Panel(bpy.types.Panel, registry.Registrable):
    @classmethod
    def register(cls) -> None: pass

    @classmethod
    def unregister(cls) -> None: pass
