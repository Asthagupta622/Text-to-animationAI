import bpy

# === CLEAN UP EXISTING SCENE ===
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# === IMPORT FBX ANIMATION ===
fbx_path = "C:/Users/user/Desktop/text_to_animation_project/animations/jump.fbx"
bpy.ops.import_scene.fbx(filepath=fbx_path)

# === ADD NEW CAMERA ===
bpy.ops.object.camera_add(location=(0, -10, 5), rotation=(1.1, 0, 0))
camera = bpy.context.object
camera.name = "Camera"
bpy.context.scene.camera = camera

# === RENDER SETTINGS ===
bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'  # Updated for Blender 4.4
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 60

# === OUTPUT VIDEO SETTINGS ===
bpy.context.scene.render.filepath = "C:/Users/user/Desktop/text_to_animation_project/output/output_jump.mp4"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'

# === START RENDERING ===
bpy.ops.render.render(animation=True)

print("🎉 Render complete! Check your output folder.")
