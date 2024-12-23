def modified_secant_method(f, x0, delta=1e-20, tol=1e-6, max_iter=100):

    for i in range(max_iter):
        # Calculate f(x) and f(x + delta * x)
        fx = f(x0)
        f_delta = f(x0 + delta * x0)

        # Prevent division by zero
        if f_delta - fx == 0:
            raise ValueError("Division by zero encountered in the modified secant method.")

        # Update x using the modified secant method formula
        x_new = x0 - fx * delta * x0 / (f_delta - fx)

        # Check for convergence
        if abs(x_new - x0) < tol:
            return x_new, i + 1

        # Update x0 for the next iteration
        x0 = x_new

    raise ValueError("Modified secant method did not converge within the maximum number of iterations.")

# Example usage:
if __name__ == "__main__":
    import math

    # Define the function for which the root is to be found
    def f(x):
        return x**3 - 6*x**2 + 11*x - 6  # Example: f(x) = x^3 - 6x^2 + 11x - 6

    # Initial guess
    x0 = 2.4

    # Solve using the modified secant method
    try:
        root, iterations = modified_secant_method(f, x0, delta=1e-5, tol=1e-8)
        print(f"Root found: {root:.6f} after {iterations} iterations")
    except ValueError as e:
        print(str(e))