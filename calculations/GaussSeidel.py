from time import time
import numpy as np

def gaussSeidel(A, B, initial_guess, max_iterations=100, tolerance=1e-8):
    start_time = time() 
    n = len(A)
    x = np.array(initial_guess, dtype=float)
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (B[i] - sum1 - sum2) / A[i, i]
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if error < tolerance:
            execution_time = time() - start_time
            return x, k + 1, execution_time
    
    execution_time = time() - start_time  
    return x, max_iterations, execution_time

# Test example
A = np.array([
    [4, -1, 0, 0],
    [-1, 4, -1, 0],
    [0, -1, 4, -1],
    [0, 0, -1, 3]
], dtype=float)
B = np.array([15, 10, 10, 10])
initial_guess = [0, 0, 0, 0]

solution, iterations, execution_time = gaussSeidel(A, B, initial_guess, tolerance=1e-5)
print("Solution:", solution)
print("Iterations:", iterations)
print("Execution Time:", execution_time, "seconds")
