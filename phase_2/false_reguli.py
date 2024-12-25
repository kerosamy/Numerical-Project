import sympy as sp

from phase_2.roundOff import *
import time
import math

def regula_falsi_method(func_str, xl, xu, tol=1e-6, max_iter=100, sf='none'):

    start_time = time.perf_counter()
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    f = sp.lambdify(x, func, 'math')

    xr = None

    steps = []  # Array to store steps

    for itr in range(max_iter):
        fxl = f(xl)
        fxu = f(xu)

        # Prevent division by zero
        if fxu - fxl == 0:
            return None, itr, None, None, None, "Division by ZERO Error", steps

        xr_new = (xl * fxu - xu * fxl) / (fxu - fxl)
        fxr = f(xr_new)
        error = abs((xr_new - (xr if xr else 1e9)) / (xr_new + 1e-12))
        xr = xr_new

        # Store the current step
        steps.append({
            "iteration": itr + 1,
            "xl": xl,
            "xu": xu,
            "xr": xr_new,
            "fxl": fxl,
            "fxu": fxu,
            "fxr": fxr,
            "error": error
        })

        # Update bounds
        if fxl * fxr < 0:

            xu = xr
        else:
            xl = xr

        if error < tol:
            break

    xr_rounded = Round_off(xr, sf)  # Assuming Round_off is defined elsewhere properly

    n_figures = calculate_significant_figures(error,sf)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    if itr == max_iter - 1:
        return xr_rounded, itr + 1, error, n_figures, execution_time, "Couldn't reach result in maximum number of iterations", steps

    return xr_rounded, itr + 1, error, n_figures, execution_time, "Converged", steps

