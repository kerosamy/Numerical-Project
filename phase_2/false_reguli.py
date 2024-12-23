import sympy as sp
from roundOff import *
import time
import math

def regula_falsi_method(func_str, xl, xu, tol=1e-6, max_iter=100, sf=4):
    start_time = time.perf_counter()
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    f = sp.lambdify(x, func, 'math')

    xr = None
    for itr in range(max_iter):
        fxl = f(xl)
        fxu = f(xu)

        if fxl * fxu > 0:
            return None, None, None, None, None  # Indicating no root is present within the interval
        
        if fxu - fxl == 0:
            print("Division by ZERO")
            return None, None, None, None, None  # Indicating no root is present within the interval
        
        xr_new = (xl * fxu - xu * fxl) / (fxu - fxl)
        error = abs((xr_new - (xr if xr else 1e9)) / (xr_new + 1e-12))
        xr = xr_new

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        if error < tol:
            break

    xr_rounded = Round_off(xr, sf)  # Assuming Round_off is defined elsewhere properly
    n_figures = calculate_significant_figures(error)  # Ensure positive input for log
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return xr_rounded, itr, error, n_figures, execution_time

# Example Usage
equation = "x^2-2"
xl, xu = 0,4
tol = 1e-6
max_iter = 100
sf = 4
# Regula Falsi Method
root_regula, iterations,error,figures_regula,exec_time = regula_falsi_method(equation, xl, xu, tol, max_iter, sf)

print(f"Regula Falsi Root: {root_regula}, \n"
      f"Iterations: {iterations}, \n"
      f"Error: {error}, \n"
      f"Significant Figures Assured: {figures_regula}, \n"
      f"Execution Time: {exec_time}")
