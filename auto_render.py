import bpy
import sys
import os

# ========== USER CUSTOMIZATION ==========
# You can modify these values or pass via CLI later
fbx_filename = "jump.fbx"  # Put your animation file here
camera_position = (0, -10, 5)  # X, Y, Z coordinates
camera_rotation = (1.1, 0, 0)  # Rotation in radians
output_filename = "output_jump.mp4"  # Output video name

# Construct full file paths
project_dir = "C:/Users/user/Desktop/text_to_animation_project"
fbx_path = os.path.join(project_dir, "animations", fbx_filename)
output_path = os.path.join(project_dir, "output", output_filename)

# ========== STEP 1: Clear the Scene ==========
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ========== STEP 2: Import FBX ==========
bpy.ops.import_scene.fbx(filepath=fbx_path)

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
bpy.ops.render.render(animation=True)

print("✅ Render complete! Check your output folder.")
