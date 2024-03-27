from numpy import cos, exp


class Functions:
    """
    - helper class that contains useful functions, such as unit-step, under-damped oscillators, and so on.

    - inspired by the following source: https://scholar.harvard.edu/files/schwartz/files/lecture8-fouriertransforms.pdf
    """

    @staticmethod
    def cos_t(t: float, omega: float) -> float:
        """
        - regular cosine function, but applied to `$(t\omega)$` instead of `$t$`
        """
        return cos(t * omega)

    @staticmethod
    def exp_t(t: float, gamma: float) -> float:
        """
        - regular exponential function, but applied to `$(t\gamma)$` instead of `$t$`
        """
        return exp(t * gamma)

    @staticmethod
    def unit_step(t: float) -> int:
        """
        - returns 0 if the value of `t` is less than 0 and `1` otherwise
        """
        return 0 if t <= 0 else 1

    @staticmethod
    def oscillator_ud(t: float, gamma: float, omega_0: float) -> float:
        """
        - the equation for the under-damped (ud) oscillator

        - source: https://scholar.harvard.edu/files/schwartz/files/lecture8-fouriertransforms.pdf
        """
        osc_ud = Functions.exp_t(-t, gamma) * \
            Functions.cos_t(t, omega_0) * Functions.unit_step(t)
        return osc_ud
