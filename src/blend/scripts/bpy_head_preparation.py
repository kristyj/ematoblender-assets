"""Begins with a MakeHuman file, ends with a rigged face"""
import bpy
import os
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
