import fourier

import pandas as pd
import numpy as np


def generate_csv_data():
    print(1)


def main():
    generate_csv_data()


HEADER = "This is a plot representing the evolution of the under-damped oscillator"


def generate_ud_df(n_points: int, gamma: float, omega: float) -> pd.DataFrame:
    """
    - takes the value of gamma (argument that goes into the exponential function) value of omega (argument that controls the cosine function) and creates a data frame object containing all the values for the under-damped oscillator on a fixed interval for `t`
    """
    t_data = np.linspace(0, 3.14, n_points)
    df = pd.DataFrame({
        "exp": {
            "t": t_data,
            "ud": [fourier.Functions.oscillator_ud(t, gamma, omega) for t in t_data]
        },
        "th": {
            "t": t_data,
            "ud": [generate_th_value(fourier.Functions.oscillator_ud(t, gamma, omega), 10) for t in t_data]
        }
    })
    return df


def generate_th_value(exp_value: float, delta: int) -> float:
    """
    - generate a *theoretical* value based on an experimental one.
    - the degree of deviation from the experiment will be provided by a "delta" scale, measuring how much the theoretical value will deviate from the experimental one

    - th value is evaluated using the following approach:
        `th = exp+ rand(0,1)*delta`
    """
    d = np.random.random()
    return exp_value+(d/delta)*exp_value


def generate_gamma_values(g_min: float, g_max: float, step: float) -> np.ndarray:
    n_points = int((g_max-g_min)/step+1)
    gammas = np.linspace(g_min, g_max, n_points)
    return gammas


def generate_omega_values(w_min: float, w_max: float, step: float) -> np.ndarray:
    n_points = int((w_max-w_min)/step+1)
    gammas = np.linspace(w_min, w_max, n_points)
    return gammas
