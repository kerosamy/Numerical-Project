import numpy as np
from time import time
from Substitution import *
from Elimination import *

def doolittleDecomposition(size,A,B,sig_figs):
    start_time = time()
    L = np.eye(size)
    U = np.zeros((size,size))
    A, B, Multipliers = forward_elimination(size,A,B,sig_figs)

    
    pointer = 0  # Reset pointer to start of multipliers list
    for j in range(size):
        for i in range(size):
            if i == j:  # Diagonal elements of U
                U[i][j] = A[i][j]
            elif i > j:  # Lower triangular matrix (L)
                L[i][j] = Multipliers[pointer]
                pointer+=1
            else:  # Upper triangular matrix (U)
                U[i][j] = A[i][j]

                
    Y = forward_substitution(size, L, B, sig_figs)
    
    X = back_substitution(size, U, Y, sig_figs)
    
    end_time = time()
    execution_time = end_time - start_time

    return X,execution_time

A = np.array([
    [6, -2, 2],
    [-2, 3, -1],
    [2, -1, 3]
], dtype=float)

B = np.array([6, -2, 2], dtype=float)

print(doolittleDecomposition(3,A,B,5))