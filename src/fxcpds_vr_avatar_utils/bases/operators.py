from bpy.types import Operator


class FxOperator(Operator):
    bl_options = {'REGISTER', 'UNDO'}
