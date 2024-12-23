import sympy as sp
from roundOff import *
import time
import math


def bisection_method(func_str, xl, xu, tol=1e-6, max_iter=100, sf=4):
    start_time = time.perf_counter()
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    f = sp.lambdify(x, func, 'math')
    
    fxl = f(xl)
    fxu = f(xu)
    if fxl * fxu > 0:
        return None, None,None,None,None  # Indicating no root is present within the interval
    
    xr = None
    
    for itr in range(max_iter):
        xr_new = (xl + xu) / 2
        fxr_new = f(xr_new)
        error = abs((xr_new - (xr if xr else 1e9)) / (xr_new + 1e-12))

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
        
    # for itr in range(max_iter):
    #     xr_new = (xl + xu) / 2
    #     error = abs((xr_new - (xr if xr else 1e9)) / (xr_new + 1e-12))
    #     xr = xr_new

    #     if f(xl) * f(xr) < 0:
    #         xu = xr
    #     else:
    #         xl = xr

    #     if error < tol:
    #         break
    #     print(itr)

    xr_rounded = Round_off(xr, sf)
    n_figures = calculate_significant_figures(error)  # Ensure positive input for log
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return xr_rounded, itr, error, n_figures, execution_time



# Example Usage
equation = "x**5 - 8*x**4 - 2*x**3 + 40*x**2 + 24*x"
xl, xu = -0.5,1
tol = 1e-6
max_iter = 100
sf = 4

# Bisection Method
root_bisection,iterations,error, figures_bisection,exec_time = bisection_method(equation, xl, xu, tol, max_iter, sf)

print(f"Bisection Root: {root_bisection}, \n"
      f"Iterations: {iterations}, \n"
      f"Error: {error}, \n"
      f"Significant Figures Assured: {figures_bisection}, \n"
      f"Execution Time: {exec_time}")