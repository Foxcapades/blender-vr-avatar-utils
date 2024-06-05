import bpy

################################################################################
#
#     Import-Safe Type Aliases.
#
#  Aliases of blender enum types and type wrappers that don't actually exist in
#  the Blender Python API.
#
#  When developing locally, these aliases will resolve to Python Protocols that
#  will allow for smart editor features like type checking and autocompletion.
#
#  At runtime, these aliases will be mapped to either the real Blender API type,
#  or a primitive type for enums.
#
################################################################################

Context = bpy.AnyContext
Icon = bpy.types.Icon
ObjectMode = bpy.types.o.ObjectMode
ObjectRotationMode = bpy.types.o.ObjectRotationMode
ObjectType = bpy.types.o.ObjectType
OperatorReturn = bpy.types.o.OperatorReturn
