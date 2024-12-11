import numpy as np
import time
from roundOff import Round_off
from Substitution import forward_substitution, back_substitution

# comment
def choleskyDecomposition(size, A, B, sig_figs):
    start_time = time.perf_counter()
    A = np.array(A) 
    B = np.array(B) 
    L = np.zeros_like(A)

    for i in range(size):
        for j in range(i + 1):
            if i == j: 
                sum_diagonal = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = Round_off(np.sqrt(A[i][i] - sum_diagonal), sig_figs)
            else:
                sum_off_diagonal = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = Round_off((A[i][j] - sum_off_diagonal) / L[j][j], sig_figs)

    LT = L.T    
    Y = forward_substitution(size, L, B, sig_figs)
    X = back_substitution(size, LT, Y, sig_figs)
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return X, execution_time

def is_symmetric(matrix):
    matrix = np.array(matrix)
    return np.array_equal(matrix, matrix.T)  
