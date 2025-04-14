import bpy
import os
import sys

# ========== USER CONFIGURATION ==========
# Use dynamic project path (relative to the script location)
project_dir = os.path.dirname(os.path.abspath(__file__))

# Customizable parameters
fbx_filename = "jump.fbx"                     # Name of your FBX animation file
output_filename = "output_jump.mp4"           # Name of output video
camera_position = (0, -10, 5)
camera_rotation = (1.1, 0, 0)

# Construct proper paths
animations_dir = os.path.join(project_dir, "animations")
output_dir = os.path.join(project_dir, "output")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Full paths
fbx_path = os.path.join(animations_dir, fbx_filename)
output_path = os.path.join(output_dir, output_filename)

# ========== STEP 1: Clear Scene ==========
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ========== STEP 2: Import FBX ==========
if os.path.exists(fbx_path):
    bpy.ops.import_scene.fbx(filepath=fbx_path)
else:
    raise FileNotFoundError(f"❌ FBX file not found at {fbx_path}")

# ========== STEP 3: Add and Set Camera ==========
bpy.ops.object.camera_add(location=camera_position, rotation=camera_rotation)
camera = bpy.context.object
camera.name = "Camera"
bpy.context.scene.camera = camera

# ========== STEP 4: Render Settings ==========
bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 60

# ========== STEP 5: Output Settings ==========
bpy.context.scene.render.filepath = output_path
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'

# ========== STEP 6: Render Animation ==========
print("🎬 Rendering started...")
bpy.ops.render.render(animation=True)
print(f"✅ Render complete! Output saved at: {output_path}")
