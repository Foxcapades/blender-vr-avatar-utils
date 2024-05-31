import bpy

try:
    Context = bpy.AnyContext
    Icon = bpy.types.Icon
    ObjectType = bpy.types.o.ObjectType
    OperatorReturn = bpy.types.o.OperatorReturn
except Exception:
    Context = bpy.types.Context
    Icon = str
    ObjectType = str
    OperatorReturn = str
