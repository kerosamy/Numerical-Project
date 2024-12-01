import numpy as np
from time import time
from Substitution import *
from Elimination import *

def doolittle_lu_solve(n, A, B,sig_figs):
        start_time = time()
        A = np.array(A) 
        B = np.array(B) 
    

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
   

# Example Usage

