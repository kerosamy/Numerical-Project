import sympy as sp
import time
from phase_2.roundOff import *

def modified_secant_method(func, x0, tol=1e-6, max_iter=100, sig="none"):
    delta=0.1
    start_time = time.perf_counter()
    x = sp.symbols('x')
    f = sp.sympify(func)
    steps = []  # Array to store steps
    
    for i in range(max_iter):
        # Calculate the function values
        f_x0 = float(f.subs(x, x0))
        f_delta = float(f.subs(x, x0 + delta * x0))
        
        # Prevent division by very small denominators
        if abs(f_delta - f_x0) < 1e-15:
            totTime = time.perf_counter() - start_time
            return None, None, None, None, totTime, "Division by zero occurred. Ensure the function is well-defined for the input range.", steps

        # Update x using the modified secant method formula
        x_new = x0 - (f_x0 * delta * x0) / (f_delta - f_x0)
        relError = abs((x_new - x0) / (x_new + 1e-15))  # Avoid division by zero in relative error

        # Store the current step
        steps.append({
            "iteration": i + 1,
            "x0": float(x0),
            "x_new": float(x_new),
            "f_x0": float(f_x0),
            "f_delta": float(f_delta),
            "error": float(relError),
        })

        # Check for convergence
        if relError < tol:
            totTime = time.perf_counter() - start_time
            correctSigFig =calculate_significant_figures(relError,sig)
            x_rounded = Round_off(x_new, sig) if sig != "none" else x_new
            return x_rounded, i + 1, relError, correctSigFig, totTime, "Converged", steps

        # Update x0 for the next iteration
        x0 = x_new

    # If maximum iterations are reached without convergence
    totTime = time.perf_counter() - start_time
    return x_rounded, max_iter, relError, None, totTime, "Exceeded the maximum number of iterations.", steps
