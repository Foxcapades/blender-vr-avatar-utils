from typing import Literal

from .base import bpy_struct

from .a import AOV, AOVs
from .c import CyclesRenderLayerSettings
from .d import Depsgraph
from .f import FreestyleSettings
from .l import LayerCollection, LayerObjects, Lightgroup, Lightgroups
from .m import Material


VelocityUnit = Literal['SECOND', 'FRAME']


# noinspection PyPropertyDefinition
class ViewLayer(bpy_struct):  # NEW REGEX
    active_aov_index: int
    active_layer_collection: LayerCollection
    active_lightgroup_index: int
    material_override: Material
    name: str
    pass_alpha_threshold: float
    pass_cryptomatte_depth: int
    samples: int
    use: bool
    use_ao: bool
    use_freestyle: bool
    use_motion_blur: bool
    use_pass_ambient_occlusion: bool
    use_pass_combined: bool
    use_pass_cryptomatte_accurate: bool
    use_pass_cryptomatte_asset: bool
    use_pass_cryptomatte_material: bool
    use_pass_cryptomatte_object: bool
    use_pass_diffuse_color: bool
    use_pass_diffuse_direct: bool
    use_pass_diffuse_indirect: bool
    use_pass_emit: bool
    use_pass_environment: bool
    use_pass_glossy_color: bool
    use_pass_glossy_direct: bool
    use_pass_glossy_indirect: bool
    use_pass_material_index: bool
    use_pass_mist: bool
    use_pass_normal: bool
    use_pass_object_index: bool
    use_pass_position: bool
    use_pass_shadow: bool
    use_pass_subsurface_color: bool
    use_pass_subsurface_direct: bool
    use_pass_subsurface_indirect: bool
    use_pass_transmission_color: bool
    use_pass_transmission_direct: bool
    use_pass_transmission_indirect: bool
    use_pass_uv: bool
    use_pass_vector: bool
    use_pass_z: bool
    use_sky: bool
    use_solid: bool
    use_strand: bool
    use_volumes: bool

    @property
    def active_aov(self) -> AOV: pass

    @property
    def active_lightgroup(self) -> Lightgroup: pass

    @property
    def aovs(self) -> AOVs: pass

    @property
    def cycles(self) -> CyclesRenderLayerSettings: pass

    @property
    def depsgraph(self) -> Depsgraph: pass

    @property
    def eevee(self) -> 'ViewLayerEEVEE': pass

    @property
    def freestyle_settings(self) -> FreestyleSettings: pass

    @property
    def layer_collection(self) -> LayerCollection: pass

    @property
    def lightgroups(self) -> Lightgroups: pass

    @property
    def objects(self) -> LayerObjects: pass

    @classmethod
    def update_render_passes(cls): pass

    def update(self): pass


class ViewLayerEEVEE(bpy_struct):
    use_pass_bloom: bool
    use_pass_transparent: bool
    use_pass_volume_direct: bool
