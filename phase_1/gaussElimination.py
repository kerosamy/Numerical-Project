from phase_1.Elimination import forward_elimination
from phase_1.Substitution import back_substitution
from phase_1.roundOff import Round_off
from phase_1.solutionType import checkSolutionType
import time
import numpy as np


def gauss_elimination(size, A, B, sig_figs):
    start_time = time.perf_counter()
    A = np.array(A) 
    B = np.array(B) 
    for i in range(size):
        for j in range(size):
                A[i][j] = Round_off(A[i][j], sig_figs)
    for i in range(size):
            B[i] = Round_off(B[i], sig_figs)
    A_transformed, B_transformed, multipliers = forward_elimination(size, A, B, sig_figs)
    solutions = back_substitution(size, A_transformed, B_transformed, sig_figs)        
    end_time = time.perf_counter()
    gauss_time = end_time - start_time
    return solutions, gauss_time


