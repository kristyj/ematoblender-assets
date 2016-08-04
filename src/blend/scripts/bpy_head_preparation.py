"""Begins with a MakeHuman file, ends with a rigged face"""
import bpy
import os
import math
import asset_properties as pps

def import_makehuman():
    mhxpath = os.path.normpath("$resourcesDir/" + pps.makehuman_filename)
    bpy.ops.import_scene.makehuman_mhx(filepath=mhxpath, clothes=False, shapekeys=False, shapedrivers=False, rigify=False)

def cut_head():
    """Delete all vertices in the MakeHuman body object except for DEF-neck, DEF-head and DEF-jaw vertex groups"""
    mhxname = os.join('', pps.makehuman_filename.split('.')[:-1]) # filename without mhx extension
    savegroups = pps.makehuman_face_vertex_groups

    # select all vertices in the object (this could be more efficient)
    for vg in bpy.data.objects[mhxname+':Body'].vertex_groups:
        bpy.ops.object.vertex_group_set_active(group=vg.name)
        bpy.ops.object.vertex_group_select()

        if vg.name not in savegroups:
            bpy.ops.object.vertex_group_remove() # remove group reference if not to be kept

    # deselect vertices to keep
    for sg in [bpy.data.objects[mhxname+':Body'].vertex_groups[s] for s in savegroups]:
        bpy.ops.object.vertex_group_set_active(group=sg.name)
        bpy.ops.object.vertex_group_deselect()

    # delete vertices that remain selected
    bpy.ops.mesh.delete(type='VERT')

def set_origin_to_lower_lip_center(mymeshname):
    """Providing that the model stands straddling the y-axis with z-axis upwards, finds the middle highest vertex
    on the lower lip. Enter the name of the body mesh, eg default_makehuman:Body."""

    def find_lower_lip_center(mymeshname):
        obj = bpy.data.objects[mymeshname]
        gi = obj.vertex_groups['DEF-jaw'].index
        all_ll_vertices = [v for v in bpy.data.meshes[mymeshname].vertices for g in v.groups if g.group == gi]
        print('all ll vertices', all_ll_vertices)
        # get mid x coordinate
        x_mid = min([o.co.x for o in all_ll_vertices]) * 0.5 + max([o.co.x for o in all_ll_vertices]) * 0.5
        print(x_mid)
        # get largest y that's close to the mid x coordinate (decrease in value going backwards to capture front of mouth
        maxv, height = max([(v, v.co.z - v.co.y * 0.5) for v in all_ll_vertices if abs(v.co.x - x_mid) < 0.1], key=lambda x: x[1])
        return maxv

    def set_origin_to_result(meshname, vertexfindingfn):
        originvertex = vertexfindingfn(meshname)
        originvertex.select = True
        newlocation = originvertex.co
        bpy.context.scene.cursor_location = newlocation
        # move 3D cursor to new location
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")

    set_origin_to_result(mymeshname, find_lower_lip_center)

#set_origin_to_lower_lip_center(bpy.data.objects['default_female:Body'].name)

def scale_object(objectname, x, y, z):
    """Multiply the object's current scaling by the new dimensions given in x, y, z."""
    current_scale = bpy.data.objects[objectname].scale
    bpy.data.objects[objectname].scale  = [i for i in map(lambda x: x[0] * x[1], zip(current_scale, [x, y, z]))]

def scale_around_object_origin(objectname, x, y, z):
    obj = bpy.data.objects[objectname]
    current_location = obj.location
    current_rotation = obj.rotation_quaternion
    obj.location = [0,0,0]
    obj.rotation_quaternion = [1, 0, 0, 0]
    scale_object(obj.name, x, y, z)
    obj.location = current_location
    obj.rotation_quaternion = [1, 0, 0, 0]

scale_around_object_origin('default_female', 1, 1, 5)
#scale_object('default_female', 1, 1, 5)
