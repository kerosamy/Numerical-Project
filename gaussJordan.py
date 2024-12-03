import time
from jordanForwElim import elimination
from Elimination import backward_elimination
from roundOff import Round_off
import numpy as np

def gauss_jordan_elimination(size, A, B, sig_figs):
    start_time = time.perf_counter()
    A = np.array(A) 
    B = np.array(B) 
 
    for i in range(size):
        for j in range(size):
            A[i][j] = Round_off(A[i][j], sig_figs)
    for i in range(size):
            B[i] = Round_off(B[i], sig_figs)
    matA, matB = elimination( A, B,size, sig_figs)
    solutions = backward_elimination(size, matA, matB, sig_figs)
    end_time = time.perf_counter()
    jordan_time = end_time - start_time
    return solutions, jordan_time

