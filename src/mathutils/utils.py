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


class Color(typing.Protocol):
    def __init__(self, rgb: FloatTuple3 = (0.0, 0.0, 0.0)):
        self._rgb = rgb
        self.r: float
        self.g: float
        self.b: float
        self.h: float
        self.s: float
        self.v: float
        self.hsv: FloatTuple3
        self.is_frozen: bool
        self.is_valid: bool
        self.is_wrapped: bool
        self.owner: typing.Any

    def copy(self) -> Color: pass

    def freeze(self) -> Color: pass

    def from_aces_to_scene_linear(self) -> Color: pass

    def from_rec709_linear_to_scene_linear(self) -> Color: pass

    def from_scene_linear_to_aces(self) -> Color: pass

    def from_scene_linear_to_rec709_linear(self) -> Color: pass

    def from_scene_linear_to_srgb(self) -> Color: pass

    def from_scene_linear_to_xyz_d65(self) -> Color: pass

    def from_srgb_to_scene_linear(self) -> Color: pass

    def from_xyz_d65_to_scene_linear(self) -> Color: pass


# noinspection PyPep8Naming
class Vector(typing.Protocol):
    def __init__(self, seq: FloatTuple2 | FloatTuple3 | FloatTuple4 = (0.0, 0.0, 0.0)):
        self._seq = seq
        self.is_frozen: bool
        self.is_valid: bool
        self.is_wrapped: bool
        self.length: float
        self.length_squared: float
        self.magnitude: float
        self.owner: typing.Any
        self.w: float
        self.x: float
        self.y: float
        self.z: float

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


class Euler(typing.Protocol):
    def __init__(self, angles: Vector, order: RotationOrder = 'XYZ'):
        self._angles = angles
        self.order = order
        self.is_frozen: bool
        self.is_valid: bool
        self.is_wrapped: bool
        self.owner: typing.Any
        self.x: float
        self.y: float
        self.z: float

    def copy(self) -> 'Euler': pass

    def freeze(self) -> 'Euler': pass

    def make_compatible(self, other: 'Euler') -> None: pass

    def rotate(self, other: 'Euler | Quaternion | Matrix') -> None: pass

    def rotate_axis(self, axis: Axis, angle: float) -> None: pass

    def to_matrix(self) -> 'Matrix': pass

    def to_quaternion(self) -> 'Quaternion': pass

    def zero(self) -> None: pass


# noinspection PyPep8Naming
class Quaternion(typing.Protocol):
    def __init__(self, seq: FloatTuple3 | FloatTuple4 = None, angle: float = None):
        self._seq = seq
        self.angle = angle
        self.axis: Vector
        self.is_frozen: bool
        self.is_valid: bool
        self.is_wrapped: bool
        self.magnitude: float
        self.owner: typing.Any | None
        self.w: float
        self.x: float
        self.y: float
        self.z: float

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
    def __init__(
        self,
        rows: Matrix2 | Matrix3 | Matrix4 = (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    ):
        self._rows = rows
        self.col: typing.Any  # TODO: what the heck is "Matrix Access"?
        self.is_frozen: bool
        self.is_identity: bool
        self.is_negative: bool
        self.is_orthogonal: bool
        self.is_orthogonal_axis_vectors: bool
        self.is_valid: bool
        self.is_wrapped: bool
        self.median_scale: float
        self.owner: typing.Any
        self.row: typing.Any  # TODO: what the heck is "Matrix Access"?
        self.translation: Vector

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
