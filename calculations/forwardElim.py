from partialPiv import partial_pivoting
from roundOff import Round_off

def forward_elimination(size, A, B, sig_figs):
    multipliers = []  
    for k in range(size):
        partial_pivoting(A, B, size, k)
        for i in range(k + 1, size):
            factor = A[i][k] / A[k][k]
            rounded_factor = Round_off(factor, sig_figs)
            multipliers.append(rounded_factor)
            for j in range(k, size):  
                A[i][j] -= factor * A[k][j]
                A[i][j] = Round_off(A[i][j], sig_figs)
            B[i] -= factor * B[k] 
            B[i] = Round_off(B[i], sig_figs)
    return A, B, multipliers
