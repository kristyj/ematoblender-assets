import bpy
import sys

def example_manipulation():
    bpy.data.objects['Cube'].rotation_euler = [0.5] * 3
    bpy.data.objects['Cube'].location.x +=1

    print(sys.argv)
    outputfilename = sys.argv[sys.argv.index('--') + 1]  # Must give filename as first argument after argument '--'
    bpy.ops.wm.save_as_mainfile(filepath=outputfilename, compress=True)

if __name__=="__main__":
    example_manipulation()