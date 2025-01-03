import time
import numpy as np
from phase_1.roundOff import Round_off
from phase_1.make_diagonally_dominant import make_diagonally_dominant


def gaussSeidel(A, B, initial_guess,sig_figs, max_iterations=100, tolerance=1e-8):
    start_time = time.perf_counter()
    is_diagonally_dominant, A, B = make_diagonally_dominant(A, B)
    n = len(A)
    x = np.array(initial_guess, dtype=float)
    max_iterations = int(max_iterations)
    tolerance = float(tolerance)
    A = np.array(A) 
    B = np.array(B) 
    
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (B[i] - sum1 - sum2) / A[i, i]
            x[i] = Round_off(x[i], sig_figs)  # Apply significant figures
        
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if error < tolerance:
            execution_time = time.perf_counter() - start_time
            return x, execution_time, k+1,is_diagonally_dominant
    
    execution_time = time.perf_counter() - start_time  
    return x, execution_time, max_iterations, is_diagonally_dominant
