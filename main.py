import sys
import os

# Specify the project path manually (adjust as needed)
project_path = r"C:\Users\user\Desktop\text_to_animation_project"

# Add project path to sys.path
if project_path not in sys.path:
    sys.path.append(project_path)

# Ensure that the current working directory is correctly set for Blender
os.chdir(project_path)

import bpy
from utils.text_to_action import extract_action
from utils.scraper import download_fbx
from utils.blender_integration import import_fbx, setup_camera


def main(input_text):
    # Step 1: Extract action from text
    action = extract_action(input_text)
    if not action:
        print("Error: No action extracted")
        return

    # Step 2: Download the FBX file
    fbx_filename = download_fbx(action)
    fbx_path = os.path.join(project_path, "animations", fbx_filename)

    # === CLEAN SCENE ===
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # === IMPORT ANIMATION ===
    import_fbx(fbx_path)

    # === CAMERA SETUP ===
    setup_camera()

    # === RENDER SETTINGS ===
    bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 60

    # === OUTPUT SETTINGS ===
    output_path = os.path.join(project_path, "output", f"output_{action}.mp4")
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'

    # === RENDER ANIMATION ===
    bpy.ops.render.render(animation=True)
    print(f"✅ Render complete! Check: {output_path}")

# Run from Blender
if __name__ == "__main__":
    main("A man jumping")  # Replace with dynamic input if needed
