try:
    from bpy.types import o

    ObjectType = o.ObjectType
except Exception:
    ObjectType = str
