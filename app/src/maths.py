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


class Functions:
    @staticmethod
    def special_sin(x: float) -> float:
        """
        - a special mathematical function that uses the built-in math tools from the current module
        """
        func = squared(x)*sin_k_x(x, 3)
        return func

    @staticmethod
    def e_x(x: float) -> float:
        """
        - returns the exponential function for a given argument
        """
        exp = np.exp(x)
        return exp


class Integration:

    N_INTERVALS = 100

    @staticmethod
    def simpson_13(func: 'Functions', interval: tuple) -> float:
        """
        - uses Simpson's 1/3 rule to determine the numerical integral of a function
        """
        a, b = interval
        step = np.abs((b-a)/Integration.N_INTERVALS)

        half_range = int(
            Integration.N_INTERVALS / 2) if Integration.N_INTERVALS % 2 == 0 else int((Integration.N_INTERVALS+1)/2)

        f_a = func(a)
        f_b = func(b)

        sum1 = 0
        for i in range(1, half_range+1):
            x_i = a+(2*i-1)*step
            sum1 += func(x_i)

        sum2 = 0
        for i in range(1, half_range):
            x_i = a+(2*i)*step
            sum2 += func(x_i)

        simpson_term = f_a+4*sum1+2*sum2+f_b

        return simpson_term*step/3.0

    @staticmethod
    def simpson_38(func: 'Functions', interval: tuple) -> float:
        """
        - uses Simpson's 3/8 rule to determine the numerical integral of a function
        """

        a, b = interval

        # make sure the number of evaluation intervals is a multiple of 3
        n_intervals_3 = 3*Integration.N_INTERVALS

        step = np.abs((b-a)/n_intervals_3)

        third_range = int(n_intervals_3/3)

        sum1 = 0
        for i in range(1, third_range+1):
            x_i = a+(3*i-3)*step
            sum1 += func(x_i)

        sum2 = 0
        for i in range(1, third_range+1):
            x_i = a+(3*i-2)*step
            sum2 += func(x_i)

        sum3 = 0
        for i in range(1, third_range+1):
            x_i = a+(3*i-1)*step
            sum3 += func(x_i)

        sum4 = 0
        for i in range(1, third_range+1):
            x_i = a+(3*i)*step
            sum4 += func(x_i)

        simpson_term = sum1+3*sum2+3*sum3+sum4

        return simpson_term*3*step/8

    @staticmethod
    def trapezoidal(func: 'Functions', interval: tuple) -> float:
        """
        - uses the trapezoidal method to integrate a function over a given interval
        """
        a, b = interval

        step = np.abs((b-a)/Integration.N_INTERVALS)

        f_a = func(a)
        f_b = func(b)

        sum_i = 0
        for i in range(1, Integration.N_INTERVALS):
            x_i = a+step*i
            f_x = func(x_i)
            sum_i += f_x

        trapezoidal_term = f_a+2*sum_i+f_b

        return trapezoidal_term*step/2
