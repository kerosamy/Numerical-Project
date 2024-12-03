
import numpy as np
import time
from roundOff import *

def lu_decomposition_with_pivoting(n,A,B,sig_figs):
    n = len(A)
    L = np.zeros((n, n))  # Lower triangular matrix
    U = np.zeros((n, n))  # Upper triangular matrix
    P = np.eye(n)         # Permutation matrix (for partial pivoting)

    # Perform LU Decomposition with Partial Pivoting
    for i in range(n):
        # Partial Pivoting
        max_row = np.argmax(np.abs(A[i:n, i])) + i
        if i != max_row:
            # Swap the rows in A, L, U and P
            A[[i, max_row]] = A[[max_row, i]]
            P[[i, max_row]] = P[[max_row, i]]
            L[[i, max_row]] = L[[max_row, i]]
        # Decompose the matrix
        for j in range(i, n):
            U[i, j] = Round_off(A[i, j] - np.dot(L[i, :i], U[:i, j]), sig_figs)  # Upper matrix
        for j in range(i+1, n):
            if U[i, i] == 0:
                raise ValueError("Zero pivot encountered, matrix is singular")
            L[j, i] = Round_off((A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i],sig_figs)  # Lower matrix

    return P, L, U

def forward_substitution(L, b,sig_figs):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = Round_off(b[i] - np.dot(L[i, :i], y[:i]),sig_figs)
    return y

def backward_substitution(U, y,sig_figs):
    n = len(U)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = Round_off((y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i],sig_figs)
    return x

def doolittle_lu_solve(n,A, B,sig_figs):
    start_time = time.perf_counter()
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    P, L, U = lu_decomposition_with_pivoting(n,A,B,sig_figs)

    Pb = np.dot(P, B)
    y = forward_substitution(L, Pb,sig_figs)

    x = backward_substitution(U, y,sig_figs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return x,execution_time
