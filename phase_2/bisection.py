import sympy as sp
from phase_2.roundOff import *
import time
import math


def bisection_method(func_str, xl, xu, tol=1e-6, max_iter=100, sf='none'):
    start_time = time.perf_counter()
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    f = sp.lambdify(x, func, 'math')
    fxl = f(xl)
    fxu = f(xu)
    xr = None
    steps = [] 

    for itr in range(max_iter):
        xr_new = (xl + xu) / 2
        fxr_new = f(xr_new)
        error = abs((xr_new - (xr if xr else 1e9)) / (xr_new + 1e-12))

        # Store the current step
        steps.append({
            "iteration": itr + 1,
            "xl": xl,
            "xu": xu,
            "xr": xr_new,
            "fxl": fxl,
            "fxu": fxu,
            "fxr": fxr_new,
            "error": error
        })

        if fxr_new == 0 or abs(xu - xl) < tol:
            xr = xr_new
            break
        if fxl * fxr_new < 0:
            xu = xr_new
            fxu = fxr_new
        else:
            xl = xr_new
            fxl = fxr_new
        xr = xr_new

    xr_rounded = Round_off(xr, sf)
    n_figures = calculate_significant_figures(error)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    if itr == max_iter - 1:
        return None, itr, error, None, execution_time, "Couldn't reach result in maximum number of iterations", steps

    return xr_rounded, itr + 1, error, n_figures, execution_time, "Converged", steps
