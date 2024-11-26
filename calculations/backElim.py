from roundOff import Round_off
def backward_elimination(A, B, size, sig_figs):
    for k in range(size - 1, -1, -1):
        for i in range(k - 1, -1, -1):
            factor = A[i][k]
            for j in range(size):
                A[i][j] -= factor * A[k][j]
                A[i][j] = Round_off(A[i][j], sig_figs)
            B[i] -= factor * B[k]  
            B[i] = Round_off(B[i], sig_figs)
    return B