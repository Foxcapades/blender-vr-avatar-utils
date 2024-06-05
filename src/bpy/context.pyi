import typing

from . import types


AnyContext = typing.Union[
    'GlobalContext',
    'ButtonsContext',
    'ClipContext',
    'FileContext',
    'ImageContext',
    'NodeContext',
    'ScreenContext',
    'SequencerContext',
    'TextContext',
    'View3DContext',
]


# noinspection PyPropertyDefinition
class GlobalContext(types.Context):
    pass


# noinspection PyPropertyDefinition
class ButtonsContext(GlobalContext):
    @property
    def texture_slot(self) -> types.TextureSlot: pass
    @property
    def world(self) -> types.World: pass
    @property
    def object(self) -> types.Object: pass
    @property
    def mesh(self) -> types.Mesh: pass
    @property
    def armature(self) -> types.Armature: pass
    @property
    def lattice(self) -> types.Lattice: pass
    @property
    def curve(self) -> types.Curve: pass
    @property
    def meta_ball(self) -> types.MetaBall: pass
    @property
    def light(self) -> types.Light: pass
    @property
    def speaker(self) -> types.Speaker: pass
    @property
    def lightprobe(self) -> types.LightProbe: pass
    @property
    def camera(self) -> types.Camera: pass
    @property
    def material(self) -> types.Material: pass
    @property
    def material_slot(self) -> types.MaterialSlot: pass
    @property
    def texture(self) -> types.Texture: pass
    @property
    def texture_user(self) -> types.ID: pass
    @property
    def texture_user_property(self) -> types.Property: pass
    @property
    def texture_node(self) -> types.Node: pass
    @property
    def bone(self) -> types.Bone: pass
    @property
    def edit_bone(self) -> types.EditBone: pass
    @property
    def pose_bone(self) -> types.PoseBone: pass
    @property
    def particle_system(self) -> types.ParticleSystem: pass
    @property
    def particle_system_editable(self) -> types.ParticleSystem: pass
    @property
    def particle_settings(self) -> types.ParticleSettings: pass
    @property
    def cloth(self) -> types.ClothModifier: pass
    @property
    def soft_body(self) -> types.SoftBodyModifier: pass
    @property
    def fluid(self) -> types.FluidSimulationModifier: pass
    @property
    def collision(self) -> types.CollisionModifier: pass
    @property
    def brush(self) -> types.Brush: pass
    @property
    def dynamic_paint(self) -> types.DynamicPaintModifier: pass
    @property
    def line_style(self) -> types.FreestyleLineStyle: pass
    @property
    def gpencil(self) -> types.GreasePencil: pass
    # TODO: what is "Hair Curves"???
    @property
    def curves(self) -> typing.Any: pass  # -> Hair Curves
    @property
    def volume(self) -> types.Volume: pass


# noinspection PyPropertyDefinition
class ClipContext(GlobalContext):
    @property
    def edit_movieclip(self) -> types.MovieClip: pass
    @property
    def edit_mask(self) -> types.Mask: pass


# noinspection PyPropertyDefinition
class FileContext(GlobalContext):
    @property
    def active_file(self) -> types.FileSelectEntry: pass

    @property
    def selected_files(self) -> types.FileSelectEntry: pass

    @property
    def asset_library_reference(self) -> types.AssetLibraryReference: pass

    @property
    def selected_assets(self) -> types.AssetRepresentation: pass

    @property
    def id(self) -> types.ID: pass

    @property
    def selected_ids(self) -> types.ID: pass


# noinspection PyPropertyDefinition
class ImageContext(GlobalContext):
    @property
    def edit_image(self) -> types.Image: pass

    @property
    def edit_mask(self) -> types.Mask: pass


# noinspection PyPropertyDefinition
class NodeContext(GlobalContext):
    @property
    def selected_nodes(self) -> types.Node: pass

    @property
    def active_node(self) -> types.Node: pass

    @property
    def light(self) -> types.Light: pass

    @property
    def material(self) -> types.Material: pass

    @property
    def world(self) -> types.World: pass


# noinspection PyPropertyDefinition
class ScreenContext(GlobalContext):
    @property
    def visible_objects(self) -> types.Object: pass

    @property
    def selectable_objects(self) -> types.Object: pass

    @property
    def selected_objects(self) -> types.Object: pass

    @property
    def editable_objects(self) -> types.Object: pass

    @property
    def selected_editable_objects(self) -> types.Object: pass

    @property
    def objects_in_mode(self) -> types.Object: pass

    @property
    def objects_in_mode_unique_data(self) -> types.Object: pass

    @property
    def visible_bones(self) -> types.EditBone: pass

    @property
    def editable_bones(self) -> types.EditBone: pass

    @property
    def selected_bones(self) -> types.EditBone: pass

    @property
    def selected_editable_bones(self) -> types.EditBone: pass

    @property
    def visible_pose_bones(self) -> types.PoseBone: pass

    @property
    def selected_pose_bones(self) -> types.PoseBone: pass

    @property
    def selected_pose_bones_from_active_object(self) -> types.PoseBone: pass

    @property
    def active_bone(self) -> types.EditBone: pass

    @property
    def active_pose_bone(self) -> types.PoseBone: pass

    @property
    def active_object(self) -> types.Object: pass

    @property
    def object(self) -> types.Object: pass

    @property
    def edit_object(self) -> types.Object: pass

    @property
    def sculpt_object(self) -> types.Object: pass

    @property
    def vertex_paint_object(self) -> types.Object: pass

    @property
    def weight_paint_object(self) -> types.Object: pass

    @property
    def image_paint_object(self) -> types.Object: pass

    @property
    def particle_edit_object(self) -> types.Object: pass

    @property
    def pose_object(self) -> types.Object: pass

    @property
    def active_sequence_strip(self) -> types.Sequence: pass

    @property
    def sequences(self) -> types.Sequence: pass

    @property
    def selected_sequences(self) -> types.Sequence: pass

    @property
    def selected_editable_sequences(self) -> types.Sequence: pass

    @property
    def active_nla_track(self) -> types.NlaTrack: pass

    @property
    def active_nla_strip(self) -> types.NlaStrip: pass

    @property
    def selected_nla_strips(self) -> types.NlaStrip: pass

    @property
    def selected_movieclip_tracks(self) -> types.MovieTrackingTrack: pass

    @property
    def gpencil_data(self) -> types.GreasePencil: pass

    @property
    def gpencil_data_owner(self) -> types.ID: pass

    @property
    def annotation_data(self) -> types.GreasePencil: pass

    @property
    def annotation_data_owner(self) -> types.ID: pass

    @property
    def visible_gpencil_layers(self) -> types.GPencilLayer: pass

    @property
    def editable_gpencil_layers(self) -> types.GPencilLayer: pass

    @property
    def editable_gpencil_strokes(self) -> types.GPencilStroke: pass

    @property
    def active_gpencil_layer(self) -> types.GPencilLayer: pass

    @property
    def active_gpencil_frame(self) -> types.GreasePencilLayer: pass

    @property
    def active_annotation_layer(self) -> types.GPencilLayer: pass

    @property
    def active_operator(self) -> types.Operator: pass

    @property
    def active_action(self) -> types.Action: pass

    @property
    def selected_visible_actions(self) -> types.Action: pass

    @property
    def selected_editable_actions(self) -> types.Action: pass

    @property
    def visible_fcurves(self) -> types.FCurve: pass

    @property
    def editable_fcurves(self) -> types.FCurve: pass

    @property
    def selected_visible_fcurves(self) -> types.FCurve: pass

    @property
    def selected_editable_fcurves(self) -> types.FCurve: pass

    @property
    def active_editable_fcurve(self) -> types.FCurve: pass

    @property
    def selected_editable_keyframes(self) -> types.Keyframe: pass

    @property
    def ui_list(self) -> types.UIList: pass

    @property
    def asset_library_reference(self) -> types.AssetLibraryReference: pass

    @property
    def property(self) -> types.AnyType | str | int: pass


# noinspection PyPropertyDefinition
class SequencerContext(GlobalContext):
    @property
    def edit_mask(self) -> types.Mask: pass


# noinspection PyPropertyDefinition
class TextContext(GlobalContext):
    @property
    def edit_text(self) -> types.Text: pass


# noinspection PyPropertyDefinition
class View3DContext(GlobalContext):
    @property
    def active_object(self) -> types.Object: pass

    @property
    def selected_ids(self) -> typing.Sequence[types.ID]: pass
