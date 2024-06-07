import bpy
from .. import registry

class Panel(bpy.types.Panel, registry.Registrable): pass
