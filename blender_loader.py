import bpy
import os

# Path to the folder containing FBX files
animations_path = r"C:\Users\user\Desktop\text_to_animation_project\animations"

# Path to the action.txt file
action_file_path = r"C:\Users\user\Desktop\text_to_animation_project\action.txt"

# Read the extracted action
with open(action_file_path, 'r') as f:
    action = f.read().strip()

# Map action to file name
action_to_animation = {
    "walk": "walk.fbx",
    "run": "run.fbx",
    "jump": "jump.fbx",
    "sit": "sit.fbx"
}

animation_file = action_to_animation.get(action, "idle.fbx")
animation_path = os.path.join(animations_path, animation_file)

# Clear existing scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Import the selected animation
if os.path.exists(animation_path):
    bpy.ops.import_scene.fbx(filepath=animation_path)
    print(f"Loaded animation: {animation_file}")
else:
    print(f"Animation file not found: {animation_path}")
