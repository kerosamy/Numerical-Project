import sympy as sp

def fixed_point_iteration(func_str, x0, tol, max_iter):
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    g = sp.lambdify(x, func, 'math')

    iter_count = 0
    error = float('inf')
    xi = x0
    prev_values = set()

    while error > tol and iter_count < max_iter:
        try:
            xi_new = g(xi)
            if isinstance(xi_new, complex):  # Handle complex numbers
                return None, False
            if abs(xi_new) > 1e6:  # Divergence detection
                return None, False
        except (OverflowError, ZeroDivisionError):  # Handle runtime errors
            return None, False

        if xi_new in prev_values:  # Detect oscillations or cycles
            return None, False
        prev_values.add(xi_new)

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
