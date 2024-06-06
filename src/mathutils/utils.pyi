import typing

FloatTuple2 = typing.Tuple[float, float]
FloatTuple3 = typing.Tuple[float, float, float]
FloatTuple4 = typing.Tuple[float, float, float, float]

Matrix2 = typing.Tuple[FloatTuple2, FloatTuple2]
Matrix3 = typing.Tuple[FloatTuple3, FloatTuple3, FloatTuple3]
Matrix4 = typing.Tuple[FloatTuple4, FloatTuple4, FloatTuple4, FloatTuple4]

RotationOrder = typing.Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']

Axis = typing.Literal['X', 'Y', 'Z']

Plane = typing.Literal['X', 'Y', 'Z', 'XY', 'XZ', 'YZ']


class Color:
    """
    This object gives access to Colors in Blender.

    Most colors returned by Blender APIs are in scene linear color space, as
    defined by the OpenColorIO configuration. The notable exception is user
    interface theming colors, which are in sRGB color space.

    Attributes:
        r: Red color channel.
        g: Green color channel.
        b: Blue color channel.

        h: HSV Hue component in [0, 1].
        s: HSV Saturation component in [0, 1].
        v: HSV Value component in [0, 1].

        hsv: HSV Values in [0, 1].
    """
    r: float
    g: float
    b: float

    h: float
    s: float
    v: float

    hsv: FloatTuple3

    def __init__(self, rgb: FloatTuple3 = (0.0, 0.0, 0.0)): pass

    @property
    def owner(self) -> typing.Any | None:
        """The item this is wrapping or None."""
        pass

    @property
    def is_frozen(self) -> bool:
        """True when this object has been frozen."""
        pass

    @property
    def is_valid(self) -> bool:
        """True when the owner of this data is valid."""
        pass

    @property
    def is_wrapped(self) -> bool:
        """True when this object wraps external data."""
        pass

    def copy(self) -> Color:
        """
        Returns a copy of this color.

        Returns:
            A copy of the color.
        """
        pass

    def freeze(self) -> Color:
        """
        Make this object immutable.

        After this the object can be hashed, used in dictionaries & sets.

        Returns:
            An instance of this object.
        """
        pass

    def from_aces_to_scene_linear(self) -> Color:
        """
        Convert from ACES2065-1 linear to scene linear color space.

        Returns:
            A color in scene linear color space.
        """
        pass

    def from_rec709_linear_to_scene_linear(self) -> Color:
        """
        Convert from Rec.709 linear color space to scene linear color space.

        Returns:
            A color in scene linear color space.
        """
        pass

    def from_scene_linear_to_aces(self) -> Color:
        """
        Convert from scene linear to ACES2065-1 linear color space.

        Returns:
            A color in ACES2065-1 linear color space.
        """
        pass

    def from_scene_linear_to_rec709_linear(self) -> Color:
        """
        Convert from scene linear to Rec.709 linear color space.

        Returns:
            A color in Rec.709 linear color space.
        """
        pass

    def from_scene_linear_to_srgb(self) -> Color:
        """
        Convert from scene linear to sRGB color space.

        Returns:
            A color in sRGB color space.
        """
        pass

    def from_scene_linear_to_xyz_d65(self) -> Color:
        """
        Convert from scene linear to CIE XYZ (Illuminant D65) color space.

        Returns:
            A color in XYZ color space.
        """
        pass

    def from_srgb_to_scene_linear(self) -> Color:
        """
        Convert from sRGB to scene linear color space.

        Returns:
            A color in scene linear color space.
        """
        pass

    def from_xyz_d65_to_scene_linear(self) -> Color:
        """
        Convert from CIE XYZ (Illuminant D65) to scene linear color space.

        Returns:
            A color in scene linear color space.
        """
        pass


# noinspection PyPep8Naming
class Vector:
    is_frozen: bool
    is_valid: bool
    is_wrapped: bool
    length: float
    length_squared: float
    magnitude: float
    owner: typing.Any
    w: float
    x: float
    y: float
    z: float

    def __init__(self, seq: FloatTuple2 | FloatTuple3 | FloatTuple4 = (0.0, 0.0, 0.0)): pass

    def angle(self, other: 'Vector', fallback: 'Vector' = None) -> float: pass

    def angle_signed(self, other: 'Vector', fallback: 'Vector') -> float: pass

    def copy(self) -> 'Vector': pass

    def cross(self, other: 'Vector') -> 'Vector': pass

    def dot(self, other: 'Vector') -> float: pass

    def freeze(self) -> 'Vector': pass

    def lerp(self, other: 'Vector', factor: float) -> 'Vector': pass

    def negate(self) -> None: pass

    def normalze(self) -> None: pass

    def normalized(self) -> 'Vector': pass

    def orthogonal(self) -> 'Vector': pass

    def project(self, other: 'Vector') -> 'Vector': pass

    def reflect(self, mirror: 'Vector') -> 'Vector': pass

    def resize(self, size: int = 3) -> None: pass

    def resize_2d(self) -> None: pass

    def resize_3d(self) -> None: pass

    def resize_4d(self) -> None: pass

    def resized(self, size: int = 3) -> 'Vector': pass

    def rotate(self, other: 'Euler | Quaternion | Matrix') -> None: pass

    def rotation_difference(self, other: 'Vector') -> 'Quaternion': pass

    def slerp(self, other: 'Vector', factor: float, fallback: 'Vector' = None) -> 'Vector': pass

    def to_2d(self) -> 'Vector': pass

    def to_3d(self) -> 'Vector': pass

    def to_4d(self) -> 'Vector': pass

    def to_track_quat(self, track: typing.Literal['X', 'Y', 'Z', '-X', '-Y', '-Z'], up: Axis) -> 'Quaternion': pass

    def to_tuple(self, precision: int = -1) -> FloatTuple2 | FloatTuple3 | FloatTuple4: pass

    def zero(self) -> None: pass

    @classmethod
    def Fill(cls, size: int, fill: float = 0.0) -> 'Vector': pass

    @classmethod
    def Linspace(cls, start: int, stop: int, size: int) -> 'Vector': pass

    @classmethod
    def Range(cls, start: int, stop: int, step: int = 1) -> 'Vector': pass

    @classmethod
    def Repeat(cls, vector: 'Vector', size: int) -> 'Vector': pass

class Euler:
    """
    This object gives access to Eulers in Blender.

    Attributes:
        order: Euler rotation order.

        x: Euler axis angle in radians.
        y: Euler axis angle in radians.
        z: Euler axis angle in radians.
    """

    order: RotationOrder

    x: float
    y: float
    z: float

    def __init__(self, angles: Vector, order: RotationOrder = 'XYZ'):
        """
        Args:
            angles: Three angles, in radians
            order: Optional order of the angles, a permutation of `XYZ`.
        """
        pass

    @property
    def owner(self) -> typing.Any | None:
        """The item this is wrapping or None (read-only)."""
        pass

    @property
    def is_frozen(self) -> bool:
        """True when this object has been frozen."""
        pass

    @property
    def is_valid(self) -> bool:
        """True when the owner of this data is valid."""
        pass

    @property
    def is_wrapped(self) -> bool:
        """True when this object wraps external data."""
        pass

    def copy(self) -> Euler:
        """
        Returns a copy of this euler.

        Returns:
            A copy of the euler.
        """
        pass

    def freeze(self) -> Euler:
        """
        Make this object immutable.

        After this the object can be hashed, used in dictionaries & sets.

        Returns:
            An instance of this object.
        """
        pass

    def make_compatible(self, other: Euler) -> None:
        """
        Make this euler compatible with another, so interpolating between them
        works as intended.

        The rotation order is not taken into account for this function.

        Args:
            other:
        """
        pass

    def rotate(self, other: Euler | Quaternion | Matrix) -> None:
        """
        Rotates the euler by another mathutils value.

        Args:
            other: Rotation component of mathutils value.
        """
        pass

    def rotate_axis(self, axis: Axis, angle: float) -> None:
        """
        Rotates the euler a certain amount and returning a unique euler rotation
        (no 720 degree pitches).

        Args:
            axis: Single character in ['X', 'Y', 'Z'].
            angle: Angle in radians.
        """
        pass

    def to_matrix(self) -> Matrix:
        """
        Return a matrix representation of the euler.

        Returns:
            A 3x3 rotation matrix representation of the euler.
        """
        pass

    def to_quaternion(self) -> Quaternion:
        """
        Return a quaternion representation of the euler.

        Returns:
            Quaternion representation of the euler.
        """
        pass

    def zero(self) -> None:
        """Set all values to zero."""
        pass

# noinspection PyPep8Naming
class Quaternion:
    angle: float
    axis: Vector
    is_frozen: bool
    is_valid: bool
    is_wrapped: bool
    magnitude: float
    owner: typing.Any | None
    w: float
    x: float
    y: float
    z: float

    def __init__(self, seq: FloatTuple3 | FloatTuple4 = None, angle: float = None): pass

    def conjugate(self) -> None: pass

    def conjugated(self) -> 'Quaternion': pass

    def copy(self) -> 'Quaternion': pass

    def cross(self, other: 'Quaternion') -> 'Quaternion': pass

    def dot(self, other: 'Quaternion') -> float: pass

    def freeze(self) -> 'Quaternion': pass

    def identity(self) -> None: pass

    def invert(self) -> None: pass

    def inverted(self) -> 'Quaternion': pass

    def make_compatible(self, other: 'Quaternion') -> None: pass

    def negate(self) -> None: pass

    def normalize(self) -> None: pass

    def normalized(self) -> 'Quaternion': pass

    def rotate(self, other: Euler | 'Quaternion' | 'Matrix') -> None: pass

    def rotation_difference(self, other: 'Quaternion') -> 'Quaternion': pass

    def slerp(self, other: 'Quaternion', factor: float) -> 'Quaternion': pass

    def to_axis_angle(self) -> tuple[Vector, float]: pass

    def to_euler(self, order: RotationOrder = None, euler_compat: Euler = None) -> Euler: pass

    def to_exponential_map(self) -> Vector: pass

    def to_matrix(self) -> 'Matrix': pass

    def to_swing_twist(self, axis: Axis) -> 'Quaternion': pass

# noinspection PyPep8Naming
class Matrix(typing.Protocol):
    col: typing.Any  # TODO: what the heck is "Matrix Access"?
    is_frozen: bool
    is_identity: bool
    is_negative: bool
    is_orthogonal: bool
    is_orthogonal_axis_vectors: bool
    is_valid: bool
    is_wrapped: bool
    median_scale: float
    owner: typing.Any
    row: typing.Any  # TODO: what the heck is "Matrix Access"?
    translation: Vector

    def __init__(
        self,
        rows: Matrix2 | Matrix3 | Matrix4 = (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    ) -> None: pass

    def adjugate(self): pass

    def adjugated(self) -> 'Matrix': pass

    def copy(self) -> 'Matrix': pass

    def decompose(self) -> tuple[Vector, Quaternion, Vector]: pass

    def determinant(self) -> float: pass

    def freeze(self) -> 'Matrix': pass

    def identity(self) -> None:
        """Set the matrix to the identity matrix."""

    def invert(self, fallback: 'Matrix' = None) -> None:
        """Set the matrix to its inverse."""

    def invert_safe(self) -> None:
        """
        Set the matrix to its inverse, will never error.

        If degenerated (e.g. zero scale on an axis), add some epsilon to its
        diagonal, to get an invertible one. If tweaked matrix is still
        degenerated, set to the identity matrix instead.
        """

    def inverted(self, fallback: 'Matrix' = None) -> 'Matrix':
        """
        Return an inverted copy of the matrix.

        Args:
            fallback: Return this when the inverse can’t be calculated (instead
                of raising a ValueError

        Returns:
            The inverted matrix or fallback when given.
        """

    def inverted_safe(self) -> 'Matrix': pass

    def lerp(self, other: 'Matrix', factor: float) -> 'Matrix': pass

    def normalize(self) -> None: pass

    def normalized(self) -> 'Matrix': pass

    def resize_4x4(self) -> None: pass

    def rotate(self, other: Euler | Quaternion | 'Matrix') -> None: pass

    def to_2x2(self) -> 'Matrix': pass

    def to_3x3(self) -> 'Matrix': pass

    def to_4x4(self) -> 'Matrix': pass

    def to_euler(self, order: RotationOrder, euler_compat: Euler = None) -> Euler: pass

    def to_quaternion(self) -> Quaternion: pass

    def to_scale(self) -> Vector: pass

    def to_translation(self) -> Vector: pass

    def transpose(self) -> None: pass

    def transposed(self) -> 'Matrix': pass

    def zero(self) -> None: pass

    @classmethod
    def Diagonal(cls, vector: Vector) -> 'Matrix': pass

    @classmethod
    def Identity(cls, size: typing.Literal[2, 4]) -> 'Matrix': pass

    @classmethod
    def LocRotScale(
        cls,
        location: Vector | None, rotation: 'Matrix' | Quaternion | Euler | None,
        scale: Vector | None,
    ) -> 'Matrix': pass

    @classmethod
    def OrthoProjection(cls, angle: float, size: typing.Literal[2, 4], axis: Axis | Vector = None) -> 'Matrix': pass

    @classmethod
    def Rotation(cls, angle: float, size: typing.Literal[2, 4], axis: Axis | Vector = None) -> 'Matrix': pass

    @classmethod
    def Scale(cls, factor: float, size: typing.Literal[2, 4], axis: Vector = None) -> 'Matrix': pass

    @classmethod
    def Shear(cls, plane: Plane, size: typing.Literal[2, 4], factor: float | tuple[float, float]) -> 'Matrix': pass

    @classmethod
    def Translation(cls, vector: Vector) -> 'Matrix': pass
