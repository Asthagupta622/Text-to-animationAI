import os
import requests

def download_fbx(action):
    if action == "swimming":
        fbx_filename = "swimming.fbx"  # Path to the swimming.fbx file
    elif action == "jump":
        fbx_filename = "jump.fbx"  # Similarly, handle other actions
    else:
        fbx_filename = None  # Return None if action is not recognized
    
    if fbx_filename:
        # Assuming the file is already downloaded and saved in the 'animations' directory
        fbx_path = os.path.join(os.getcwd(), "animations", fbx_filename)
        return fbx_path
    else:
        raise ValueError(f"FBX file not found for action: {action}")
