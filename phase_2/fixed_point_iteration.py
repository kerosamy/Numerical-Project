import sympy as sp

def fixed_point_iteration(func_str, x0, tol, max_iter):
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    g = sp.lambdify(x, func, 'math')

    iter_count = 0
    error = float('inf')
    xi = x0

    while error > tol and iter_count < max_iter:
        xi_new = g(xi)
        if abs(xi_new) > 1e6:  
            return xi_new, False
        error = abs((xi_new - xi) / (xi_new + (1e-12)*(xi==0)))
        xi = xi_new
        iter_count += 1

    converged = error <= tol
    return xi, converged

# Example Usage
equation = "(2*x+3)**0.5"
initial_guess = 4
relative_error = 1e-6
max_iterations = 100

root, is_converged = fixed_point_iteration(equation, initial_guess, relative_error, max_iterations)
print(f"Root: {root}, Converged: {is_converged}")
