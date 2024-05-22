from typing import cast

import bpy
import re

C = bpy.context
D = C.blend_data

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='DESELECT')


def bake_transforms(obj: bpy.types.Object) -> None:
    mb = obj.matrix_basis
    cast(bpy.types.Armature, obj.data).transform(mb)
    obj.matrix_basis.identity()


def fix_armature(obj: bpy.types.Object) -> None:
    # select the current object
    obj.select = True
    C.view_layer.objects.active = obj

    # Scale the armature
    bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))

    # Bake the scale transform
    bake_transforms(obj)

    # Switch to pose mode
    bpy.ops.object.mode_set(mode='POSE')

    # for each bone in the armature
    for pbone in C.pose_object.pose.bones.values():
        # fix the name (remove any suffixes added by the fbx import)
        pbone.bone.name = re.sub("_\\d+$", "", pbone.bone.name)
        # Select the bone
        pbone.bone.select = True

    # Fix the location
    C.pose_object.pose.bones['Hips'].location *= 0.01

    bpy.ops.pose.rotation_mode_set(type='QUATERNION')

    bpy.ops.poselib.create_pose_asset()

    bpy.ops.object.mode_set(mode='OBJECT')

    obj.select = False


# Multi-pose processing.
#
# Assumes that the only objects present are armatures.
#
# For each armature performs the following steps:
#
#   1. Trims any trailing '_#' suffixes from the bones in the armature.
#
#   2. Corrects the locations of the root bone ('Hips') of each armature to
#      bring the pose back to center.
#
#   3. Fixes the location of the root bone ('Hips') to bring the
#      pose back to center.
#
#   4. Ensures all the bones have their rotation mode set to quaternion.
#
#   5. Creates a pose asset for each armature.
for o in D.objects.values():

    # Filter out non-armature objects
    if o.type != 'ARMATURE':
        continue

    fix_armature(o)


# from pathlib import Path


# collection_map = {}

# for col in D.collections.values():
#    for obj in col.objects.keys():
#        collection_map[obj] = col.name


# catalog_map = {}


# with (Path(D.filepath).parent.parent.parent.parent / "blender_assets.cats.txt").open() as f:
#    for line in f.readlines():
#        if line.startswith(('#', 'VERSION', "\n")):
#            continue
#        (id, path, *_) = line.strip().split(':')
#
#        catalog_map[Path(path).name] = id


# for obj in D.objects.values():
#    obj.select = True
#    C.view_layer.objects.active = obj
#
#    bpy.ops.object.mode_set(mode='POSE')
#
#    for pbone in C.pose_object.pose.bones.values():
#        pbone.bone.select=True

#    bpy.ops.poselib.create_pose_asset()
#
#    D.actions[C.pose_object.name].asset_data.catalog_id = catalog_map[collection_map[C.pose_object.name]]

#    bpy.ops.object.mode_set(mode='OBJECT')
