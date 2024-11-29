import numpy as np
from time import time
from Substitution import *
from Elimination import *

def doolittleDecomposition(size,A,B,sig_figs):
    start_time = time()
    if(np.linalg.det(A)):
        L = np.eye(size)
        U = np.zeros((size,size))
        C = [0]*size
        A, C, Multipliers = forward_elimination(size,A,C,sig_figs)

        
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
                    
        print(L)
        print(U)
        print(B)

                    
        Y = forward_substitution(size, L, B, sig_figs)
        
        X = back_substitution(size, U, Y, sig_figs)
        
        end_time = time()
        execution_time = end_time - start_time

        return X,execution_time
    else:
        return "Ah ya bared"
A = np.array([
    [5, -2, 3, 0, 1],
    [-2, 4, 1, 5, -1],
    [3, 1, 7, 1, 2],
    [0, 5, 1, 8, -2],
    [1, -1, 2, -2, 6]
], dtype=float)

B = np.array([1, 2, 3, 4, 5])

print(doolittleDecomposition(len(A),A,B,10))