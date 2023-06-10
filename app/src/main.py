import maths
import plotter


def func_evolution(func: maths.Functions, interval: tuple):
    """
    returns the numerical values for a function evaluated over an interval
    """
    N_POINTS = 100
    a, b = interval
    step = maths.np.abs((b-a)/N_POINTS)
    print(f'Fixing the step size to: {step}')

    x_data = maths.np.arange(a, b, step)
    print(
        f'Created the data set for the x-values; {x_data[0]}, {x_data[1]}, ...')

    y_data = [func(x) for x in x_data]
    print(
        f'Generated {len(y_data)} numerical values for the function < {func} >')

    plotter.plot_data(x_data, y_data)


def main():
    """
    - The main workflow of the application
    """
    # func_evolution(maths.Functions.special_sin, (0, 10))
    int_13 = maths.Integration.simpson_13(maths.Functions.e_x, (0, 1))
    int_38 = maths.Integration.simpson_38(maths.Functions.e_x, (0, 1))
    int_trapezoidal = maths.Integration.trapezoidal(
        maths.Functions.e_x, (0, 1))
    print(int_13)
    print(int_38)
    print(int_trapezoidal)


if __name__ == "__main__":
    print("App is running...")
    main()
