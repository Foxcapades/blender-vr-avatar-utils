import bpy

try:
    Context = bpy.AnyContext
    ObjectType = bpy.types.ObjectType
except Exception:
    from bpy.types import Context

    ObjectType = str
