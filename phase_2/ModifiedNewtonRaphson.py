import sympy as sp
import time
from phase_2.roundOff import *

def modified_newton_raphson(func, x0, tol, max_iter, sig='none'):
    startTime = time.time()
    x = sp.symbols('x')
    f = sp.sympify(func)
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)
    steps = []  # Array to store steps

    for i in range(max_iter):
        fx = f.subs(x, x0)
        fpx = f_prime.subs(x, x0)
        fppx = f_double_prime.subs(x, x0)
        denominator = fpx**2 - fx * fppx

        if abs(denominator) == 0:
            totTime = time.time() - startTime
            return None, None, None, None, totTime, "Division by zero", steps

        x_next = x0 - (fx * fpx) / denominator
        relError = abs((x_next - x0) / (x_next + 1e-15))  # Avoid division by zero

        # Store the current step
        steps.append({
            "iteration": i + 1,
            "x0": float(x0),
            "x_next": float(x_next),
            "fx": float(fx),
            "fpx": float(fpx),
            "fppx": float(fppx),
            "error": float(relError),
        })

        if relError < tol:
            totTime = time.time() - startTime
            correctSigFig = 0 if relError == 0 else calculate_significant_figures(relError)
            return Round_off(float(x_next), sig), i + 1, relError, correctSigFig, totTime, "Converged", steps

        x0 = x_next

    totTime = time.time() - startTime
    return Round_off(float(x_next), sig), max_iter, relError, None, totTime, "Exceeded maximum iterations", steps
