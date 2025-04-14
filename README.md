# Text to Animation - Blender Automation

## How to Run

1. Install Blender 4.0
2. Clone or download this project
3. Place your `.fbx` file in the `animations/` folder
4. Run the script using:

```powershell
& "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" --background --python "main.py"
# 🌀 Text to Animation - Blender Automation

This project automates the process of rendering FBX animation files using Blender's Python scripting.

---

## 📁 Project Structure
text_to_animation_project/ │ ├── main.py # Main entry script ├── requirements.txt # Python + Blender add-ons version info ├── README.md # You're reading this │ ├── animations/ # Folder for .fbx animation files │ └── jump.fbx │ ├── output/ # Folder where rendered videos will be saved │ └── output_jump.mp4
