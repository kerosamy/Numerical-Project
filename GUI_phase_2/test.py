import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def plot_string_function(func_str, variable='x', x_range=(-10, 10), points=500):
    """
    Plots a mathematical function given as a string.
    
    Parameters:
        func_str (str): The mathematical function as a string (e.g., "x^2 + 2*x + 1").
        variable (str): The variable in the function (default is 'x').
        x_range (tuple): The range of x values (default is (-10, 10)).
        points (int): Number of points to plot (default is 500).
    """
    try:
        # Define the variable symbolically
        x = symbols(variable)
        
        # Parse the function string into a symbolic expression
        func_sym = sympify(func_str.replace("^", "**"))
        
        # Convert the symbolic function into a numerical function
        func_num = lambdify(x, func_sym, modules=["numpy"])
        
        # Generate x values and corresponding y values
        x_vals = np.linspace(x_range[0], x_range[1], points)
        y_vals = func_num(x_vals)
        
        # Plot the function
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f"${func_sym}$")
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.title("Plot of the Function")
        plt.xlabel(variable)
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage
plot_string_function("x^2 + 2*x + 1", x_range=(-5, 5))
