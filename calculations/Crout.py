import numpy as np
from Substitution import *
from CroutLUDecomposition import *
from time import time



def croutDecomposition(size,A,B,sig_figs):
    start_time = time()
    
    if(np.linalg.det(A)):
        L,U = createLUCrout(size,A,sig_figs)
        
        Y = forward_substitution(size, L, B, sig_figs)
        
        X = back_substitution(size, U, Y, sig_figs)
        
        end_time = time()
        execution_time = end_time - start_time

        return X, execution_time
    else:
        return "ahh ya bared"

    

A = np.array([
     [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]]
, dtype=float)

B = np.array([0.6, 1.5, 2.4])

print(len(A[0]))
print(np.linalg.det(A))
# Print the results
print(croutDecomposition(len(A[0]),A,B,8))


