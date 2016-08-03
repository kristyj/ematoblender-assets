import bpy
import sys

def example_manipulation():
    bpy.data.objects['Cube'].rotation_euler = [0.5] * 3
    bpy.data.objects['Cube'].location.x +=1

def save_blend_to_dest(override=None):
    # Must give filename as first argument after argument '--' if using sys.argv procedure
    outputfilename = sys.argv[sys.argv.index('--') + 1] if override is None else override
    bpy.ops.wm.save_as_mainfile(filepath=outputfilename, compress=True)

if __name__=="__main__":
    example_manipulation()
    save_blend_to_dest()

