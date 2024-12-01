import numpy as np
from time import time
from Substitution import *
from CroutLUDecomposition import *

def croutDecomposition(size,A,B,sig_figs):
        start_time = time()
        A = np.array(A) 
        B = np.array(B) 
        L,U = createLUCrout(size,A,sig_figs)
        
        Y = forward_substitution(size, L, B, sig_figs)
        
        X = back_substitution(size, U, Y, sig_figs)
        
        end_time = time()
        execution_time = end_time - start_time

        return X, execution_time
    




