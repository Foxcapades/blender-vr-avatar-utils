from typing import Literal


NodeFilter = Literal['SOFTEN', 'SHARPEN', 'SHARPEN_DIAMOND', 'LAPLACE', 'SOBEL', 'PREWITT', 'KIRSCH', 'SHADOW']

NodeMath = Literal[
    'ADD',
    'SUBTRACT',
    'MULTIPLY',
    'DIVIDE',
    'MULTIPLY_ADD',
    'POWER',
    'LOGARITHM',
    'SQRT',
    'INVERSE_SQRT',
    'ABSOLUTE',
    'EXPONENT',
    'MINIMUM',
    'MAXIMUM',
    'LESS_THAN',
    'GREATER_THAN',
    'SIGN',
    'COMPARE',
    'SMOOTH_MIN',
    'SMOOTH_MAX',
    'ROUND',
    'FLOOR',
    'CEIL',
    'TRUNC',
    'FRACT',
    'MODULO',
    'FLOORED_MODULO',
    'WRAP',
    'SNAP',
    'PINGPONG',
    'SINE',
    'COSINE',
    'TANGENT',
    'ARCSINE',
    'ARCCOSINE',
    'ARCTANGENT',
    'ARCTAN2',
    'SINH',
    'COSH',
    'TANH',
    'RADIANS',
    'DEGREES',
]

NormalSwizzle = Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']

NormalSpace = Literal['OBJECT', 'TANGENT']
