bl_info = {
    "name": "Text to Animation",
    "blender": (2, 93, 0),
    "category": "Animation",
}

import bpy
import os

class TEXTTOANIM_PT_Panel(bpy.types.Panel):
    bl_label = "Text to Animation"
    bl_idname = "TEXTTOANIM_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Text2Anim'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "input_text")
        layout.operator("object.text_to_animation")

class TextToAnimationOperator(bpy.types.Operator):
    bl_idname = "object.text_to_animation"
    bl_label = "Text to Animation"

    def execute(self, context):
        input_text = context.scene.input_text
        if input_text:
            self.report({'INFO'}, f"Text entered: {input_text}")
            # You can add the logic here to convert the text to an animation
            # For example, download FBX file and import it
            self.render_animation(input_text)
        else:
            self.report({'ERROR'}, "No input text provided")
        return {'FINISHED'}
    
    def render_animation(self, action):
        # Define the path for the swimming animation (adjust as needed)
        fbx_filename = "swimming.fbx"
        fbx_path = os.path.join(os.getcwd(), "animations", fbx_filename)

        if not os.path.exists(fbx_path):
            self.report({'ERROR'}, f"FBX file not found: {fbx_path}")
            return {'CANCELLED'}

        # === CLEAN SCENE ===
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        # === IMPORT ANIMATION ===
        self.import_fbx(fbx_path)

        # === CAMERA SETUP ===
        self.setup_camera()

        # === RENDER SETTINGS ===
        bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'
        bpy.context.scene.render.resolution_x = 1280
        bpy.context.scene.render.resolution_y = 720
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 60

        # === OUTPUT SETTINGS ===
        output_path = f"{os.getcwd()}/output/output_{action}.mp4"
        bpy.context.scene.render.filepath = output_path
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'
        bpy.context.scene.render.ffmpeg.codec = 'H264'

        # === RENDER ANIMATION ===
        bpy.ops.render.render(animation=True)
        self.report({'INFO'}, f"✅ Render complete! Check: {output_path}")
        return {'FINISHED'}

    def setup_camera(self):
        bpy.ops.object.camera_add(location=(0, -8, 4), rotation=(1.1, 0, 0))
        camera = bpy.context.object
        camera.name = "Camera"
        bpy.context.scene.camera = camera
        print("Camera setup complete")

    def import_fbx(self, fbx_path):
        if not os.path.exists(fbx_path):
            raise FileNotFoundError(f"FBX file not found at: {fbx_path}")
        bpy.ops.import_scene.fbx(filepath=fbx_path)
        print(f"Successfully imported FBX file from: {fbx_path}")

def register():
    bpy.utils.register_class(TEXTTOANIM_PT_Panel)
    bpy.utils.register_class(TextToAnimationOperator)
    bpy.types.Scene.input_text = bpy.props.StringProperty(name="Input Text")

def unregister():
    bpy.utils.unregister_class(TEXTTOANIM_PT_Panel)
    bpy.utils.unregister_class(TextToAnimationOperator)
    del bpy.types.Scene.input_text

if __name__ == "__main__":
    register()
