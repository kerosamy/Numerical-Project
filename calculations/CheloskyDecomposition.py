from Substitution import forward_substitution, back_substitution
from time import time
import numpy as np

def choleskyDecomposition(size, A, B, sig_figs):
    start_time = time()
    
    if np.linalg.det(A) > 0 and np.allclose(A, A.T):
        L = np.zeros((size, size))
        
        for i in range(size):
            for j in range(i + 1):
                if i == j:
                    L[i, j] = round(np.sqrt(A[i, i] - np.sum(L[i, :j]**2)), sig_figs)
                else:
                    L[i, j] = round((A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j], sig_figs)

        Y = forward_substitution(size, L, B, sig_figs)
        X = back_substitution(size, L.T, Y, sig_figs)

        end_time = time()
        execution_time = end_time - start_time

        return X, execution_time
    else:
        return "tani ya bared!"

A = np.array([
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
], dtype=float)
B = np.array([1, 2, 3])

print(len(A[0]))
print(np.linalg.det(A))
print(choleskyDecomposition(len(A), A, B, 8))
