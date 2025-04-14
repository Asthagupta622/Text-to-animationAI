import bpy
import os

def setup_camera():
    # Add camera logic
    bpy.ops.object.camera_add(location=(0, -8, 4), rotation=(1.1, 0, 0))
    camera = bpy.context.object
    camera.name = "Camera"
    bpy.context.scene.camera = camera
    print("Camera setup complete")
def import_fbx(fbx_path):
    if not os.path.exists(fbx_path):
        raise FileNotFoundError(f"FBX file not found at: {fbx_path}")
    bpy.ops.import_scene.fbx(filepath=fbx_path)
    print(f"Successfully imported FBX file from: {fbx_path}")
