from fxcpds_vr_avatar_utils.lib.xbpy import Context, Panel

from .mesh import MeshPanel
from .armature import ui as armature_ui


class FxPropsPanel(Panel):
    bl_idname = "OBJECT_PT_fxcpds_vr_avatar_utils_properties_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'data'
    bl_label = 'VR Avatar Utils'

    @classmethod
    def poll(cls, context: Context) -> bool:
        return MeshPanel.should_be_drawn(context) or armature_ui.should_be_drawn(context)

    def draw(self, context: Context) -> None:
        if MeshPanel.should_be_drawn(context):
            MeshPanel.draw(self.layout, context)
        elif armature_ui.should_be_drawn(context):
            armature_ui.draw(self.layout, context)
