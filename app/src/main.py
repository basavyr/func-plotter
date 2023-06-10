import maths


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

    n_func = [func(x) for x in x_data]
    print(
        f'Generated {len(n_func)} numerical values for the function < {func} >')


def main():
    """
    - The main workflow of the application
    """
    func_evolution(maths.Functions.special_sin, (0, 10))


if __name__ == "__main__":
    print("App is running...")
    main()
