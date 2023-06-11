import numpy as np

from scipy import integrate


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

    @staticmethod
    def yp_t_y(t: float, y: float) -> float:
        """
        - expression for a differential equation y'=f(t,y), where y=y(t)
        """
        yp = y-np.power(t, 2)+1
        return yp


class Diffs:
    """
    - A class that contains different implementation for numerical differentiation
    """
    N_INTERVALS = 5

    @staticmethod
    def runge_kutta_4(func: "Functions", alpha: float, interval: tuple) -> "list[float]":
        """
        - numerical implementation for the Runge-Kutta method of order 4
        - requires an initial value for the function `func` at x=x_0, here denoted by `alpha`
        - the interval starts at x_0=a and ends at x_n=b
        """
        debug = False

        a, b = interval

        if debug:
            print(
                f'Evaluating the numerical derivative of < {func} > between a={a} and b={b}')

        x_data = np.linspace(a, b, Diffs.N_INTERVALS)
        step = x_data[1]-x_data[0]
        if debug:
            print(f'Using a step size h={step}')

        t_values = []
        w_values = []

        for idx in range(len(x_data)):
            if idx == 0:
                t_0 = x_data[0]
                w_0 = alpha
                t_values.append(t_0)
                w_values.append(w_0)
            else:
                t_i = x_data[idx]
                k_1 = step*func(t_values[idx-1], w_values[idx-1])
                k_2 = step*func(t_values[idx-1]+step/2, w_values[idx-1]+k_1/2)
                k_3 = step*func(t_values[idx-1]+step/2, w_values[idx-1]+k_2/2)
                k_4 = step*func(t_values[idx-1]+step, w_values[idx-1]+k_3)
                w_i = w_values[idx-1]+(k_1 + 2*k_2 + 2*k_3 + k_4) / 6
                t_values.append(t_i)
                w_values.append(w_i)

        return w_values


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

    @staticmethod
    def scipy_quad(func: "Functions", interval: tuple) -> "tuple(list, list, list)":
        """
        - uses the scipy quad method to evaluate the function and its numerical integral
        - returns a tuple of lists, with the data points x, f(x) and int(f(x))
        - uses by default 100 intervals for evaluation
        """

        debug = False

        a, b = interval
        n_points = 100
        step = np.abs((b-a)/n_points)
        x_data = np.linspace(a, b, n_points)
        y_data = [func(x) for x in x_data]

        int_data = []

        for x in x_data:
            int_f_x = integrate.quad(func, a, x)
            int_data.append(int_f_x[0])

        if (debug):
            print(
                f'Generated {len(x_data)} points for evaluation. x_0={x_data[0]}, x_1={x_data[1]}, ...')
            print(f'Generated the numerical values for < {func} > f(x)')
            print(
                f'Generated the set of numerical values for the integral: {len(int_data)}')

        return x_data, y_data, int_data
