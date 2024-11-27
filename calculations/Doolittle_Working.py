import numpy as np
from time import time
from Substitution import *
from Elimination import *

def doolittle_lu_solve(n, A, B,sig_figs):
    start_time = time()

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
                raise ValueError("Matrix is singular, cannot proceed with decomposition.")
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
            

    Y = forward_substitution(n, L, B, sig_figs)

    X = back_substitution(n, U, Y, sig_figs)

    end_time = time()
    execution_time = end_time - start_time
    return X, execution_time

# Example Usage
A = np.array([
    [6, -2, 2],
    [-2, 3, -1],
    [2, -1, 3]
], dtype=float)

B = np.array([6, -2, 2], dtype=float)

try:
    X = doolittle_lu_solve(3,A, B,5)
    print("Solution X:", X)
except ValueError as e:
    print("Error:", e)
