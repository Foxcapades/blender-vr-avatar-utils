try:
    from bpy.types import o
    from bpy import AnyContext

    Context = AnyContext
    ObjectType = o.ObjectType
except Exception:
    import bpy

    Context = bpy.types.Context
    ObjectType = str
