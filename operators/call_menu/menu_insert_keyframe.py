import bpy


class MenuInsertKeyframe(bpy.types.Menu):
    bl_label = "Insert KeyFrame Menu"
    bl_idname = "VSE_MT_Insert_keyframe_Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="Location").ch = (1, 0, 0, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="Rotation").ch = (0, 1, 0, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="Scale").ch = (0, 0, 1, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="LocRot").ch = (1, 1, 0, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="LocScale").ch =(1, 0, 1, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="RotScale").ch = (0, 1, 1, 0, 0)

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="LocRotScale").ch = (1, 1, 1, 0, 0)

        layout.separator()

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="Alpha").ch = (0, 0, 0, 1, 0)

        layout.separator()

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="CropScale").ch = (0, 0, 1, 0, 1)

        layout.separator()

        layout.operator("vse_transform_tools.insert_keyframe",
                        text="All").ch = (1, 1, 1, 1, 1)
