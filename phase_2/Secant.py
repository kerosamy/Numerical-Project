import sympy as sp
import time
from phase_2.roundOff import *

def secant_method(func, x0, x1, tol=1e-6, max_iter=100, sig='none'):
    start_time = time.perf_counter()
    x = sp.symbols('x')
    f = sp.sympify(func)
    steps = []  # List to track steps

    for i in range(max_iter):
        f0 = float(f.subs(x, x0))
        f1 = float(f.subs(x, x1))

        
        if abs(f1 - f0) < 1e-10:
            return None, None, None, None, totTime, "Division by zero occurred. Ensure the function is well-defined for the input range.", steps
        
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x_new) > 1e6:
                return None, None, None, None, None, "The iteration is diverging. Values are exceeding acceptable limits.", steps
        relError = abs((x_new - x1) / (x_new + 1e-15))  
        # Log the current step
        steps.append({
            "iteration": i + 1,
            "x0": float(x0),
            "x1": float(x1),
            "f0": float(f0),
            "f1": float(f1),
            "x_new": float(x_new),
            "error": float(relError),
        })

        # Check for convergence
        if relError < tol:
            totTime = time.perf_counter() - start_time
            correctSigFig = calculate_significant_figures(relError,sig)
            x_rounded = Round_off(x_new, sig) if sig != 'none' else x_new
            return x_rounded, i + 1, relError, correctSigFig, totTime, "Converged", steps

        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x_new

    # If maximum iterations are reached without convergence
    totTime = time.perf_counter() - start_time
    return None, max_iter, None, None, totTime, "Exceeded the maximum number of iterations.", steps


if __name__ == "__main__":
    func = "x**3 - 6*x**2 + 11*x - 6"  # Example function
    x0, x1 = 2.5, 3.5  # Initial guesses
    tol = 1e-6
    max_iter = 50

    print("Secant Method:")
    root, iterations, error, correctSigFig, time_taken, status, steps = secant_method(func, x0, x1, tol, max_iter, 8)

    print(f"Root: {root}, Iterations: {iterations}, Error: {error}, Significant Figures: {correctSigFig}, Time: {time_taken:.6f}s, Status: {status}")
    print("\nSteps:")
    for step in steps:
        print(step)
