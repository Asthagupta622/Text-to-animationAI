import bpy

# 🧹 Clear the existing scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 📥 Import FBX animation
bpy.ops.import_scene.fbx(filepath="C:/Users/user/Desktop/text_to_animation_project/animations/jump.fbx")

# 🎥 Add and set the camera
bpy.ops.object.camera_add(location=(0, -8, 4), rotation=(1.1, 0, 0))
camera = bpy.context.object
bpy.context.scene.camera = camera

# ⚙️ Set render engine
bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'

# 📏 Set resolution and frames
bpy.context.scene.render.resolution_x = 320
bpy.context.scene.render.resolution_y = 240
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 10  # Use full length later

# 💾 Output video settings
bpy.context.scene.render.filepath = "C:/Users/user/Desktop/text_to_animation_project/output_test.mp4"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'

# 🎬 Render animation
print("Rendering started...")
bpy.ops.render.render(animation=True)
print("Rendering finished!")
