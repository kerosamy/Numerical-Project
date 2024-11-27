import numpy as np
from Substitution import *
from CroutLUDecomposition import *
from time import time



def croutDecomposition(size,A,B,sig_figs):
    start_time = time()

    L,U = createLUCrout(size,A,sig_figs)
    
    Y = forward_substitution(size, L, B, sig_figs)
    
    X = back_substitution(size, U, Y, sig_figs)
    
    end_time = time()
    execution_time = end_time - start_time

    return X, execution_time

    

A = np.array([
    [6, -2, 2],
    [-2, 3, -1],
    [2, -1, 3]
], dtype=float)

B = np.array([6, -2, 2], dtype=float)

# Print the results
print(croutDecomposition(3,A,B,5))


