import sympy as sp
import time
from phase_2.roundOff import *

def newton_raphson(func, x0, tol, max_iter, sig='none'):
    start_time = time.perf_counter()  
    x = sp.symbols('x')
    f = sp.sympify(func)
    f_prime = sp.diff(f, x)
    steps = []  
    print(func)

    for i in range(max_iter):
        fx = f.subs(x, x0).evalf()  
        fpx = f_prime.subs(x, x0).evalf()  

        if abs(fpx) == 0:
            totTime = time.perf_counter() - start_time
            print(f"Division by zero at Iteration {i+1}")
            return None, None, None, None, totTime, "Division by zero", steps

        x_next = x0 - fx / fpx
        relError = abs((x_next - x0) / (x_next + 1e-15))*100

       
        steps.append({
            "iteration": i + 1,
            "x0": float(x0),
            "fx": float(fx),
            "fpx": float(fpx),
            "x_next": float(x_next),
            "error": float(relError),
        })

        if relError < tol:
            totTime = time.perf_counter() - start_time
            correctSigFig = calculate_significant_figures(relError,sig)
            x_rounded = Round_off(float(x_next), sig) if sig != "none" else x_next
            return x_rounded, i + 1, relError, correctSigFig, totTime, "Converged", steps

        x0 = x_next

    totTime = time.perf_counter() - start_time
    print("Exceeded the maximum number of iterations")
    return None, max_iter, None, None, totTime, "Exceeded the maximum number of iterations", steps


