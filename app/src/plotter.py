from matplotlib import pyplot as plt
import os
import uuid
import maths

DATA_DIR = os.path.join("../", "data")
os.makedirs(DATA_DIR, exist_ok=True)


def plot_data(x_data: "list[float]", y_data: "list[float]") -> None:
    """
    - Create a plot for a given data set containing the x values and the y=f(x) values as separated lists
    - Uses the UUID python module to generate file names
    """
    plot_name = f'plot_{str(uuid.uuid4())[2:6]}.pdf'
    plt.plot(x_data, y_data, '-r', label='f(x)')
    x_data_2 = [x_data[i] for i in range(0, len(x_data)) if i % 5 == 0]
    y_data_2 = [y_data[i] for i in range(0, len(y_data)) if i % 5 == 0]
    plt.plot(x_data_2, y_data_2, 'ok')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.savefig(os.path.join(DATA_DIR, plot_name),
                bbox_inches='tight', dpi=300)
    plt.close()


def plot_func_integral(func: "maths.Functions", interval: tuple, precision: int):
    """
    - uses the maths package to plot a function and its integral over a specific interval
    - use a fixed number of points that will be used for plotting via `precision`
    """
    plot_name = os.path.join(
        DATA_DIR, f'f_vs_intf_{str(uuid.uuid4())[2:6]}.pdf')
    a, b = interval

    print(
        f'Plotting the function < {func} > and its integral over the interval [{a}, {b}]')

    x_data = maths.np.linspace(a, b, precision)

    y_data = [func(x) for x in x_data]

    int_data = [maths.integrate.quad(func, 0, x)[0] for x in x_data]

    plt.plot(x_data, y_data, '-b', label='f(x)')
    plt.plot(x_data, int_data, '-r', label=r'$\int f(x)dx$')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.savefig(plot_name, dpi=300, bbox_inches='tight')
    plt.close()


def plot_tuple(input_tuple: "tuple(list,list,list)") -> None:
    """
    - create a graphical representation from a tuple of three lists
    - first list is the set of x values, second list is the numerical values for f(x), and third list is the numerical integral of the function
    """
    plot_name = os.path.join(
        DATA_DIR, f'integration_plot_{str(uuid.uuid4())[2:7]}.pdf')
    # unpack the input tuple for proper plotting
    x_data, f_x_data, int_f_x_data = input_tuple

    plt.plot(x_data, f_x_data, '-r', label='f(x)')
    plt.plot(x_data, int_f_x_data, '*k', label=r'$F_n$')
    plt.legend(loc='best')
    plt.xlabel(f'x')
    plt.ylabel(f'N_X')

    plt.savefig(plot_name, dpi=300, bbox_inches='tight')
    plt.close()
