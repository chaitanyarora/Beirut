import bpy
from datetime import datetime
import os


bpy.context.scene.my_tool.drone.total_spheres = 100
bpy.context.scene.my_tool.drone.total_rows = 10
bpy.context.scene.my_tool.drone.x_diff = 1.00
bpy.context.scene.my_tool.drone.y_diff = 1.00

# Part 2: Sphere Grid
bpy.ops.object.sphere_grid()
print("Test passed ✅ - PARTYYYYYY grid")
bpy.ops.object.reset_scene()
print("Test passed ✅ - PARTYYYYYY reset")