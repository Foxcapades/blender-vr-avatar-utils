from .BoneRotationNormalizeOp import BoneRotationNormalizeOp
from .ShapeKeyRenameOp import ShapeKeyRenameOp
from .ShapeKeySyncOp import ShapeKeySyncOp

import bpy


def register_operators() -> None:
    bpy.utils.register_class(BoneRotationNormalizeOp)
    bpy.utils.register_class(ShapeKeyRenameOp)
    bpy.utils.register_class(ShapeKeySyncOp)


def unregister_operators() -> None:
    bpy.utils.unregister_class(BoneRotationNormalizeOp)
    bpy.utils.unregister_class(ShapeKeyRenameOp)
    bpy.utils.unregister_class(ShapeKeySyncOp)
