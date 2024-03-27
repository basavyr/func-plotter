import fourier

import pandas as pd
import numpy as np


def generate_csv_data():
    print(1)


def main():
    generate_csv_data()


HEADER = "This is a plot representing the evolution of the under-damped oscillator"


gamma = [0.5, 1, 2, 3, 5]
omega0 = [1, 2, 5, 7, 10]
t_data = np.linspace(0, 3.14, 75)
df = pd.DataFrame({
    "t": t_data,
    "ud": [fourier.Functions.oscillator_ud(t, gamma[0], omega0[0]) for t in t_data],
})


def main():
    df


if __name__ == '__main__':
    main()
