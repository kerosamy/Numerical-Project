import time
import numpy as np
from phase_1.roundOff import Round_off
import numpy as np
from phase_1.make_diagonally_dominant import make_diagonally_dominant


def jacobiMethod(A, B, initial_guess, max_iterations=100, tolerance=1e-8, sig_figs=8):
    start_time = time.perf_counter()
    is_diagonally_dominant, A, B = make_diagonally_dominant(A, B)
    n = len(A)
    A = np.array(A) 
    B = np.array(B) 
    max_iterations = int(max_iterations)
    tolerance = float(tolerance)
   
    
    x = np.array(initial_guess, dtype=float)
    x_new = x.copy()
    

    for k in range(max_iterations):
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (B[i] - sum1 - sum2) / A[i, i]
            x_new[i] = Round_off(x_new[i], sig_figs)

        error = np.linalg.norm(x_new - x, ord=np.inf)
        if error < tolerance:
            execution_time = time.perf_counter() - start_time 
            return x_new,  execution_time ,k + 1,is_diagonally_dominant
        
        x[:] = x_new

    execution_time = time.perf_counter() - start_time 
    return x,execution_time , max_iterations, is_diagonally_dominant
