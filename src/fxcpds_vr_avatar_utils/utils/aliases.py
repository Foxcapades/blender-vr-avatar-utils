try:
    from bpy.types import o
    from bpy import AnyContext

    Context = AnyContext
    ObjectType = o.ObjectType
except Exception:
    import bpy

    Context = type(bpy.context)
    ObjectType = str
