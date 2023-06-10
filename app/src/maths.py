import numpy as np

PI = np.pi


def deg_to_rad(x_deg: float) -> float:
    """
    - returns the value of the argument as radians (from degrees)
    """
    x_rad = x_deg*PI/180.0
    return x_rad


def squared(x: float) -> float:
    """
    - returns the argument raised to the power 2, using numpy
    """
    x_squared = np.power(x, 2)
    return x_squared


def sin_k_x(x: float, k: int) -> float:
    """
    - returns the trigonometric `sin` function applied for the argument `x`, raised to the `k` exponent
    """
    arg = np.power(np.sin(x), k)
    return arg
