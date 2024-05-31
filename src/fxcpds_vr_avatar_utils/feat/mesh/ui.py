from bpy.types import UILayout

from ...properties.scene import FxSceneProps
from ...utils.aliases import Context
from ...utils import context as C


def draw(layout: UILayout, context: Context) -> None:
    if (key := C.current_key(context)) is None or (count := len(key.key_blocks)) == 0:
        layout.label(text='Target object must have one or more shape keys to enable utilities.')
        return

    global_options = layout.box().column()
    global_options.label('Global Options', icon='WORLD')
    FxSceneProps.draw_dry_run(context.scene, layout)

