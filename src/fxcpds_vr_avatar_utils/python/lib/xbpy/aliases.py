import bpy

try:
    Context = bpy.AnyContext
    Icon = bpy.types.Icon
    ObjectMode = bpy.types.o.ObjectMode
    ObjectRotationMode = bpy.types.o.ObjectRotationMode
    ObjectType = bpy.types.o.ObjectType
    OperatorReturn = bpy.types.o.OperatorReturn
except Exception:
    Context = bpy.types.Context
    Icon = str
    ObjectMode = str
    ObjectRotationMode = str
    ObjectType = str
    OperatorReturn = str
