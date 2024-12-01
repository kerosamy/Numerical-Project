import numpy as np
import time
from Substitution import *
from CroutLUDecomposition import *

def croutDecomposition(size,A,B,sig_figs):
        start_time = time.perf_counter()
        A = np.array(A) 
        B = np.array(B) 
        L,U = createLUCrout(size,A,sig_figs)
        
        Y = forward_substitution(size, L, B, sig_figs)
        
        X = back_substitution(size, U, Y, sig_figs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        return X, execution_time
    




