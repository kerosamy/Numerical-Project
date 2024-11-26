from partialPiv import partial_pivoting
from roundOff import Round_off

def forw_elimination(A, B, size, sig_figs):
    for k in range(size):
        partial_pivoting(A, B, size, k)
        pivot = A[k][k]
        for j in range(size): 
            A[k][j] /= pivot
            A[k][j] = Round_off(A[k][j], sig_figs)
        B[k] /= pivot  
        B[k] = Round_off(B[k], sig_figs)
        for i in range(k + 1, size):
            factor = A[i][k]
            for j in range(size):
                A[i][j] -= factor * A[k][j]
                A[i][j] = Round_off(A[i][j], sig_figs)
            B[i] -= factor * B[k] 
            B[i] = Round_off(B[i], sig_figs)
    return A, B