import sympy as sp
from phase_2.roundOff import *
import time

def fixed_point_iteration(func_str, x0, tol, max_iter, sf=4):
    start_time = time.perf_counter()
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    g = sp.lambdify(x, func, 'math')

    iter_count = 0
    error = float('inf')
    xi = x0
    prev_values = set()
    steps = []  
   
    while error > tol and iter_count < max_iter:
        try:
            xi_new = g(xi)
            if isinstance(xi_new, complex):
                return None, iter_count, error, None, None, "Iteration resulted in a complex number. Check the function for validity.", steps
            if abs(xi_new) > 1e6:
                return None, iter_count, error, None, None, "The iteration is diverging. Values are exceeding acceptable limits.", steps
        except OverflowError:
            return None, iter_count, error, None, None, "Overflow error occurred during computation. The values may be too large.", steps
        except ZeroDivisionError:
            return None, iter_count, error, None, None, "Division by zero occurred. Ensure the function is well-defined for the input range.", steps

        if xi_new in prev_values:
            return None, iter_count, error, None, None, "The iteration is oscillating or cycling. Check the function or initial guess.", steps

        prev_values.add(xi_new)
        error = abs((xi_new - xi) / (xi_new + (1e-12) * (xi == 0)))

        # Store the current step
        steps.append({
            "iteration": iter_count + 1,
            "xi": xi,
            "xi_new": xi_new,
            "error": error
        })

        xi = xi_new
        iter_count += 1

    converged = error <= tol
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    xi_rounded = Round_off(xi, sf)

    # Calculate number of significant figures assured
    n_figures = int(-sp.log(2 * error * 100) / sp.log(10))

    if not converged:
        return xi_rounded, iter_count, error, n_figures, execution_time, "Couldn't reach result in maximum number of iterations", steps

    return xi_rounded, iter_count, error, n_figures, execution_time, "Converged", steps
