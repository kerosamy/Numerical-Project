import math
import numpy as np
import pandas as pd

def Round_off(x, sf): 
    if(sf=='none'):
        return x
    if x == 0:
        return 0
    sf = int(sf)
    return round(x, sf - int(np.floor(np.log10(abs(x)))) - 1)

def bisection_method(equation, xl, xu, 
                     rel_error=1e-6, 
                     abs_error=1e-6, 
                     max_iterations=100, 
                     significant_figures=4):


    fxl = equation(xl, significant_figures)
    fxu = equation(xu, significant_figures)
    
    xr = 1e9

    if fxl * fxu >= 0:
        raise ValueError("Root is not bracketed between xl and xu. Choose different initial interval.")
    
    iterations = []
    iteration = 0
    
    while iteration < max_iterations:
        new_xr = (xl + xu) / 2
        
        
        abs_error_current = abs(new_xr - xr)
        rel_error_current = abs_error_current / (abs(new_xr) if new_xr != 0 else 1)
        
        xr = new_xr
        fxr = equation(xr, significant_figures)
        
        iteration_details = {
            'Iteration': iteration + 1,
            'xl': Round_off(xl, significant_figures),
            'xu': Round_off(xu, significant_figures),
            'xr (root estimate)': Round_off(xr, significant_figures),
            'f(xl)': Round_off(fxl, significant_figures),
            'f(xu)': Round_off(fxu, significant_figures),
            'f(xr)': Round_off(fxr, significant_figures),
            'Absolute Error': Round_off(abs_error_current, significant_figures),
            'Relative Error': Round_off(rel_error_current, significant_figures)
        }
        iterations.append(iteration_details)
        
        if (abs_error_current < abs_error or 
            rel_error_current < rel_error or 
            fxr == 0):
            df = pd.DataFrame(iterations)
            return df
        
        if fxl * fxr < 0:
            xu = xr
            fxu = fxr
        else:
            xl = xr
            fxl = fxr
        
        iteration += 1
    
    raise ValueError("Maximum iterations reached without convergence")

def run_bisection_example():
    def example_equation(x,significant_figures):
        return round(3*x**4 + 6.1*x**3 - 2*x**2 + 3*x + 2, significant_figures)
    
    print("Bisection Method Example:")
    print("Equation: f(x) = 3x⁴ + 6.1x³ - 2x² + 3x + 2 = 0")
    print("Search Interval: [-1, 0]")
    
    result = bisection_method(
        equation=example_equation, 
        xl=-1, 
        xu=0, 
        rel_error=1e-8, 
        abs_error=1e-2, 
        max_iterations=20, 
        significant_figures=5
    )
    
    print("\nBisection Method Iterations:")
    print(result)
    
    print("\nFinal Root Estimate:", 
          result.loc[result.index[-1], 'xr (root estimate)'])

if __name__ == "__main__":
    run_bisection_example()