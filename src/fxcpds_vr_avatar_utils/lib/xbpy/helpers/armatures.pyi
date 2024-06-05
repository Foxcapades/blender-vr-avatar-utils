import bpy.types

def is_armature(obj: bpy.types.Object) -> bool: pass

def is_usable_armature(obj: bpy.types.Object) -> bool: pass

def has_bones(obj: bpy.types.Object) -> bool: pass

def to_armature(obj: bpy.types.Object) -> bpy.types.Armature: pass
