import numpy as np
from time import time
from Substitution import *
from Elimination import *

def doolittle_lu_solve(n, A, B,sig_figs):
    start_time = time()
    if(np.linalg.det(A)):

        L = np.eye(n)  # L with ones on the diagonal
        U = np.zeros((n, n))

        # Perform LU decomposition
        for i in range(n):
            # Compute U matrix
            for j in range(i, n):
                U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

            # Compute L matrix
            for j in range(i + 1, n):
                if U[i, i] == 0:
                    return "ahh ya bared"
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
                
                
        Y = forward_substitution(n, L, B, sig_figs)
        
        X = back_substitution(n, U, Y, sig_figs)

        end_time = time()
        execution_time = end_time - start_time
        return X, execution_time
    else:
        return "Ah ya bared"

# Example Usage
A = np.array([
    [5, -2, 3, 0, 1],
    [-2, 4, 1, 5, -1],
    [3, 1, 7, 1, 2],
    [0, 5, 1, 8, -2],
    [1, -1, 2, -2, 6]
], dtype=float)

B = np.array([1, 2, 3, 4, 5])

print(np.linalg.det(A))
print( doolittle_lu_solve(len(A[0]),A, B,5))

