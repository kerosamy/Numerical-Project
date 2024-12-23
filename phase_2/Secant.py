def secant_method(f, x0, x1, tol=1e-6, max_iter=100):

    for i in range(max_iter):
        # Calculate the value of the function at x0 and x1
        f0, f1 = f(x0), f(x1)

        # Prevent division by zero
        if f1 - f0 == 0:
            raise ValueError("Division by zero encountered in the secant method.")

        # Update x using the secant method formula
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)

        # Check for convergence
        if abs(x_new - x1) < tol:
            return x_new, i + 1

        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x_new

    raise ValueError("Secant method did not converge within the maximum number of iterations.")

# Example usage:
if __name__ == "__main__":
    import math

    # Define the nth-order equation as a Python function
    def f(x):
        return x**3 - 6*x**2 + 11*x - 6  # Example: f(x) = x^3 - 6x^2 + 11x - 6

    # Initial guesses
    x0 = 3.5
    x1 = 2.5

    # Solve using the secant method
    try:
        root, iterations = secant_method(f, x0, x1)
        print(f"Root found: {root:.6f}")
        print(f"Number of iterations: {iterations}")
    except ValueError as e:
        print(str(e))